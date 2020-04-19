import turtle, random
from utils import log
from utils import ensure
from utils import isEquals

t = turtle.Turtle()
t.hideturtle()

turtle.tracer(10000, 0.0001)  # draw speed


def forward(step):
    t.forward(step)


# penup 可以把笔抬起来, 这样往前走就不会画线了
def penup():
    t.penup()


# pendown 后又可以画线了
def pendown():
    t.pendown()


# left 可以往左转, 参数是角度
def left(angle):
    t.left(angle)


def right(angle):
    t.right(angle)


# setHeading(注意大小写) 可以设置箭头的朝向, 0 就是朝右
# 90 和 -90 的朝向, 自行摸索一下
def setHeading(angle):
    t.setheading(angle)


def jump(x, y):  # jump 可以无痕走到某个坐标
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(0)


def fill_color(color):
    t.fillcolor(color)


def edge_color(color):
    t.color(color)


def start():
    t.begin_fill()


def end():
    t.end_fill()


def write(x, y, str, font_size, edgecolor):
    edge_color(edgecolor)
    jump(x, y)
    t.write(str, font=("宋体", font_size, "normal"))


def author_inform():
    str = "author：大侄子"
    write(-200, 200, str, 33, 'pink')


def rect(x, y, width, height, fillcolor, edgecolor):
    w = width
    h = height
    jump(x, y)
    setHeading(0)
    edge_color(edgecolor)
    fill_color(fillcolor)
    start()
    i = 0
    while (i < 2):
        forward(w)
        right(90)
        forward(h)
        right(90)
        i = i + 1
    end()


def polygon(length, num, fillcolor, edgecolor):
    l = length
    n = num
    angle = (n - 2) * 180 / n
    degree = 180 - angle
    edge_color(edgecolor)
    fill_color(fillcolor)
    i = 0
    start()
    while (i < n):
        forward(l)
        right(degree)
        # 特别注意，循环结束前一定要改变 i 的值
        # 否则循环永远不会结束的
        i = i + 1
    end()


def circle(x, y, r, fillcolor, edgecolor):
    jump(x, y)
    num = 36
    import math
    length = (2 * math.pi * r) / num
    jcdu = (90 + (360 / num) / 2)
    start()
    left(jcdu)
    forward(r)
    right(jcdu)
    end()
    polygon(length, num, fillcolor, edgecolor)


def fan(length, num, fillcolor, edgecolor):
    l = length
    n = num
    angle = (n - 2) * 180 / n
    degree = 180 - angle
    edge_color(edgecolor)
    fill_color(fillcolor)
    i = 0
    start()
    while (i < n / 2):
        forward(l)
        right(degree)
        # 特别注意，循环结束前一定要改变 i 的值
        # 否则循环永远不会结束的
        i = i + 1

    end()


def semicircle(x, y, r, fillcolor, edgecolor):  # 半圆
    jump(x, y)
    num = 36
    import math
    length = (2 * math.pi * r) / num
    jcdu = (90 + (360 / num) / 2)
    start()
    left(jcdu)
    forward(r)
    right(jcdu)
    fan(length, num, fillcolor, edgecolor)
    right(180 - jcdu)
    forward(2 * r)
    end()
    pass


def star(x, y, length, fillcolor, edgecolor):
    jump(x, y)
    edge_color(edgecolor)
    fill_color(fillcolor)
    i = 0
    start()
    while (i < 5):
        forward(length)
        right(144)
        i = i + 1
    end()


def sin(degree):
    import math
    # 如上课所述, 数学库里面的 sin 函数接受弧度作为参数
    # 我们这个函数接受角度, 下面是弧度转角度的公式
    radians = degree * math.pi / 180
    return math.sin(radians)


def cos(degree):
    import math
    radians = degree * math.pi / 180
    return math.cos(radians)


def center_star(x, y, r, fillcolor, edgecolor):
    du = 18
    x1 = x - cos(du) * r
    y1 = y - sin(du) * r
    length = cos(du) * r * 2
    star(x1, -y1, length, fillcolor, edgecolor)


def test_star_circle(x, y, r):
    circle(x, y, r, 'pink', 'black')
    center_star(x, y, r, 'yellow', 'black')

    pass


# 美国队长盾牌
def sheild(x, y, space):
    circle(x, y, 6 * space, 'red', 'black')

    circle(x, y, 5 * space, 'white', 'white')

    circle(x, y, 4 * space, 'red', 'red')

    circle(x, y, 3 * space, 'blue', 'blue')
    r = 3 * space
    center_star(x, y, r, 'white', 'white')


