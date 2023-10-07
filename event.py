import qrcode
from PIL import Image

object_details = "This is the object details you want to encode in the QR code."

qr = qrcode.QRCode(
    version=1,  # QR code version (adjust as needed)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level (adjust as needed)
    box_size=10,  # Size of each QR code box (adjust as needed)
    border=4,  # Border around the QR code (adjust as needed)
)

qr.add_data(object_details)
qr.make(fit=True)

# Create a QR code image
qr_code = qr.make_image(fill_color="black", back_color="white")
qr_code.save("object_qr_code.png")  # Change the filename and format as needed (e.g., .png, .jpg)
