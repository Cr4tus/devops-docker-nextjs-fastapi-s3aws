import boto3
import logging

from configs.constants import (
    AWS_ACCESS_KEY,
    AWS_SECRET_KEY,
    S3_BUCKET_NAME
)


_logger = logging.getLogger(__name__)

__s3_client = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY
)

def upload_to_s3(file_name: str, file_content, content_type="image/png") -> str | None:
    """
    Uploads a file to an Amazon S3 bucket.

    Args:
        file_name (str):                The name of the file.
        file_content:                   The file content as a binary stream (e.g., a BytesIO object).
        content_type (str, optional):   The MIME type of the file. Defaults to "image/png".

    Returns:
        str | None: The public URL of the uploaded file if successful, otherwise None.
    
    Example:
        >>> from io import BytesIO
        >>> file_content = BytesIO(b'test content')
        >>> upload_to_s3("uploads/test.txt", file_content, "text/plain")
        'https://your-bucket.s3.amazonaws.com/uploads/test.txt'
    """

    try:
        __s3_client.put_object(
            Bucket=S3_BUCKET_NAME,
            Key=file_name,
            Body=file_content,
            ContentType=content_type,
            ACL='public-read'
        )

        return f"https://{S3_BUCKET_NAME}.s3.amazonaws.com/{file_name}"
    
    except Exception as e:
        _logger.error(f"Failed to upload file to S3 bucket because:\n{e}", exc_info=True)
        return None
