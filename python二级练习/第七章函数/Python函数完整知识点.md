# Python 函数完整知识点

## 一、函数是什么

函数是一段具有特定功能、可以重复调用的代码。

```python
def add(a, b):
    return a + b
```

调用：

```python
result = add(10, 20)
print(result)  # 30
```

从底层逻辑看，执行 `def` 时，Python 会：

1. 创建一个函数对象；
2. 将函数体暂时保存起来，而不是立刻执行；
3. 把函数对象绑定到函数名 `add`；
4. 遇到 `add(10, 20)` 时才执行函数体。

因此，函数名本质上也是一个变量，里面保存着函数对象的引用。

```python
def add(a, b):
    return a + b

print(add)
print(type(add))
```

结果类似：

```text
<function add at 0x...>
<class 'function'>
```

---

## 二、定义函数

### 1. 基本格式

```python
def 函数名(参数列表):
    函数体
    return 返回值
```

例如：

```python
def greet(name):
    message = f"你好，{name}"
    return message
```

### 2. 函数名命名规则

函数名必须符合标识符规则：

- 由字母、数字、下划线组成；
- 不能以数字开头；
- 不能使用关键字；
- 区分大小写。

推荐使用小写字母加下划线：

```python
def calculate_average():
    pass
```

类名通常才使用大驼峰命名法。

### 3. 空函数

暂时不写函数内容时，可以使用 `pass`：

```python
def test():
    pass
```

`pass` 什么都不做，只是为了保证语法完整。

### 4. 函数文档字符串

函数体第一条字符串可以作为函数说明：

```python
def add(a, b):
    """返回两个数的和。"""
    return a + b
```

查看文档：

```python
print(add.__doc__)
help(add)
```

多行文档字符串：

```python
def divide(a, b):
    """
    计算两个数的商。

    参数：
        a: 被除数
        b: 除数

    返回：
        a / b 的结果
    """
    return a / b
```

---

## 三、函数调用过程

```python
def add(a, b):
    result = a + b
    return result

x = add(3, 5)
```

调用过程可以理解为：

```text
1. 先计算实参 3 和 5
2. 创建本次函数调用的局部作用域
3. 让形参 a 指向对象 3
4. 让形参 b 指向对象 5
5. 执行 result = a + b
6. 执行 return result
7. 销毁普通局部作用域
8. 将返回对象交给调用位置
9. 让变量 x 指向返回对象
```

每调用一次函数，都会产生一次新的调用环境：

```python
def test(x):
    y = x + 1
    return y

a = test(10)
b = test(20)
```

两次调用中的 `x` 和 `y` 是互相独立的局部变量。

---

## 四、形参与实参

### 1. 形参

定义函数时括号中的变量称为形式参数，简称形参：

```python
def add(a, b):
    return a + b
```

其中 `a`、`b` 是形参。

### 2. 实参

调用函数时传入的具体数据称为实际参数，简称实参：

```python
add(10, 20)
```

其中 `10`、`20` 是实参。

---

## 五、Python 的参数传递本质

Python 的参数传递通常称为：

> 对象引用传递，或者共享传参。

调用函数时，不会把整个对象复制一份，而是让形参指向实参所指向的对象。

### 1. 不可变对象

```python
def change(x):
    x = 100

a = 10
change(a)
print(a)  # 10
```

过程：

```text
调用前：
a ──→ 10

调用后：
a ──→ 10
x ──→ 10

执行 x = 100 后：
a ──→ 10
x ──→ 100
```

`x = 100` 只是让局部变量 `x` 改为指向新对象，没有修改 `a`。

### 2. 可变对象

```python
def change(lst):
    lst.append(100)

a = [1, 2, 3]
change(a)
print(a)
```

结果：

```python
[1, 2, 3, 100]
```

因为 `a` 和 `lst` 指向同一个列表对象：

```text
a   ─┐
     ├──→ [1, 2, 3]
lst ─┘
```

执行 `lst.append(100)` 修改的是共同指向的列表。

### 3. 重新赋值和修改对象的区别

修改对象：

```python
def change(lst):
    lst.append(4)
```

会影响外部列表。

重新赋值：

```python
def change(lst):
    lst = [100, 200]
```

不会影响外部变量：

```python
a = [1, 2, 3]
change(a)
print(a)  # [1, 2, 3]
```

---

## 六、位置参数

按照参数位置进行传递：

```python
def introduce(name, age):
    print(name, age)

introduce("小明", 20)
```

