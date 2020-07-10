from utils import (
    log,
    random_num,
    floor,
    text,
)
from PIL import (
    Image,
    ImageFont,
    ImageDraw,
    ImageFilter
)


def colors_of_gray(colors):
    r = colors[0]
    g = colors[1]
    b = colors[2]
    gray = (colors[0] + colors[1] + colors[2]) / 3
    R = gray
    G = gray
    B = gray
    return (int(R), int(G), int(B))


def grayscale(img):
    w, h = img.size
    for i in range(w):
        for j in range(h):
            position = (i, j)
            # log("position", position)
            colors = img.getpixel(position)
            # log('colors', colors)
            new_colors = colors_of_gray(colors)
            img.putpixel(position, new_colors)
    # text('lin 聚聚!!!', img)
    img.save('grayscale.png')
    img.show()


def position_of_frosted_glass(position):
    i, j = position
    index = random_num(0, 8)
    x = i + index
    y = j + index
    new_position = (x, y)
    return new_position


def frosted_glass(img):
    img = img.convert('RGBA')  # 修改颜色通道为RGBA
    w, h = img.size
    for i in range(w - 8):
        for j in range(h - 8):
            position = (i, j)
            new_position = position_of_frosted_glass(position)
            colors = img.getpixel(new_position)
            img.putpixel(position, colors)
    # text('lin 聚聚!!!', img)
    img.save('frosted_glass.png')
    img.show()


def position_of_mosaic(position):
    n = 10  # 每块 10 px
    i, j = position
    x = floor(i / n) * n
    y = floor(j / n) * n
    new_position = (x, y)
    return new_position


def mosaic(img):
    w, h = img.size
    for i in range(w):
        for j in range(h):
            position = (i, j)
            new_position = position_of_mosaic(position)
            colors = img.getpixel(new_position)
            # log('colors', colors)
            img.putpixel(position, colors)
    # text('lin 聚聚!!!', img)
    img.save('mosaic.png')
    img.show()


def colors_of_comic_books(colors):
    r = colors[0]
    g = colors[1]
    b = colors[2]
    R = abs(g - b + g + r) * r / 256
    G = abs(b - g + b + r) * r / 256
    B = abs(b - g + b + r) * g / 256
    return (int(R), int(G), int(B))


def comic_books(img):
    w, h = img.size
    for i in range(w):
        for j in range(h):
            position = (i, j)
            colors = img.getpixel(position)
            new_colors = colors_of_comic_books(colors)
            img.putpixel(position, new_colors)
    # text('lin 聚聚!!!', img)
    img.save('comic_books.png')
    img.show()


def colors_of_negative(colors):
    r = colors[0]
    g = colors[1]
    b = colors[2]
    R = 255 - r
    G = 255 - g
    B = 255 - b
    return (int(R), int(G), int(B))


def negative(img):
    w, h = img.size
    for i in range(w):
        for j in range(h):
            position = (i, j)
            # log("position", position)
            colors = img.getpixel(position)
            # log('colors', colors)
            new_colors = colors_of_negative(colors)
            img.putpixel(position, new_colors)
    # text('lin 聚聚!!!', img)
    img.save('negative.png')
    img.show()


def colors_of_dark(colors):
    r = colors[0]
    g = colors[1]
    b = colors[2]
    R = r * 128 / (g + b + 1)
    G = g * 128 / (r + b + 1)
    B = b * 128 / (g + r + 1)
    return (int(R), int(G), int(B))


def dark(img):
    w, h = img.size
    for i in range(w):
        for j in range(h):
            position = (i, j)
            colors = img.getpixel(position)
            dark_colors = colors_of_dark(colors)
            img.putpixel(position, dark_colors)
    # text('lin 聚聚!!!', img)
    img.save('dark.png')
    img.show()


def colors_of_black_white(colors):
    r = colors[0]
    g = colors[1]
    b = colors[2]
    gray = (r + g + b) / 3
    if gray >= 100:
        gray = 255
    else:
        gray = 0
    R = gray
    G = gray
    B = gray
    return (int(R), int(G), int(B))


def black_white(img):
    w, h = img.size
    for i in range(w):
        for j in range(h):
            position = (i, j)
            # log("position", position)
            colors = img.getpixel(position)
            # log('colors', colors)
            new_colors = colors_of_black_white(colors)
            img.putpixel(position, new_colors)
    # text('lin 聚聚!!!', img)
    img.save('black_white.png')
    img.show()