def rects(x, y, w, h):
    space = h / (4 + 1 + 15 + 1 + 4)
    rect(x, -(y + 0 * space), w, 4 * space, 'blue', 'blue')
    rect(x, -(y + 5 * space), w, 15 * space, 'red', 'red')
    rect(x, -(y + 21 * space), w, 4 * space, 'blue', 'blue')


def else_draw(x, y, w, h):
    space = h / (4 + 1 + 15 + 1 + 4)
    center_red = 15 * space
    r = center_red * (2 / 3) / 2  # 圆形的直径和红色矩形的高度的比为 2:3
    x1 = x + w * (2 / 5)  # 圆形的圆点 x 坐标在国旗宽的 2/5 处
    y1 = y + 5 * space + 15 * space / 2
    circle(x1, -y1, r, fillcolor='white', edgecolor='white')
    center_star(x1, y1, r, fillcolor='red', edgecolor='red')


def northkorea(x, y):
    w = 200
    h = 150
    rects(x, y, w, h)
    else_draw(x, y, w, h)


def ellipse(x, y, space, fillcolor, edgecolor):
    jump(x, y)
    step = space
    tmp = 0.005
    edge_color(edgecolor)
    fill_color(fillcolor)
    start()
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            step = step + tmp
            left(3)  # 向左转3度
            forward(step)  # 向前走step的步长
        else:
            step = step - tmp
            left(3)  # 向左转3度
            forward(step)
    end()


def gua_skin(x, y, r, fillcolor, edgecolor):
    semicircle(x, y, r, fillcolor, edgecolor)


def gua_meat(x, y, r, fillcolor, edgecolor):
    semicircle(x, y, r, fillcolor, edgecolor)
    pass


def gua_seeds(x, y, r, fillcolor, edgecolor):
    # 0 - r
    import random
    for i in range(2):
        x = x + 10 * (i + 1)
        y = y + 10 + 5 * i
        ellipse(x, y, 0.08, fillcolor, edgecolor)

    for i in range(3):
        x = -x + 5 * i
        y = y + 5 * i
        ellipse(x, -y, 0.08, fillcolor, edgecolor)


def gua(x, y):
    gua_skin(x, y, 88, 'green', 'black')
    gua_meat(x, y, 66, 'pink', 'gray')
    gua_seeds(x, y, 22, 'black', 'black')


"""
根据本周天气，绘制柱状图
中国本周的每日平均气温, 从周一到周日


分步提示：
    1. 遍历数组 temps，每一个温度都画一个矩形。矩形之间的间距通过 space 参数传递
"""


def forecast1(temps, space):
    # 柱壮图里每个图宽 30，间距为 space
    x = 0
    y = -100
    for i in range(len(temps)):
        h = temps[i] * 10
        x = (30 + space) * i
        rect(x, y, 30, -h, 'pink', 'black')


def test_forecast1():
    temps = [22, 19, 22, 21, 25, 27, 30]
    space = 5
    forecast1(temps, space)


def forecast2(temps, space, base):
    # 柱壮图里每个图宽 30，间距为 space
    # 增加一个 base 参数，每个温度都减去 base，可以更好地区分不同温度
    x = 0
    y = -100
    for i in range(len(temps)):
        h = (temps[i] - base) * 10
        x = (30 + space) * i
        rect(x, y, 30, -h, 'pink', 'black')


"""
分步提示：
    1. 在原点处往左移动到左边边缘，然后前进画布宽度的距离，这样就可以画出 x 轴
    2. 以同样的方式画出 y 轴，注意向下为 y 轴正方向
    3. 然后在坐标轴上画出天气预报的柱状图
"""


def triangle(x=0, y=0, length=101, fillcolor='gray', edgecolor='gray'):
    l = length
    jump(x, y)
    edge_color(edgecolor)
    fill_color(fillcolor)
    i = 0
    start()
    setHeading(180)
    while (i < 3):
        forward(l)
        right(120)
        i += 1
    end()


def triangle_y(x=0, y=0, length=10, fillcolor='gray', edgecolor='gray'):
    triangle(x, y, length, edgecolor, edgecolor)


def triangle_x(x=0, y=0, length=10, fillcolor='gary', edgecolor='gray'):
    l = length
    jump(x, y)
    edge_color(edgecolor)
    fill_color(fillcolor)
    i = 0
    start()
    setHeading(90)
    while (i < 3):
        forward(l)
        right(120)
        i += 1
    end()


