# Python 元组完整知识点整理

## 1. 元组是什么

元组（`tuple`）是 Python 中一种**有序、可重复、不可变**的序列类型。

```python
t = (10, 20, 30)
```

元组具有以下特点：

| 特点 | 说明 |
|---|---|
| 有序 | 每个元素都有固定索引 |
| 可重复 | 可以包含相同元素 |
| 可存放不同类型 | 可以同时存放整数、字符串、列表、字典等对象 |
| 不可变 | 创建后不能增加、删除或替换元素 |
| 支持嵌套 | 元组中可以包含元组、列表、字典等对象 |

示例：

```python
t = (10, "hello", 3.14, [1, 2], (3, 4))
```

---

## 2. 创建元组

### 2.1 使用小括号创建

```python
t = (10, 20, 30)
print(t)
```

输出：

```text
(10, 20, 30)
```

### 2.2 省略小括号创建

元组真正的标志通常是**逗号**，而不是小括号。

```python
t = 10, 20, 30

print(t)
print(type(t))
```

输出：

```text
(10, 20, 30)
<class 'tuple'>
```

因此：

```python
t = 10, 20
```

等价于：

```python
t = (10, 20)
```

### 2.3 创建空元组

```python
t = ()
```

也可以：

```python
t = tuple()
```

### 2.4 创建单元素元组

只有一个元素时，必须在元素后面加逗号。

```python
t = (10,)
```

如果不加逗号：

```python
t = (10)
```

此时 `t` 只是整数 `10`，不是元组。

```python
print(type((10)))    # int
print(type((10,)))   # tuple
```

单元素元组的标准写法：

```python
(元素,)
```

也可以省略小括号：

```python
t = 10,
```

### 2.5 使用 `tuple()` 创建元组

基本格式：

```python
tuple(可迭代对象)
```

#### 字符串转元组

```python
t = tuple("Python")
print(t)
```

输出：

```text
('P', 'y', 't', 'h', 'o', 'n')
```

#### 列表转元组

```python
t = tuple([10, 20, 30])
print(t)
```

输出：

```text
(10, 20, 30)
```

#### 集合转元组

```python
t = tuple({10, 20, 30})
```

集合本身无固定顺序，因此不应依赖转换后的元素顺序。

#### 字典转元组

```python
d = {"name": "Tom", "age": 18}
t = tuple(d)

print(t)
```

默认转换字典的键：

```text
('name', 'age')
```

转换字典的值：

```python
tuple(d.values())
```

转换字典的键值对：

```python
tuple(d.items())
```

结果：

```text
(('name', 'Tom'), ('age', 18))
```

---

## 3. 元组的索引

元组是有序序列，可以通过索引访问元素。

```python
t = ("A", "B", "C", "D")
```

### 3.1 正向索引

索引从 `0` 开始：

| 元素 | A | B | C | D |
|---|---:|---:|---:|---:|
| 正向索引 | 0 | 1 | 2 | 3 |

```python
print(t[0])    # A
print(t[2])    # C
```

### 3.2 反向索引

反向索引从 `-1` 开始：

| 元素 | A | B | C | D |
|---|---:|---:|---:|---:|
| 反向索引 | -4 | -3 | -2 | -1 |

```python
print(t[-1])   # D
print(t[-2])   # C
```

### 3.3 索引越界

```python
t = (10, 20, 30)
print(t[5])
```

报错：

```text
IndexError: tuple index out of range
```

---

## 4. 元组切片

元组支持切片。

基本格式：

```python
元组[start:stop:step]
```

规则：

- 包含 `start`
- 不包含 `stop`
- `step` 表示步长
- 切片结果仍然是元组

```python
t = (0, 1, 2, 3, 4, 5)
```

常见切片：

```python
print(t[1:4])    # (1, 2, 3)
print(t[:3])     # (0, 1, 2)
print(t[3:])     # (3, 4, 5)
print(t[::2])    # (0, 2, 4)
print(t[::-1])   # (5, 4, 3, 2, 1, 0)
```

