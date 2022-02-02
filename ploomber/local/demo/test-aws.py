import boto3
import os

os.environ['AWS_PROFILE'] = "Profile1"
os.environ['AWS_DEFAULT_REGION'] = "eu-west-1"

s3 = boto3.client('s3', region_name='eu-west-1')
print("[INFO:] Connecting to cloud")

# Retrieves all regions/endpoints that work with S3

response = s3.list_buckets()
print('Regions:', response)