def write_triangle_y(x, y, str, color):
    t = str
    move_size = 15
    x1 = x
    y1 = y + move_size
    write(x1, y1, t, 10, color)
    pass


def write_triangle_x(x, y, str, color):
    t = str
    move_size = 15
    x1 = x + move_size
    y1 = y
    write(x1, y1, t, 10, color)
    pass


def triangles(x, y, length, fillcolor, edgecolor, size):
    x1 = length / 2 + x
    y1 = size + y
    triangle_y(x1, y1, length, edgecolor, edgecolor)
    write_triangle_x(x1, y1, 'Temperature ℃', edgecolor)
    x2 = size + x
    y2 = -length / 2 + y
    triangle_x(x2, y2, length, edgecolor, edgecolor)
    write_triangle_x(x2, y2, 'Days', edgecolor)
    pass


def write_temp_cali(x, y, temp, color):
    t = str(temp)
    move_size = 15
    x1 = x - move_size
    y1 = y - 6
    write(x1, y1, t, 10, color)


def calibration(x, y, size, space, length, fillcolor, edgecolor):  # 刻度
    l = length
    time = int(size / space)
    x1 = x
    y1 = y
    edge_color(edgecolor)
    for i in range(time):
        temp = int(i * space / 10)
        jump(x1, y1)
        forward(l)
        write_temp_cali(x1, y1, temp, edgecolor)
        y1 += space
    end()


def calibration_x(x, y, size, fillcolor, edgecolor):  # y
    s = size
    edge_color(edgecolor)
    fill_color(fillcolor)
    start()
    jump(x, y)
    forward(s)
    end()


def calibration_y(x, y, size, fillcolor, edgecolor):  # x
    s = size
    edge_color(edgecolor)
    fill_color(fillcolor)
    start()
    jump(x, y)
    right(-90)
    forward(s)
    end()
    calibration(x, y, size, 50, 5, fillcolor, edgecolor)


# 绘制坐标轴
def coordinateAxis(x, y, size, fillcolor, edgecolor):  # 坐标轴
    # 在坐标原点处绘制两条坐标轴
    s = size
    calibration_x(x, y, s, fillcolor, edgecolor)
    calibration_y(x, y, s, fillcolor, edgecolor)
    length = 12  # 三角形的边长
    triangles(x, y, length, fillcolor, edgecolor, s)
    pass


def write_week(x, y, week, color):  # rect width  30
    move_size = 6
    x1 = x + 30 / 2 - move_size
    y1 = y - 13 - move_size
    write(x1, y1, week, 13, color)


def write_temp(x, y, h, temp, color):
    x1 = x + 30 / 2 - 6
    move_size = 4
    y1 = y + h + 13 - move_size
    write(x1, y1, temp, 13, color)


def cylindricals(x, y, temps, space, base, per_length):  # 所有柱形
    keys = [k for k in temps.keys()]
    per = per_length
    for i in range(len(keys)):
        week = keys[i]  # 'Mon'
        week_temp = temps[week]['temp']  # temp
        color = temps[week]['color']  # color
        h = (week_temp - base) * per
        x1 = (30 + space) * i + space + x  # rect width  30

        write_week(x1, y, week, color)
        rect(x1, y, 30, -h, color, 'black')
        write_temp(x1, y, h, week_temp, color)


def forecast_bar_charts(temps, space, base, per_length):  # bar charts
    x = -55
    y = -200
    # 原点 temp 0
    coordinateAxis(x, y, 350, fillcolor='white', edgecolor='gray')
    cylindricals(x, y, temps, space, base, per_length)
    pass


def test_forecast_bar_charts():
    # temps = []
    # Mon Tue Thu Wed Fri Sat Sun
    data = {
        'Mon': {
            'temp': 21,
            'color': '#FF7D40',
        },
        'Tue': {
            'temp': 19,
            'color': '#33A1C9',
        },
        'Thu': {
            'temp': 22,
            'color': '#FF7D40',
        },
        'Wed': {
            'temp': 24,
            'color': '#FF6347',
        },
        'Fri': {
            'temp': 25,
            'color': '#F00',
        },
        'Sun': {
            'temp': 30,
            'color': '#F00',
        },
    }
    forecast_bar_charts(data, 24, 0, 10)


def square(x, y, width, fillcolor, edgecolor):
    w = width
    jump(x, y)
    setHeading(0)
    fill_color(fillcolor)
    edge_color(edgecolor)
    i = 0
    start()
    while (i < 4):
        forward(w)
        right(90)
        i = i + 1
    end()