对应关系：

```text
name ← "小明"
age  ← 20
```

位置不能随意颠倒：

```python
introduce(20, "小明")
```

虽然语法可能不报错，但含义错误。

---

## 七、关键字参数

调用时明确指定参数名：

```python
def introduce(name, age):
    print(name, age)

introduce(name="小明", age=20)
```

可以改变顺序：

```python
introduce(age=20, name="小明")
```

### 位置参数与关键字参数混合

```python
introduce("小明", age=20)
```

位置参数必须写在普通关键字参数前面：

```python
introduce(name="小明", 20)
```

这是语法错误。

同一个参数不能被重复赋值：

```python
introduce("小明", name="小红")
```

会报错：

```text
TypeError: got multiple values for argument 'name'
```

---

## 八、默认参数

定义函数时为参数指定默认值：

```python
def greet(name, message="你好"):
    print(message, name)
```

调用：

```python
greet("小明")           # 你好 小明
greet("小明", "欢迎")   # 欢迎 小明
```

### 1. 默认参数必须放在非默认参数后面

正确：

```python
def test(a, b=10):
    pass
```

错误：

```python
def test(a=10, b):
    pass
```

### 2. 默认值只在定义函数时计算一次

这是一个重要规则：

```python
def add_item(item, items=[]):
    items.append(item)
    return items
```

调用：

```python
print(add_item(1))  # [1]
print(add_item(2))  # [1, 2]
print(add_item(3))  # [1, 2, 3]
```

原因是默认列表只创建一次，之后每次调用都使用同一个列表。

```text
默认参数 items ──→ 同一个列表对象
```

### 3. 正确处理可变默认参数

使用 `None`：

```python
def add_item(item, items=None):
    if items is None:
        items = []

    items.append(item)
    return items
```

调用：

```python
print(add_item(1))  # [1]
print(add_item(2))  # [2]
```

通常不要将以下可变对象作为默认值：

```python
[]
{}
set()
```

不可变默认值一般没有问题：

```python
def test(a=0, name="", flag=False, data=None):
    pass
```

---

## 九、可变位置参数 `*args`

当位置参数数量不确定时，可以使用 `*args`：

```python
def add_all(*args):
    print(args)
    return sum(args)
```

调用：

```python
print(add_all(1, 2, 3, 4))
```

函数内部：

```python
args == (1, 2, 3, 4)
```

也就是说，`args` 是一个元组。

参数名不一定必须叫 `args`：

```python
def test(*numbers):
    print(numbers)
```

但一般遵循约定写成 `args`。

### 普通参数和 `*args`

```python
def test(a, b, *args):
    print(a)
    print(b)
    print(args)

test(1, 2, 3, 4, 5)
```

结果：

```text
a = 1
b = 2
args = (3, 4, 5)
```

---

## 十、可变关键字参数 `**kwargs`

当关键字参数数量不确定时，使用 `**kwargs`：

```python
def show_info(**kwargs):
    print(kwargs)

show_info(name="小明", age=20, city="杭州")
```

结果：

```python
{
    "name": "小明",
    "age": 20,
    "city": "杭州"
}
```

函数内部的 `kwargs` 是字典。

参数名不一定必须叫 `kwargs`，但一般遵循这一约定。

### 普通参数与 `**kwargs`

```python
def test(name, **kwargs):
    print(name)
    print(kwargs)

test("小明", age=20, city="杭州")
```

结果：

```text
小明
{'age': 20, 'city': '杭州'}
```

---

## 十一、完整参数顺序

函数参数的标准顺序是：

```python
def function(
    位置专用参数,
    /,
    普通参数,
    *可变位置参数,
    仅限关键字参数,
    **可变关键字参数
):
    pass
```

常见形式：

```python
def test(a, b=10, *args, c, d=20, **kwargs):
    pass
```

其中：

- `a`：普通必需参数；
- `b`：普通默认参数；
- `args`：额外位置参数；
- `c`：仅限关键字参数；
- `d`：带默认值的仅限关键字参数；
- `kwargs`：额外关键字参数。

调用：

```python
test(
    1,
    2,
    3,
    4,
    c=5,
    d=6,
    name="小明"
)
```

对应：

```text
a = 1
b = 2
args = (3, 4)
c = 5
d = 6
kwargs = {'name': '小明'}
```

---

## 十二、仅限关键字参数

写在 `*` 或 `*args` 后面的参数，只能通过关键字传递。

