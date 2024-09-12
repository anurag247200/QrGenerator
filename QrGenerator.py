#First install the package qrcode[pil] using command "pip install qrcode[pil]"
import qrcode
from PIL import Image

# Data to be encoded
data = "https://www.example.com"

# Create a QR Code object
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Add data to the QR Code object
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill='black', back_color='white')

# Display the image
img.show()