def center_square(x, y, width, fillcolor, edgecolor):
    w = width
    x1 = x + w / 2
    y1 = y + w / 2
    square(x1, y1, w, fillcolor, edgecolor)
    pass


def line(x1, y1, x2, y2, color):
    edge_color(color)
    start()
    t.up()
    t.goto(x1, y1)
    t.down()
    t.goto(x2, y2)
    end()


def connected_point(A, B):  # A点 和 B 点 相连
    x1 = A['x']
    y1 = A['y']
    jump(x1, y1)
    x2 = B['x']
    y2 = B['y']
    color = B['color']
    # import math
    # l = math.sqrt(((x1-x2)**2)+((y1-y2)**2))
    line(x1, y1, x2, y2, color)


def connected_points(arr):  # 所有点 相连
    l = len(arr)
    for i in range(l-1):
        A = arr[i]
        B = arr[i + 1]
        connected_point(A, B)
    connected_point(arr[l-2], arr[l-1])


def broken_lines(x, y, temps, space, base, per_length):  # 所有柱形
    keys = [k for k in temps.keys()]
    per = per_length
    points = []
    for i in range(len(keys)):
        week = keys[i]  # 'Mon'
        week_temp = temps[week]['temp']  # temp
        color = temps[week]['color']  # color
        h = (week_temp - base) * per
        x1 = (30 + space) * i + space + x  # rect width  30
        x1 = x1 + 30 / 2  # 中点横坐标

        write_week(x1, y, week, color)
        y1 = y + h + + 30 / 2  - 7 # 中点纵坐标
        center_square(x1, y1, 8, color, color)
        write_temp(x1, y + 10, h, week_temp, color)

        point = {}
        point['x'] = x1 + 7
        point['y'] = y1
        point['color'] = color
        points.append(point)
    connected_points(points)


def forecast_line_charts(temps, space, base, per_length):  # bar charts
    x = -55
    y = -200
    # 原点 temp 0
    coordinateAxis(x, y, 350, fillcolor='white', edgecolor='gray')
    broken_lines(x, y, temps, space, base, per_length)
    pass


def test_forecast_line_charts():  # line chart
    # temps = []
    # Mon Tue Thu Wed Fri Sat Sun
    # d = [
    #     {
    #         'xbqi': 'Mon',
    #         'tmp': 32,
    #         'color'
    #     }
    # ]
    data = {
        'Mon': {
            'temp': 21,
            'color': '#FF7D40',
        },
        'Tue': {
            'temp': 19,
            'color': '#1E90FF',
        },
        'Thu': {
            'temp': 22,
            'color': '#FF7D40',
        },
        'Wed': {
            'temp': 24,
            'color': '#FF6347',
        },
        'Fri': {
            'temp': 25,
            'color': '#F00',
        },
        'Sun': {
            'temp': 30,
            'color': '#F00',
        },
    }
    forecast_line_charts(data, 24, 0, 10)


def test_write():
    str = 'gua 123 瓜'
    write(0, 0, str, 55, 'blue')


def test_keys():
    dic = {
        'Mon': {
            'temp': 21,
            'color': 'orange',
        },
        'Tue': {
            'temp': 19,
            'color': 'blue',
        },
        'Thu': {
            'temp': 22,
            'color': 'orange',
        },
        'Wed': {
            'temp': 24,
            'color': 'orange',
        },
        'fri': {
            'temp': 25,
            'color': 'red',
        },
        'Sun': {
            'temp': 30,
            'color': 'red',
        },
    }
    keys = dic.keys()
    log('keys', keys, len(keys))
    log('type keys', type(keys))
    # v = keys[0]  错误
    # log('v', v)



def main():
    author_inform()
    test_forecast_line_charts()
    # test_forecast_bar_charts()
    # test_keys()
    # circle(0, 0, 30, 'white', 'black')
    # test_star_circle(0, 0, 40)
    # sheild(0, 0, 12)
    # northkorea(0, 0)
    # semicircle(0, 0, 30, 'white', 'black')
    # gua(0, 0)
    # test_forecast1()
    # test_write()
    # triangle(x=0, y=0, length=101, fillcolor='gray', edgecolor='gray')
    # triangle_x(x=0, y=0, length=101, fillcolor='gray', edgecolor='gray')
    # triangle_y(x=0, y=0, length=101, fillcolor='gray', edgecolor='gray')

    turtle.done()


if __name__ == '__main__':
    main()