```python
def connect(host, *, timeout=10, retry=3):
    print(host, timeout, retry)
```

正确：

```python
connect("localhost", timeout=5, retry=2)
```

错误：

```python
connect("localhost", 5, 2)
```

这样设计可以增强函数调用的可读性：

```python
connect("localhost", timeout=5)
```

比下面更容易理解：

```python
connect("localhost", 5)
```

---

## 十三、位置专用参数

`/` 前面的参数只能按照位置传递，不能使用参数名。

```python
def divide(a, b, /):
    return a / b
```

正确：

```python
divide(10, 2)
```

错误：

```python
divide(a=10, b=2)
```

综合示例：

```python
def test(a, b, /, c, *, d):
    print(a, b, c, d)
```

调用：

```python
test(1, 2, 3, d=4)
test(1, 2, c=3, d=4)
```

规则：

- `a`、`b`：只能按位置传递；
- `c`：可以按位置，也可以按关键字；
- `d`：只能按关键字传递。

---

## 十四、参数解包

### 1. 使用 `*` 解包序列

```python
def add(a, b, c):
    return a + b + c

numbers = [1, 2, 3]

print(add(*numbers))
```

等价于：

```python
print(add(1, 2, 3))
```

可以解包：

- 列表；
- 元组；
- 字符串；
- `range`；
- 其他可迭代对象。

```python
args = (10, 20)
print(pow(*args))
```

### 2. 使用 `**` 解包字典

```python
def introduce(name, age):
    print(name, age)

info = {
    "name": "小明",
    "age": 20
}

introduce(**info)
```

等价于：

```python
introduce(name="小明", age=20)
```

用于参数解包时，字典的键必须是字符串，而且必须能够对应参数名。

### 3. 同时解包

```python
def test(a, b, c=0, d=0):
    print(a, b, c, d)

args = [1, 2]
kwargs = {"c": 3, "d": 4}

test(*args, **kwargs)
```

---

## 十五、`return` 返回值

### 1. 返回一个值

```python
def square(x):
    return x * x
```

### 2. 没有写 `return`

```python
def test():
    print("执行函数")
```

调用：

```python
result = test()
print(result)
```

结果：

```text
执行函数
None
```

函数没有明确返回值时，默认返回 `None`。

### 3. `return` 后不写内容

```python
def test():
    return
```

等价于：

```python
def test():
    return None
```

### 4. 返回多个值

```python
def calculate(a, b):
    return a + b, a - b, a * b
```

接收：

```python
result = calculate(10, 2)
print(result)
```

结果：

```python
(12, 8, 20)
```

所谓“返回多个值”，本质上是返回一个元组。

可以使用序列解包：

```python
total, difference, product = calculate(10, 2)
```

### 5. `return` 会立即结束当前函数

```python
def test():
    print("开始")
    return 100
    print("结束")
```

`return` 后面的 `print("结束")` 永远不会执行。

### 6. 分支返回

```python
def absolute(x):
    if x >= 0:
        return x
    else:
        return -x
```

可以简化：

```python
def absolute(x):
    if x >= 0:
        return x

    return -x
```

### 7. 返回值不是复制对象

```python
def create_list():
    data = [1, 2, 3]
    return data

a = create_list()
```

`return data` 返回的是列表对象的引用，不是自动深拷贝。

---

## 十六、局部变量和全局变量

### 1. 局部变量

在函数内部定义的变量通常是局部变量：

```python
def test():
    x = 10
    print(x)
```

函数外不能直接访问：

```python
test()
print(x)
```

会出现：

```text
NameError
```

### 2. 全局变量

在函数外定义的变量通常属于模块全局作用域：

```python
x = 10

def test():
    print(x)

test()
```

函数内部可以读取全局变量。

### 3. 局部变量遮蔽全局变量

```python
x = 10

def test():
    x = 20
    print(x)

test()
print(x)
```

结果：

```text
20
10
```

函数内部的 `x` 是新的局部变量，不会修改全局 `x`。

---

## 十七、LEGB 作用域规则

Python 查找变量时，遵循 LEGB 顺序：

```text
L：Local，当前函数局部作用域
E：Enclosing，外层嵌套函数作用域
G：Global，当前模块全局作用域
B：Built-in，内置作用域
```

示例：

```python
x = "全局变量"

def outer():
    x = "外层变量"

    def inner():
        x = "局部变量"
        print(x)

    inner()

outer()
```

