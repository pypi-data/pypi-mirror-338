# setup.py
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="parking-utils-aec",
    version="0.1.7",
    author="Harish Challa",
    author_email="x23417498@student.ncirl.ie",
    description="A utility library for parking applications with AWS integration",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[
        "Pillow==10.4.0",
        "boto3==1.37.23",
        "tenacity==9.0.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9,<3.14",
)