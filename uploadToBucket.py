import logging
import boto3
from botocore.exceptions import ClientError
import os
import glob
import time
import json

def upload_file(bucket='s2030512', object_name=None):
    
    images = glob.glob("images/*.jpg") + glob.glob("images/*.png")
    FOLDER_NAME = "images/"

    if not images:
        print("images is empty")

    # Upload the file
    s3_client = boto3.client('s3', region_name='us-east-1')
    try:
        for filename in images:

            object_name = os.path.basename(filename)
            print("Putting %s as %s" % (filename, object_name))
            s3_client.upload_file(filename, bucket, object_name)
            message = {"key":object_name,"bucket":bucket}
            sns_client = boto3.client('sns',region_name='us-east-1')
            sns_response = sns_client.publish(
                    TopicArn='arn:aws:sns:us-east-1:481685060162:topic_s2030512',
                    Message=json.dumps({'default': json.dumps(message)}),
                    MessageStructure='json'
                    )
            #print(response)
            time.sleep(30)
    except ClientError as e:
        logging.error(e)
    return False
    return True


upload_file()