输出：

```text
局部变量
```

因为首先在 Local 中找到了 `x`。

如果删掉局部 `x`：

```python
x = "全局变量"

def outer():
    x = "外层变量"

    def inner():
        print(x)

    inner()

outer()
```

输出：

```text
外层变量
```

---

## 十八、`global`

在函数中需要重新绑定全局变量时，使用 `global`：

```python
count = 0

def increase():
    global count
    count += 1
```

调用：

```python
increase()
print(count)  # 1
```

### 为什么下面会报错

```python
count = 0

def increase():
    count += 1
```

因为只要一个函数中存在：

```python
count = ...
```

或者：

```python
count += ...
```

Python 就会把 `count` 判定为局部变量。

`count += 1` 类似于：

```python
count = count + 1
```

但在计算右边的 `count + 1` 时，局部变量还没有值，因此出现：

```text
UnboundLocalError
```

### 修改全局可变对象不一定需要 `global`

```python
data = []

def add_item():
    data.append(1)
```

这里没有让 `data` 重新指向其他对象，只是修改列表内容，因此不需要 `global`。

但下面需要：

```python
data = []

def reset():
    global data
    data = []
```

---

## 十九、`nonlocal`

`nonlocal` 用于修改外层嵌套函数中的变量：

```python
def outer():
    count = 0

    def inner():
        nonlocal count
        count += 1
        return count

    return inner
```

使用：

```python
counter = outer()

print(counter())  # 1
print(counter())  # 2
print(counter())  # 3
```

`nonlocal` 查找的是最近的外层函数作用域，不包括全局作用域。

---

## 二十、嵌套函数

函数内部可以定义另一个函数：

```python
def outer():
    print("outer 开始")

    def inner():
        print("inner 执行")

    inner()
```

调用：

```python
outer()
```

外部通常不能直接访问 `inner`：

```python
inner()
```

会出现 `NameError`。

---

## 二十一、闭包

当内部函数使用了外部函数的局部变量，而且内部函数被返回到外部时，就形成闭包。

```python
def make_multiplier(n):
    def multiply(x):
        return x * n

    return multiply
```

调用：

```python
double = make_multiplier(2)
triple = make_multiplier(3)

print(double(10))  # 20
print(triple(10))  # 30
```

虽然 `make_multiplier()` 已经执行结束，但是变量 `n` 仍然被内部函数保存。

```text
double ──→ multiply 函数对象
              │
              └── 保存外层变量 n = 2
```

闭包常用于：

- 保存状态；
- 函数工厂；
- 装饰器；
- 回调函数。

---

## 二十二、闭包的延迟绑定问题

```python
functions = []

for i in range(3):
    functions.append(lambda: i)

for function in functions:
    print(function())
```

结果：

```text
2
2
2
```

原因是 `lambda` 使用的是变量 `i`，而不是定义时立刻保存 `i` 的值。等真正调用时，循环已经结束，`i == 2`。

解决方法：

```python
functions = []

for i in range(3):
    functions.append(lambda i=i: i)
```

结果：

```text
0
1
2
```

这里利用了“默认参数在函数定义时计算”的规则。

---

## 二十三、匿名函数 `lambda`

### 1. 基本格式

```python
lambda 参数: 表达式
```

例如：

```python
square = lambda x: x * x

print(square(5))  # 25
```

基本等价于：

```python
def square(x):
    return x * x
```

### 2. 多个参数

```python
add = lambda a, b: a + b
```

### 3. 无参数

```python
get_message = lambda: "你好"
```

### 4. 条件表达式

```python
maximum = lambda a, b: a if a > b else b
```

### 5. 常与排序结合

```python
students = [
    ("小明", 80),
    ("小红", 95),
    ("小刚", 70)
]

students.sort(key=lambda item: item[1])
```

按照成绩排序。

### 6. `lambda` 的限制

`lambda` 函数体只能是一个表达式，不能直接写普通语句。

复杂逻辑应使用 `def`。

---

## 二十四、函数也是对象

Python 中函数属于“一等对象”，意味着函数可以像普通数据一样使用。

### 1. 赋值给变量

```python
def add(a, b):
    return a + b

operation = add

print(operation(1, 2))
```

注意：

```python
operation = add
```

保存的是函数对象。

而：

```python
operation = add(1, 2)
```

保存的是函数调用结果。

### 2. 放入容器

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

operations = [add, subtract]

