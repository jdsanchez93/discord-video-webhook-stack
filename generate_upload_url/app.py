import json
import boto3
import uuid
import os
import requests


def lambda_handler(event, context):
    """Sample pure Lambda function

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """
    bucketName = event['Records'][0]['s3']['bucket']['name']
    objectKey = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])
    clipUrl = "https://" + bucket+ ".s3.us-west-1.amazonaws.com/" + key

    webhookUrl = os.environ['webhookUrl']

    options = {method: 'POST', headers: {'Content-Type': 'application/json', 'Content-Length': dataString.length}}
    res = requests.post(webhookUrl, json = options)