# 怀旧
def colors_of_nostalgia(colors):
    r = colors[0]
    g = colors[1]
    b = colors[2]
    R = 0.393 * r + 0.769 * g + 0.189 * b
    G = 0.349 * r + 0.686 * g + 0.168 * b
    B = 0.272 * r + 0.534 * g + 0.131 * b
    return (int(R), int(G), int(B))


def nostalgia(img):
    w, h = img.size
    for i in range(w):
        for j in range(h):
            position = (i, j)
            # log("position", position)
            colors = img.getpixel(position)
            # log('colors', colors)
            new_colors = colors_of_nostalgia(colors)
            img.putpixel(position, new_colors)
    # text('lin 聚聚!!!', img)
    img.save('怀旧.png')
    img.show()


def colors_of_frozen(colors):
    r = colors[0]
    g = colors[1]
    b = colors[2]
    R = (r - g - b) * 3 / 2
    G = (g - r - b) * 3 / 2
    B = (b - g - r) * 3 / 2
    return (int(R), int(G), int(B))


def frozen(img):
    w, h = img.size
    for i in range(w):
        for j in range(h):
            position = (i, j)
            colors = img.getpixel(position)
            new_colors = colors_of_frozen(colors)
            img.putpixel(position, new_colors)
    # text('lin 聚聚!!!', img)
    img.save('frozen.png')
    img.show()


def colors_of_fused_cast(colors):
    r = colors[0]
    g = colors[1]
    b = colors[2]
    R = r * 128 / (g + b + 1)
    G = g * 128 / (r + b + 1)
    B = b * 128 / (g + r + 1)
    return (int(R), int(G), int(B))


def fused_cast(img):
    w, h = img.size
    for i in range(w):
        for j in range(h):
            position = (i, j)
            colors = img.getpixel(position)
            new_colors = colors_of_fused_cast(colors)
            img.putpixel(position, new_colors)
    # text('lin 聚聚!!!', img)
    img.save('fused_cast.png')
    img.show()


def position_of_mboss(position, w, h):
    i, j = position
    x = i + 5
    if x > w:
        x = w
    y = j + 5
    if y > h:
        y = h
    new_position = (x, y)
    return new_position


def colors_of_mboss(colors1, colors2):
    r = abs(colors1[0] - colors2[0] + 128)
    b = abs(colors1[1] - colors2[1] + 128)
    g = abs(colors1[2] - colors2[2] + 128)
    if r > 255:
        r = 255
    if b > 255:
        b = 255
    if g > 255:
        g = 255
    gray = int((r + b + g) / 3)
    R = gray
    G = gray
    B = gray
    return (int(R), int(G), int(B))
    pass


def mboss(img):
    w, h = img.size
    for i in range(w - 5):
        for j in range(h - 5):
            position1 = (i, j)
            position2 = position_of_mboss(position1, w, h)
            colors1 = img.getpixel(position1)
            # log('colors1', colors1)
            colors2 = img.getpixel(position2)
            # log('colors2', colors2)
            new_colors = colors_of_mboss(colors1, colors2)
            # log('colors', gray_colors)
            img.putpixel(position1, new_colors)
    # text('lin 聚聚!!!', img)
    img.save('mboss.png')
    img.show()


def colors_of_no_color(colors):
    r = colors[0]
    g = colors[1]
    b = colors[2]
    gray = int((r * 30 + g * 59 + b * 11) / 100)
    R = gray
    G = gray
    B = gray
    return (int(R), int(G), int(B))


# 去色
def no_color(img):
    w, h = img.size
    log('w', w, 'h', h)
    for i in range(w):
        for j in range(h):
            position = (i, j)
            colors = img.getpixel(position)
            new_colors = colors_of_no_color(colors)
            img.putpixel(position, new_colors)
    # text('lin 聚聚!!!', img)
    img.save('去色.png')
    img.show()


def main():
    img = Image.open("davizi.png")
    # grayscale(img)
    # black_white(img)
    # negative(img)
    # frosted_glass(img)
    # mosaic(img)
    # nostalgia(img)
    # comic_books(img)
    # frozen(img)
    # fused_cast(img)
    # dark(img)
    # mboss(img)
    # no_color(img)


if __name__ == '__main__':
    main()
