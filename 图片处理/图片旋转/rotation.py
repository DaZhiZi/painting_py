from utils import (
    log,
    formatted_image,
    new_image,
)


def position_of_rotate_left(position, w, h):
    i, j = position
    # (i, j) 坐标旋转 90 度 相对原点坐标为 矩形中心
    # 特殊处理
    w -= 1
    x = j
    y = w - i
    return (x, y)
    pass


def rotate_left(image):
    w, h = image.size
    # log('w h rotate_left', w, h)
    img = new_image(h, w)
    # log('new_image', img.size)
    for i in range(w):
        for j in range(h):
            position = (i, j)
            new_position = position_of_rotate_left(position, w, h)
            # log('new_position',new_position)
            colors = image.getpixel(position)
            img.putpixel(new_position, colors)
    # img.save('rotate_left.png')
    # img.show()
    return img
    pass


def position_of_rotate_right(position, w, h):
    i, j = position
    # (i, j) 坐标旋转 90 度 相对原点坐标为 矩形中心
    # 特殊处理
    h -= 1
    x = h - j
    y = i
    return (x, y)
    pass


def rotate_right(image):
    w, h = image.size
    # log('w h rotate_left', w, h)
    img = new_image(h, w)
    # log('new_image', img.size)
    for i in range(w):
        for j in range(h):
            position = (i, j)
            new_position = position_of_rotate_right(position, w, h)
            # log('new_position',new_position)
            colors = image.getpixel(position)
            img.putpixel(new_position, colors)
    img.save('rotate_right.png')
    img.show()
    # return img


def position_of_rotate_180(position, w, h):
    i, j = position
    # (i, j) 坐标旋转 90 度 相对原点坐标为 矩形中心
    # 特殊处理
    w -= 1
    h -= 1
    x = w - i
    y = h - j
    return (x, y)
    pass


def rotate_180(image):
    w, h = image.size
    # log('w h rotate_left', w, h)
    img = new_image(w, h)
    # log('new_image', img.size)
    for i in range(w):
        for j in range(h):
            position = (i, j)
            new_position = position_of_rotate_180(position, w, h)
            # log('new_position',new_position)
            colors = image.getpixel(position)
            img.putpixel(new_position, colors)
    img.save('rotate_180.png')
    img.show()
    # return img


# image 原图
# img   新图
def rotate_image(image, img, w, h):
    for i in range(w):
        for j in range(h - 25):
            position = (i, j)
            new_position = position_of_rotate_180(position, w, h)
            # log('new_position',new_position)
            colors = image.getpixel(position)
            img.putpixel(new_position, colors)
    pass


def rotate_word(image, img, w, h):
    for i in range(w):
        for j in range(h - 25 + 1, h):
            position = (i, j)
            new_position = (i, j - (h - 25))
            # new_position = position_of_rotate_180(position, w, 25)
            # log('new_position',new_position)
            colors = image.getpixel(position)
            img.putpixel(new_position, colors)
    pass


def rotate(image):
    w, h = image.size
    img = new_image(w, h)
    # log('new_image', img.size)
    rotate_image(image, img, w, h)
    rotate_word(image, img, w, h)
    img.save('rotate.png')
    img.show()
    # return img


def test_rotation():
    log('test rotation left')
    image = formatted_image('dog.jpg')
    # rotate_left(image)
    # rotate_right(image)
    # rotate_180(image)
    rotate(image)


def main():
    test_rotation()
    pass


if __name__ == '__main__':
    main()
