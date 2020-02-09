import turtle, random
from utils import log
from utils import ensure
from utils import isEquals

t = turtle.Turtle()
t.hideturtle()


# turtle.tracer(10000, 0.0001)  draw speed

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


def author_inform():
    t.pensize(2)
    t.color('black', 'pink')
    jump(-200, 200)
    t.write("author：大侄子", move=True, align="left", font=("宋体", 30, "normal"))


def triangle(x=0, y=0, length=101):
    l = length
    jump(x, y)
    i = 0
    while (i < 3):
        forward(l)
        right(120)
        i += 1


def square(x, y, width):
    w = width
    jump(x, y)
    setHeading(0)
    i = 0
    while (i < 4):
        forward(w)
        right(90)
        i = i + 1


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


def polygon(x, y, length, num, fillcolor, edgecolor):
    l = length
    n = num
    angle = (n - 2) * 180 / n
    degree = 180 - angle
    jump(x, y)
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


def get_pi():
    import math
    r = math.pi
    return r


"""
注意, 本次作业中提到的所有国旗，我们只画黑色线框不填色
中国国旗的尺寸是 300 * 200
其他所有国旗的矩形长宽都定为 200 * 150(包括瑞士国旗)


作业 1
实现一个圆形函数
x y 是圆形的圆心
r 是半径
circle(x, y, r)


实现步骤如下
第一节课的作业 polygon 在边数很大的时候就像是一个近似源
而实际上电脑是通过模拟多边形来实现画一个圆的
在画 polygon 的时候需要从左上角开始
而我们这个 circle 的 x y 参数是表示圆心的坐标
所以要先从圆心移动到左上角
"""


def circle(x, y, r, fillcolor, edgecolor):
    num = 36
    length = (2 * get_pi() * r) / num
    y1 = y + r
    polygon(x, y1, length, num, fillcolor, edgecolor)


"""
作业 2
实现一个矩形函数
x y 是矩形中心的坐标
w h 是宽高
center_rect(x, y, w, h)

在第一课的作业中已经实现了 rect 函数,
不过 rect 函数中的 x, y 是表示左上角坐标,
现在需要实现的 center_rect 函数的 x, y 是矩形中心的坐标,
所以应该先从矩形中心移动到矩形左上角, 然后调用 rect 函数

实现步骤如下
1. 根据矩形中心坐标 x, y 计算出左上角坐标 x1, y1
2. 调用 rect 函数, 传入的参数分别为左上角坐标, 宽和高
"""


def center_rect(x, y, w, h, fillcolor, edgecolor):
    x1 = x - w / 2
    y1 = y + h / 2
    rect(x1, y1, w, h, fillcolor, edgecolor)


"""
作业 3
实现一个正五角星(国旗大星星那种)函数
x y 是五角星顶部横边的左边点坐标
length 是一条线的长度
这是一个正五角星
penta(x, y, length)

实现步骤如下
1. 正五角星需要重复 5 次, 所以需要循环 5 次
2. 每次循环中前进 length 的长度, 右转 144 度
3. 别忘了循环的时候 i 增加 1
"""


def penta(x, y, length, fillcolor, edgecolor):
    l = length
    jump(x, y)
    setHeading(0)
    edge_color(edgecolor)
    fill_color(fillcolor)
    start()
    i = 0
    while (i < 5):
        forward(l)
        right(144)
        i += 1
    end()


"""
作业 4
实现一个函数画日本国旗
调用 2 个函数画日本国旗
一个画背景的白色矩形
一个画中间的圆，圆的直径必须为国旗高的 3/5
x, y 是国旗左上角座标
japan(x, y)


实现步骤如下
日本国旗由两部分组成, 矩形和圆形. 所以依次画出这两个图形
1. 调用 center_rect 函数画一个矩形
2. 调用 circle 函数画一个圆形  200 * 150
"""


def japan(x, y):
    w = 200
    h = 150
    center_rect(x, y, w, h, 'white', 'black')
    r = h * (3 / 5) / 2
    circle(x, y, r, 'red', 'white')
    pass


"""
作业 5
实现一个五角星函数
x y 是五角星的中心点坐标
r 是五角星外接圆的半径
penta1(x, y, r)

为了实现这个函数, 你需要使用三角函数计算顶点在圆上的坐标
你不需要懂这个数学计算过程, 直接拿来用即可
我们这里帮你实现了正弦余弦函数如下
"""


def sin(degree):
    # 这里的
    # sin
    # 函数接受弧度作为参数
    # 我们这个函数接受角度, 下面是弧度转角度的公式
    import math
    radians = degree * math.pi / 180
    return math.sin(radians)


