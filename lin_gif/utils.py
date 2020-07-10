import time


def log(*args, **kwargs):
    # time.time() 返回 unix time
    # 如何把 unix time 转换为普通人类可以看懂的格式呢？
    format = '%Y/%m/%d %H:%M:%S'
    value = time.localtime(int(time.time()))
    dt = time.strftime(format, value)
    print(dt, *args, **kwargs)


def ensure(condition, message):
    if not condition:
        log('xxxxx 测试失败', message)
    else:
        log('>>>>> 测试成功', message)


def isEquals(a, b, message):
    import json
    if json.dumps(a) == json.dumps(b):
        log('***  {} 测试成功, 大侄子牛逼呀'.format(message))
    else:
        log('xxxxx 测试失败 结果（{}）  预期（{}）, {}'.format(a, b, message))


import random


def random_num(num1, num2):
    return random.randint(num1, num2)


def load_file(file_path):
    p = file_path
    with  open(p, 'r') as f:
        data = f.read()
    # log('type data', type(data))
    return data


def floor(num):
    import math
    return math.floor(num)


def abs(num):
    if num < 0:
        return -num
    return num


def load_lines(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = f.readlines()
        return data


def formatted_image(path):
    from PIL import Image
    img = Image.open(path)
    # 注意由于不是每个图像都有 a 所以这里强制转换成 RGBA 格式
    img = img.convert('RGBA')
    return img


def new_image(w, h):
    from PIL import Image
    return Image.new('RGBA', (w, h))


from PIL import Image, ImageFont, ImageDraw

# w 402 h 431
def random_colors():
    r = random_num(1, 254)
    b = random_num(1, 254)
    g = random_num(1, 254)
    return (r, b, g)


def random_position(w, h):
    f = random_num(int(w / 10), int(w / 2))
    x = random_num(f, w - f)
    y = random_num(f, h - f)
    x = 20
    y = 20
    return (x, y)
    pass


def text(content, img):
    w, h = img.size

    size = int(h / 8)  # 字体大小

    color = random_colors()
    # x = w - size
    # y = 0
    (x, y) = random_position(w, h)
    coordinate = (x, y)  # 坐标
    txt = content
    # color = (256, 0, 0)  # 颜色
    draw_text(coordinate, txt, color, size, img)


def draw_text(coordinate, txt, color, size, img):
    draw = ImageDraw.Draw(img)
    # 确定字体格式和字体大小
    font = ImageFont.truetype("C:\\WINDOWS\\Fonts\\SIMYOU.TTF", size)
    draw.text(coordinate, txt, color, font)
    del draw  # 结束画图
