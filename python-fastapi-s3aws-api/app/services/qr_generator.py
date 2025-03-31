import qrcode
from io import BytesIO


def generate_qr_code(url: str) -> BytesIO:
    """
    Generates a QR code from a given URL and returns it as a binary image stream.

    Args:
        url (str): The URL or data to encode in the QR code.

    Returns:
        BytesIO: A binary stream containing the PNG image of the generated QR code.

    Example:
        >>> qr_image = generate_qr_code("https://example.com")
        >>> with open("qr_code.png", "wb") as f:
        >>>     f.write(qr_image.getvalue())
    """
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    
    img_byte_arr = BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)
    
    return img_byte_arr
