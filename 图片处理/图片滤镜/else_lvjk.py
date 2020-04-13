from utils import (
    log,
    random_num,
    floor,
    formatted_image,
)
from PIL import (
    Image,
    ImageFont,
    ImageDraw,
    ImageFilter,
)


def new_image(w, h):
    return Image.new('RGBA', (w, h))


def colors_of_no_color(colors):
    r = colors[0]
    g = colors[1]
    b = colors[2]
    a = colors[3]
    gray = (r * 30 + g * 59 + b * 11) / 100
    R = gray
    G = gray
    B = gray
    A = a
    return (int(R), int(G), int(B), int(A))


def no_color(image):
    w, h = image.size
    log('w h no_color', w, h)
    img = new_image(w, h)
    for i in range(w):
        for j in range(h):
            position = (i, j)
            colors = image.getpixel(position)
            new_colors = colors_of_no_color(colors)
            # log('new_colors', new_colors)
            img.putpixel(position, new_colors)
    # img.save('no_color.png')
    # img.show()
    return img


def test_no_color():
    image = formatted_image('cemo.jpg')
    no_color(image)
    pass


def colors_of_fjsedn(colors):
    r = colors[0]
    g = colors[1]
    b = colors[2]
    a = colors[3]
    R = 255 - r
    G = 255 - g
    B = 255 - b
    A = a
    return (int(R), int(G), int(B), int(A))


def fjsedn(image):
    w, h = image.size
    log('w h 反色调', w, h)
    img = new_image(w, h)
    image = no_color(image)
    for i in range(w):
        for j in range(h):
            position = (i, j)
            colors = image.getpixel(position)
            new_colors = colors_of_fjsedn(colors)
            # log('new_colors', new_colors)
            img.putpixel(position, new_colors)
    # img.save('fjseqn.png')
    # img.show()
    return img


def test_fjsedn():
    image = formatted_image('cemo.jpg')
    fjsedn(image)
    pass


def gcsi(image):
    image = fjsedn(image)
    img = image.filter(ImageFilter.GaussianBlur(radius=2))
    # image.save('gcsi.png')
    # image.show()
    return img


def test_gcsi():
    image = formatted_image('davizi.jpg')
    gcsi(image)
    pass


# B colors2
# A colors1
# 以下的if else语句是为了实现公式 A +（A×B）/（255-B），
# 为了说明公式 A +（A×B）/（255-B）暂记作 temp
# 其中 255-B 如果为0，需要特殊考虑
# 以下三行为了实现min(temp, 255)
def coculator_color(num1, num2):
    r = 0
    if (255 - num2) == 0:
        r = num1
    else:
        r = num1 + (num1 * num2) / (255 - num2)
    return min(r, 255)


def colors_of_sumn(colors1, colors2):
    r = coculator_color(colors1[0], colors2[0])
    g = coculator_color(colors1[1], colors2[1])
    b = coculator_color(colors1[2], colors2[2])
    a = colors1[3]
    R = r
    G = g
    B = b
    A = a
    return (int(R), int(G), int(B), int(A))


def sumn(image):
    # image是计算公式中的C
    w, h = image.size
    log('w sumn', w, h)
    img = new_image(w, h)
    #   quse是计算公式中的A
    q = no_color(image)
    #  gcsi为计算公式中的B
    g = gcsi(image)
    for i in range(w):
        for j in range(h):
            position = (i, j)
            colors1 = q.getpixel(position)
            colors2 = g.getpixel(position)
            new_colors = colors_of_sumn(colors1, colors2)
            # log('new_colors', new_colors)
            img.putpixel(position, new_colors)
    # img.save('sumn.png')
    # img.show()
    return image


def test_sumn():
    image = formatted_image('davizi.jpg')
    sumn(image)


def colorful(image):
    w, h = image.size
    log('w h coloful', w, h)
    img = new_image(w, h)
    #  image是计算公式中的A
    q = image
    #  gcsi为计算公式中的B
    g = gcsi(image)
    for i in range(w):
        for j in range(h):
            position = (i, j)
            colors1 = q.getpixel(position)
            colors2 = g.getpixel(position)
            new_colors = colors_of_sumn(colors1, colors2)
            # log('new_colors', new_colors)
            img.putpixel(position, new_colors)
    img.save('colorful.png')
    img.show()
    # return image


def test_colorful():
    image = formatted_image('davizi.jpg')
    colorful(image)


def positions_of_ghost(i, j, length):
    l = length
    offset = 10

    li = i + offset
    if li > (l - 1):
        li = l - 1

    ri = i - offset
    if ri < 0:
        ri = 0

    position1 = (li, j)  # w
    position2 = (ri, j)  # w
    return (position1, position2)


def coculator_ghost(c1, c2, c3, c4):
    return (c1 + c2 + c3 + c4) / 4


def colors_of_ghost(colors1, colors2, colors3, colors4):
    r = coculator_ghost(colors1[0], colors2[0], colors3[0], colors4[0])
    g = coculator_ghost(colors1[1], colors2[1], colors3[1], colors4[1])
    b = coculator_ghost(colors1[2], colors2[2], colors3[2], colors4[2])
    a = coculator_ghost(colors1[3], colors2[3], colors3[3], colors4[3])
    R = r
    G = g
    B = b
    A = a
    return (int(R), int(G), int(B), int(A))
    pass


def ghost(image):
    w, h = image.size
    log('w h ghost', w, h)
    img = new_image(w, h)
    for i in range(0, w):
        for j in range(0, h):
            position = (i, j)
            # postions
            p1, p2 = positions_of_ghost(i, j, w)
            p3, p4 = positions_of_ghost(i, j, h)
            c1 = image.getpixel(p1)
            c2 = image.getpixel(p2)
            c3 = image.getpixel(p3)
            c4 = image.getpixel(p4)
            new_colors = colors_of_ghost(c1, c2, c3, c4)
            img.putpixel(position, new_colors)
    img.save('ghost.png')
    img.show()
    # return img


def test_ghost():
    image = formatted_image('davizi.jpg')
    ghost(image)


def test():
    # test_no_color()
    # test_fjsedn()
    # test_fjsedn()
    # test_gcsi()
    # test_sumn()
    # test_colorful()
    test_ghost()


def main():
    pass


if __name__ == '__main__':
    main()