print(operations[0](10, 3))
print(operations[1](10, 3))
```

### 3. 作为参数传递

```python
def calculate(operation, a, b):
    return operation(a, b)

def add(a, b):
    return a + b

print(calculate(add, 10, 20))
```

接收其他函数作为参数的函数称为高阶函数。

### 4. 作为返回值

```python
def select_operation(symbol):
    if symbol == "+":
        return lambda a, b: a + b

    if symbol == "-":
        return lambda a, b: a - b
```

使用：

```python
operation = select_operation("+")
print(operation(10, 5))
```

---

## 二十五、高阶函数

高阶函数满足至少一个条件：

- 接收函数作为参数；
- 返回一个函数。

常见高阶函数包括：

- `sorted()`；
- `map()`；
- `filter()`；
- `functools.reduce()`；
- 装饰器函数。

### 1. `sorted()` 的 `key`

```python
words = ["apple", "cat", "banana"]

result = sorted(words, key=len)
print(result)
```

结果：

```python
['cat', 'apple', 'banana']
```

`sorted()` 会把每一个元素传给 `len()`，然后按照返回结果排序。

### 2. `map()`

对每个元素执行函数：

```python
numbers = [1, 2, 3, 4]

result = map(lambda x: x * x, numbers)

print(list(result))
```

结果：

```python
[1, 4, 9, 16]
```

通常列表推导式更直观：

```python
result = [x * x for x in numbers]
```

### 3. `filter()`

保留使函数返回真值的元素：

```python
numbers = [1, 2, 3, 4, 5]

result = filter(lambda x: x % 2 == 0, numbers)

print(list(result))
```

结果：

```python
[2, 4]
```

列表推导式：

```python
result = [x for x in numbers if x % 2 == 0]
```

### 4. `reduce()`

```python
from functools import reduce

numbers = [1, 2, 3, 4]

result = reduce(lambda a, b: a * b, numbers)

print(result)  # 24
```

计算过程：

```text
1 × 2 = 2
2 × 3 = 6
6 × 4 = 24
```

---

## 二十六、递归函数

函数直接或间接调用自己，称为递归。

```python
def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n - 1)
```

调用：

```python
print(factorial(5))
```

展开过程：

```text
factorial(5)
= 5 × factorial(4)
= 5 × 4 × factorial(3)
= 5 × 4 × 3 × factorial(2)
= 5 × 4 × 3 × 2 × factorial(1)
= 5 × 4 × 3 × 2 × 1 × factorial(0)
= 120
```

### 递归必须有终止条件

```python
if n == 0:
    return 1
```

否则会无限递归，最终出现：

```text
RecursionError
```

### 递归的两个必要部分

递归终止条件：

```python
if n == 0:
    return 1
```

向终止条件靠近：

```python
factorial(n - 1)
```

### Python 不进行尾递归优化

即使递归调用写在最后，Python 仍会保存每一层调用栈。

因此，深层递归可能超过最大递归深度。普通循环通常更节省空间。

---

## 二十七、装饰器

装饰器是在不直接修改原函数代码的情况下，为函数增加功能。

### 1. 基础形式

```python
def decorator(function):
    def wrapper():
        print("函数执行前")
        function()
        print("函数执行后")

    return wrapper
```

使用：

```python
@decorator
def greet():
    print("你好")
```

调用：

```python
greet()
```

结果：

```text
函数执行前
你好
函数执行后
```

### 2. `@decorator` 的本质

```python
@decorator
def greet():
    print("你好")
```

等价于：

```python
def greet():
    print("你好")

greet = decorator(greet)
```

原来的 `greet` 函数被传给装饰器，装饰器返回的新函数重新绑定给 `greet`。

### 3. 通用装饰器

```python
from functools import wraps