---

## 5. 元组不可变

元组创建后，不能修改其中的元素。

```python
t = (10, 20, 30)
t[0] = 100
```

报错：

```text
TypeError: 'tuple' object does not support item assignment
```

元组不能直接进行以下操作：

```python
t[0] = 100       # 不能修改
del t[0]         # 不能删除单个元素
t.append(40)     # 没有 append()
t.insert(0, 5)   # 没有 insert()
t.remove(20)     # 没有 remove()
t.pop()          # 没有 pop()
```

### 5.1 删除整个元组变量

虽然不能删除元组中的单个元素，但可以删除整个变量。

```python
t = (10, 20, 30)
del t
```

之后再使用 `t`：

```python
print(t)
```

会报错：

```text
NameError: name 't' is not defined
```

这里删除的是变量名 `t`，不是修改元组内部元素。

---

## 6. 元组中的可变对象

“元组不可变”指的是：

> 元组中每个位置保存的对象引用不能被替换。

但如果元组中包含列表等可变对象，列表内部仍然可以修改。

```python
t = (10, [20, 30], 40)

t[1].append(50)

print(t)
```

输出：

```text
(10, [20, 30, 50], 40)
```

这是因为 `t[1]` 仍然指向原来的列表对象，只是该列表内部发生了变化。

下面的操作不允许：

```python
t[1] = [100, 200]
```

因为这相当于把元组中的第二个元素替换成另一个对象。

因此，元组的不可变性可以理解为：

> 元组自身是浅层不可变的。

---

## 7. 元组的基本运算

### 7.1 拼接：`+`

```python
t1 = (1, 2)
t2 = (3, 4)

t3 = t1 + t2

print(t3)
```

输出：

```text
(1, 2, 3, 4)
```

这不是修改原元组，而是创建了一个新元组。

### 7.2 重复：`*`

```python
t = (1, 2) * 3
print(t)
```

输出：

```text
(1, 2, 1, 2, 1, 2)
```

### 7.3 成员判断：`in`

```python
t = (10, 20, 30)

print(20 in t)
```

输出：

```text
True
```

### 7.4 非成员判断：`not in`

```python
print(100 not in t)
```

输出：

```text
True
```

---

## 8. 元组常用函数

### 8.1 `len()`：获取元素个数

```python
t = (10, 20, 30)
print(len(t))
```

输出：

```text
3
```

### 8.2 `max()`：获取最大值

```python
t = (10, 50, 20)
print(max(t))
```

输出：

```text
50
```

### 8.3 `min()`：获取最小值

```python
print(min(t))
```

输出：

```text
10
```

### 8.4 `sum()`：求和

```python
t = (10, 20, 30)
print(sum(t))
```

输出：

```text
60
```

元素必须是可以进行加法运算的数值。

### 8.5 `sorted()`：排序

```python
t = (30, 10, 20)

result = sorted(t)

print(result)
print(type(result))
```

输出：

```text
[10, 20, 30]
<class 'list'>
```

注意：

> `sorted()` 对元组排序后返回的是列表。

需要得到元组，可以再次转换：

```python
result = tuple(sorted(t))
```

### 8.6 `reversed()`：反向迭代

```python
t = (10, 20, 30)

result = reversed(t)

print(tuple(result))
```

输出：

```text
(30, 20, 10)
```

### 8.7 `enumerate()`：同时获取索引和元素

```python
t = ("A", "B", "C")

for index, value in enumerate(t):
    print(index, value)
```

输出：

```text
0 A
1 B
2 C
```

`enumerate()` 每次产生一个二元组：

```text
(索引, 元素)
```

---

## 9. 元组的方法

元组只有两个常用方法：

```python
count()
index()
```

因为元组不可变，所以没有增加、删除和修改相关方法。

### 9.1 `count()`：统计出现次数

格式：

```python
元组.count(元素)
```

示例：

```python
t = (10, 20, 10, 30, 10)

print(t.count(10))
```

输出：

```text
3
```

