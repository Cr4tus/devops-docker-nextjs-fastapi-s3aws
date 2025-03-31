import os
from dotenv import load_dotenv


load_dotenv(dotenv_path="/Users/dsabau/.personal/devops-docker-kubernetes-fastapi-nextjs-s3aws/python-fastapi-s3aws-api/.env.local")


DEFAULT_LOG_MESSAGE_FORMAT = os.getenv("DEFAULT_LOG_MESSAGE_FORMAT")

ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS").split('|')

AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")
