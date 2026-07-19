# Python `turtle` 库完整知识点

## 一、`turtle` 是什么

`turtle` 中文通常称为“海龟绘图”。可以把它想象成：

> 屏幕上有一只携带画笔的海龟，通过移动和转向在画布上绘图。

海龟具有一组内部状态：

```text
位置：(x, y)
方向：heading
画笔：抬起或落下
画笔颜色：pencolor
填充颜色：fillcolor
画笔粗细：pensize
移动速度：speed
外观形状：shape
是否可见：visible
```

调用函数，本质上就是修改这些状态。例如：

```python
t.forward(100)
```

它的执行过程是：

1. 根据当前朝向计算新的位置；
2. 如果画笔落下，就绘制移动轨迹；
3. 将海龟的位置更新为新位置。

`turtle` 基于 Tk 图形界面运行，通常随 Python 一起提供；程序运行时会打开一个独立绘图窗口。

---

## 二、基本程序结构

### 1. 推荐写法

```python
import turtle as t

t.forward(100)

t.done()
```

其中：

```python
import turtle as t
```

表示导入 `turtle` 模块，并将其简称为 `t`。

```python
t.done()
```

表示进入图形窗口的事件循环，让窗口保持打开。

### 2. 三种导入方式

#### 写法一：导入模块

```python
import turtle

turtle.forward(100)
turtle.done()
```

优点是函数来源清晰，不容易发生命名冲突。

#### 写法二：使用别名，最常用

```python
import turtle as t

t.forward(100)
t.done()
```

#### 写法三：全部导入，不推荐用于大型程序

```python
from turtle import *

forward(100)
done()
```

这种写法简单，但 `turtle` 中函数很多，容易和其他变量、函数重名。

---

## 三、坐标系与方向

### 1. 默认坐标系

绘图窗口中心是原点：

```text
                 y轴正方向
                    ↑
                    |
                    |
x轴负方向  ←────── (0,0) ──────→  x轴正方向
                    |
                    |
                    ↓
                 y轴负方向
```

初始状态：

```text
位置：(0, 0)
方向：向右
方向角：0°
```

### 2. 默认方向角

在默认的 `standard` 模式中：

| 角度 | 方向 |
|---:|---|
| `0°` | 向右、东 |
| `90°` | 向上、北 |
| `180°` | 向左、西 |
| `270°` | 向下、南 |

注意：

```python
t.left(90)
```

表示在当前方向基础上左转 90°。

```python
t.setheading(90)
```

表示直接把绝对方向设为 90°，即朝上。

二者不是同一种操作。

---

## 四、海龟移动

### 1. 前进和后退

```python
t.forward(distance)
t.fd(distance)
```

向当前朝向前进。

```python
t.forward(100)
t.fd(100)
```

二者完全等价。

后退：

```python
t.backward(distance)
t.back(distance)
t.bk(distance)
```

例如：

```python
t.backward(50)
```

海龟向后移动，但朝向不变。

还可以使用负数：

```python
t.forward(-100)
```

效果相当于后退 100。

### 2. 左转和右转

```python
t.left(angle)
t.lt(angle)
```

逆时针旋转。

```python
t.right(angle)
t.rt(angle)
```

顺时针旋转。

例如：

```python
t.forward(100)
t.left(90)
t.forward(100)
```

### 3. 移动到指定坐标

```python
t.goto(x, y)
t.setpos(x, y)
t.setposition(x, y)
```

三者基本等价。

```python
t.goto(100, 50)
```

特点：

- 移动到绝对坐标 `(100, 50)`；
- 不改变海龟朝向；
- 如果画笔落下，会画出当前位置到目标位置的直线。

也可以传入坐标元组：

```python
t.goto((100, 50))
```

### 4. 单独设置横坐标或纵坐标

```python
t.setx(100)
```

只修改横坐标，纵坐标保持不变。

```python
t.sety(-50)
```

只修改纵坐标，横坐标保持不变。

### 5. 瞬移

较新的 Python 版本支持：

```python
t.teleport(x, y)
```

它会直接移动到目标位置，不绘制移动轨迹。

传统兼容写法：

```python
t.penup()
t.goto(x, y)
t.pendown()
```

### 6. 返回原点

```python
t.home()
```

执行后：

```text
位置变为：(0, 0)
方向恢复为初始方向：0°
```

如果画笔处于落下状态，返回原点的过程中会画线。

---

## 五、获取位置和方向

### 1. 获取当前位置

```python
t.position()
t.pos()
```