如果元素不存在，返回 `0`：

```python
print(t.count(100))    # 0
```

### 9.2 `index()`：查找第一次出现的位置

格式：

```python
元组.index(元素)
```

示例：

```python
t = (10, 20, 30, 20)

print(t.index(20))
```

输出：

```text
1
```

即使有多个 `20`，也只返回第一次出现的位置。

#### 指定查找范围

```python
元组.index(元素, start, stop)
```

示例：

```python
t = (10, 20, 30, 20, 40)

print(t.index(20, 2))
```

输出：

```text
3
```

也可以指定结束位置：

```python
t.index(20, 2, 5)
```

查找范围是：

```text
[2, 5)
```

#### 元素不存在

```python
t.index(100)
```

报错：

```text
ValueError: tuple.index(x): x not in tuple
```

安全查找：

```python
if 100 in t:
    print(t.index(100))
else:
    print("元素不存在")
```

---

## 10. 遍历元组

### 10.1 直接遍历元素

```python
t = ("A", "B", "C")

for value in t:
    print(value)
```

### 10.2 通过索引遍历

```python
t = ("A", "B", "C")

for i in range(len(t)):
    print(i, t[i])
```

### 10.3 使用 `enumerate()`

```python
for i, value in enumerate(t):
    print(i, value)
```

需要同时使用索引和元素时，推荐使用 `enumerate()`。

### 10.4 使用 `while`

```python
t = ("A", "B", "C")

i = 0

while i < len(t):
    print(t[i])
    i += 1
```

---

## 11. 元组打包

将多个值自动组合成一个元组，称为**元组打包**。

```python
t = 10, 20, 30

print(t)
```

输出：

```text
(10, 20, 30)
```

等价于：

```python
t = (10, 20, 30)
```

---

## 12. 元组解包

把元组中的元素分别赋值给多个变量，称为**元组解包**。

```python
t = (10, 20, 30)

a, b, c = t

print(a)
print(b)
print(c)
```

输出：

```text
10
20
30
```

要求：

> 左侧变量数量必须与右侧元素数量一致。

错误示例：

```python
a, b = (10, 20, 30)
```

报错：

```text
ValueError: too many values to unpack
```

```python
a, b, c = (10, 20)
```

报错：

```text
ValueError: not enough values to unpack
```

---

## 13. 扩展解包

使用 `*` 可以接收剩余元素。

### 13.1 星号变量在后面

```python
a, *b = (10, 20, 30, 40)

print(a)
print(b)
```

输出：

```text
10
[20, 30, 40]
```

注意：

> 星号变量接收到的是列表，不是元组。

### 13.2 星号变量在前面

```python
*a, b = (10, 20, 30, 40)

print(a)
print(b)
```

输出：

```text
[10, 20, 30]
40
```

### 13.3 星号变量在中间

```python
a, *b, c = (10, 20, 30, 40, 50)

print(a)
print(b)
print(c)
```

输出：

```text
10
[20, 30, 40]
50
```

### 13.4 星号变量可以接收空列表

```python
a, *b, c = (10, 20)

print(a)
print(b)
print(c)
```

输出：

```text
10
[]
20
```

### 13.5 同一级只能有一个星号变量

错误写法：

```python
*a, *b = (1, 2, 3)
```

会报语法错误。

---

## 14. 利用解包交换变量

Python 可以直接交换两个变量的值：

```python
a = 10
b = 20

a, b = b, a

print(a, b)
```

输出：

```text
20 10
```

原理可以理解为：

1. 右侧先打包为元组 `(b, a)`；
2. 左侧再进行解包；
3. 因此不会发生数据覆盖。

---

## 15. 函数返回多个值

函数返回多个值时，本质上通常是返回一个元组。

```python
def calculate(a, b):
    return a + b, a - b

result = calculate(10, 3)

print(result)
print(type(result))
```

输出：

```text
(13, 7)
<class 'tuple'>
```

可以直接解包：

```python
add_result, sub_result = calculate(10, 3)

print(add_result)
print(sub_result)
```

