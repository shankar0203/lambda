import boto3
import json
import os

def lambda_handler(event, context):
    region = os.environ['AWS_REGION']
    print('Lambda region: ', region)
    kms = boto3.client('kms', region_name=region)
