import boto3

s3 = boto3.client("s3")

bucket = "test-070306-jv" 

s3.upload_file("vacantes_bi.json", bucket, "vacantes_bi.json")
print("archivo subido")