---

## 16. 函数中的 `*args`

函数定义中的 `*args` 会把多余的位置参数收集成一个元组。

```python
def test(*args):
    print(args)
    print(type(args))

test(10, 20, 30)
```

输出：

```text
(10, 20, 30)
<class 'tuple'>
```

名称不一定必须是 `args`：

```python
def test(*numbers):
    print(numbers)
```

关键是前面的 `*`。

---

## 17. 元组嵌套

元组中可以包含其他元组。

```python
t = ((1, 2), (3, 4), (5, 6))
```

访问外层元素：

```python
print(t[1])
```

输出：

```text
(3, 4)
```

访问内层元素：

```python
print(t[1][0])
```

输出：

```text
3
```

访问过程：

```text
t[1]     → (3, 4)
t[1][0]  → 3
```

### 17.1 嵌套解包

```python
t = (10, (20, 30))

a, (b, c) = t

print(a, b, c)
```

输出：

```text
10 20 30
```

左右结构必须对应。

---

## 18. 元组与列表相互转换

### 18.1 列表转元组

```python
lst = [10, 20, 30]

t = tuple(lst)

print(t)
```

输出：

```text
(10, 20, 30)
```

### 18.2 元组转列表

```python
t = (10, 20, 30)

lst = list(t)

print(lst)
```

输出：

```text
[10, 20, 30]
```

### 18.3 间接修改元组

元组本身不能修改，但可以先转换为列表，修改后再转回元组。

```python
t = (10, 20, 30)

lst = list(t)
lst[1] = 200
t = tuple(lst)

print(t)
```

输出：

```text
(10, 200, 30)
```

这里不是修改原元组，而是创建了一个新元组，并让变量 `t` 指向它。

---

## 19. 元组比较运算

元组支持以下比较运算符：

```python
==
!=
<
<=
>
>=
```

### 19.1 判断是否相等

```python
print((1, 2, 3) == (1, 2, 3))    # True
print((1, 2) == (2, 1))          # False
```

元素数量、顺序和值都必须相同。

### 19.2 大小比较

元组采用**字典序比较**，从左到右依次比较元素。

```python
print((1, 5) < (2, 0))
```

输出：

```text
True
```

因为第一个元素已经满足：

```text
1 < 2
```

所以不再继续比较。

再例如：

```python
print((1, 5) < (1, 8))
```

输出：

```text
True
```

第一个元素相同，继续比较第二个元素：

```text
5 < 8
```

### 19.3 公共部分完全相同

```python
print((1, 2) < (1, 2, 0))
```

输出：

```text
True
```

当公共部分完全相同时，较短的元组更小。

### 19.4 不同类型可能无法比较

```python
print((1, 2) < ("1", "2"))
```

在 Python 3 中会报错，因为整数和字符串不能直接比较大小。

但判断是否相等通常可以：

```python
print((1, 2) == ("1", "2"))    # False
```

---

## 20. 元组作为字典的键

字典的键必须是可哈希对象。普通元组通常可以作为字典的键。

```python
d = {
    (1, 2): "A",
    (3, 4): "B"
}

print(d[(1, 2)])
```

输出：

```text
A
```

常用于表示坐标：

```python
positions = {
    (0, 0): "起点",
    (1, 2): "目标点"
}
```

### 20.1 元组不一定都能作为字典键

只有当元组中的所有元素都可哈希时，元组才可哈希。

可以：

```python
t = (1, 2, "A")
d = {t: "value"}
```

不可以：

```python
t = (1, [2, 3])
d = {t: "value"}
```

报错：

```text
TypeError: unhashable type: 'list'
```

包含列表、字典、集合的元组通常不能作为：

- 字典的键
- 集合的元素

---

## 21. 元组作为集合元素

可哈希元组可以放入集合。

```python
s = {
    (1, 2),
    (3, 4)
}

print(s)
```

但包含列表的元组不能放入集合：

```python
s = {(1, [2, 3])}
```