返回类似：

```python
(100.00, 50.00)
```

可以拆包：

```python
x, y = t.pos()
print(x)
print(y)
```

### 2. 获取横纵坐标

```python
t.xcor()
t.ycor()
```

### 3. 获取当前方向

```python
t.heading()
```

例如：

```python
t.setheading(90)
print(t.heading())     # 90.0
```

### 4. 设置绝对方向

```python
t.setheading(angle)
t.seth(angle)
```

例如：

```python
t.seth(180)
```

海龟直接朝左。

### 5. 计算到目标点的方向

```python
t.towards(x, y)
```

例如：

```python
angle = t.towards(100, 100)
t.setheading(angle)
```

### 6. 计算距离

```python
t.distance(x, y)
```

例如：

```python
print(t.distance(30, 40))   # 50.0
```

也可以计算两只海龟之间的距离：

```python
a.distance(b)
```

---

## 六、画笔控制

### 1. 抬起画笔

```python
t.penup()
t.pu()
t.up()
```

抬起后移动不会画线。

### 2. 落下画笔

```python
t.pendown()
t.pd()
t.down()
```

落下后移动会画线。

### 3. 判断画笔是否落下

```python
t.isdown()
```

返回布尔值：

```python
print(t.isdown())   # True 或 False
```

### 4. 设置画笔粗细

```python
t.pensize(width)
t.width(width)
```

例如：

```python
t.pensize(5)
```

不传参数时返回当前粗细：

```python
print(t.pensize())
```

### 5. 综合设置画笔属性

```python
t.pen()
```

不传参数时返回当前画笔状态字典。

也可以批量设置：

```python
t.pen(
    pencolor="red",
    fillcolor="yellow",
    pensize=5,
    speed=0
)
```

---

## 七、颜色设置

### 1. 设置线条颜色

```python
t.pencolor("red")
```

### 2. 设置填充颜色

```python
t.fillcolor("yellow")
```

### 3. 同时设置两种颜色

```python
t.color("red", "yellow")
```

含义：

```text
red    → 画笔颜色
yellow → 填充颜色
```

只传一个颜色时：

```python
t.color("blue")
```

画笔颜色和填充颜色都会设为蓝色。

### 4. 颜色表示方法

#### 英文颜色名

```python
t.pencolor("red")
t.pencolor("blue")
t.pencolor("orange")
t.pencolor("purple")
```

#### 十六进制颜色

```python
t.pencolor("#33cc8c")
```

#### RGB 颜色

默认 RGB 模式是 `0.0～1.0`：

```python
t.colormode(1.0)
t.pencolor(1.0, 0.0, 0.0)
```

也可以切换为 `0～255`：

```python
t.colormode(255)
t.pencolor(255, 0, 0)
```

必须先设置：

```python
t.colormode(255)
```

否则直接传入 `(255, 0, 0)` 可能报颜色范围错误。

---

## 八、填充图形

填充的基本过程：

```python
t.begin_fill()

# 绘制封闭图形

t.end_fill()
```

例如填充正方形：

```python
import turtle as t

t.color("red", "yellow")

t.begin_fill()

for _ in range(4):
    t.forward(100)
    t.right(90)

t.end_fill()

t.done()
```

注意：

1. `begin_fill()` 开始记录填充路径；
2. 中间绘制图形；
3. `end_fill()` 完成填充；
4. 图形最好封闭，否则填充结果可能不符合预期。

判断当前是否处于填充状态：

```python
t.filling()
```

部分新版本还支持：

```python
with t.fill():
    for _ in range(4):
        t.forward(100)
        t.right(90)
```

为了兼容旧版本，学习阶段优先掌握 `begin_fill()` 和 `end_fill()`。

---

## 九、绘制圆、圆弧和多边形

### 1. 绘制圆

```python
t.circle(radius)
```

例如：

```python
t.circle(100)
```

这里的起点通常位于圆周上，而不是圆心。

默认情况下，圆心位于海龟当前位置左侧 `radius` 距离处。

### 2. 绘制圆弧

```python
t.circle(radius, extent)
```

例如：

```python
t.circle(100, 180)
```

绘制半圆。

```python
t.circle(100, 90)
```

绘制四分之一圆。

### 3. 正负半径

```python
t.circle(100)
```

正半径通常逆时针绘制。

```python
t.circle(-100)
```

负半径反向绘制，圆心位于海龟右侧。

### 4. 使用 `steps` 画正多边形

```python
t.circle(radius, extent, steps)
```

例如：

