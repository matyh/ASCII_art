from PIL import Image
import numpy as np


SOURCE = '../media/IMG_20191023_065955.jpg'
CHAR_MATRIX = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"  # len = 65


pic: Image.Image = Image.open(SOURCE)
print("Image loaded successfully!")
w, h = pic.size
pic = pic.resize((round(560), round(560 / w * h)), Image.ANTIALIAS)
w, h = pic.size
print(f"Pixel matrix size: {w} x {h}")


pixels = list(pic.getdata())
pixels = [pixels[i * w:(i + 1) * w] for i in range(h)]

# print(pixels)

brightness = []
for x in range(h):
    line = []
    for y in range(w):
        r,g,b = pixels[x][y]
        res = 0.21 * r + 0.72 * g + 0.07 * b  # luminosity
        # res = (r + g + b) / 3  # average
        # normalize to fit in the CHAR_MATRIX scale
        line.append(round(res / 255 * len(CHAR_MATRIX)))
    brightness.append(line)
# print(brightness)

char_list = [list(map(lambda x: 2 * CHAR_MATRIX[x-1], i)) for i in brightness]
# print(char_list)

for i in char_list:
    print(''.join(i))