会报错。

---

## 22. 元组与复制

### 22.1 直接赋值

```python
t1 = (10, 20, 30)
t2 = t1
```

此时 `t1` 和 `t2` 指向同一个元组对象。

```python
print(t1 is t2)    # True
```

因为元组不可变，所以共享同一个对象通常没有修改风险。

### 22.2 使用切片

```python
t2 = t1[:]
```

对于不可变元组，Python 可能直接返回原对象：

```python
print(t1 is t2)
```

结果可能为：

```text
True
```

因此不能简单认为元组切片一定产生一个不同地址的新对象。

### 22.3 元组中包含可变对象

```python
t1 = ([1, 2], 10)
t2 = t1

t2[0].append(3)

print(t1)
```

输出：

```text
([1, 2, 3], 10)
```

因为二者内部引用的是同一个列表对象。

---

## 23. `+=` 对元组的作用

```python
t = (1, 2)
t += (3, 4)

print(t)
```

输出：

```text
(1, 2, 3, 4)
```

虽然看起来像修改元组，但实际相当于：

```python
t = t + (3, 4)
```

过程是：

1. 创建一个新元组；
2. 让变量 `t` 指向新元组。

可以观察对象编号：

```python
t = (1, 2)
print(id(t))

t += (3, 4)
print(id(t))
```

两次 `id` 通常不同。

---

## 24. 元组乘法与可变对象陷阱

```python
lst = [0]
t = (lst,) * 3

print(t)
```

输出：

```text
([0], [0], [0])
```

这三个位置指向的是同一个列表对象。

```python
t[0].append(1)

print(t)
```

输出：

```text
([0, 1], [0, 1], [0, 1])
```

验证：

```python
print(t[0] is t[1])    # True
print(t[1] is t[2])    # True
```

元组乘法不会自动复制内部的可变对象，只会重复保存同一个对象的引用。

---

## 25. 生成器表达式与“元组推导式”

Python 没有真正的“元组推导式”。

下面的代码：

```python
result = (x * x for x in range(5))
```

得到的不是元组，而是生成器。

```python
print(type(result))
```

输出：

```text
<class 'generator'>
```

要得到元组，需要使用 `tuple()`：

```python
result = tuple(x * x for x in range(5))

print(result)
```

输出：

```text
(0, 1, 4, 9, 16)
```

对比：

```python
[x * x for x in range(5)]          # 列表推导式
{x * x for x in range(5)}          # 集合推导式
{x: x * x for x in range(5)}       # 字典推导式
(x * x for x in range(5))          # 生成器表达式
```

---

## 26. 小括号不一定表示元组

小括号在 Python 中还可以用于改变运算优先级。

```python
result = (1 + 2) * 3
```

这里的小括号不是元组。

判断是否为元组，关键看逗号：

```python
a = (10)     # 整数
b = (10,)    # 元组
```

```python
print(type((1 + 2)))     # int
print(type((1 + 2,)))    # tuple
```

---

## 27. 元组中的逗号

### 27.1 末尾逗号可以存在

```python
t = (1, 2, 3,)
```

等价于：

```python
t = (1, 2, 3)
```

### 27.2 单元素元组必须有逗号

```python
t = (1,)
```

这里的逗号不能省略。

### 27.3 `return` 多值本质上包含逗号

```python
def test():
    return 1, 2
```

可以理解为返回：

```python
(1, 2)
```

---

## 28. 元组与字符串格式化

旧式 `%` 格式化中，元组有特殊含义。

```python
name = "Tom"
age = 18

print("姓名：%s，年龄：%d" % (name, age))
```

右侧元组用于提供多个格式化数据。

如果想把一个元组作为单个数据传入 `%s`，需要额外包一层：

```python
t = (1, 2)

print("元组是：%s" % (t,))
```

这里 `(t,)` 是一个只有一个元素的元组，该元素本身又是元组 `t`。

现代 Python 更推荐使用 f-string：

```python
print(f"元组是：{t}")
```

---

