import boto3
import os
import sys

if __name__=="__main__":
    session = boto3.Session(
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID", ""),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY", "")
    )

    try:
        s3 = session.resource('s3')
    except Exception as e:
        print(f"[-] Error: Connection: {e}")
        sys.exit(-1)

    bucket_name = "terraform-demo-choilab"
    upload_filename = "helloworld.txt"
    txt_data = b'hello world'
    object = s3.Object(bucket_name, upload_filename)

    try:    
        result = object.put(Body=txt_data)
    except Exception as e:
        print(f"[-] error: fileupload: {e}")
        sys.exit(-1)

    print("done")