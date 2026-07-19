# Python `print()` 格式化方法大全

> 适用范围：Python 3  
> 重点内容：`print()` 参数、`%` 格式化、`str.format()`、f-string、数字格式、对齐、填充、进制、百分比、文件输出等。

---

## 目录

1. [`print()` 基本语法](#一print-基本语法)
2. [逗号输出多个对象](#二逗号输出多个对象)
3. [`sep` 设置分隔符](#三sep-设置分隔符)
4. [`end` 设置结束符](#四end-设置结束符)
5. [常用转义字符](#五常用转义字符)
6. [字符串拼接](#六字符串拼接)
7. [`%` 格式化](#七-格式化)
8. [`str.format()` 格式化](#八strformat-格式化)
9. [格式说明符](#九格式说明符)
10. [f-string](#十f-string)
11. [`format()` 内置函数](#十一format-内置函数)
12. [输出到文件](#十二输出到文件)
13. [`flush` 与动态刷新](#十三flush-与动态刷新)
14. [可迭代对象解包输出](#十四可迭代对象解包输出)
15. [`join()` 配合输出](#十五join-配合输出)
16. [`str()` 与 `repr()`](#十六str-与-repr)
17. [自定义对象打印](#十七自定义对象打印)
18. [格式化方式对比](#十八格式化方式对比)
19. [常用格式速查](#十九常用格式速查)
20. [常见错误](#二十常见错误)
21. [核心总结](#二十一核心总结)

---

# 一、`print()` 基本语法

```python
print(*objects, sep=' ', end='\n', file=None, flush=False)
```

| 参数 | 含义 | 默认值 |
|---|---|---|
| `*objects` | 要输出的一个或多个对象 | 无 |
| `sep` | 多个对象之间的分隔符 | 空格 `' '` |
| `end` | 输出结束后添加的内容 | 换行符 `'\n'` |
| `file` | 输出目标 | 标准输出终端 |
| `flush` | 是否立即刷新输出缓冲区 | `False` |

基本示例：

```python
print("Hello")
print(100)
print(3.14)
print([1, 2, 3])
```

输出：

```text
Hello
100
3.14
[1, 2, 3]
```

---

# 二、逗号输出多个对象

```python
name = "Tom"
age = 20

print("姓名：", name, "年龄：", age)
```

输出：

```text
姓名： Tom 年龄： 20
```

特点：

- 可以输出不同类型的数据；
- 不需要手动调用 `str()`；
- 多个对象之间默认使用空格分隔；
- 本质上不是字符串拼接，而是将多个对象分别交给 `print()`。

```python
print("结果：", 10 + 20)
```

推荐写法：

```python
age = 20

print("年龄：", age)
print(f"年龄：{age}")
```

不推荐：

```python
print("年龄：" + str(age))
```

---

# 三、`sep` 设置分隔符

`sep` 控制多个输出对象之间插入什么内容。

## 3.1 默认空格

```python
print("A", "B", "C")
```

等价于：

```python
print("A", "B", "C", sep=" ")
```

输出：

```text
A B C
```

## 3.2 自定义分隔符

```python
print("2026", "07", "18", sep="-")
```

输出：

```text
2026-07-18
```

```python
print("www", "example", "com", sep=".")
```

输出：

```text
www.example.com
```

```python
print(1, 2, 3, 4, sep=", ")
```

输出：

```text
1, 2, 3, 4
```

## 3.3 不使用分隔符

```python
print("A", "B", "C", sep="")
```

输出：

```text
ABC
```

---

# 四、`end` 设置结束符

默认情况下，`print()` 输出后会自动换行：

```python
print("Hello")
print("Python")
```

等价于：

```python
print("Hello", end="\n")
print("Python", end="\n")
```

## 4.1 不换行

```python
print("Hello", end="")
print("Python")
```

输出：

```text
HelloPython
```

## 4.2 使用空格结束

```python
print("Hello", end=" ")
print("Python")
```

输出：

```text
Hello Python
```

## 4.3 使用其他字符结束

```python
print("第一项", end="；")
print("第二项")
```

输出：

```text
第一项；第二项
```

## 4.4 循环中横向输出

```python
for i in range(5):
    print(i, end=" ")
```

输出：

```text
0 1 2 3 4
```

---

# 五、常用转义字符

| 转义字符 | 含义 |
|---|---|
| `\n` | 换行 |
| `\t` | 制表符 |
| `\\` | 一个反斜杠 |
| `\'` | 单引号 |
| `\"` | 双引号 |
| `\r` | 回到当前行开头 |
| `\b` | 退格 |
| `\0` | 空字符 |

## 5.1 换行符 `\n`

```python
print("第一行\n第二行\n第三行")
```

输出：

```text
第一行
第二行
第三行
```

## 5.2 制表符 `\t`

```python
print("姓名\t年龄\t成绩")
print("Tom\t20\t95")
```

`\t` 表示移动到下一个制表位，不一定严格等于固定数量的空格。

## 5.3 输出引号

```python
print("他说：\"你好\"")
print('It\'s Python.')
```

## 5.4 输出反斜杠

```python
print("C:\\Users\\Tom")
```

输出：

```text
C:\Users\Tom
```

---

# 六、字符串拼接

使用 `+` 可以拼接字符串：

```python
name = "Tom"

print("Hello, " + name)
```

但 `+` 两边必须都是字符串。

错误：

```python
age = 20
print("年龄：" + age)
```

会产生：

```text
TypeError
```

正确：

```python
print("年龄：" + str(age))
print("年龄：", age)
print(f"年龄：{age}")
```

---

# 七、`%` 格式化

旧式 `%` 格式化与 C 语言中的 `printf()` 类似。

基本语法：

```python
"格式字符串" % 数据
```

示例：

```python
name = "Tom"
age = 20

print("姓名：%s，年龄：%d" % (name, age))
```

输出：

```text
姓名：Tom，年龄：20
```

## 7.1 常用占位符

| 占位符 | 含义 |
|---|---|
| `%s` | 字符串 |
| `%d` | 十进制整数 |
| `%i` | 十进制整数 |
| `%f` | 浮点数 |
| `%e` | 科学计数法，小写 `e` |
| `%E` | 科学计数法，大写 `E` |
| `%o` | 八进制整数 |
| `%x` | 小写十六进制整数 |
| `%X` | 大写十六进制整数 |
| `%c` | 单个字符 |
| `%r` | 使用 `repr()` 转换 |
| `%%` | 输出百分号 `%` |

## 7.2 字符串 `%s`

```python
name = "Python"

print("语言：%s" % name)
```

`%s` 会调用 `str()`，因此也可以输出其他类型：

```python
print("数字：%s" % 100)
```

## 7.3 整数 `%d`

```python
age = 20

print("年龄：%d" % age)
```

多个数据要放入元组：

```python
a = 10
b = 20

print("%d + %d = %d" % (a, b, a + b))
```

## 7.4 浮点数 `%f`

```python
pi = 3.1415926

print("%f" % pi)
```

默认保留 6 位小数：

```text
3.141593
```

指定小数位数：

```python
print("%.2f" % pi)
print("%.4f" % pi)
```

## 7.5 设置字段宽度

```python
print("%5d" % 12)
```

输出：

```text
   12
```

字段宽度是最小宽度，数据超出时不会截断：

```python
print("%3d" % 12345)
```

输出：

```text
12345
```

## 7.6 左对齐

```python
print("%-5d|" % 12)
```

输出：

```text
12   |
```

## 7.7 补零

```python
print("%05d" % 12)
```

输出：

```text
00012
```

## 7.8 宽度和精度

```python
num = 3.1415926

print("%10.2f" % num)
```

其中：

- `10`：总宽度至少为 10；
- `.2`：保留 2 位小数；
- `f`：浮点数格式。

## 7.9 显示正负号

```python
print("%+d" % 10)
print("%+d" % -10)
```

输出：

```text
+10
-10
```

## 7.10 输出百分号

```python
score = 95

print("正确率：%d%%" % score)
```

输出：

```text
正确率：95%
```

## 7.11 字典格式化

```python
data = {
    "name": "Tom",
    "age": 20
}

print("姓名：%(name)s，年龄：%(age)d" % data)
```

---

# 八、`str.format()` 格式化

基本语法：

```python
"字符串{}".format(数据)
```

示例：

```python
name = "Tom"
age = 20

print("姓名：{}，年龄：{}".format(name, age))
```

## 8.1 按顺序填充

```python
print("{} + {} = {}".format(10, 20, 30))
```

## 8.2 使用位置编号

编号从 `0` 开始：

```python
print("{0} + {1} = {2}".format(10, 20, 30))
```

重复使用参数：

```python
print("{0}爱学习，{0}爱编程".format("Tom"))
```

调整顺序：

```python
print("{1} {0}".format("Python", "Hello"))
```

注意：自动编号和手动编号不能混用。

错误：

```python
"{} {1}".format("A", "B")
```

## 8.3 使用关键字参数

```python
print("姓名：{name}，年龄：{age}".format(name="Tom", age=20))
```

## 8.4 使用字典

```python
student = {
    "name": "Tom",
    "score": 95
}

print("姓名：{name}，成绩：{score}".format(**student))
```

也可以直接访问字典键：

```python
print("姓名：{0[name]}，成绩：{0[score]}".format(student))
```

## 8.5 访问列表元素

```python
data = ["Tom", 20, 95]

print("姓名：{0[0]}，年龄：{0[1]}，成绩：{0[2]}".format(data))
```

## 8.6 访问对象属性

```python
class Student:
    def __init__(self):
        self.name = "Tom"
        self.age = 20


student = Student()

print("姓名：{0.name}，年龄：{0.age}".format(student))
```

---

# 九、格式说明符

基本形式：

```python
"{字段名:格式说明符}".format(数据)
```

或：

```python
f"{表达式:格式说明符}"
```

格式说明符的大致结构：

```text
填充字符 对齐方式 符号 # 0 宽度 分组符 .精度 类型
```

并不是每个部分都必须填写。

---

## 9.1 对齐方式

| 符号 | 含义 |
|---|---|
| `<` | 左对齐 |
| `>` | 右对齐 |
| `^` | 居中对齐 |
| `=` | 符号后填充，主要用于数字 |

### 左对齐

```python
print("{:<10}|".format("Python"))
```

输出：

```text
Python    |
```

### 右对齐

```python
print("{:>10}|".format("Python"))
```

输出：

```text
    Python|
```

### 居中对齐

```python
print("{:^10}|".format("Python"))
```

输出：

```text
  Python  |
```

### 符号后填充

```python
print("{:0=6d}".format(-12))
```

输出：

```text
-00012
```

---

## 9.2 自定义填充字符

填充字符写在对齐符号前面。

```python
print("{:*<10}".format("Python"))
print("{:*>10}".format("Python"))
print("{:*^10}".format("Python"))
```

输出：

```text
Python****
****Python
**Python**
```

结构：

```text
填充字符 + 对齐符号 + 宽度
```

例如：

```text
*^10
```

表示：

- 用 `*` 填充；
- 居中对齐；
- 总宽度至少为 10。

---

## 9.3 字段宽度

```python
print("{:10}".format("Python"))
print("{:10}".format(123))
```

默认情况：

- 字符串通常左对齐；
- 数字通常右对齐。

建议明确写对齐方式：

```python
print("{:<10}".format("Python"))
print("{:>10}".format(123))
```

字段宽度是最小宽度，不是最大宽度。

---

## 9.4 整数格式化

```python
num = 255

print("{:d}".format(num))  # 十进制
print("{:b}".format(num))  # 二进制
print("{:o}".format(num))  # 八进制
print("{:x}".format(num))  # 小写十六进制
print("{:X}".format(num))  # 大写十六进制
```

输出：

```text
255
11111111
377
ff
FF
```

### 显示进制前缀

```python
print("{:#b}".format(num))
print("{:#o}".format(num))
print("{:#x}".format(num))
print("{:#X}".format(num))
```

输出：

```text
0b11111111
0o377
0xff
0XFF
```

### 字符格式 `c`

```python
print("{:c}".format(65))
print("{:c}".format(97))
```

输出：

```text
A
a
```

等价于：

```python
print(chr(65))
```

---

## 9.5 显示正负号

### 正负数都显示符号

```python
print("{:+d}".format(10))
print("{:+d}".format(-10))
```

### 仅负数显示负号

```python
print("{:-d}".format(10))
print("{:-d}".format(-10))
```

这是默认行为。

### 正数前留空格

```python
print("{: d}".format(10))
print("{: d}".format(-10))
```

输出：

```text
 10
-10
```

这种方式适合让正负数纵向对齐。

---

## 9.6 数字补零

```python
print("{:05d}".format(12))
```

输出：

```text
00012
```

负数：

```python
print("{:05d}".format(-12))
```

输出：

```text
-0012
```

负号也占一个宽度。

---

## 9.7 千位分隔符

### 逗号分隔

```python
num = 123456789

print("{:,}".format(num))
```

输出：

```text
123,456,789
```

### 下划线分隔

```python
print("{:_}".format(num))
```

输出：

```text
123_456_789
```

浮点数：

```python
num = 1234567.89

print("{:,.2f}".format(num))
```

输出：

```text
1,234,567.89
```

---

## 9.8 浮点数格式化

```python
num = 3.1415926
```

### 固定小数格式 `f`

```python
print("{:f}".format(num))
```

默认保留 6 位小数。

### 指定小数位数

```python
print("{:.2f}".format(num))
print("{:.4f}".format(num))
```

### 总宽度和精度

```python
print("{:10.2f}".format(num))
```

表示：

- 总宽度至少为 10；
- 保留 2 位小数；
- 使用固定小数格式。

### 左对齐

```python
print("{:<10.2f}|".format(num))
```

### 补零

```python
print("{:010.2f}".format(num))
```

输出：

```text
0000003.14
```

---

## 9.9 科学计数法

```python
num = 123456

print("{:e}".format(num))
print("{:E}".format(num))
print("{:.2e}".format(num))
```

输出类似：

```text
1.234560e+05
1.234560E+05
1.23e+05
```

---

## 9.10 通用数字格式 `g`

`g` 会根据数字大小，在普通小数和科学计数法之间自动选择。

```python
print("{:g}".format(123.456))
print("{:g}".format(123456789))
```

`G` 与 `g` 类似，但科学计数法使用大写 `E`。

```python
print("{:.4g}".format(123.456))
```

输出：

```text
123.5
```

注意：`g` 的精度通常表示有效数字位数，而不是小数位数。

---

## 9.11 百分比格式

```python
rate = 0.8567

print("{:.2%}".format(rate))
```

输出：

```text
85.67%
```

百分比格式会自动：

1. 将数据乘以 100；
2. 添加 `%`。

所以数据应写成小数：

```python
rate = 0.95
print("{:.0%}".format(rate))
```

输出：

```text
95%
```

如果写成：

```python
rate = 95
print("{:.0%}".format(rate))
```

会输出：

```text
9500%
```

---

## 9.12 字符串截断

对于字符串，精度表示最多保留多少个字符。

```python
text = "Python"

print("{:.3}".format(text))
```

输出：

```text
Pyt
```

配合宽度：

```python
print("{:10.3}".format(text))
```

表示：

- 字段宽度至少为 10；
- 最多显示 3 个字符。

---

## 9.13 动态宽度和动态精度

```python
num = 3.1415926
width = 10
precision = 3

print("{0:{1}.{2}f}".format(num, width, precision))
```

输出：

```text
     3.142
```

关键字形式：

```python
print(
    "{num:{width}.{precision}f}".format(
        num=3.1415926,
        width=10,
        precision=3
    )
)
```

---

## 9.14 输出普通花括号

因为 `{}` 是格式化符号，所以输出普通花括号要写成双花括号。

```python
print("{{Python}}".format())
```

输出：

```text
{Python}
```

---

# 十、f-string

f-string 从 Python 3.6 开始支持，是现代 Python 中最常用的格式化方法。

基本语法：

```python
f"字符串{表达式}"
```

示例：

```python
name = "Tom"
age = 20

print(f"姓名：{name}，年龄：{age}")
```

优点：

- 写法简洁；
- 可读性高；
- 可以直接写表达式；
- 支持完整的格式说明符。

---

## 10.1 直接计算表达式

```python
a = 10
b = 20

print(f"{a} + {b} = {a + b}")
```

调用方法：

```python
name = "python"

print(f"{name.upper()}")
```

访问列表：

```python
data = [10, 20, 30]

print(f"第一个元素：{data[0]}")
```

访问字典：

```python
student = {
    "name": "Tom",
    "score": 95
}

print(f"姓名：{student['name']}，成绩：{student['score']}")
```

访问对象属性：

```python
print(f"姓名：{student.name}")
```

---

## 10.2 对齐和填充

```python
text = "Python"

print(f"{text:<10}|")
print(f"{text:>10}|")
print(f"{text:^10}|")
```

自定义填充：

```python
print(f"{text:*<10}")
print(f"{text:*>10}")
print(f"{text:*^10}")
```

---

## 10.3 整数进制

```python
num = 255

print(f"{num:d}")
print(f"{num:b}")
print(f"{num:o}")
print(f"{num:x}")
print(f"{num:X}")
```

带进制前缀：

```python
print(f"{num:#b}")
print(f"{num:#o}")
print(f"{num:#x}")
```

---

## 10.4 浮点数

```python
pi = 3.1415926

print(f"{pi:.2f}")
print(f"{pi:.4f}")
print(f"{pi:10.2f}")
print(f"{pi:<10.2f}|")
print(f"{pi:010.2f}")
```

---

## 10.5 千位分隔符

```python
money = 123456789.5

print(f"{money:,.2f}")
```

输出：

```text
123,456,789.50
```

使用下划线：

```python
print(f"{money:_.2f}")
```

---

## 10.6 百分比

```python
rate = 0.8567

print(f"{rate:.2%}")
```

输出：

```text
85.67%
```

---

## 10.7 动态宽度和精度

```python
num = 3.1415926
width = 10
precision = 3

print(f"{num:{width}.{precision}f}")
```

动态填充：

```python
fill = "*"
align = "^"
width = 12
text = "Python"

print(f"{text:{fill}{align}{width}}")
```

---

## 10.8 `=` 调试语法

Python 3.8 及以上支持：

```python
x = 10
y = 20

print(f"{x=}")
print(f"{x + y=}")
```

输出：

```text
x=10
x + y=30
```

也可以结合格式说明符：

```python
pi = 3.1415926

print(f"{pi=:.2f}")
```

输出：

```text
pi=3.14
```

---

## 10.9 `!s`、`!r`、`!a`

### `!s`

调用 `str()`：

```python
text = "Python\nJava"

print(f"{text!s}")
```

### `!r`

调用 `repr()`：

```python
print(f"{text!r}")
```

输出：

```text
'Python\nJava'
```

### `!a`

调用 `ascii()`：

```python
text = "你好"

print(f"{text!a}")
```

非 ASCII 字符会显示为转义形式。

---

## 10.10 输出普通花括号

```python
print(f"{{Python}}")
```

输出：

```text
{Python}
```

结合变量：

```python
name = "Tom"

print(f"{{name: {name}}}")
```

输出：

```text
{name: Tom}
```

---

# 十一、`format()` 内置函数

Python 内置函数：

```python
format(value, format_spec)
```

示例：

```python
num = 3.1415926

result = format(num, ".2f")

print(result)
```

输出：

```text
3.14
```

下面三种写法基本等价：

```python
format(num, ".2f")
"{:.2f}".format(num)
f"{num:.2f}"
```

更多示例：

```python
print(format(255, "b"))
print(format(255, "#x"))
print(format(1234567, ","))
print(format(0.8567, ".2%"))
```

---

# 十二、输出到文件

`print()` 的 `file` 参数可以指定输出目标。

```python
with open("output.txt", "w", encoding="utf-8") as file:
    print("Hello, Python!", file=file)
```

内容会写入文件，而不是显示在终端。

写入类似 CSV 的内容：

```python
with open("output.txt", "w", encoding="utf-8") as file:
    print("姓名", "年龄", "成绩", sep=",", file=file)
    print("Tom", 20, 95, sep=",", file=file)
```

文件内容：

```text
姓名,年龄,成绩
Tom,20,95
```

---

# 十三、`flush` 与动态刷新

默认情况下，输出可能先进入缓冲区。

```python
print("正在处理……", flush=True)
```

`flush=True` 表示立即刷新输出缓冲区。

常见用途：

- 进度显示；
- 实时日志；
- 长时间运行程序；
- 不换行输出。

示例：

```python
import time

for i in range(5):
    print(i, end=" ", flush=True)
    time.sleep(1)
```

## 13.1 使用 `\r` 单行刷新

`\r` 表示回到当前行开头。

```python
import time

for i in range(101):
    print(f"\r进度：{i}%", end="", flush=True)
    time.sleep(0.05)

print()
```

为了避免旧内容残留，可以设置固定宽度：

```python
for i in range(101):
    print(f"\r进度：{i:3d}%", end="", flush=True)
```

---

# 十四、可迭代对象解包输出

```python
nums = [1, 2, 3, 4]
```

直接打印列表：

```python
print(nums)
```

输出：

```text
[1, 2, 3, 4]
```

使用 `*` 解包：

```python
print(*nums)
```

输出：

```text
1 2 3 4
```

设置分隔符：

```python
print(*nums, sep=", ")
```

输出：

```text
1, 2, 3, 4
```

字符串也可以解包：

```python
print(*"Python", sep="-")
```

输出：

```text
P-y-t-h-o-n
```

---

# 十五、`join()` 配合输出

如果列表中都是字符串，可以使用 `join()`：

```python
words = ["Python", "Java", "C"]

print(", ".join(words))
```

输出：

```text
Python, Java, C
```

如果列表中有数字，需要先转换：

```python
nums = [1, 2, 3, 4]

print(", ".join(map(str, nums)))
```

也可以直接使用：

```python
print(*nums, sep=", ")
```

区别：

```python
result = ", ".join(map(str, nums))
```

会生成并返回一个完整字符串，可以保存或继续处理。

```python
print(*nums, sep=", ")
```

只是直接输出，不会返回拼接后的字符串。

---

# 十六、`str()` 与 `repr()`

`print()` 默认显示对象的字符串形式。

```python
text = "Hello\nPython"

print(text)
```

输出：

```text
Hello
Python
```

使用 `repr()`：

```python
print(repr(text))
```

输出：

```text
'Hello\nPython'
```

一般来说：

- `str()`：面向普通用户，强调易读；
- `repr()`：面向程序员，强调准确表示。

在 f-string 中：

```python
print(f"{text}")
print(f"{text!r}")
```

分别接近：

```python
str(text)
repr(text)
```

---

# 十七、自定义对象打印

定义类时，可以通过 `__str__()` 控制 `print()` 的结果。

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Student(name={self.name}, age={self.age})"


student = Student("Tom", 20)

print(student)
```

输出：

```text
Student(name=Tom, age=20)
```

`print(student)` 会先获取对象的字符串表示。

还可以定义 `__repr__()`：

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}，{self.age}岁"

    def __repr__(self):
        return f"Student({self.name!r}, {self.age!r})"
```

```python
student = Student("Tom", 20)

print(student)
print(repr(student))
```

输出：

```text
Tom，20岁
Student('Tom', 20)
```

---

# 十八、格式化方式对比

假设：

```python
name = "Tom"
age = 20
score = 95.567
```

## 18.1 逗号输出

```python
print("姓名：", name, "年龄：", age, "成绩：", score)
```

优点：

- 简单；
- 不需要类型转换；
- 适合快速调试。

缺点：

- 不方便精确控制格式；
- 默认会添加空格。

## 18.2 `%` 格式化

```python
print("姓名：%s，年龄：%d，成绩：%.2f" % (name, age, score))
```

优点：

- 类似 C 语言；
- 旧代码中常见。

缺点：

- 参数多时可读性较差；
- 类型匹配要求明显。

## 18.3 `str.format()`

```python
print("姓名：{}，年龄：{}，成绩：{:.2f}".format(name, age, score))
```

优点：

- 功能强大；
- 支持位置参数和关键字参数；
- 兼容较老版本 Python。

缺点：

- 参数较多时写法较长。

## 18.4 f-string

```python
print(f"姓名：{name}，年龄：{age}，成绩：{score:.2f}")
```

优点：

- 最简洁；
- 可读性高；
- 可直接写表达式；
- 现代 Python 中最推荐。

---

# 十九、常用格式速查

```python
num = 12345.6789
```

| 需求 | 写法 | 结果示例 |
|---|---|---|
| 保留两位小数 | `f"{num:.2f}"` | `12345.68` |
| 总宽度为 12 | `f"{num:12.2f}"` | 右对齐 |
| 左对齐 | `f"{num:<12.2f}"` | 左对齐 |
| 右对齐 | `f"{num:>12.2f}"` | 右对齐 |
| 居中 | `f"{num:^12.2f}"` | 居中 |
| 前面补零 | `f"{num:012.2f}"` | `000012345.68` |
| 显示正号 | `f"{num:+.2f}"` | `+12345.68` |
| 千位分隔 | `f"{num:,.2f}"` | `12,345.68` |
| 科学计数法 | `f"{num:.2e}"` | `1.23e+04` |
| 百分比 | `f"{0.856:.2%}"` | `85.60%` |
| 二进制 | `f"{255:b}"` | `11111111` |
| 带前缀二进制 | `f"{255:#b}"` | `0b11111111` |
| 十六进制 | `f"{255:x}"` | `ff` |
| 大写十六进制 | `f"{255:X}"` | `FF` |
| 字符串左对齐 | `f"{'Python':<10}"` | 右侧补空格 |
| 字符串居中 | `f"{'Python':^10}"` | 两侧补空格 |
| 自定义填充 | `f"{'Python':*^10}"` | `**Python**` |

---

# 二十、常见错误

## 20.1 字符串和整数直接使用 `+`

错误：

```python
age = 20
print("年龄：" + age)
```

正确：

```python
print("年龄：" + str(age))
print("年龄：", age)
print(f"年龄：{age}")
```

---

## 20.2 占位符数量不一致

错误：

```python
print("{} {}".format(10))
```

正确：

```python
print("{} {}".format(10, 20))
```

---

## 20.3 自动编号和手动编号混用

错误：

```python
print("{} {1}".format("A", "B"))
```

正确：

```python
print("{} {}".format("A", "B"))
```

或者：

```python
print("{0} {1}".format("A", "B"))
```

---

## 20.4 格式类型不匹配

错误：

```python
print("{:d}".format(3.14))
```

`d` 要求整数，但传入了浮点数。

正确：

```python
print("{:.2f}".format(3.14))
```

---

## 20.5 百分比数据写成 95

错误：

```python
rate = 95

print(f"{rate:.2%}")
```

输出：

```text
9500.00%
```

正确：

```python
rate = 0.95

print(f"{rate:.2%}")
```

---

## 20.6 忘记转义花括号

需要显示普通花括号时：

```python
name = "Tom"

print(f"{{name: {name}}}")
```

---

## 20.7 把字段宽度理解为固定宽度

```python
print(f"{123456:3d}")
```

仍然会输出：

```text
123456
```

字段宽度是最小宽度，数据超出时不会被截断。

---

# 二十一、核心总结

`print()` 的完整语法：

```python
print(*objects, sep=" ", end="\n", file=None, flush=False)
```

常见格式化方式：

```python
age = 20

# 1. 逗号输出
print("年龄：", age)

# 2. % 格式化
print("年龄：%d" % age)

# 3. str.format()
print("年龄：{}".format(age))

# 4. f-string
print(f"年龄：{age}")
```

现代 Python 中，重点掌握：

```python
f"{数据:格式说明符}"
```

最常用格式：

```python
f"{num:.2f}"       # 保留两位小数
f"{num:10.2f}"     # 宽度10，保留两位小数
f"{num:<10.2f}"    # 左对齐
f"{num:>10.2f}"    # 右对齐
f"{num:^10.2f}"    # 居中
f"{num:010.2f}"    # 补零
f"{num:+.2f}"      # 显示正负号
f"{num:,.2f}"      # 千位分隔
f"{num:.2e}"       # 科学计数法
f"{rate:.2%}"      # 百分比
f"{num:#b}"        # 二进制并显示前缀
f"{num:#x}"        # 十六进制并显示前缀
```

可以将格式说明符理解为：

```text
数据如何转换
+ 保留多少精度
+ 占多宽
+ 如何对齐
+ 使用什么字符填充
```

学习优先级建议：

1. 先掌握 `print()` 的 `sep` 和 `end`；
2. 熟练使用 f-string；
3. 掌握 `.2f`、宽度、对齐、补零、千位分隔、百分比；
4. 能看懂 `%` 和 `str.format()`；
5. 最后学习动态宽度、`repr()`、`flush`、自定义对象格式化。
