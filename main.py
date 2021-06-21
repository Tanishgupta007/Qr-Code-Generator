import pyqrcode
import png
from pyqrcode import QRCode
import random
print("Enter: ")
s = input("")
a = ("[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+")
i = random(a)
url = pyqrcode.create(s)
url.svg(f"myqr{i}.svg", scale=8)
url.png(f"myqr{i}.png", scale=6)
input('enter to exit')