## 29. 常见返回元组的操作

### 29.1 `divmod()`

同时返回商和余数：

```python
result = divmod(17, 5)

print(result)
```

输出：

```text
(3, 2)
```

可以直接解包：

```python
quotient, remainder = divmod(17, 5)
```

### 29.2 `enumerate()`

遍历时每次产生：

```text
(索引, 元素)
```

### 29.3 字典的 `items()`

```python
d = {"name": "Tom", "age": 18}

for item in d.items():
    print(item)
```

输出：

```text
('name', 'Tom')
('age', 18)
```

### 29.4 `zip()`

```python
names = ["Tom", "Jack"]
scores = [90, 80]

for item in zip(names, scores):
    print(item)
```

输出：

```text
('Tom', 90)
('Jack', 80)
```

---

## 30. 元组与列表的区别

| 对比项 | 元组 `tuple` | 列表 `list` |
|---|---|---|
| 符号 | `()` | `[]` |
| 是否有序 | 是 | 是 |
| 是否可重复 | 是 | 是 |
| 是否可修改 | 否 | 是 |
| 是否可增加元素 | 否 | 是 |
| 是否可删除元素 | 否 | 是 |
| 常用方法数量 | 少 | 多 |
| 能否作为字典键 | 满足可哈希条件时可以 | 不可以 |
| 适用场景 | 固定数据 | 经常变化的数据 |

### 30.1 适合使用元组的场景

```python
position = (100, 200)
rgb = (255, 0, 0)
date = (2026, 7, 17)
```

这些数据结构固定，一般不应随意改变。

### 30.2 适合使用列表的场景

```python
scores = [80, 90, 75]
students = ["Tom", "Jack"]
```

这些数据以后可能增加、删除或修改。

---

## 31. 元组的优点

### 31.1 防止数据被意外修改

```python
point = (10, 20)
```

坐标一旦确定，不希望随意修改，使用元组更合适。

### 31.2 可以作为字典键

```python
board = {
    (0, 0): "A",
    (0, 1): "B"
}
```

列表不能作为字典键。

### 31.3 通常比列表占用更少的内存

```python
import sys

lst = [1, 2, 3]
t = (1, 2, 3)

print(sys.getsizeof(lst))
print(sys.getsizeof(t))
```

具体数值会受到 Python 版本和运行环境影响。

### 31.4 某些情况下访问效率略高

由于元组结构固定，Python 可以进行一定优化。

不过日常编程中，应优先根据“数据是否需要修改”选择元组或列表，而不是过度追求这点性能差异。

---

## 32. 元组拼接的效率问题

元组不可变，因此每次拼接都要创建新元组。

```python
t = ()

for i in range(10000):
    t += (i,)
```

每次循环都需要：

1. 创建新元组；
2. 复制原来的元素；
3. 添加新元素。

数据较多时效率较低。

更好的方式：

```python
lst = []

for i in range(10000):
    lst.append(i)

t = tuple(lst)
```

需要频繁增加元素时，应先使用列表，最后再转换为元组。

---

## 33. 元组排序

元组本身没有 `sort()` 方法。

错误：

```python
t = (3, 1, 2)
t.sort()
```

报错：

```text
AttributeError: 'tuple' object has no attribute 'sort'
```

正确方式：

```python
t = (3, 1, 2)

result = tuple(sorted(t))

print(result)
```

输出：

```text
(1, 2, 3)
```

原元组不变：

```python
print(t)
```

输出：

```text
(3, 1, 2)
```

---

## 34. 元组去重

可以先转换为集合：

```python
t = (1, 2, 1, 3, 2)

result = tuple(set(t))

print(result)
```

但集合无固定顺序，因此结果顺序不一定与原元组一致。

需要保持原有顺序：

```python
t = (1, 2, 1, 3, 2)

result = tuple(dict.fromkeys(t))

print(result)
```

输出：

```text
(1, 2, 3)
```

---

## 35. 常见错误

### 错误 1：忘记单元素元组的逗号

```python
t = (10)
```

