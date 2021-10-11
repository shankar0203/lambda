# get the state of ec2 instance and also send the state of ec2 machine to subscribers through SNS

import json
import boto3

def lambda_handler(event, context):
    ec2_instance=boto3.resource("ec2" ,'us-east-1')
    sns_client=boto3.client('sns', 'us-east-1')
    my_instance=ec2_instance.Instance('i-09d2c4ed2e32cf4cc')
    print (my_instance.state['Name'])
    
    sns_client.publish(TargetArn="ARN" ,Message= my_instance.state['Name'])
