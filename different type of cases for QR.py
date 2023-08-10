import qrcode
from PIL import Image

qr=qrcode.QRCode(version=12,
                 error_correction=qrcode.constants.ERROR_CORRECT_H ,
                 box_size=10, border=4,)
qr.add_data("https://github.com/suyashftr")
qr.make(fit=True)
image=qr.make_image(fill_color="blue",background_color="white")
image.save("linkedIn_diff_cases.png")