def cos(degree):
    # 这里的
    # cos
    # 函数接受弧度作为参数
    # 我们这个函数接受角度, 下面是弧度转角度的公式
    import math
    radians = degree * math.pi / 180
    return math.cos(radians)


# 实现步骤如下
# 1. 正五角星顶角的一半是 18 度，  du = 18
# 2. 五角星顶部横边的左边点 B 的 x 坐标为   x1 = x - cos(du) * r
# 3. 五角星顶部横边的左边点 B 的 y 坐标为   y1 = y - sin(du) * r
# 4. 五角星的长度为   length = cos(du) * r * 2
# 5. 调用作业 3 的函数 penta(x1, y1, length)

def penta1(x, y, r, fillcolor, edgecolor):
    du = 18
    x1 = x - cos(du) * r
    y1 = y - sin(du) * r
    length = cos(du) * r * 2
    # log(' penta1 x1', x1)
    # log('penta1 y1', y1)
    # log('penta1 length', length)
    penta(x1, -y1, length, fillcolor, edgecolor)
    pass



# 作业 6
# 实现一个函数画中国国旗(以下国旗题目都是如此 不重复了)
# 五角星不要求角度朝向（统一用正五角星）
# 学有余力的话, 可以调整五个五角星的角度为标准角度
# 但是要求尺寸必须符合下图中的比例
# 中国国旗的尺寸是 300 * 200
# x, y 是国旗左上角座标（后面的题都是这个要求，不再重复说明）
# china(x, y)
#
# 实现步骤
# 中国国旗由两部分组成, 矩形和 5 个五角星, 计算好比例, 依次画完
# 1. 使用 rect 函数画一个矩形
# 2. 计算比例，画 5 个五角星(调用 5 次)
#
# 国旗比例要求： 中国国旗的尺寸是 300 * 200
# http://www.woqucha.com/uploads/allimg/16/1_161116111341_1.JPG
def big_penta(x, y, w, h, fillcolor, edgecolor):
    space = h / 2 / 10
    x1 = x + 5 * space
    y1 = y + 5 * space
    r = 6 * space / 2
    penta1(x1, y1, r, fillcolor, edgecolor)
    pass


"""
def small_1(x, y, space, fillcolor, edgecolor):
    x1 = x + 10 * space
    y1 = y + 2 * space
    r = 2 * space / 2
    penta1(x1, -y1, r, fillcolor, edgecolor)

def small_3(x, y, space, fillcolor, edgecolor):
    x1 = x + 12 * space
    y1 = y + 7 * space
    r = 2 * space / 2
    penta1(x1, -y1, r, fillcolor, edgecolor)
"""
# x y  单位长度： XX space    space = h / 2 / 10
def small_penta(x, y, space, space_x, space_y, fillcolor, edgecolor):
    x1 = x + space * space_x
    y1 = y + space * space_y
    r = 2 * space / 2
    penta1(x1, y1, r, fillcolor, edgecolor)


def small_pentas(x, y, w, h, fillcolor, edgecolor):
    space = h / 2 / 10
    small_penta(x, y, space, 10, 2, fillcolor, edgecolor)  # 1
    small_penta(x, y, space, 12, 4, fillcolor, edgecolor)  # 2
    small_penta(x, y, space, 12, 7, fillcolor, edgecolor)  # 3
    small_penta(x, y, space, 10, 9, fillcolor, edgecolor)  # 4
   

def pentas(x, y, w, h, fillcolor, edgecolor):
    big_penta(x, y, w, h, fillcolor, edgecolor)
    small_pentas(x, y, w, h, fillcolor, edgecolor)


def china(x, y):
    w = 300
    h = 200
    rect(x, y, w, h, fillcolor='red', edgecolor='white')
    pentas(x, y, w, h, fillcolor='yellow', edgecolor='yellow')
    pass

"""

作业 7
实现一个函数画法国国旗
france(x, y)

实现步骤
法国国旗由三个纵向矩形组成, 依次画出这三个矩形
1. 计算出三个矩形的宽, 均为 1/3 * w
2. 计算出三个矩形的左上角坐标, 分别为 x1, y1、x2, y2 和 x3, y3
3. 调用三次 rect 函数, 每次传入不一样的参数  200 * 150
"""
def france(x, y):
    w = 200
    h = 150
    space = w / 3
    rect(x + 0 * space, y, space, h, 'blue', 'blue')
    rect(x + 1 * space, y, space, h, 'white', 'white')
    rect(x + 2 * space, y, space, h, 'red', 'red')


