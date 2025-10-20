import random
import string
import qrcode
from PIL import Image
import io


def generate_code(length=10):
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choices(chars, k=length))

def generate_qr_and_show(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")


    img.show()


if __name__ == "__main__":
    code = generate_code()
    print(f"Generated Code: {code}")
    generate_qr_and_show(code)