```python
t.circle(100, steps=6)
```

绘制近似正六边形。

---

## 十、点、印章和文字

### 1. 绘制圆点

```python
t.dot()
t.dot(size)
t.dot(size, color)
```

例如：

```python
t.dot(20, "red")
```

这里的 `20` 是圆点直径。

### 2. 印制海龟形状

```python
stamp_id = t.stamp()
```

清除指定印章：

```python
t.clearstamp(stamp_id)
```

清除多个印章：

```python
t.clearstamps()
```

### 3. 写文字

```python
t.write(
    arg,
    move=False,
    align="left",
    font=("Arial", 16, "normal")
)
```

例如：

```python
t.write(
    "Hello, Turtle!",
    align="center",
    font=("Arial", 20, "bold")
)
```

参数说明：

| 参数 | 作用 |
|---|---|
| `arg` | 要显示的内容 |
| `move` | 写完后海龟是否移动 |
| `align` | `"left"`、`"center"`、`"right"` |
| `font` | `(字体名, 字号, 字体样式)` |

常见字体样式：

```python
"normal"
"bold"
"italic"
```

---

## 十一、海龟速度与动画

### 1. 设置速度

```python
t.speed(value)
```

可以传整数：

| 数值 | 速度 |
|---:|---|
| `0` | 最快，无逐步移动动画 |
| `1` | 最慢 |
| `3` | 较慢 |
| `6` | 正常 |
| `10` | 较快 |

注意：不是简单地“数值越小越快”。

特殊规则：

```python
t.speed(0)
```

表示取消逐步移动动画，因此通常最快。

也可以传字符串：

```python
t.speed("fastest")
t.speed("fast")
t.speed("normal")
t.speed("slow")
t.speed("slowest")
```

对应关系：

| 字符串 | 数值 |
|---|---:|
| `"fastest"` | `0` |
| `"fast"` | `10` |
| `"normal"` | `6` |
| `"slow"` | `3` |
| `"slowest"` | `1` |

### 2. 批量关闭动画

```python
screen.tracer(0)
```

绘制结束后：

```python
screen.update()
```

完整示例：

```python
import turtle as t

screen = t.Screen()
screen.tracer(0)

for i in range(360):
    t.forward(i / 5)
    t.right(59)

screen.update()
screen.mainloop()
```

### 3. 设置刷新频率

```python
screen.tracer(n)
```

例如：

```python
screen.tracer(10)
```

### 4. 设置延迟

```python
screen.delay(milliseconds)
```

例如：

```python
screen.delay(10)
```

---

## 十二、海龟外观

### 1. 设置海龟形状

```python
t.shape(name)
```

内置常用形状：

```python
"arrow"
"turtle"
"circle"
"square"
"triangle"
"classic"
```

例如：

```python
t.shape("turtle")
```

查看当前形状：

```python
print(t.shape())
```

### 2. 显示和隐藏海龟

隐藏：

```python
t.hideturtle()
t.ht()
```

显示：

```python
t.showturtle()
t.st()
```

判断是否可见：

```python
t.isvisible()
```

### 3. 调整海龟大小

```python
t.shapesize(stretch_wid, stretch_len, outline)
```

例如：

```python
t.shapesize(2, 3, 2)
```

含义：

- `stretch_wid`：宽度拉伸；
- `stretch_len`：长度拉伸；
- `outline`：轮廓粗细。

别名：

```python
t.turtlesize()
```

这只改变海龟图标大小，不改变画笔粗细，也不缩放已经绘制的图形。

---

## 十三、清除与重置

### 1. `clear()`

```python
t.clear()
```

清除当前海龟绘制的内容，但：

- 海龟位置不变；
- 朝向不变；
- 画笔属性不变。

### 2. `reset()`

```python
t.reset()
```

清除当前海龟绘制的内容，并让当前海龟恢复初始状态。

### 3. `clearscreen()`

```python
t.clearscreen()
```

清空整个屏幕，包括所有海龟的绘图、事件绑定和屏幕设置，并恢复初始状态。

面向对象写法：

```python
screen.clear()
```

### 4. `resetscreen()`

```python
t.resetscreen()
```

重置屏幕上的所有海龟。

面向对象写法：

```python
screen.reset()
```

---

## 十四、屏幕对象 `Screen`

推荐显式创建屏幕：

```python
import turtle as t

screen = t.Screen()
```

### 1. 设置窗口标题

```python
screen.title("我的海龟绘图")
```

### 2. 设置窗口大小和位置

