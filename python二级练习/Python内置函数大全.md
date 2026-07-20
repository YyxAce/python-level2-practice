# Python 内置函数大全

> 适用范围：Python 3  
> 内置函数无需 `import`，可以直接调用。  
> 说明：官方“内置函数”页面也收录了 `int()`、`list()`、`dict()` 等内置类型构造器。

---

## 目录

1. [完整函数列表](#1-完整函数列表)
2. [输入与输出](#2-输入与输出)
3. [数值计算与进制转换](#3-数值计算与进制转换)
4. [类型转换与对象构造](#4-类型转换与对象构造)
5. [序列与迭代](#5-序列与迭代)
6. [字符、编码与格式化](#6-字符编码与格式化)
7. [类型判断与对象信息](#7-类型判断与对象信息)
8. [属性与命名空间操作](#8-属性与命名空间操作)
9. [面向对象相关函数](#9-面向对象相关函数)
10. [异步迭代](#10-异步迭代)
11. [代码执行、调试与帮助](#11-代码执行调试与帮助)
12. [易混淆函数对比](#12-易混淆函数对比)
13. [学习优先级](#13-学习优先级)
14. [内置函数速查表](#14-内置函数速查表)

---

# 1. 完整函数列表

```text
abs()          aiter()        all()          anext()        any()
ascii()        bin()          bool()         breakpoint()   bytearray()
bytes()        callable()     chr()          classmethod()  compile()
complex()      delattr()      dict()         dir()          divmod()
enumerate()    eval()         exec()         filter()       float()
format()       frozenset()    getattr()      globals()      hasattr()
hash()         help()         hex()          id()           input()
int()          isinstance()   issubclass()   iter()         len()
list()         locals()       map()          max()          memoryview()
min()          next()         object()       oct()          open()
ord()          pow()          print()        property()     range()
repr()         reversed()     round()        set()          setattr()
slice()        sorted()       staticmethod() str()          sum()
super()        tuple()        type()         vars()         zip()
__import__()
```

---

# 2. 输入与输出

## 2.1 `print()`：输出内容

```python
print(*objects, sep=' ', end='\n', file=None, flush=False)
```

| 参数 | 作用 |
|---|---|
| `objects` | 要输出的一个或多个对象 |
| `sep` | 多个对象之间的分隔符，默认空格 |
| `end` | 输出结束时追加的内容，默认换行 |
| `file` | 输出目标，默认是屏幕 |
| `flush` | 是否立即刷新输出缓冲区 |

```python
print("姓名", "Jok", sep="：")
print("Hello", end=" ")
print("Python")
```

输出：

```text
姓名：Jok
Hello Python
```

---

## 2.2 `input()`：接收键盘输入

```python
input(prompt='')
```

```python
name = input("请输入姓名：")
age = int(input("请输入年龄："))
```

`input()` 的返回值永远是字符串：

```python
x = input("请输入：")
print(type(x))       # <class 'str'>
```

---

## 2.3 `open()`：打开文件

```python
open(file, mode='r', encoding=None, ...)
```

常见模式：

| 模式 | 作用 |
|---|---|
| `'r'` | 只读 |
| `'w'` | 写入；原文件存在时清空 |
| `'a'` | 追加写入 |
| `'x'` | 创建新文件；已存在则报错 |
| `'b'` | 二进制模式 |
| `'t'` | 文本模式 |
| `'+'` | 同时允许读写 |

推荐使用 `with`：

```python
with open("test.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(content)
```

写入文件：

```python
with open("test.txt", "w", encoding="utf-8") as file:
    file.write("Hello, Python!")
```

---

# 3. 数值计算与进制转换

## 3.1 `abs()`：绝对值或复数的模

```python
print(abs(-10))       # 10
print(abs(-3.5))      # 3.5
print(abs(3 + 4j))    # 5.0
```

---

## 3.2 `max()`：最大值

```python
print(max(3, 8, 5))              # 8
print(max([10, 20, 15]))         # 20
print(max(["aaa", "b"], key=len)) # aaa
```

空序列可以设置默认值：

```python
print(max([], default=0))        # 0
```

---

## 3.3 `min()`：最小值

```python
print(min(3, 8, 5))              # 3
print(min(["aaa", "b"], key=len)) # b
```

---

## 3.4 `sum()`：求和

```python
print(sum([1, 2, 3, 4]))         # 10
print(sum([1, 2, 3], 10))        # 16
```

第二个参数是初始值，因此第二个例子相当于：

```text
10 + 1 + 2 + 3
```

字符串拼接应使用：

```python
result = "".join(["Python", "很", "好"])
```

---

## 3.5 `round()`：数值舍入

```python
print(round(3.14159))       # 3
print(round(3.14159, 2))    # 3.14
print(round(1234, -2))      # 1200
```

Python 通常采用“向偶数舍入”：

```python
print(round(2.5))           # 2
print(round(3.5))           # 4
```

浮点数存在二进制表示误差：

```python
print(round(2.675, 2))      # 可能得到 2.67
```

---

## 3.6 `pow()`：幂运算

```python
print(pow(2, 3))       # 8
print(pow(2, 3, 5))    # 3
```

三参数形式相当于：

```python
(2 ** 3) % 5
```

---

## 3.7 `divmod()`：同时求商和余数

```python
quotient, remainder = divmod(17, 5)

print(quotient)       # 3
print(remainder)      # 2
```

返回值相当于：

```python
(a // b, a % b)
```

---

## 3.8 `bin()`、`oct()`、`hex()`：进制转换

```python
number = 10

print(bin(number))    # 0b1010
print(oct(number))    # 0o12
print(hex(number))    # 0xa
```

去掉前缀：

```python
print(format(number, "b"))    # 1010
print(format(number, "o"))    # 12
print(format(number, "x"))    # a
```

---

# 4. 类型转换与对象构造

## 4.1 `int()`：转换为整数

```python
print(int(3.9))          # 3
print(int(-3.9))         # -3
print(int("123"))        # 123
print(int("1010", 2))    # 10
print(int("ff", 16))     # 255
```

注意：浮点数转整数是截断小数部分，不是四舍五入。

---

## 4.2 `float()`：转换为浮点数

```python
print(float(10))         # 10.0
print(float("3.14"))     # 3.14
```

---

## 4.3 `complex()`：创建复数

```python
print(complex(3, 4))       # (3+4j)
print(complex("3+4j"))     # (3+4j)
```

---

## 4.4 `bool()`：转换为布尔值

常见假值：

```python
False
None
0
0.0
0j
""
[]
()
{}
set()
```

```python
print(bool(0))          # False
print(bool(""))         # False
print(bool([]))         # False
print(bool("0"))        # True
print(bool("False"))    # True
```

非空字符串都是真值。

---

## 4.5 `str()`：转换为字符串

```python
age = 20
text = str(age)

print(text)          # 20
print(type(text))    # <class 'str'>
```

---

## 4.6 `list()`：创建列表

```python
print(list("abc"))             # ['a', 'b', 'c']
print(list((1, 2, 3)))         # [1, 2, 3]
print(list(range(5)))          # [0, 1, 2, 3, 4]
```

---

## 4.7 `tuple()`：创建元组

```python
print(tuple([1, 2, 3]))        # (1, 2, 3)
print(tuple("abc"))            # ('a', 'b', 'c')
```

---

## 4.8 `set()`：创建可变集合

```python
print(set([1, 2, 2, 3]))       # {1, 2, 3}
```

常用于去重：

```python
numbers = [1, 1, 2, 2, 3]
result = list(set(numbers))
```

集合不保证按原列表顺序排列。保持顺序去重可以使用：

```python
result = list(dict.fromkeys(numbers))
```

---

## 4.9 `frozenset()`：创建不可变集合

```python
s = frozenset([1, 2, 3])
print(s)
```

`frozenset` 不能添加或删除元素，因此可以在满足条件时作为：

- 字典的键
- 另一个集合的元素

---

## 4.10 `dict()`：创建字典

```python
print(dict())                         # {}
print(dict(name="Jok", age=20))
print(dict([("a", 1), ("b", 2)]))
```

---

## 4.11 `range()`：创建整数范围对象

```python
print(list(range(5)))
# [0, 1, 2, 3, 4]

print(list(range(2, 8)))
# [2, 3, 4, 5, 6, 7]

print(list(range(10, 0, -2)))
# [10, 8, 6, 4, 2]
```

特点：

- 包含 `start`
- 不包含 `stop`
- `step` 不能为 `0`
- `range` 本身不是列表
- 使用惰性计算，不会一次保存全部整数

---

## 4.12 `bytes()`：不可变字节序列

```python
data = bytes([65, 66, 67])
print(data)                  # b'ABC'
```

字符串编码：

```python
data = "你好".encode("utf-8")
```

---

## 4.13 `bytearray()`：可变字节序列

```python
data = bytearray(b"ABC")
data[0] = 97

print(data)                 # bytearray(b'aBC')
```

---

## 4.14 `memoryview()`：内存视图

可在不复制底层二进制数据的情况下访问数据：

```python
data = bytearray(b"abcd")
view = memoryview(data)

view[0] = 65
print(data)                 # bytearray(b'Abcd')
```

常用于：

- 大型二进制数据
- 网络编程
- 图像处理
- 高性能数据操作

---

## 4.15 `object()`：基础对象

```python
obj = object()
print(type(obj))           # <class 'object'>
```

`object` 是 Python 类体系中最基础的类。

---

## 4.16 `slice()`：创建切片对象

```python
numbers = [0, 1, 2, 3, 4, 5]
s = slice(1, 5, 2)

print(numbers[s])          # [1, 3]
```

相当于：

```python
numbers[1:5:2]
```

---

# 5. 序列与迭代

## 5.1 `len()`：获取长度

```python
print(len("Python"))              # 6
print(len([10, 20, 30]))          # 3
print(len({"a": 1, "b": 2}))      # 2
```

字典的长度表示键值对数量。

---

## 5.2 `enumerate()`：同时获得索引和元素

```python
names = ["张三", "李四", "王五"]

for index, name in enumerate(names):
    print(index, name)
```

从 `1` 开始编号：

```python
for index, name in enumerate(names, start=1):
    print(index, name)
```

---

## 5.3 `zip()`：并行组合多个可迭代对象

```python
names = ["张三", "李四"]
scores = [90, 85]

print(list(zip(names, scores)))
# [('张三', 90), ('李四', 85)]
```

并行遍历：

```python
for name, score in zip(names, scores):
    print(name, score)
```

默认以最短对象为准：

```python
print(list(zip([1, 2, 3], ["a", "b"])))
# [(1, 'a'), (2, 'b')]
```

严格检查长度：

```python
zip([1, 2, 3], ["a", "b"], strict=True)
```

长度不一致会抛出 `ValueError`。

---

## 5.4 `sorted()`：排序并返回新列表

```python
numbers = [3, 1, 4, 2]

result = sorted(numbers)

print(result)       # [1, 2, 3, 4]
print(numbers)      # [3, 1, 4, 2]
```

降序：

```python
sorted(numbers, reverse=True)
```

按长度排序：

```python
words = ["Python", "C", "Java"]
print(sorted(words, key=len))
```

按字典字段排序：

```python
students = [
    {"name": "张三", "score": 80},
    {"name": "李四", "score": 95}
]

result = sorted(students, key=lambda x: x["score"])
```

---

## 5.5 `reversed()`：反向迭代

```python
numbers = [1, 2, 3]

print(list(reversed(numbers)))
# [3, 2, 1]
```

不会修改原对象。

---

## 5.6 `iter()`：获取迭代器

```python
numbers = [10, 20, 30]
iterator = iter(numbers)

print(next(iterator))      # 10
print(next(iterator))      # 20
```

双参数形式会不断调用函数，直到返回哨兵值：

```python
with open("data.bin", "rb") as file:
    for block in iter(lambda: file.read(1024), b""):
        print(block)
```

---

## 5.7 `next()`：获取迭代器下一个元素

```python
iterator = iter([10, 20])

print(next(iterator))              # 10
print(next(iterator))              # 20
print(next(iterator, "结束"))      # 结束
```

没有默认值且迭代结束时，会抛出 `StopIteration`。

---

## 5.8 `map()`：对元素逐个执行函数

```python
numbers = [1, 2, 3]

result = map(lambda x: x * 2, numbers)

print(list(result))
# [2, 4, 6]
```

多个可迭代对象：

```python
result = map(lambda x, y: x + y, [1, 2], [10, 20])
print(list(result))       # [11, 22]
```

`map()` 返回迭代器。简单转换通常也可以写成列表推导式：

```python
result = [x * 2 for x in numbers]
```

---

## 5.9 `filter()`：筛选元素

```python
numbers = [1, 2, 3, 4, 5]

result = filter(lambda x: x % 2 == 0, numbers)

print(list(result))
# [2, 4]
```

列表推导式写法：

```python
result = [x for x in numbers if x % 2 == 0]
```

函数参数为 `None` 时，保留真值元素：

```python
data = [0, 1, "", "Python", None, [], [1]]
print(list(filter(None, data)))
# [1, 'Python', [1]]
```

---

## 5.10 `all()`：是否全部为真

```python
print(all([True, True]))          # True
print(all([True, False]))         # False
print(all([]))                    # True
```

应用：

```python
scores = [80, 75, 90]

if all(score >= 60 for score in scores):
    print("全部及格")
```

---

## 5.11 `any()`：是否至少一个为真

```python
print(any([False, True]))         # True
print(any([False, False]))        # False
print(any([]))                    # False
```

应用：

```python
scores = [50, 55, 80]

if any(score >= 60 for score in scores):
    print("至少一人及格")
```

---

# 6. 字符、编码与格式化

## 6.1 `ord()`：字符转 Unicode 码位

```python
print(ord("A"))        # 65
print(ord("中"))       # 20013
```

参数必须是长度为 `1` 的字符串。

---

## 6.2 `chr()`：Unicode 码位转字符

```python
print(chr(65))         # A
print(chr(20013))      # 中
```

`chr()` 和 `ord()` 互为逆操作。

---

## 6.3 `repr()`：开发者表示形式

```python
text = "hello\nworld"

print(text)
print(repr(text))
```

输出：

```text
hello
world
'hello\nworld'
```

- `str()` 偏向用户阅读
- `repr()` 偏向调试和开发者阅读

---

## 6.4 `ascii()`：仅含 ASCII 的表示

```python
print(ascii("中国"))
# '\u4e2d\u56fd'
```

与 `repr()` 类似，但会转义非 ASCII 字符。

---

## 6.5 `format()`：格式化对象

```python
print(format(3.14159, ".2f"))    # 3.14
print(format(255, "x"))          # ff
print(format(10, "08b"))         # 00001010
print(format(1234567, ","))      # 1,234,567
print(format(0.856, ".1%"))      # 85.6%
```

常见格式：

| 格式 | 作用 |
|---|---|
| `.2f` | 保留两位小数 |
| `b` | 二进制 |
| `o` | 八进制 |
| `x` / `X` | 十六进制 |
| `e` | 科学计数法 |
| `%` | 百分比 |
| `,` | 千位分隔符 |
| `>10` | 右对齐，宽度 10 |
| `<10` | 左对齐，宽度 10 |
| `^10` | 居中，宽度 10 |

对应的 f-string：

```python
value = 3.14159
print(f"{value:.2f}")
```

---

# 7. 类型判断与对象信息

## 7.1 `type()`：查看对象类型

```python
print(type(10))          # <class 'int'>
print(type(3.14))        # <class 'float'>
print(type("Python"))    # <class 'str'>
```

三参数形式：

```python
type(name, bases, namespace)
```

可动态创建类，初学阶段一般不需要。

---

## 7.2 `isinstance()`：判断对象类型

```python
print(isinstance(10, int))               # True
print(isinstance(10, (int, float)))      # True
```

相比 `type(x) == int`，`isinstance()` 会考虑继承关系。

---

## 7.3 `issubclass()`：判断子类关系

```python
class Animal:
    pass

class Dog(Animal):
    pass

print(issubclass(Dog, Animal))       # True
print(issubclass(Animal, Animal))    # True
```

---

## 7.4 `id()`：获取对象身份标识

```python
a = [1, 2]
b = a
c = [1, 2]

print(id(a) == id(b))       # True
print(id(a) == id(c))       # False
```

不要把 `id()` 简单理解为永久固定的内存地址。

---

## 7.5 `hash()`：获取哈希值

```python
print(hash("Python"))
print(hash((1, 2, 3)))
```

列表不可哈希：

```python
hash([1, 2, 3])       # TypeError
```

常见可哈希对象：

- 整数、浮点数
- 字符串
- 元素均可哈希的元组
- `frozenset`

常见不可哈希对象：

- 列表
- 字典
- 普通集合

---

## 7.6 `callable()`：判断对象能否被调用

```python
def func():
    pass

print(callable(func))       # True
print(callable(len))        # True
print(callable(list))       # True
print(callable(10))         # False
```

---

# 8. 属性与命名空间操作

## 8.1 `getattr()`：获取属性

```python
class Student:
    name = "Jok"

student = Student()

print(getattr(student, "name"))               # Jok
print(getattr(student, "age", "不存在"))       # 不存在
```

属性名可以由字符串动态指定。

---

## 8.2 `setattr()`：设置属性

```python
setattr(student, "age", 20)
print(student.age)       # 20
```

相当于：

```python
student.age = 20
```

---

## 8.3 `hasattr()`：判断属性是否存在

```python
print(hasattr(student, "name"))       # True
print(hasattr(student, "score"))      # False
```

---

## 8.4 `delattr()`：删除属性

```python
delattr(student, "age")
```

相当于：

```python
del student.age
```

---

## 8.5 `dir()`：查看属性和方法名称

```python
print(dir(str))
print(dir([]))
```

常用于交互式探索，但不保证列出对象可动态访问的全部属性。

---

## 8.6 `vars()`：查看属性字典

```python
class Student:
    def __init__(self):
        self.name = "Jok"
        self.age = 20

student = Student()

print(vars(student))
# {'name': 'Jok', 'age': 20}
```

通常等价于：

```python
student.__dict__
```

---

## 8.7 `globals()`：全局命名空间

```python
x = 100
print(globals()["x"])       # 100
```

返回当前模块的全局命名空间字典。

---

## 8.8 `locals()`：局部命名空间

```python
def test():
    x = 10
    y = 20
    print(locals())

test()
```

不建议依靠修改 `locals()` 的返回结果来修改函数局部变量。

---

# 9. 面向对象相关函数

## 9.1 `classmethod()`：类方法

```python
class Student:
    school = "金职大"

    @classmethod
    def show_school(cls):
        print(cls.school)

Student.show_school()
```

- 第一个参数通常写作 `cls`
- `cls` 代表当前类

---

## 9.2 `staticmethod()`：静态方法

```python
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

print(Calculator.add(3, 5))       # 8
```

静态方法不会自动接收 `self` 或 `cls`。

---

## 9.3 `property()`：把方法作为属性访问

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return 3.14 * self.radius ** 2

circle = Circle(2)
print(circle.area)
```

访问时写：

```python
circle.area
```

而不是：

```python
circle.area()
```

---

## 9.4 `super()`：按 MRO 调用后续类方法

```python
class Animal:
    def speak(self):
        print("动物叫")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("汪汪")

dog = Dog()
dog.speak()
```

`super()` 按方法解析顺序（MRO）查找，不应简单理解成“直接找到父类”。

---

# 10. 异步迭代

## 10.1 `aiter()`：获取异步迭代器

```python
async_iterator = aiter(async_iterable)
```

近似等价于：

```python
async_iterable.__aiter__()
```

---

## 10.2 `anext()`：获取异步迭代器下一项

```python
value = await anext(async_iterator)
```

它是异步版本的 `next()`。

可以提供默认值：

```python
value = await anext(async_iterator, default)
```

---

# 11. 代码执行、调试与帮助

## 11.1 `help()`：查看帮助文档

```python
help(print)
help(str)
help(str.split)
```

适合在 IDLE、交互式解释器和 Jupyter 中使用。

---

## 11.2 `breakpoint()`：进入调试器

```python
def divide(a, b):
    breakpoint()
    return a / b

divide(10, 2)
```

常见 `pdb` 命令：

| 命令 | 作用 |
|---|---|
| `n` | 执行下一行 |
| `s` | 进入函数 |
| `c` | 继续执行 |
| `p 表达式` | 查看表达式 |
| `q` | 退出调试 |

---

## 11.3 `eval()`：计算表达式

```python
result = eval("1 + 2 * 3")
print(result)                 # 7
```

`eval()` 只能直接计算表达式：

```python
eval("x = 10")       # SyntaxError
```

安全警告：不要把不可信输入直接交给 `eval()`。

---

## 11.4 `exec()`：执行语句或代码块

```python
code = '''
x = 10
y = 20
print(x + y)
'''

exec(code)
```

区别：

| 函数 | 处理内容 | 返回表达式结果 |
|---|---|---|
| `eval()` | 单个表达式 | 是 |
| `exec()` | 语句或代码块 | 通常返回 `None` |

不要用 `exec()` 执行不可信代码。

---

## 11.5 `compile()`：编译 Python 代码

```python
code = compile("1 + 2", "<string>", "eval")
print(eval(code))                # 3
```

常见模式：

| 模式 | 用途 |
|---|---|
| `'eval'` | 编译单个表达式 |
| `'exec'` | 编译语句或代码块 |
| `'single'` | 编译单条交互式语句 |

---

## 11.6 `__import__()`：底层导入函数

```python
math_module = __import__("math")
print(math_module.sqrt(16))       # 4.0
```

普通代码应直接写：

```python
import math
```

动态导入通常推荐：

```python
import importlib

module = importlib.import_module("math")
```

---

# 12. 易混淆函数对比

## 12.1 `str()`、`repr()`、`ascii()`

| 函数 | 主要用途 |
|---|---|
| `str()` | 给普通用户阅读 |
| `repr()` | 给开发者调试 |
| `ascii()` | 类似 `repr()`，但转义非 ASCII 字符 |

---

## 12.2 `sorted()` 与 `list.sort()`

| 项目 | `sorted()` | `list.sort()` |
|---|---|---|
| 支持对象 | 任意可迭代对象 | 仅列表 |
| 修改原对象 | 否 | 是 |
| 返回值 | 新列表 | `None` |

---

## 12.3 `type()` 与 `isinstance()`

```python
print(type(True) == int)         # False
print(isinstance(True, int))     # True
```

原因：`bool` 是 `int` 的子类。

类型判断通常优先使用 `isinstance()`。

---

## 12.4 `map()` 与列表推导式

```python
result1 = map(lambda x: x * 2, [1, 2, 3])
result2 = [x * 2 for x in [1, 2, 3]]
```

- 简单转换：列表推导式通常更直观
- 已有现成函数：`map()` 很方便
- 需要惰性迭代：可以使用 `map()`

---

## 12.5 `all()` 与 `any()`

| 输入 | `all()` | `any()` |
|---|---:|---:|
| `[True, True]` | `True` | `True` |
| `[True, False]` | `False` | `True` |
| `[False, False]` | `False` | `False` |
| `[]` | `True` | `False` |

---

## 12.6 `int()` 与 `round()`

```python
print(int(3.9))       # 3
print(round(3.9))     # 4
```

- `int()`：截断小数部分
- `round()`：舍入到指定精度

---

# 13. 学习优先级

## 第一阶段：必须熟练掌握

```text
print()       input()
int()         float()       str()         bool()
list()        tuple()       set()         dict()
len()         range()
max()         min()         sum()
abs()         round()
type()        isinstance()
enumerate()   zip()
sorted()      reversed()
open()
```

---

## 第二阶段：理解并能使用

```text
all()         any()
map()         filter()
iter()        next()
bin()         oct()         hex()
ord()         chr()
repr()        format()
getattr()     setattr()     hasattr()
dir()         vars()
```

---

## 第三阶段：面向对象阶段掌握

```text
classmethod()
staticmethod()
property()
super()
issubclass()
object()
```

---

## 第四阶段：高级或特殊场景

```text
aiter()       anext()
memoryview()
compile()     eval()        exec()
globals()     locals()
breakpoint()
__import__()
```

其中以下函数不要为了代码简短而随意使用：

```text
eval()
exec()
__import__()
```

---

# 14. 内置函数速查表

| 函数 | 主要作用 |
|---|---|
| `abs()` | 求绝对值或复数的模 |
| `aiter()` | 获取异步迭代器 |
| `all()` | 判断所有元素是否都为真 |
| `anext()` | 获取异步迭代器下一项 |
| `any()` | 判断是否至少一个元素为真 |
| `ascii()` | 返回非 ASCII 字符被转义后的表示 |
| `bin()` | 整数转二进制字符串 |
| `bool()` | 转换为布尔值 |
| `breakpoint()` | 进入调试器 |
| `bytearray()` | 创建可变字节序列 |
| `bytes()` | 创建不可变字节序列 |
| `callable()` | 判断对象能否被调用 |
| `chr()` | Unicode 码位转字符 |
| `classmethod()` | 创建类方法 |
| `compile()` | 编译 Python 代码 |
| `complex()` | 创建复数 |
| `delattr()` | 删除对象属性 |
| `dict()` | 创建字典 |
| `dir()` | 查看对象的属性和方法名称 |
| `divmod()` | 同时计算整除商和余数 |
| `enumerate()` | 同时获取索引和元素 |
| `eval()` | 计算表达式 |
| `exec()` | 执行语句或代码块 |
| `filter()` | 按条件筛选元素 |
| `float()` | 转换为浮点数 |
| `format()` | 格式化对象 |
| `frozenset()` | 创建不可变集合 |
| `getattr()` | 获取对象属性 |
| `globals()` | 获取全局命名空间 |
| `hasattr()` | 判断对象是否具有某属性 |
| `hash()` | 获取对象哈希值 |
| `help()` | 查看帮助文档 |
| `hex()` | 整数转十六进制字符串 |
| `id()` | 获取对象身份标识 |
| `input()` | 接收键盘输入 |
| `int()` | 转换为整数 |
| `isinstance()` | 判断对象是否属于某类型 |
| `issubclass()` | 判断类是否为另一个类的子类 |
| `iter()` | 获取迭代器 |
| `len()` | 获取对象长度 |
| `list()` | 创建列表 |
| `locals()` | 获取局部命名空间 |
| `map()` | 对元素逐个执行函数 |
| `max()` | 获取最大值 |
| `memoryview()` | 创建内存视图 |
| `min()` | 获取最小值 |
| `next()` | 获取迭代器下一项 |
| `object()` | 创建基础对象 |
| `oct()` | 整数转八进制字符串 |
| `open()` | 打开文件 |
| `ord()` | 字符转 Unicode 码位 |
| `pow()` | 幂运算 |
| `print()` | 输出内容 |
| `property()` | 将方法转换为属性 |
| `range()` | 创建整数范围对象 |
| `repr()` | 获取适合调试的对象表示 |
| `reversed()` | 创建反向迭代器 |
| `round()` | 数值舍入 |
| `set()` | 创建集合 |
| `setattr()` | 设置对象属性 |
| `slice()` | 创建切片对象 |
| `sorted()` | 排序并返回新列表 |
| `staticmethod()` | 创建静态方法 |
| `str()` | 转换为字符串 |
| `sum()` | 对元素求和 |
| `super()` | 按 MRO 调用后续类的方法 |
| `tuple()` | 创建元组 |
| `type()` | 查看类型或动态创建类 |
| `vars()` | 获取对象属性字典 |
| `zip()` | 并行组合多个可迭代对象 |
| `__import__()` | 底层导入模块 |

---

# 总结

Python 内置函数可以大致分为：

1. 输入输出：`print()`、`input()`、`open()`
2. 数值计算：`abs()`、`sum()`、`max()`、`min()`、`round()`
3. 类型转换：`int()`、`float()`、`str()`、`list()`、`dict()`
4. 序列迭代：`len()`、`range()`、`enumerate()`、`zip()`、`sorted()`
5. 类型判断：`type()`、`isinstance()`、`issubclass()`
6. 属性操作：`getattr()`、`setattr()`、`hasattr()`、`delattr()`
7. 面向对象：`classmethod()`、`staticmethod()`、`property()`、`super()`
8. 高级功能：`eval()`、`exec()`、`compile()`、`memoryview()`

学习时不需要一次性背完。更重要的是：

- 知道函数属于哪一类
- 知道函数解决什么问题
- 掌握最常见的参数
- 通过代码练习形成使用习惯
- 遇到陌生函数时使用 `help()` 查看说明
