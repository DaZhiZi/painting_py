from utils import (
    log,
)
from PIL import (
    Image,
)


def formatted_image(path):
    img = Image.open(path)
    # 注意由于不是每个图像都有 a 所以这里强制转换成 RGBA 格式
    img = img.convert('RGBA')
    return img

def new_image(w, h):
    return Image.new('RGBA', (w, h))


def is_equal(value1, value2):
    return value1 - value2 < 10


def colors_equal(colors1, colors2):
    c1 = colors1
    c2 = colors2
    r = is_equal(c1[0], c2[0])
    b = is_equal(c1[1], c2[1])
    g = is_equal(c1[2], c2[2])
    a = is_equal(c1[3], c2[3])
    return r and b and g and a


def colors_of_compare(colors1, colors2, colors3=(255, 0, 0, 255)):
    # 填充 红色
    if colors_equal(colors1, colors2):
        return colors1
    else:
        return colors3
    pass


# image1 和 image2 默认 w , h 一样
def compare_image(image1, image2):
    w, h = image1.size
    img = new_image(w, h)
    for i in range(w):
        for j in range(h):
            position = (i, j)
            colors1 = image1.getpixel(position)
            colors2 = image2.getpixel(position)
            new_colors = colors_of_compare(colors1, colors2)
            # log('new_colors', new_colors)
            img.putpixel(position, new_colors)
    img.save('compare.png')
    img.show()
    pass


def test_compare():
    img1 = formatted_image('./images/big_buck_bunny_07501.png')
    img2 = formatted_image('./images/big_buck_bunny_07502.png')
    compare_image(img1, img2)


def main():
    test_compare()
    pass


if __name__ == '__main__':
    main()