```python
screen.setup(width, height, startx, starty)
```

例如：

```python
screen.setup(800, 600)
```

指定窗口位置：

```python
screen.setup(800, 600, 100, 50)
```

### 3. 设置背景颜色

```python
screen.bgcolor("lightblue")
```

或者：

```python
screen.bgcolor("#87CEEB")
```

### 4. 设置背景图片

```python
screen.bgpic("background.gif")
```

移除背景：

```python
screen.bgpic("nopic")
```

### 5. 获取窗口大小

```python
screen.window_width()
screen.window_height()
```

### 6. 设置画布大小

```python
screen.screensize(canvwidth, canvheight)
```

区别：

```python
screen.setup()
```

调整外部窗口大小。

```python
screen.screensize()
```

调整内部可滚动画布大小。

### 7. 自定义坐标系

```python
screen.setworldcoordinates(llx, lly, urx, ury)
```

例如：

```python
screen.setworldcoordinates(-10, -10, 10, 10)
```

此时左下角为 `(-10, -10)`，右上角为 `(10, 10)`。

---

## 十五、屏幕模式

```python
screen.mode("standard")
screen.mode("logo")
screen.mode("world")
```

### `standard`

默认模式：

```text
0°向右
正角度逆时针
```

### `logo`

模仿 Logo 语言：

```text
0°向上
正角度顺时针
```

### `world`

可以配合自定义世界坐标系使用。

一般学习和考试中保持默认的 `standard` 即可。

---

## 十六、键盘事件

键盘事件通常需要先让屏幕监听键盘：

```python
screen.listen()
```

### 1. 松开按键时触发

```python
screen.onkey(function, key)
```

例如：

```python
import turtle as t

screen = t.Screen()
pen = t.Turtle()

def move_up():
    pen.setheading(90)
    pen.forward(20)

screen.listen()
screen.onkey(move_up, "Up")

screen.mainloop()
```

错误写法：

```python
screen.onkey(move_up(), "Up")
```

这里会立即调用函数。

正确写法：

```python
screen.onkey(move_up, "Up")
```

传递的是函数对象。

### 2. 按下按键时触发

```python
screen.onkeypress(function, key)
```

例如：

```python
screen.onkeypress(move_up, "Up")
```

### 3. 常用按键名称

```python
"Up"
"Down"
"Left"
"Right"
"space"
"Return"
"Escape"
"a"
"b"
```

---

## 十七、鼠标事件

### 1. 点击海龟

```python
t.onclick(function)
```

回调函数必须能接收鼠标坐标：

```python
def handle_click(x, y):
    print(x, y)

t.onclick(handle_click)
```

### 2. 点击屏幕

```python
screen.onclick(function)
screen.onscreenclick(function)
```

例如：

```python
def move_to(x, y):
    pen.goto(x, y)

screen.onclick(move_to)
```

### 3. 拖动海龟

```python
t.ondrag(function)
```

例如：

```python
def drag(x, y):
    t.goto(x, y)

t.ondrag(drag)
```

### 4. 鼠标释放

```python
t.onrelease(function)
```

---

## 十八、定时器事件

```python
screen.ontimer(function, milliseconds)
```

例如：

```python
import turtle as t

screen = t.Screen()
pen = t.Turtle()

def move():
    pen.forward(10)
    screen.ontimer(move, 100)

move()

screen.mainloop()
```

`ontimer()` 通常只安排一次调用。要形成持续动画，需要在回调函数内部再次调用 `ontimer()`。

---

## 十九、输入对话框

### 1. 输入字符串

```python
name = screen.textinput("标题", "请输入姓名：")
```

用户取消时返回：

```python
None
```

### 2. 输入数字

```python
age = screen.numinput(
    "年龄",
    "请输入年龄：",
    default=18,
    minval=0,
    maxval=150
)
```

用户取消时同样返回 `None`。

使用前应判断：

```python
if age is not None:
    print(age)
```

---

## 二十、函数式写法与面向对象写法

### 1. 函数式写法

```python
import turtle as t

t.forward(100)
t.left(90)
t.forward(100)

t.done()
```

这种写法实际上在操作模块自动创建的默认海龟。

适合：

- 初学；
- 简单绘图；
- 只有一只海龟。

### 2. 面向对象写法

```python
import turtle

screen = turtle.Screen()
pen = turtle.Turtle()

pen.forward(100)

screen.mainloop()
```

适合：

- 多只海龟；
- 游戏；
- 动画；
- 较大型程序。

### 3. 创建多只海龟

