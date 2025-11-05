import os, pandas as pd, boto3
from io import StringIO

AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_BUCKET = "superstore-processed-data"
REGION_NAME = "us-east-1"

df = pd.read_csv("data/Superstore.csv").dropna(subset=["Sales","Profit"])
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Profit Margin (%)"] = round(df["Profit"]/df["Sales"]*100,2)

summary = (df.groupby("Region")[["Sales","Profit"]].sum().reset_index())

buffer = StringIO()
summary.to_csv(buffer,index=False)

s3 = boto3.client("s3",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=REGION_NAME)
s3.put_object(Bucket=AWS_BUCKET, Key="region_summary.csv", Body=buffer.getvalue())
print("✅ Uploaded region_summary.csv to S3")
