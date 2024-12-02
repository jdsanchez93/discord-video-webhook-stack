
import os
import requests

def lambda_handler(event, context):
    bucketName = event['Records'][0]['s3']['bucket']['name']
    objectKey = event['Records'][0]['s3']['object']['key']
    region = event['Records'][0]['awsRegion']
    clipUrl = "https://" + bucketName + ".s3." + region + ".amazonaws.com/" + objectKey
    webhookUrl = os.environ['WEBHOOK_URL']
    # e.g. the filename
    message = objectKey.rsplit("/", 1)[-1]
    maskedLink = "[" + message + "](" + clipUrl + ")"
    
    data = {
        'content': maskedLink
    }
    headers = {'Content-type': 'application/json'}

    r = requests.post(webhookUrl, json=data, headers=headers)
    print(r.status_code)