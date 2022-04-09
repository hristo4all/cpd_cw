import logging
import boto3
from botocore.exceptions import ClientError
import os
import glob

images = glob.glob("/home/ec2-user/environment/images/*.jpg") + glob.glob("/home/ec2-user/environment/images/*.png")
FOLDER_NAME = "images/"
s3_client = boto3.client('s3')

try:
  #response = s3_client.upload_file(file_name, bucket, object_name)
  for filename in images:
    object_name = os.path.basename(filename)
    print("Putting %s as %s" % (filename,object_name))
    s3_client.upload_file(filename, bucket, object_name)
            
except ClientError as e:
  logging.error(e)