这不是元组，而是整数。

正确：

```python
t = (10,)
```

### 错误 2：尝试修改元组元素

```python
t = (10, 20, 30)
t[0] = 100
```

元组不可修改。

### 错误 3：使用列表的方法

```python
t.append(40)
t.remove(20)
t.pop()
t.sort()
```

元组没有这些方法。

### 错误 4：解包数量不一致

```python
a, b = (1, 2, 3)
```

变量数量与元素数量不匹配。

可以使用扩展解包：

```python
a, *b = (1, 2, 3)
```

### 错误 5：认为元组内部所有内容都绝对不可变

```python
t = ([1, 2], 3)
t[0].append(4)
```

这是允许的，因为修改的是元组内部的列表，而不是替换元组元素。

### 错误 6：认为圆括号推导式是元组推导式

```python
(x * x for x in range(5))
```

这是生成器，不是元组。

正确：

```python
tuple(x * x for x in range(5))
```

### 错误 7：认为 `sorted()` 返回元组

```python
result = sorted((3, 1, 2))
```

返回的是列表：

```text
[1, 2, 3]
```

---

## 36. 常用代码模板

### 36.1 创建元组

```python
t1 = ()
t2 = (10,)
t3 = (10, 20, 30)
t4 = 10, 20, 30
t5 = tuple([10, 20, 30])
```

### 36.2 访问元素

```python
t = (10, 20, 30)

print(t[0])
print(t[-1])
print(t[1:3])
```

### 36.3 遍历元组

```python
for value in t:
    print(value)
```

```python
for i, value in enumerate(t):
    print(i, value)
```

### 36.4 查找元素

```python
if 20 in t:
    print(t.index(20))
```

### 36.5 统计元素

```python
print(t.count(20))
```

### 36.6 解包

```python
a, b, c = t
```

```python
a, *b = t
```

### 36.7 排序

```python
new_t = tuple(sorted(t))
```

### 36.8 间接修改

```python
lst = list(t)
lst[0] = 100
t = tuple(lst)
```

---

## 37. 考试常考结论

1. 元组是**有序、可重复、不可变**的序列。
2. 元组真正的关键符号是**逗号**。
3. 单元素元组必须写逗号：`(10,)`。
4. 元组支持索引、切片、遍历、拼接、重复、成员判断和比较。
5. 元组不支持增加、删除单个元素、替换元素和原地排序。
6. 元组只有两个主要方法：`count()` 和 `index()`。
7. 元组切片的结果仍然是元组。
8. `sorted(元组)` 返回列表。
9. 元组中可以包含列表，列表内部可以修改。
10. 函数返回多个值时，通常返回的是元组。
11. `*args` 收集到的是元组。
12. 扩展解包中，星号变量得到的是列表。
13. 可哈希元组可以作为字典的键和集合的元素。
14. 元组中只要含有列表等不可哈希对象，整个元组通常就不可哈希。
15. `(表达式 for 变量 in 可迭代对象)` 是生成器表达式，不是元组推导式。

---

## 38. 综合示例

```python
# 创建元组
student = ("Tom", 18, 90, 85, 90)

# 索引
name = student[0]
age = student[1]

# 切片
scores = student[2:]

# 统计
count_90 = scores.count(90)

# 最大值、最小值、平均值
max_score = max(scores)
min_score = min(scores)
average = sum(scores) / len(scores)

# 解包
name, age, *scores_list = student

print("姓名：", name)
print("年龄：", age)
print("成绩：", scores_list)
print("90分出现次数：", count_90)
print("最高分：", max_score)
print("最低分：", min_score)
print("平均分：", average)
```

输出：

```text
姓名： Tom
年龄： 18
成绩： [90, 85, 90]
90分出现次数： 2
最高分： 90
最低分： 85
平均分： 88.33333333333333
```

---

## 39. 一句话总结

> 元组是一个有序、可重复、不可变的序列；逗号是创建元组的关键，适合保存结构固定、不希望被随意修改的数据。
