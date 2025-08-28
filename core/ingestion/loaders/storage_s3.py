# pip install boto3
from pathlib import Path
from typing import Union
import boto3


class S3Storage:
    def __init__(self, region_name: str | None = None, endpoint_url: str | None = None):
        self.client = boto3.client("s3", region_name=region_name, endpoint_url=endpoint_url)

    def put_object(self, bucket: str, key: str, file_path: Union[str, Path], content_type: str) -> str:
        self.client.upload_file(
            Filename=str(file_path),
            Bucket=bucket,
            Key=key,
            ExtraArgs={"ContentType": content_type},
        )
        return f"s3://{bucket}/{key}"
