send the file to s3-bucket

import pandas as pd
import boto3 s3 = boto3.client('s3') 
def lambda_handler(event, context):
    # Create a DataFrame
    data = {'Name': ['John', 'Jane', 'Jim', 'Joan'],
            'Age': [30, 28, 31, 35],
            'Country': ['USA', 'Canada', 'UK', 'Australia']}
    df = pd.DataFrame(data)
    # Write the DataFrame to an Excel sheet
    writer = pd.ExcelWriter('/tmp/example.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1', index=False)
    writer.save()
    # Upload the Excel sheet to an S3 bucket
    s3.upload_file('/tmp/example.xlsx', 'ashok11', 'example.xlsx')
    return 'Excel sheet uploaded to S3'
