from PIL import Image
import boto3
import os
import json
import logging
from datetime import datetime
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type

# Configure a basic logger (independent of Django)
logger = logging.getLogger(__name__)
if not logger.handlers:
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

class ParkingUtils:
    def __init__(self, media_bucket_name, static_bucket_name, sns_topic_arn, aws_region='us-east-1'):
        self.region = aws_region
        self.s3_client = boto3.client('s3', region_name=self.region)
        self.sns_client = boto3.client('sns', region_name=self.region)
        self.cloudwatch_logs = boto3.client('logs', region_name=self.region)
        self.cloudwatch_metrics = boto3.client('cloudwatch', region_name=self.region)
        self.sqs_client = boto3.client('sqs', region_name=self.region)
        self.media_bucket = media_bucket_name
        self.static_bucket = static_bucket_name
        self.topic_arn = sns_topic_arn
        self.log_group_name = 'ParkingLogs'
        self.log_stream_name = 'ApplicationStream'
        self.sequence_token = None
        self.queue_url = self._create_sqs_queue()
        # Validate sns_topic_arn during initialization
        if not self.topic_arn or not isinstance(self.topic_arn, str):
            logger.error(f"SNS_TOPIC_ARN is not set or invalid: {self.topic_arn}")
            raise ValueError("SNS_TOPIC_ARN must be provided and must be a valid string")

    def resize_image(self, image_path, output_path, size=None):
        try:
            s3_key = f"parking_spots/{os.path.basename(image_path)}"
            if size:
                with Image.open(image_path) as img:
                    img.thumbnail(size)
                    img.save(output_path, quality=95)
                self.s3_client.upload_file(
                    output_path, self.media_bucket, s3_key,
                    ExtraArgs={'ContentType': 'image/jpeg'}
                )
            else:
                self.s3_client.upload_file(
                    image_path, self.media_bucket, s3_key,
                    ExtraArgs={'ContentType': 'image/jpeg'}
                )
            url = f"https://{self.media_bucket}.s3.amazonaws.com/{s3_key}"
            self.log_to_cloudwatch(f"Uploaded image to S3: {url}")
            return url
        except Exception as e:
            self.log_to_cloudwatch(f"Error uploading image {image_path}: {str(e)}", level='ERROR')
            raise

    def check_spot_availability(self, parking_spot, start_time, end_time, total_spots, bookings):
        """Check if any spot is available for the given time range."""
        overlapping = sum(
            1 for booking in bookings
            if booking['start_time'] < end_time and booking['end_time'] > start_time
        )
        available = overlapping < total_spots
        logger.debug(f"Availability check for {parking_spot}: {available}, Overlapping: {overlapping}")
        return available

    def subscribe_user(self, email):
        """Subscribe the user to the SNS topic and return the subscription ARN."""
        try:
            # Validate TopicArn
            if not self.topic_arn or not isinstance(self.topic_arn, str) or not self.topic_arn.startswith('arn:aws:sns'):
                logger.error(f"Invalid TopicArn: {self.topic_arn}")
                self.log_to_cloudwatch(f"Invalid TopicArn: {self.topic_arn}", level='ERROR')
                return None

            # Check if the user is already subscribed
            response = self.sns_client.list_subscriptions_by_topic(TopicArn=self.topic_arn)
            for subscription in response.get('Subscriptions', []):
                if subscription['Endpoint'] == email:
                    subscription_arn = subscription['SubscriptionArn']
                    if subscription_arn == 'PendingConfirmation':
                        logger.debug(f"Subscription for {email} is pending confirmation")
                        return 'PendingConfirmation'
                    if subscription_arn.startswith('arn:aws:sns'):
                        logger.debug(f"Found confirmed subscription for {email}: {subscription_arn}")
                        return subscription_arn
                    logger.warning(f"Unexpected subscription ARN format for {email}: {subscription_arn}")
                    return None

            # If not subscribed, create a new subscription
            response = self.sns_client.subscribe(
                TopicArn=self.topic_arn,
                Protocol='email',
                Endpoint=email
            )
            subscription_arn = response.get('SubscriptionArn')
            logger.debug(f"Created new subscription for {email}: {subscription_arn}")
            return subscription_arn if subscription_arn != 'PendingConfirmation' else 'PendingConfirmation'
        except Exception as e:
            logger.error(f"Error subscribing {email}: {str(e)}")
            self.log_to_cloudwatch(f"Error subscribing {email}: {str(e)}", level='ERROR')
            return None

    def set_subscription_filter(self, subscription_arn, email):
        if not subscription_arn.startswith('arn:aws:sns'):
            logger.error(f"Invalid SubscriptionArn: {subscription_arn}")
            self.log_to_cloudwatch(f"Invalid SubscriptionArn: {subscription_arn}", level='ERROR')
            raise ValueError(f"Invalid SubscriptionArn: {subscription_arn}")

        filter_policy = {
            'email': [email]
        }
        self.sns_client.set_subscription_attributes(
            SubscriptionArn=subscription_arn,
            AttributeName='FilterPolicy',
            AttributeValue=json.dumps(filter_policy)
        )

    def notify_user(self, email, subject, message):
        logger.info(f"Attempting to notify {email} with subject: {subject}")
        try:
            if not isinstance(email, str) or '@' not in email:
                logger.error(f"Invalid email format: {email}")
                self.log_to_cloudwatch(f"Invalid email format: {email}", level='ERROR')
                return "error"

            subscription_arn = self.subscribe_user(email)
            logger.debug(f"Subscription ARN for {email}: {subscription_arn}")

            if subscription_arn == 'PendingConfirmation':
                # Fallback: Log the notification to CloudWatch instead of skipping
                logger.warning(f"Subscription for {email} is pending confirmation. Logging notification to CloudWatch.")
                self.log_to_cloudwatch(f"Fallback Notification for {email}: Subject: {subject}, Message: {message}", level='INFO')
                return "pending_confirmation"
            elif not subscription_arn:
                logger.warning(f"No confirmed subscription found for {email}. Logging notification to CloudWatch.")
                self.log_to_cloudwatch(f"Fallback Notification for {email}: Subject: {subject}, Message: {message}", level='INFO')
                return "no_subscription"

            try:
                self.set_subscription_filter(subscription_arn, email)
                logger.debug(f"Set subscription filter for {subscription_arn}")
            except Exception as e:
                logger.error(f"Failed to set subscription filter for {subscription_arn}: {str(e)}")
                self.log_to_cloudwatch(f"Failed to set subscription filter for {subscription_arn}: {str(e)}", level='ERROR')
                return "error"

            @retry(
                stop=stop_after_attempt(3),
                wait=wait_exponential(multiplier=1, min=2, max=10),
                retry=retry_if_exception_type(Exception),
                before_sleep=lambda retry_state: logger.debug(
                    f"Retrying SNS publish (attempt {retry_state.attempt_number})...")
            )
            def publish_message():
                return self.sns_client.publish(
                    TopicArn=self.topic_arn,
                    Message=message,
                    Subject=subject,
                    MessageAttributes={
                        'email': {
                            'DataType': 'String',
                            'StringValue': email
                        }
                    }
                )

            response = publish_message()
            logger.debug(f"SNS notification sent to {email} with subject: {subject}")
            self.log_to_cloudwatch(f"SNS notification sent to {email} with subject: {subject}")
            return "success"
        except Exception as e:
            error_msg = str(e).replace(self.topic_arn, "[TopicARN]") if self.topic_arn in str(e) else str(e)
            logger.error(f"Failed to send SNS notification to {email}: {error_msg}")
            self.log_to_cloudwatch(f"Failed to send SNS notification to {email}: {error_msg}", level='ERROR')
            return "error"

    def log_to_cloudwatch(self, message, level='INFO'):
        try:
            log_event = {
                'logGroupName': self.log_group_name,
                'logStreamName': self.log_stream_name,
                'logEvents': [
                    {
                        'timestamp': int(datetime.utcnow().timestamp() * 1000),
                        'message': f"{level}: {message}"
                    }
                ]
            }
            if self.sequence_token:
                log_event['sequenceToken'] = self.sequence_token
            response = self.cloudwatch_logs.put_log_events(**log_event)
            self.sequence_token = response['nextSequenceToken']
            logger.debug(f"Logged to CloudWatch: {message}")
        except Exception as e:
            logger.error(f"Failed to log to CloudWatch: {str(e)}")

    def put_metric(self, metric_name, value, unit='Count'):
        try:
            self.cloudwatch_metrics.put_metric_data(
                Namespace='ParkingAppMetrics',
                MetricData=[{
                    'MetricName': metric_name,
                    'Value': value,
                    'Unit': unit
                }]
            )
            logger.debug(f"Sent metric {metric_name}: {value} to CloudWatch")
        except Exception as e:
            logger.error(f"Failed to send metric {metric_name}: {str(e)}")

    def _create_sqs_queue(self):
        queue_name = 'parking-app-qr-queue'
        try:
            response = self.sqs_client.get_queue_url(QueueName=queue_name)
            queue_url = response['QueueUrl']
            logger.debug(f"SQS queue {queue_name} already exists: {queue_url}")
        except self.sqs_client.exceptions.QueueDoesNotExist:
            response = self.sqs_client.create_queue(
                QueueName=queue_name,
                Attributes={
                    'MessageRetentionPeriod': '345600',  # 4 days
                    'VisibilityTimeout': '30'  # 30 seconds
                }
            )
            queue_url = response['QueueUrl']
            logger.debug(f"Created SQS queue {queue_name}: {queue_url}")
            self.log_to_cloudwatch(f"Created SQS queue: {queue_name}")
        except Exception as e:
            logger.error(f"Error creating SQS queue {queue_name}: {str(e)}")
            self.log_to_cloudwatch(f"Error creating SQS queue {queue_name}: {str(e)}", level='ERROR')
            raise
        return queue_url

    def send_sqs_message(self, booking_id, user_email, booking_details):
        try:
            message_body = {
                'task_type': 'generate_qr',
                'booking_id': str(booking_id),
                'user_email': user_email,
                'booking_details': booking_details
            }
            response = self.sqs_client.send_message(
                QueueUrl=self.queue_url,
                MessageBody=json.dumps(message_body)
            )
            logger.debug(f"Sent SQS message: {response['MessageId']}")
            self.log_to_cloudwatch(f"Sent SQS message for booking {booking_id}: {response['MessageId']}")
            return response['MessageId']
        except Exception as e:
            logger.error(f"Error sending SQS message for booking {booking_id}: {str(e)}")
            self.log_to_cloudwatch(f"Error sending SQS message for booking {booking_id}: {str(e)}", level='ERROR')
            raise