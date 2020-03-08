from typing import List

from PIL import Image
import numpy as np


SOURCE = '../media/IMG_20191029_064400.jpg'
CHAR_MATRIX = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"  # len = 65


def load_image():
    pic: Image.Image = Image.open(SOURCE)
    print("Image loaded successfully!")
    return pic


def resize_image(original_picture: Image.Image, target_width: int=0, target_height: int=0) -> Image.Image:
    ori_w, orig_h = original_picture.size
    if target_width and target_height:
        pic = original_picture.resize((target_width, target_width), Image.ANTIALIAS)
    elif target_width and not target_height:
        pic = original_picture.resize((target_width, round(target_width / ori_w * orig_h)), Image.ANTIALIAS)
    elif target_height and not target_width:
        pic = original_picture.resize((round(target_height * ori_w / orig_h), round(target_height)), Image.ANTIALIAS)
    return pic


def pixel_extractor(pic: Image.Image) -> List[List]:
    w, h = pic.size
    pixels = list(pic.getdata())
    pixels = [pixels[i * w:(i + 1) * w] for i in range(h)]
    return pixels


def convert_to_brightness(pix_array: List[List]):
    w = len(pix_array)
    h = len(pix_array[0])
    brightness = []
    for line in pix_array:
        bri = []
        for pixel in line:
            r, g, b = pixel
            level = 0.21 * r + 0.72 * g + 0.07 * b  # luminosity
            # bri = (r + g + b) / 3  # average
            # normalize to fit in the CHAR_MATRIX scale
            bri.append(round(level / 255 * len(CHAR_MATRIX)))
        brightness.append(bri)
    return brightness




def make_pic(bri_array: list):
    f = open('new.txt', 'w')
    char_list = [list(map(lambda x: 2 * CHAR_MATRIX[x-1], i)) for i in bri_array]
    for i in char_list:
        # print(''.join(i))
        f.write(''.join(i) + '\n')


img = load_image()
img = resize_image(img, 560)
pixels = pixel_extractor(img)
brig = convert_to_brightness(pixels)
make_pic(brig)