```python
import turtle

screen = turtle.Screen()

a = turtle.Turtle()
b = turtle.Turtle()

a.color("red")
b.color("blue")

a.forward(100)

b.left(90)
b.forward(100)

screen.mainloop()
```

每只海龟都有独立的位置、方向、画笔和外观状态。

---

## 二十一、复制海龟

```python
new_turtle = old_turtle.clone()
```

例如：

```python
a = t.Turtle()
a.color("red")

b = a.clone()
b.color("blue")
b.left(90)
```

`clone()` 会创建一只状态相似的新海龟，但之后二者独立变化。

查看屏幕上的所有海龟：

```python
screen.turtles()
```

---

## 二十二、自定义海龟形状

### 1. 注册图片形状

```python
screen.register_shape("player.gif")
pen.shape("player.gif")
```

也可以使用别名：

```python
screen.addshape("player.gif")
```

### 2. 注册多边形形状

```python
triangle = ((0, 20), (-15, -10), (15, -10))

screen.register_shape("my_triangle", triangle)
pen.shape("my_triangle")
```

### 3. 查看所有可用形状

```python
print(screen.getshapes())
```

---

## 二十三、撤销操作

```python
t.undo()
```

撤销上一项海龟操作。

设置撤销缓冲区大小：

```python
t.setundobuffer(100)
```

查看撤销缓冲区中有多少项：

```python
t.undobufferentries()
```

连续撤销：

```python
while t.undobufferentries():
    t.undo()
```

---

## 二十四、保存绘图

部分新版本提供：

```python
screen.save("drawing.ps")
```

传统兼容写法：

```python
canvas = screen.getcanvas()
canvas.postscript(file="drawing.ps")
```

注意：保存的是 PostScript 文件，不是直接保存 PNG。转成 PNG 通常还需要额外图像工具。

---

## 二十五、绘制常见图形

### 1. 正方形

```python
import turtle as t

for _ in range(4):
    t.forward(100)
    t.right(90)

t.done()
```

### 2. 正三角形

```python
for _ in range(3):
    t.forward(100)
    t.left(120)
```

### 3. 正六边形

```python
for _ in range(6):
    t.forward(100)
    t.left(60)
```

### 4. 正 `n` 边形

正多边形外角：

```text
外角 = 360° ÷ 边数
```

代码：

```python
def polygon(n, length):
    angle = 360 / n

    for _ in range(n):
        t.forward(length)
        t.left(angle)
```

调用：

```python
polygon(8, 80)
```

### 5. 五角星

```python
for _ in range(5):
    t.forward(200)
    t.right(144)
```

### 6. 螺旋线

```python
for length in range(5, 300, 5):
    t.forward(length)
    t.right(91)
```

### 7. 彩色旋转图案

```python
import turtle as t

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

t.speed(0)
t.bgcolor("black")
t.pensize(2)

for i in range(200):
    t.pencolor(colors[i % len(colors)])
    t.forward(i)
    t.right(59)

t.done()
```

其中：

```python
i % len(colors)
```

会让颜色下标循环变化。

---

## 二十六、综合示例：键盘控制海龟

```python
import turtle

screen = turtle.Screen()
screen.title("键盘控制海龟")
screen.setup(800, 600)
screen.bgcolor("white")

player = turtle.Turtle()
player.shape("turtle")
player.color("blue")
player.speed(0)


def move_forward():
    player.forward(20)


def move_backward():
    player.backward(20)


def turn_left():
    player.left(15)


def turn_right():
    player.right(15)


def clear_drawing():
    player.clear()


def return_home():
    player.penup()
    player.home()
    player.pendown()


screen.listen()

screen.onkey(move_forward, "Up")
screen.onkey(move_backward, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(clear_drawing, "c")
screen.onkey(return_home, "h")

screen.mainloop()
```

---

## 二十七、常见错误

### 1. 窗口一闪而过

错误：

```python
import turtle as t

t.forward(100)
```

解决：

```python
t.done()
```

或：

```python
screen.mainloop()
```

### 2. 回调函数加了括号

错误：

```python
screen.onkey(move(), "Up")
```

正确：

```python
screen.onkey(move, "Up")
```

### 3. 键盘没有反应

通常缺少：

```python
screen.listen()
```

或者绘图窗口没有获得键盘焦点，可以先点击一下绘图窗口。

### 4. 移动时不想画线

```python
t.penup()
t.goto(100, 100)
t.pendown()
```

### 5. RGB 颜色报错

错误：