# 作业 8
# 画德国国旗
# germany(x, y)
#
# 实现步骤
#     德国国旗由三个横向矩形组成, 依次画出这三个矩形
#
# 分步提示:
# 1. 计算出三个矩形的高, 均为 1/3 * h
# 2. 计算出三个矩形的左上角坐标, 分别为 x1, y1、x2, y2 和 x3, y3
# 3. 调用三次 rect 函数, 每次传入不一样的参数
def germany(x, y):
    w = 200
    h = 150
    space = h / 3
    rect(x, -(y + 0 * space), w, space, 'black', 'black')
    rect(x, -(y + 1 * space), w, space, 'red', 'red')
    rect(x, -(y + 2 * space), w, space, 'yellow', 'yellow')
    pass


# 作业 9
# 画 冈比亚国旗
# gambia(x, y)
#
# 实现步骤
#     冈比亚国旗和德国国旗类似, 中间的矩形由一个大纵向矩形和两个小纵向矩形组成,
#         所以画 5 个矩形
# 1. 最上面和最下面两个矩形和德国国旗一致
# 2. 中间的矩形分成三个矩形, 高度占比分别为 1:6:1, 分别计算出这三个矩形的中心坐标
# 3. 分别计算中间三个矩形的长度和高度
# 4. 使用 center_rect 画出 5 个矩形, 每次传入的参数不一致
def gambia(x, y):
    w = 200
    h = 150
    space = h / 3
    rect(x, -(y + 0 * space), w, space, 'red', 'red')
    new_space = space / (1 + 6 + 1)
    center_h = space - 2 * new_space
    rect(x, -(y + 1 * space + new_space), w, center_h, 'blue', 'blue')
    rect(x, -(y + 2 * space), w, space, 'green', 'green')

# 作业 10
# 画 瑞士国旗
# switzerland(x, y)
#
# 实现步骤
#     瑞士国旗由一个大矩形和两个小矩形组成, 需要画三个矩形
#
# 分步提示:
# 1. 瑞士国旗中的两个矩形大小是一样的, 都按照长边 75, 短边 25 来计算
# 2. 计算出三个矩形的中心点坐标、长、宽
# 3. 依次画出这三个矩形
def switzerland(x, y):
    w = 200
    h = 150
    rect(x, -y, w, h, 'red', 'red')
    x1 = x + w / 2
    y1 = y + h / 2
    center_rect(x1, -y1, 75, 25, 'white', 'white')
    center_rect(x1, -y1, 25, 75, 'white', 'white')

# 作业 11
# 画朝鲜国旗
# northkorea(x, y)
#
# 提示:
#     朝鲜国旗从上往下依次为蓝色矩形、白色矩形、红色矩形、白色矩形和蓝色矩形,
#     这些矩形的高度比分别为 4:1:15:1:4, 红色矩形里包含了一个圆形和一个五角星
# 圆形的直径和红色矩形的高度的比为 2:3, 圆形的圆点 x 坐标在国旗宽的 2/5 处
# 使用这些数据计算出各个图形的坐标, 然后画出来
#
# 实现步骤
# 1. 分别计算出 5 个矩形的坐标和长宽
# 2. 计算出圆形的圆心, 圆形的直径和红色矩形的高度的比为 2:3
#      圆形的圆点 x 坐标在国旗宽的 2/5 处
# 3. 画 5 个矩形
# 4. 画圆形
# 5. 画五角星
def rects(x, y, w, h):
    space = h / (4 + 1 + 15 + 1 + 4)
    rect(x, -(y + 0 * space), w, 4 * space, 'blue', 'blue')
    rect(x, -(y + 5 * space), w, 15 * space, 'red', 'red')
    rect(x, -(y + 21 * space), w, 4 * space, 'blue', 'blue')
    pass

def else_draw(x, y, w, h):
    space = h / (4 + 1 + 15 + 1 + 4)
    center_red = 15 * space
    r = center_red * (2 / 3) / 2  # 圆形的直径和红色矩形的高度的比为 2:3
    x1 = x + w * (2 / 5)  # 圆形的圆点 x 坐标在国旗宽的 2/5 处
    y1 = y + 5 * space + 15 * space / 2
    circle(x1, -y1, r, fillcolor='white', edgecolor='white')
    penta1(x1, y1, r, fillcolor='red', edgecolor='red')

def northkorea(x, y):
    w = 200
    h = 150
    rects(x, y, w, h)
    else_draw(x, y, w, h)


def main():
    author_inform()
    # japan(0, 0)
    # penta1(0, 0, 30, 'yellow', 'yellow')
    # china(0, 0)
    # france(0, 0)
    # germany(0, 0)
    # gambia(0, 0)
    switzerland(0, 0)
    # northkorea(0, 0)
    # sheild(0, 0)
    turtle.done()


if __name__ == '__main__':
    main()
