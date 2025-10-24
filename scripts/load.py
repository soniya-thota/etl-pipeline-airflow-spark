import boto3

def load_to_s3(df, bucket_name, key):
    s3 = boto3.client('s3')
    df.to_csv('/tmp/final_output.csv', index=False)
    s3.upload_file('/tmp/final_output.csv', bucket_name, key)
    print(f"Data loaded to s3://{bucket_name}/{key}")