```python
t.pencolor(255, 0, 0)
```

正确：

```python
t.colormode(255)
t.pencolor(255, 0, 0)
```

### 6. 图形绘制特别慢

```python
t.hideturtle()
t.speed(0)
```

复杂绘图可以：

```python
screen.tracer(0)

# 绘图代码

screen.update()
```

### 7. `clear()` 后海龟没有回原点

因为：

```python
t.clear()
```

只清除绘图。

需要恢复状态：

```python
t.reset()
```

只返回原点：

```python
t.home()
```

### 8. `goto()` 画出意外的直线

因为画笔仍然落下。

```python
t.penup()
t.goto(x, y)
t.pendown()
```

### 9. 文件名不能叫 `turtle.py`

不要把自己的程序命名为：

```text
turtle.py
```

否则：

```python
import turtle
```

可能导入自己的文件，而不是 Python 标准库。

还应删除同目录下可能残留的：

```text
turtle.pyc
__pycache__
```

---

## 二十八、常用函数速查表

### 移动

| 函数 | 作用 |
|---|---|
| `forward(d)`、`fd(d)` | 前进 |
| `backward(d)`、`back(d)`、`bk(d)` | 后退 |
| `left(a)`、`lt(a)` | 左转 |
| `right(a)`、`rt(a)` | 右转 |
| `goto(x, y)` | 移动到指定坐标 |
| `setx(x)` | 设置横坐标 |
| `sety(y)` | 设置纵坐标 |
| `setheading(a)`、`seth(a)` | 设置绝对方向 |
| `home()` | 返回原点并恢复初始方向 |
| `circle(r)` | 绘制圆或圆弧 |

### 状态查询

| 函数 | 作用 |
|---|---|
| `pos()`、`position()` | 获取位置 |
| `xcor()` | 获取横坐标 |
| `ycor()` | 获取纵坐标 |
| `heading()` | 获取方向 |
| `distance()` | 计算距离 |
| `towards()` | 计算目标方向 |

### 画笔

| 函数 | 作用 |
|---|---|
| `penup()`、`pu()`、`up()` | 抬笔 |
| `pendown()`、`pd()`、`down()` | 落笔 |
| `pensize()`、`width()` | 设置线宽 |
| `pencolor()` | 设置画笔颜色 |
| `fillcolor()` | 设置填充颜色 |
| `color()` | 同时设置颜色 |
| `begin_fill()` | 开始填充 |
| `end_fill()` | 结束填充 |
| `isdown()` | 判断画笔状态 |

### 外观和绘图

| 函数 | 作用 |
|---|---|
| `shape()` | 设置海龟形状 |
| `shapesize()` | 调整海龟大小 |
| `hideturtle()`、`ht()` | 隐藏 |
| `showturtle()`、`st()` | 显示 |
| `dot()` | 绘制圆点 |
| `stamp()` | 盖印章 |
| `write()` | 写文字 |
| `speed()` | 设置动画速度 |
| `undo()` | 撤销 |

### 清除和退出

| 函数 | 作用 |
|---|---|
| `clear()` | 清除当前海龟绘图 |
| `reset()` | 重置当前海龟 |
| `clearscreen()` | 清空并重置屏幕 |
| `resetscreen()` | 重置所有海龟 |
| `done()`、`mainloop()` | 进入事件循环 |
| `bye()` | 关闭窗口 |
| `exitonclick()` | 点击窗口后退出 |

---

## 二十九、最重要的底层理解

学习 `turtle` 时，不要只背函数。应当始终追踪三项核心状态：

```text
当前位置在哪里？
当前朝向是多少？
画笔现在是抬起还是落下？
```

例如：

```python
t.forward(100)
t.left(90)
t.penup()
t.forward(50)
t.pendown()
t.right(90)
t.forward(100)
```

逐步分析：

| 步骤 | 位置变化 | 方向 | 是否画线 |
|---|---|---|---|
| 初始 | `(0,0)` | 向右 | — |
| `forward(100)` | 到 `(100,0)` | 向右 | 是 |
| `left(90)` | 不变 | 向上 | 否 |
| `penup()` | 不变 | 向上 | 否 |
| `forward(50)` | 到 `(100,50)` | 向上 | 否 |
| `pendown()` | 不变 | 向上 | 否 |
| `right(90)` | 不变 | 向右 | 否 |
| `forward(100)` | 到 `(200,50)` | 向右 | 是 |

`turtle` 题目的核心就是：

> 按顺序模拟海龟的位置、方向和画笔状态。