def decorator(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print("调用前")

        result = function(*args, **kwargs)

        print("调用后")
        return result

    return wrapper
```

这样可以装饰不同参数形式的函数。

### 4. 为什么使用 `functools.wraps`

如果不使用：

```python
print(greet.__name__)
```

可能得到：

```text
wrapper
```

使用 `@wraps(function)` 后，可以保留原函数的：

- `__name__`；
- `__doc__`；
- 注解；
- 其他元数据。

### 5. 带参数的装饰器

```python
from functools import wraps

def repeat(times):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            result = None

            for _ in range(times):
                result = function(*args, **kwargs)

            return result

        return wrapper

    return decorator
```

使用：

```python
@repeat(3)
def greet():
    print("你好")
```

本质上相当于：

```python
greet = repeat(3)(greet)
```

### 6. 多个装饰器

```python
@decorator_a
@decorator_b
def test():
    pass
```

等价于：

```python
test = decorator_a(decorator_b(test))
```

装饰时从下往上包裹，调用时通常从外往内进入。

---

## 二十八、生成器函数

函数体中出现 `yield`，它就是生成器函数。

```python
def count_up_to(n):
    number = 1

    while number <= n:
        yield number
        number += 1
```

调用：

```python
result = count_up_to(3)
print(result)
```

返回的不是普通结果，而是生成器对象。

遍历：

```python
for number in count_up_to(3):
    print(number)
```

### `yield` 和 `return` 的区别

`return`：

- 返回一个结果；
- 立即结束函数；
- 下次调用从头开始。

`yield`：

- 暂时返回一个结果；
- 保存当前执行状态；
- 下次继续从暂停位置向后执行。

### 手动执行生成器

```python
generator = count_up_to(3)

print(next(generator))  # 1
print(next(generator))  # 2
print(next(generator))  # 3
```

再次调用：

```python
next(generator)
```

会出现：

```text
StopIteration
```

### `yield from`

把另一个可迭代对象中的元素逐个产出：

```python
def generator():
    yield from [1, 2, 3]
```

基本等价于：

```python
def generator():
    for item in [1, 2, 3]:
        yield item
```

---

## 二十九、函数类型注解

类型注解用于说明参数和返回值的预期类型：

```python
def add(a: int, b: int) -> int:
    return a + b
```

也可以使用复杂类型：

```python
def average(numbers: list[float]) -> float:
    return sum(numbers) / len(numbers)
```

### 类型注解默认不会强制检查

```python
def add(a: int, b: int) -> int:
    return a + b

print(add("a", "b"))
```

结果仍然可能是：

```text
ab
```

类型注解主要用于：

- 提高代码可读性；
- IDE 提示；
- 静态类型检查；
- 项目维护；
- 自动生成文档。

可以使用 `mypy`、Pyright 等工具进行静态检查。

### 查看注解

```python
print(add.__annotations__)
```

结果类似：

```python
{
    'a': int,
    'b': int,
    'return': int
}
```

---

## 三十、函数对象的重要属性

```python
def add(a, b):
    """计算两个数的和。"""
    return a + b
```

常见属性：

```python
print(add.__name__)
print(add.__doc__)
print(add.__annotations__)
print(add.__module__)
```

还可以动态添加属性：

```python
add.description = "这是加法函数"

print(add.description)
```

---

## 三十一、方法与普通函数的区别

### 普通函数

```python
def add(a, b):
    return a + b
```

调用：

```python
add(1, 2)
```

### 方法

方法是定义在类中的函数：

```python
class Calculator:
    def add(self, a, b):
        return a + b
```

调用：

```python
calculator = Calculator()
calculator.add(1, 2)
```

这里：

```python
calculator.add(1, 2)
```

可以近似理解为：

```python
Calculator.add(calculator, 1, 2)
```

对象 `calculator` 会自动作为第一个参数 `self` 传入。

---

## 三十二、回调函数

把一个函数交给另一个程序，在特定时机调用，称为回调。

```python
def on_success(data):
    print("处理成功：", data)

def process(callback):
    result = "数据"
    callback(result)

process(on_success)
```

常见于：

- 图形界面按钮事件；
- 网络请求；
- 定时任务；
- 异步程序；
- 数据处理流程。

---

## 三十三、异步函数

使用 `async def` 定义协程函数：

```python
import asyncio

async def download():
    print("开始下载")
    await asyncio.sleep(1)
    print("下载完成")
```

调用异步函数：

```python
coroutine = download()
```

此时通常不会立即完整执行函数体，而是得到协程对象。

运行：

```python
asyncio.run(download())
```

### `await`

`await` 用于等待一个可等待对象：

```python
async def main():
    await download()
```

`await` 通常只能写在 `async def` 中。

异步适合：

- 网络请求；
- 文件或数据库等待；
- 大量并发 I/O；
- 服务端程序。

异步不等于自动使用多核 CPU。

---

## 三十四、可调用对象

能够使用括号调用的对象称为可调用对象。

普通函数是可调用对象：

```python
callable(print)  # True
```

类也是可调用对象：

```python
callable(list)  # True
```

实现 `__call__` 的实例也可以调用：

```python
class Counter:
    def __init__(self):
        self.count = 0

    def __call__(self):
        self.count += 1
        return self.count
```

使用：

```python
counter = Counter()

print(counter())  # 1
print(counter())  # 2
```

判断对象是否可调用：

```python
callable(obj)
```

---

## 三十五、函数重载问题

Python 不支持根据参数个数或参数类型自动选择同名函数。

```python
def test(a):
    print("一个参数")

def test(a, b):
    print("两个参数")
```

第二次定义会覆盖第一次定义：

```python
test(1)
```

会报错，因为当前只剩下：

```python
def test(a, b):
    ...
```

### Python 常见替代方案

默认参数：

```python
def test(a, b=None):
    if b is None:
        print("一个参数")
    else:
        print("两个参数")
```

`*args`：

```python
def test(*args):
    if len(args) == 1:
        print("一个参数")
    elif len(args) == 2:
        print("两个参数")
```

`singledispatch`：

```python
from functools import singledispatch

@singledispatch
def show(value):
    print("其他类型")

@show.register
def _(value: int):
    print("整数")

@show.register
def _(value: str):
    print("字符串")
```

---

## 三十六、函数中的异常

函数可以主动抛出异常：

```python
def divide(a, b):
    if b == 0:
        raise ValueError("除数不能为 0")

    return a / b
```

调用时处理：

```python
try:
    result = divide(10, 0)
except ValueError as error:
    print(error)
```

与其返回特殊数字表示错误，很多情况下抛出异常更明确。

---

## 三十七、`return` 与 `finally`

无论是否执行 `return`，`finally` 通常都会执行：

```python
def test():
    try:
        return 10
    finally:
        print("finally 执行")
```

结果：

```text
finally 执行
10
```

不要轻易在 `finally` 中写 `return`：

```python
def test():
    try:
        return 10
    finally:
        return 20
```

最终返回：

```python
20
```

`finally` 中的 `return` 会覆盖前面的返回值，甚至可能压制异常。

---

## 三十八、函数参数的计算顺序

调用函数前，实参表达式会先被计算。

```python
def show(a, b):
    print(a, b)

def first():
    print("first")
    return 1

def second():
    print("second")
    return 2

show(first(), second())
```

通常按照从左到右计算：

```text
first
second
1 2
```

然后才进入 `show()` 函数体。

---

## 三十九、函数定义执行时机

`def` 本身也是一条可执行语句。

```python
condition = True

if condition:
    def test():
        print("条件为真")
else:
    def test():
        print("条件为假")

test()
```

甚至可以在循环中定义函数，但一般不建议无必要地这样做。

函数默认值、装饰器表达式等，也会在执行到 `def` 时处理。

---

## 四十、函数名可以重新绑定

```python
def greet():
    print("你好")

greet()
```

重新赋值：

```python
greet = 100
```

此时：

```python
greet()
```

会报错：

```text
TypeError: 'int' object is not callable
```

因为函数对象没有被修改，只是名字 `greet` 改为指向整数对象。

所以不要使用内置函数名作为变量名：

```python
list = [1, 2, 3]
str = "hello"
sum = 100
```

否则会遮蔽内置函数：

```python
list("abc")
```

可能出现：

```text
TypeError: 'list' object is not callable
```

---

## 四十一、常见错误总结

### 1. 调用函数时忘记括号

```python
print
```

表示函数对象。

```python
print()
```

才表示调用函数。

### 2. 把返回值和打印混淆

```python
def add(a, b):
    print(a + b)
```

这个函数只是打印，没有返回计算结果：

```python
result = add(1, 2)
print(result)  # None
```

需要返回时应写：

```python
def add(a, b):
    return a + b
```

### 3. 使用可变默认参数

错误：

```python
def add_item(item, items=[]):
    items.append(item)
    return items
```

推荐：

```python
def add_item(item, items=None):
    if items is None:
        items = []

    items.append(item)
    return items
```

### 4. 局部变量引用前未赋值

```python
x = 10

def test():
    print(x)
    x = 20
```

会出现 `UnboundLocalError`。

因为函数中出现了 `x = 20`，Python 将整个函数中的 `x` 认定为局部变量。

### 5. 参数数量不匹配

```python
def add(a, b):
    return a + b

add(1)
```

参数过少。

```python
add(1, 2, 3)
```

参数过多。

### 6. 重复传递同一个参数

```python
def test(a, b):
    pass

test(1, a=2, b=3)
```

`a` 同时通过位置参数和关键字参数赋值。

### 7. 误认为重新赋值能修改外部变量

```python
def change(x):
    x = 100
```

这只是修改局部变量 `x` 的指向。

### 8. 递归没有终止条件

```python
def test():
    return test()
```

会无限递归，直到出现 `RecursionError`。

### 9. 把函数调用结果当函数

```python
def test():
    return 10

x = test()
x()
```

此时 `x` 是整数 `10`，不是函数。

---

## 四十二、函数设计原则

### 1. 一个函数尽量只完成一个明确任务

不推荐：

```python
def process():
    # 读取文件
    # 清洗数据
    # 计算结果
    # 画图
    # 保存文件
    pass
```

推荐拆分：

```python
def read_data():
    pass

def clean_data(data):
    pass

def calculate(data):
    pass

def draw_chart(result):
    pass

def save_result(result):
    pass
```

### 2. 参数和返回值应明确

推荐：

```python
def calculate_average(numbers):
    return sum(numbers) / len(numbers)
```

而不是大量依赖全局变量。

### 3. 函数名尽量使用动词

```python
read_file()
calculate_total()
validate_password()
save_result()
```

布尔函数可以使用：

```python
is_valid()
has_permission()
can_execute()
```

### 4. 尽量减少隐藏副作用

下面的函数不仅计算，还修改输入列表：

```python
def process(data):
    data.sort()
    return data
```

调用者可能不知道原列表被修改。

可以改为：

```python
def process(data):
    return sorted(data)
```

### 5. 参数过多时考虑重构

```python
def create_user(
    name,
    age,
    city,
    phone,
    email,
    address,
    school,
    major
):
    pass
```

参数过多时，可以考虑：

- 字典；
- 数据类；
- 配置对象；
- 拆分函数。

---

## 四十三、函数知识体系总图

```text
Python 函数
│
├─ 定义
│  ├─ def
│  ├─ 函数名
│  ├─ 函数体
│  └─ 文档字符串
│
├─ 调用
│  ├─ 函数对象
│  ├─ 函数名()
│  ├─ 调用栈
│  └─ 对象引用传递
│
├─ 参数
│  ├─ 位置参数
│  ├─ 关键字参数
│  ├─ 默认参数
│  ├─ *args
│  ├─ **kwargs
│  ├─ 仅限位置参数 /
│  ├─ 仅限关键字参数 *
│  └─ 参数解包
│
├─ 返回值
│  ├─ return
│  ├─ None
│  ├─ 返回多个值
│  └─ 立即结束函数
│
├─ 作用域
│  ├─ LEGB
│  ├─ 局部变量
│  ├─ 全局变量
│  ├─ global
│  └─ nonlocal
│
├─ 函数特性
│  ├─ 函数是一等对象
│  ├─ 高阶函数
│  ├─ 嵌套函数
│  ├─ 闭包
│  ├─ lambda
│  ├─ 递归
│  └─ 回调函数
│
├─ 高级功能
│  ├─ 装饰器
│  ├─ 生成器函数
│  ├─ 异步函数
│  ├─ 类型注解
│  └─ 可调用对象
│
└─ 常见陷阱
   ├─ 可变默认参数
   ├─ UnboundLocalError
   ├─ 闭包延迟绑定
   ├─ 函数名被覆盖
   ├─ print 与 return 混淆
   └─ finally 中使用 return
```

---

## 四十四、最核心的底层理解

理解 Python 函数，只需要牢牢记住以下几点：

1. **函数名是变量，指向函数对象。**

   ```python
   def add(a, b):
       return a + b
   ```

   `add` 指向一个函数对象。

2. **执行 `def` 是创建函数，使用括号才是调用函数。**

   ```python
   add       # 函数对象
   add(1, 2) # 调用函数
   ```

3. **参数传递是让形参指向实参对象。**

   ```text
   实参变量 ─┐
             ├──→ 对象
   形参变量 ─┘
   ```

4. **重新赋值和修改对象不是一回事。**

   ```python
   x = new_object       # 改变变量指向
   x.append(value)      # 修改原对象
   ```

5. **每次调用函数，都会创建一个新的局部调用环境。**

6. **`return` 返回的是对象引用，并立即结束当前函数。**

7. **函数本身也是对象，所以能够赋值、传参、返回和存入容器。**

这七条是贯穿 Python 函数全部知识的主线。
