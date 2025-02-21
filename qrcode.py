import pyqrcode
import png
from pyqrcode import QRCode


link = "https://jiramaru.github.io/cultural-day/"


img = pyqrcode.create(link)
img.png('qr_jc_esgae_2025.png', scale=8)
