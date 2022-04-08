#list the instance based on the tag and also running state and publish the output to sns topic
import boto3
import json
import logging
import datetime 
import os
from botocore.exceptions import ClientError
from datetime import timedelta

region ='us-east-1'
ec2 = boto3.resource('ec2',region)
client = boto3.client('ec2',region)
snsClient = boto3.client('sns',region)

def lambda_handler(event, context):
    global start
    filters = [{
         'Name': 'tag:Name',
         'Values': ['cw']
       },
       {
           'Name': 'instance-state-name',
           'Values': ['running']
       }
       ]
    start = ec2.instances.filter(Filters=filters)
    for instances in start:
        print('Ec2 Instances which are Running: ', 'Instance ID: ', instances.id, 'Instance state: ', instances.state, 'Instance type: ',instances.instance_type)
    publish_sns()
def publish_sns():
    print('publish msg')
    subject_str = 'Alert! EC2 Instances Running'
    affected_instances = [instances.id for instances in start]
    DT = datetime.datetime.now() + timedelta(hours = 5.5)
    Waqt = DT.strftime("%Y-%m-%d %H:%M:%S")
    msg = '.....\n\nHello Team, \n\nFollowing EC2 instances have been launched through the RG:\n\nRunning instances: \n'+str(affected_instances)+'\n\nInstance state changed time IST: '+str(Waqt)+'\n\n.....'
    response = snsClient.publish(TopicArn="arn:aws:sns:us-east-1:484479102124:s-demo-ses-topic", Message=msg, Subject=subject_str)
