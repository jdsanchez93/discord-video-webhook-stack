import logging
import boto3
from botocore.exceptions import ClientError
import os
import argparse

parser = argparse.ArgumentParser("s3-upload")
parser.add_argument("file_name", help="Path to file that should be uploaded", type=str)
parser.add_argument("bucket_name", help="Name of s3 bucket", type=str)
args = parser.parse_args()

def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

upload_file(args.file_name, args.bucket_name)