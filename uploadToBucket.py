import logging
# import boto3
# from botocore.exceptions import ClientError
import os
import glob
import time


def upload_file(file_name="images/image1.jpg", bucket='s2030512', object_name=None):

    images = glob.glob("images/*.jpg") + glob.glob("images/*.png")
    FOLDER_NAME = "images/"
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)
    if not images:
        print("images is empty")
    print(images)

    # Upload the file
    # s3_client = boto3.client('s3')
    # try:
    # response = s3_client.upload_file(file_name, bucket, object_name)
    for filename in images:

        # object_name = os.path.basename(filename)
        print("Putting %s as %s" % (filename, object_name))
    # s3_client.upload_file(filename, bucket, object_name)
    # time.sleep(30)
    # except ClientError as e:
    # logging.error(e)
    return False
    return True


upload_file()
