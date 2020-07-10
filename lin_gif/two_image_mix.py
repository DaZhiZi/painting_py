from utils import (
    log,
    formatted_image,
    new_image,
)
from PIL import (
    Image,
    ImageFont,
    ImageDraw,
    ImageFilter,
)

import math, cmath


def colors_of_mutltiply(colors1, colors2):
    r = colors1[0] / 255
    g = colors1[1] / 255
    b = colors1[2] / 255
    x = colors2[0] / 255
    y = colors2[1] / 255
    z = colors2[2] / 255
    R = r * x * 255
    G = g * y * 255
    B = b * z * 255
    A = colors1[3]
    return (int(R), int(G), int(B), int(A))
    pass


def mutltiply(img1, img2):
    w, h = img1.size
    image = new_image(w, h)
    for i in range(w):
        for j in range(h):
            position = (i, j)
            colors1 = img1.getpixel(position)
            colors2 = img2.getpixel(position)
            new_colors = colors_of_mutltiply(colors1, colors2)
            image.putpixel(position, new_colors)
    # image.save('mutltiply.png')
    # image.show()
    return image


def colors_of_maximage(colors1, colors2):
    R = max(colors1[0], colors2[0])
    G = max(colors1[1], colors2[1])
    B = max(colors1[2], colors2[2])
    A = colors1[3]
    return (int(R), int(G), int(B), int(A))
    pass


def maximage(img1, img2):
    w, h = img1.size
    image = new_image(w, h)
    for i in range(w):
        for j in range(h):
            position = (i, j)
            colors1 = img1.getpixel(position)
            colors2 = img2.getpixel(position)
            new_colors = colors_of_maximage(colors1, colors2)
            image.putpixel(position, new_colors)
    image.save('maximage.png')
    image.show()
    # return image

def colors_of_miniimage(colors1, colors2):
    R = min(colors1[0], colors2[0])
    G = min(colors1[1], colors2[1])
    B = min(colors1[2], colors2[2])
    A = colors1[3]
    return (int(R), int(G), int(B), int(A))
    pass


def minimage(img1, img2):
    w, h = img1.size
    image = new_image(w, h)
    for i in range(w):
        for j in range(h):
            position = (i, j)
            colors1 = img1.getpixel(position)
            colors2 = img2.getpixel(position)
            new_colors = colors_of_miniimage(colors1, colors2)
            image.putpixel(position, new_colors)
    image.save('mini.png')
    image.show()
    # return image


def test_images():
    img1 = formatted_image('cxk.png')
    img2 = formatted_image('aiky.jpg')
    # mutltiply(img1, img2)
    # maximage(img1, img2)
    minimage(img1, img2)
    pass


def main():
    test_images()
    pass


if __name__ == '__main__':
    main()
