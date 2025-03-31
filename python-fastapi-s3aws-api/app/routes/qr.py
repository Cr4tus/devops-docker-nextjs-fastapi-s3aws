import logging
from fastapi import APIRouter, HTTPException

from services.qr_generator import generate_qr_code
from services.s3_aws import upload_to_s3


_logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("/generate-qr/")
async def generate_qr(url: str) -> dict[str, str]:
    """
    Generates a QR code from the provided URL, uploads it to S3, 
    and returns the publicly accessible S3 URL.

    Args:
        url (str): The URL to encode in the QR code.

    Returns:
        dict: A dictionary containing the S3 URL of the uploaded QR code.

    Raises:
        HTTPException: If the upload fails, returns a 500 status with an error message.
    """

    img_byte_arr = generate_qr_code(url)
    file_name = f"qr_codes/{url.split('//')[-1]}.png"
    s3_url = upload_to_s3(file_name, img_byte_arr)

    if s3_url is None:
        _logger.error(f"Failed to upload QR code to S3 bucket for URL: {url}")
        raise HTTPException(status_code=500, detail="Failed to upload QR code to the S3 bucket.")
    
    return {"qr_code_url": s3_url}
