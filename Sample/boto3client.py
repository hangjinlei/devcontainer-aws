import boto3
import os


def create_client(
    service: str,
    region_name: str,
    endpoint_url: str,
    aws_access_key_id: str,
    aws_secret_access_key: str,
):

    return boto3.client(
        service,
        region_name=region_name,
        endpoint_url=endpoint_url,
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
    )


def create_dynamodb_client():

    region_name = "localhost"
    endpoint_url = os.environ.get("DYNAMODB_ENDPOINT")
    aws_access_key_id = "7romlc"
    aws_secret_access_key = "w8ykc"

    # region_name = os.environ.get("AWS_REGION")
    # endpoint_url = os.environ.get("DYNAMODB_ENDPOINT")
    # aws_access_key_id = os.environ.get("AWS_ACCESS_KEY_ID")
    # aws_secret_access_key = os.environ.get("AWS_SECRET_ACCESS_KEY")

    return create_client(
        "dynamodb",
        region_name=region_name,
        endpoint_url=endpoint_url,
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
    )


def create_dynamodb_resource():

    region_name = "localhost"
    endpoint_url = os.environ.get("DYNAMODB_ENDPOINT")
    aws_access_key_id = "7romlc"
    aws_secret_access_key = "w8ykc"

    return boto3.resource(
        "dynamodb",
        region_name=region_name,
        endpoint_url=endpoint_url,
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
    )


def create_sqs_client():

    region_name = os.environ.get("AWS_REGION")
    endpoint_url = os.environ.get("AWS_ENDPOINT")
    aws_access_key_id = os.environ.get("AWS_ACCESS_KEY_ID")
    aws_secret_access_key = os.environ.get("AWS_SECRET_ACCESS_KEY")

    return create_client(
        "sqs",
        region_name=region_name,
        endpoint_url=endpoint_url,
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
    )
