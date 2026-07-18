# Python 字典完整知识点

## 目录

1. [字典的基本概念](#一字典的基本概念)
2. [字典的主要特点](#二字典的主要特点)
3. [创建字典](#三创建字典)
4. [字典的键和值](#四字典的键和值)
5. [访问字典元素](#五访问字典元素)
6. [增加和修改键值对](#六增加和修改键值对)
7. [删除字典元素](#七删除字典元素)
8. [判断键和值是否存在](#八判断键和值是否存在)
9. [获取键值和键值对](#九获取键值和键值对)
10. [遍历字典](#十遍历字典)
11. [遍历时修改字典](#十一遍历时修改字典)
12. [字典常用函数](#十二字典常用函数)
13. [字典常用方法汇总](#十三字典常用方法汇总)
14. [字典推导式](#十四字典推导式)
15. [字典排序](#十五字典排序)
16. [字典与其他类型转换](#十六字典与其他类型转换)
17. [嵌套字典](#十七嵌套字典)
18. [字典中保存列表](#十八字典中保存列表)
19. [字典的复制](#十九字典的复制)
20. [字典的比较](#二十字典的比较)
21. [数字键的特殊情况](#二十一数字键的特殊情况)
22. [字典的真值判断](#二十二字典的真值判断)
23. [字典拆包](#二十三字典拆包)
24. [字典合并](#二十四字典合并)
25. [常见应用](#二十五常见应用)
26. [时间复杂度](#二十六时间复杂度)
27. [常见错误与易错点](#二十七常见错误与易错点)
28. [常用方法对比](#二十八常用方法对比)
29. [综合示例](#二十九综合示例)
30. [核心知识总结](#三十核心知识总结)

---

# 一、字典的基本概念

字典 `dict` 是 Python 中用于存储**键值对**的数据类型。

```python
student = {
    "name": "张三",
    "age": 20,
    "score": 95
}
```

其中：

- `"name"`、`"age"`、`"score"` 是键 `key`
- `"张三"`、`20`、`95` 是值 `value`
- 一个键和它对应的值合起来称为一个键值对

可以理解为：

```text
键       → 值
name     → 张三
age      → 20
score    → 95
```

查看数据类型：

```python
print(type(student))
```

输出：

```text
<class 'dict'>
```

---

# 二、字典的主要特点

## 2.1 通过键访问元素

列表通过位置索引访问元素：

```python
lst = ["张三", 20]
print(lst[0])
```

字典通过键访问对应的值：

```python
student = {"name": "张三", "age": 20}
print(student["name"])
```

输出：

```text
张三
```

## 2.2 键不能重复

```python
d = {
    "name": "张三",
    "name": "李四"
}

print(d)
```

输出：

```python
{'name': '李四'}
```

当键重复时，后面的值会覆盖前面的值。

## 2.3 值可以重复

```python
d = {
    "a": 10,
    "b": 10,
    "c": 10
}
```

这是合法的。

## 2.4 字典是可变对象

字典创建后，可以增加、删除、修改键值对。

```python
d = {"name": "张三"}

d["age"] = 20
d["name"] = "李四"

print(d)
```

输出：

```python
{'name': '李四', 'age': 20}
```

## 2.5 字典保留插入顺序

从 Python 3.7 开始，字典会保留键值对的插入顺序。

```python
d = {}

d["a"] = 1
d["b"] = 2
d["c"] = 3

print(d)
```

输出：

```python
{'a': 1, 'b': 2, 'c': 3}
```

但是，字典仍然不能像列表一样使用位置索引访问。

```python
d = {"a": 1, "b": 2}
print(d[0])
```

这里寻找的是键 `0`，而不是第 0 个元素，因此会产生：

```text
KeyError: 0
```

---

# 三、创建字典

## 3.1 使用花括号创建

```python
student = {
    "name": "张三",
    "age": 20,
    "score": 95
}
```

## 3.2 创建空字典

```python
d = {}
```

也可以写：

```python
d = dict()
```

注意：

```python
s = set()
```

创建的是空集合，不是空字典。

```python
print(type({}))
print(type(set()))
```

输出：

```text
<class 'dict'>
<class 'set'>
```

## 3.3 使用 `dict()` 创建字典

### 方式一：关键字参数

```python
d = dict(name="张三", age=20)
print(d)
```

输出：

```python
{'name': '张三', 'age': 20}
```

使用关键字参数时，键必须符合标识符命名规则。

例如下面的写法是错误的：

```python
dict(1="张三")
```

使用花括号时，键不需要符合标识符命名规则：

```python
d = {
    1: "整数键",
    "student-name": "字符串键"
}
```

### 方式二：二维序列

```python
d = dict([
    ["name", "张三"],
    ["age", 20]
])

print(d)
```

输出：

```python
{'name': '张三', 'age': 20}
```

内部元素也可以是元组：

```python
d = dict([
    ("name", "张三"),
    ("age", 20)
])
```

每个内部序列必须恰好包含两个元素：

```text
第一个元素作为键
第二个元素作为值
```

### 方式三：通过另一个字典创建

```python
d1 = {"a": 1, "b": 2}
d2 = dict(d1)

print(d2)
```

### 方式四：使用 `zip()`

```python
keys = ["name", "age", "score"]
values = ["张三", 20, 95]

d = dict(zip(keys, values))

print(d)
```

输出：

```python
{'name': '张三', 'age': 20, 'score': 95}
```

如果两个序列长度不同，以较短的序列为准。

```python
keys = ["a", "b", "c"]
values = [1, 2]

print(dict(zip(keys, values)))
```

输出：

```python
{'a': 1, 'b': 2}
```

## 3.4 使用 `fromkeys()` 创建字典

语法：

```python
dict.fromkeys(键序列, 默认值)
```

例如：

```python
d = dict.fromkeys(["name", "age", "score"], 0)
print(d)
```

输出：

```python
{'name': 0, 'age': 0, 'score': 0}
```

如果不指定默认值，则默认为 `None`：

```python
d = dict.fromkeys(["a", "b", "c"])
print(d)
```

输出：

```python
{'a': None, 'b': None, 'c': None}
```

### `fromkeys()` 的可变对象陷阱

```python
d = dict.fromkeys(["a", "b", "c"], [])

d["a"].append(1)

print(d)
```

输出：

```python
{'a': [1], 'b': [1], 'c': [1]}
```

原因是三个键对应的是**同一个列表对象**。

更安全的写法：

```python
d = {key: [] for key in ["a", "b", "c"]}

d["a"].append(1)

print(d)
```

输出：

```python
{'a': [1], 'b': [], 'c': []}
```

---

# 四、字典的键和值

## 4.1 键必须是可哈希对象

常见可以作为键的类型：

- 整数
- 浮点数
- 字符串
- 布尔值
- 元组，但元组内部的所有元素也必须可哈希
- `frozenset`

例如：

```python
d = {
    1: "整数键",
    3.14: "浮点数键",
    "name": "字符串键",
    True: "布尔值键",
    (1, 2): "元组键"
}
```

## 4.2 列表不能作为键

```python
d = {
    [1, 2]: "列表键"
}
```

会报错：

```text
TypeError: unhashable type: 'list'
```

因为列表是可变对象，不可哈希。

## 4.3 字典和集合不能作为键

字典和普通集合都是可变对象，因此不能作为字典的键。

```python
d = {
    {"a": 1}: "字典键"
}
```

```python
d = {
    {1, 2}: "集合键"
}
```

都会报错。

## 4.4 元组不一定可以作为键

可以：

```python
d = {
    (1, 2): "坐标"
}
```

不可以：

```python
d = {
    (1, [2, 3]): "内容"
}
```

因为这个元组内部包含不可哈希的列表。

## 4.5 值没有类型限制

字典的值可以是任意类型，也可以重复。

```python
d = {
    "number": 10,
    "text": "hello",
    "list": [1, 2, 3],
    "tuple": (4, 5),
    "set": {6, 7},
    "dict": {"a": 1},
    "function": print
}
```

---

# 五、访问字典元素

## 5.1 使用方括号访问

```python
student = {
    "name": "张三",
    "age": 20
}

print(student["name"])
```

输出：

```text
张三
```

如果键不存在：

```python
print(student["score"])
```

会报错：

```text
KeyError: 'score'
```

## 5.2 使用 `get()` 方法访问

语法：

```python
字典.get(键, 默认值)
```

例如：

```python
student = {"name": "张三"}

print(student.get("name"))
print(student.get("age"))
```

输出：

```text
张三
None
```

可以指定默认值：

```python
print(student.get("age", 0))
```

输出：

```text
0
```

### 方括号与 `get()` 的区别

| 写法 | 键存在 | 键不存在 |
|---|---|---|
| `d[key]` | 返回对应值 | 抛出 `KeyError` |
| `d.get(key)` | 返回对应值 | 返回 `None` |
| `d.get(key, default)` | 返回对应值 | 返回默认值 |

## 5.3 使用 `setdefault()` 获取值

语法：

```python
字典.setdefault(键, 默认值)
```

键存在时：

```python
d = {"a": 1}

result = d.setdefault("a", 100)

print(result)
print(d)
```

输出：

```text
1
{'a': 1}
```

键不存在时，会把键值对添加到字典：

```python
d = {"a": 1}

result = d.setdefault("b", 100)

print(result)
print(d)
```

输出：

```text
100
{'a': 1, 'b': 100}
```

区别：

- `get()` 不会修改字典
- `setdefault()` 在键不存在时会修改字典

---

# 六、增加和修改键值对

## 6.1 使用赋值语句

语法：

```python
字典[键] = 值
```

如果键不存在，就是增加：

```python
d = {"name": "张三"}

d["age"] = 20

print(d)
```

输出：

```python
{'name': '张三', 'age': 20}
```

如果键已经存在，就是修改：

```python
d = {"name": "张三"}

d["name"] = "李四"

print(d)
```

输出：

```python
{'name': '李四'}
```

## 6.2 使用 `update()`

`update()` 可以一次添加或修改多个键值对。

```python
d = {
    "name": "张三",
    "age": 20
}

d.update({
    "age": 21,
    "score": 95
})

print(d)
```

输出：

```python
{'name': '张三', 'age': 21, 'score': 95}
```

也可以使用关键字参数：

```python
d.update(age=21, score=95)
```

还可以传入二维序列：

```python
d.update([
    ("age", 21),
    ("score", 95)
])
```

## 6.3 使用合并运算符 `|`

Python 3.9 及之后可以使用：

```python
d1 = {"a": 1, "b": 2}
d2 = {"b": 20, "c": 3}

d3 = d1 | d2

print(d3)
```

输出：

```python
{'a': 1, 'b': 20, 'c': 3}
```

当键重复时，右边字典的值覆盖左边字典的值。

`|` 不会修改原字典。

## 6.4 使用 `|=` 原地合并

```python
d1 = {"a": 1, "b": 2}
d2 = {"b": 20, "c": 3}

d1 |= d2

print(d1)
```

输出：

```python
{'a': 1, 'b': 20, 'c': 3}
```

`|=` 会直接修改左边的字典。

---

# 七、删除字典元素

## 7.1 使用 `del`

```python
d = {
    "name": "张三",
    "age": 20
}

del d["age"]

print(d)
```

输出：

```python
{'name': '张三'}
```

如果键不存在，会报错：

```python
del d["score"]
```

```text
KeyError: 'score'
```

安全写法：

```python
if "score" in d:
    del d["score"]
```

## 7.2 使用 `pop()`

语法：

```python
字典.pop(键, 默认值)
```

删除指定键，并返回对应的值。

```python
d = {
    "name": "张三",
    "age": 20
}

value = d.pop("age")

print(value)
print(d)
```

输出：

```text
20
{'name': '张三'}
```

如果键不存在且没有默认值，会报错：

```python
d.pop("score")
```

可以设置默认值：

```python
value = d.pop("score", 0)
print(value)
```

输出：

```text
0
```

## 7.3 使用 `popitem()`

`popitem()` 删除并返回最后插入的键值对。

```python
d = {
    "a": 1,
    "b": 2,
    "c": 3
}

item = d.popitem()

print(item)
print(d)
```

输出：

```text
('c', 3)
{'a': 1, 'b': 2}
```

返回值是一个二元组：

```python
(键, 值)
```

空字典调用 `popitem()` 会报错：

```text
KeyError: 'popitem(): dictionary is empty'
```

## 7.4 使用 `clear()`

删除字典中的所有键值对：

```python
d = {"a": 1, "b": 2}

d.clear()

print(d)
```

输出：

```python
{}
```

## 7.5 删除整个字典变量

```python
d = {"a": 1}

del d
```

之后再访问 `d`：

```python
print(d)
```

会报错：

```text
NameError: name 'd' is not defined
```

---

# 八、判断键和值是否存在

## 8.1 使用 `in` 判断键

```python
d = {
    "name": "张三",
    "age": 20
}

print("name" in d)
print("score" in d)
```

输出：

```text
True
False
```

对字典使用 `in`，默认判断的是**键**，不是值。

## 8.2 使用 `not in`

```python
print("score" not in d)
```

输出：

```text
True
```

## 8.3 判断值是否存在

需要通过 `values()`：

```python
d = {
    "name": "张三",
    "age": 20
}

print("张三" in d.values())
```

输出：

```text
True
```

---

# 九、获取键、值和键值对

## 9.1 `keys()`

返回所有键的动态视图：

```python
d = {
    "name": "张三",
    "age": 20
}

result = d.keys()

print(result)
```

输出：

```text
dict_keys(['name', 'age'])
```

转换为列表：

```python
keys = list(d.keys())
print(keys)
```

输出：

```python
['name', 'age']
```

## 9.2 `values()`

返回所有值的动态视图：

```python
result = d.values()
print(result)
```

输出：

```text
dict_values(['张三', 20])
```

转换为列表：

```python
values = list(d.values())
```

## 9.3 `items()`

返回所有键值对的动态视图：

```python
result = d.items()
print(result)
```

输出：

```text
dict_items([('name', '张三'), ('age', 20)])
```

每个键值对使用二元组表示：

```python
("name", "张三")
("age", 20)
```

## 9.4 字典视图是动态的

```python
d = {"a": 1}

keys = d.keys()

d["b"] = 2

print(keys)
```

输出：

```text
dict_keys(['a', 'b'])
```

因为 `keys()`、`values()`、`items()` 返回的是动态视图，不是普通列表副本。

---

# 十、遍历字典

## 10.1 直接遍历字典

```python
d = {
    "name": "张三",
    "age": 20
}

for x in d:
    print(x)
```

输出：

```text
name
age
```

直接遍历字典，得到的是键。

等价于：

```python
for x in d.keys():
    print(x)
```

## 10.2 遍历键

```python
for key in d.keys():
    print(key)
```

可以简写为：

```python
for key in d:
    print(key)
```

## 10.3 遍历值

```python
for value in d.values():
    print(value)
```

## 10.4 同时遍历键和值

```python
for key, value in d.items():
    print(key, value)
```

执行过程相当于：

```python
for item in d.items():
    key, value = item
    print(key, value)
```

## 10.5 使用 `enumerate()` 编号

```python
d = {
    "name": "张三",
    "age": 20
}

for index, key in enumerate(d):
    print(index, key, d[key])
```

输出：

```text
0 name 张三
1 age 20
```

---

# 十一、遍历时修改字典

遍历字典时，不能随意增加或删除键值对，因为这会改变字典大小。

错误示例：

```python
d = {
    "a": 1,
    "b": 2,
    "c": 3
}

for key in d:
    if d[key] < 3:
        del d[key]
```

可能报错：

```text
RuntimeError: dictionary changed size during iteration
```

## 正确方法一：遍历键的副本

```python
for key in list(d.keys()):
    if d[key] < 3:
        del d[key]
```

## 正确方法二：使用字典推导式

```python
d = {
    "a": 1,
    "b": 2,
    "c": 3
}

d = {
    key: value
    for key, value in d.items()
    if value >= 3
}

print(d)
```

输出：

```python
{'c': 3}
```

注意：

- 修改已有键对应的值，一般不会改变字典大小
- 增加或删除键，会改变字典大小

---

# 十二、字典常用函数

## 12.1 `len()`

返回键值对数量：

```python
d = {"a": 1, "b": 2}

print(len(d))
```

输出：

```text
2
```

## 12.2 `type()`

```python
print(type(d))
```

输出：

```text
<class 'dict'>
```

## 12.3 `str()`

将字典转换为字符串：

```python
d = {"a": 1}

s = str(d)

print(s)
print(type(s))
```

## 12.4 `dict()`

用于创建字典，也可以进行浅拷贝：

```python
d1 = {"a": 1}
d2 = dict(d1)
```

## 12.5 `sorted()`

对字典使用 `sorted()`，默认排序的是键：

```python
d = {
    "c": 3,
    "a": 1,
    "b": 2
}

print(sorted(d))
```

输出：

```python
['a', 'b', 'c']
```

注意：返回的是列表，不是字典。

## 12.6 `max()` 和 `min()`

默认比较键：

```python
d = {
    "a": 10,
    "b": 30,
    "c": 20
}

print(max(d))
print(min(d))
```

输出：

```text
c
a
```

查找最大值：

```python
print(max(d.values()))
```

输出：

```text
30
```

查找值最大的键：

```python
print(max(d, key=d.get))
```

输出：

```text
b
```

查找值最小的键：

```python
print(min(d, key=d.get))
```

输出：

```text
a
```

## 12.7 `sum()`

对字典直接使用 `sum()`，会尝试对键求和。

```python
d = {
    1: 10,
    2: 20,
    3: 30
}

print(sum(d))
```

输出：

```text
6
```

因为计算的是：

```python
1 + 2 + 3
```

对值求和：

```python
print(sum(d.values()))
```

输出：

```text
60
```

---

# 十三、字典常用方法汇总

| 方法 | 作用 |
|---|---|
| `d.get(key)` | 获取键对应的值 |
| `d.keys()` | 获取所有键 |
| `d.values()` | 获取所有值 |
| `d.items()` | 获取所有键值对 |
| `d.update()` | 添加或修改多个键值对 |
| `d.setdefault()` | 获取值，键不存在时添加 |
| `d.pop()` | 删除指定键并返回值 |
| `d.popitem()` | 删除最后一个键值对 |
| `d.clear()` | 清空字典 |
| `d.copy()` | 浅拷贝字典 |
| `dict.fromkeys()` | 使用一组键创建字典 |

---

# 十四、字典推导式

基本格式：

```python
{键表达式: 值表达式 for 变量 in 可迭代对象}
```

带条件时：

```python
{键表达式: 值表达式 for 变量 in 可迭代对象 if 条件}
```

## 14.1 创建平方字典

```python
d = {
    x: x ** 2
    for x in range(1, 6)
}

print(d)
```

输出：

```python
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

## 14.2 带条件的字典推导式

```python
d = {
    x: x ** 2
    for x in range(1, 6)
    if x % 2 == 0
}

print(d)
```

输出：

```python
{2: 4, 4: 16}
```

## 14.3 交换键和值

```python
d = {
    "a": 1,
    "b": 2,
    "c": 3
}

new_d = {
    value: key
    for key, value in d.items()
}

print(new_d)
```

输出：

```python
{1: 'a', 2: 'b', 3: 'c'}
```

如果原字典中的值重复，交换后会因为新键重复而发生覆盖。

```python
d = {
    "a": 1,
    "b": 1
}

new_d = {
    value: key
    for key, value in d.items()
}

print(new_d)
```

输出：

```python
{1: 'b'}
```

## 14.4 筛选字典

```python
scores = {
    "张三": 90,
    "李四": 55,
    "王五": 80
}

passed = {
    name: score
    for name, score in scores.items()
    if score >= 60
}

print(passed)
```

输出：

```python
{'张三': 90, '王五': 80}
```

---

# 十五、字典排序

字典不依靠位置索引访问元素，但可以根据键或值生成排序结果。

## 15.1 按键排序

```python
d = {
    "c": 3,
    "a": 1,
    "b": 2
}

result = sorted(d.items())

print(result)
```

输出：

```python
[('a', 1), ('b', 2), ('c', 3)]
```

重新转换为字典：

```python
new_d = dict(sorted(d.items()))
```

结果：

```python
{'a': 1, 'b': 2, 'c': 3}
```

## 15.2 按值升序排序

```python
d = {
    "a": 30,
    "b": 10,
    "c": 20
}

result = sorted(
    d.items(),
    key=lambda item: item[1]
)

print(result)
```

输出：

```python
[('b', 10), ('c', 20), ('a', 30)]
```

## 15.3 按值降序排序

```python
result = sorted(
    d.items(),
    key=lambda item: item[1],
    reverse=True
)
```

## 15.4 生成排序后的字典

```python
new_d = dict(
    sorted(
        d.items(),
        key=lambda item: item[1],
        reverse=True
    )
)

print(new_d)
```

---

# 十六、字典与其他类型转换

## 16.1 字典转换为列表

直接转换，只获取键：

```python
d = {"a": 1, "b": 2}

print(list(d))
```

输出：

```python
['a', 'b']
```

获取键列表：

```python
list(d.keys())
```

获取值列表：

```python
list(d.values())
```

获取键值对列表：

```python
list(d.items())
```

结果：

```python
[('a', 1), ('b', 2)]
```

## 16.2 列表转换为字典

内部元素必须是长度为 2 的序列：

```python
lst = [
    ["a", 1],
    ["b", 2]
]

d = dict(lst)

print(d)
```

## 16.3 元组转换为字典

```python
t = (
    ("a", 1),
    ("b", 2)
)

d = dict(t)
```

## 16.4 两个列表合成字典

```python
keys = ["a", "b", "c"]
values = [1, 2, 3]

d = dict(zip(keys, values))
```

## 16.5 字符串形式转换为字典

推荐使用 `ast.literal_eval()`：

```python
import ast

s = "{'name': '张三', 'age': 20}"

d = ast.literal_eval(s)

print(d)
print(type(d))
```

不建议对不可信字符串使用：

```python
eval(s)
```

因为 `eval()` 会执行字符串中的 Python 表达式，存在安全风险。

---

# 十七、嵌套字典

字典的值可以是另一个字典。

```python
students = {
    "001": {
        "name": "张三",
        "age": 20
    },
    "002": {
        "name": "李四",
        "age": 21
    }
}
```

访问内层元素：

```python
print(students["001"]["name"])
```

输出：

```text
张三
```

修改：

```python
students["001"]["age"] = 22
```

增加：

```python
students["001"]["score"] = 95
```

遍历：

```python
for student_id, info in students.items():
    print("学号：", student_id)

    for key, value in info.items():
        print(key, value)
```

---

# 十八、字典中保存列表

```python
student = {
    "name": "张三",
    "scores": [90, 85, 95]
}
```

访问整个列表：

```python
print(student["scores"])
```

访问列表中的元素：

```python
print(student["scores"][0])
```

向列表中添加元素：

```python
student["scores"].append(100)
```

---

# 十九、字典的复制

## 19.1 直接赋值不是复制

```python
d1 = {"a": 1}
d2 = d1

d2["a"] = 100

print(d1)
```

输出：

```python
{'a': 100}
```

因为 `d1` 和 `d2` 指向同一个字典对象。

## 19.2 使用 `copy()` 浅拷贝

```python
d1 = {"a": 1}
d2 = d1.copy()

d2["a"] = 100

print(d1)
print(d2)
```

输出：

```python
{'a': 1}
{'a': 100}
```

## 19.3 使用 `dict()` 浅拷贝

```python
d2 = dict(d1)
```

效果与 `copy()` 类似。

## 19.4 浅拷贝的嵌套对象问题

```python
d1 = {
    "scores": [90, 80]
}

d2 = d1.copy()

d2["scores"].append(100)

print(d1)
print(d2)
```

输出：

```python
{'scores': [90, 80, 100]}
{'scores': [90, 80, 100]}
```

原因：浅拷贝只复制最外层字典，内部列表仍然是同一个对象。

## 19.5 深拷贝

```python
import copy

d1 = {
    "scores": [90, 80]
}

d2 = copy.deepcopy(d1)

d2["scores"].append(100)

print(d1)
print(d2)
```

输出：

```python
{'scores': [90, 80]}
{'scores': [90, 80, 100]}
```

---

# 二十、字典的比较

## 20.1 判断字典是否相等

```python
d1 = {"a": 1, "b": 2}
d2 = {"b": 2, "a": 1}

print(d1 == d2)
```

输出：

```text
True
```

字典相等主要判断：

- 键是否相同
- 对应的值是否相同

键值对的插入顺序不会影响相等结果。

## 20.2 字典不支持大小比较

```python
{"a": 1} > {"a": 0}
```

会报错：

```text
TypeError
```

字典一般只支持：

```python
==
!=
```

---

# 二十一、数字键的特殊情况

Python 中：

```python
1 == 1.0 == True
```

并且它们的哈希值相同，因此作为字典键时会被认为是同一个键。

```python
d = {
    1: "整数",
    1.0: "浮点数",
    True: "布尔值"
}

print(d)
```

最终只会保留一个键值对。

类似地：

```python
0 == 0.0 == False
```

它们作为字典键时也会被视为同一个键。

---

# 二十二、字典的真值判断

空字典的布尔值为假：

```python
d = {}

if d:
    print("非空")
else:
    print("空字典")
```

输出：

```text
空字典
```

非空字典的布尔值为真：

```python
d = {"a": 1}

if d:
    print("非空")
```

判断字典是否为空，推荐写：

```python
if not d:
    print("字典为空")
```

也可以写：

```python
if len(d) == 0:
    print("字典为空")
```

---

# 二十三、字典拆包

## 23.1 `*字典`

单个星号拆出的是键：

```python
d = {
    "a": 1,
    "b": 2
}

print(*d)
```

输出：

```text
a b
```

等价于：

```python
print(*d.keys())
```

## 23.2 `**字典`

双星号把字典拆成关键字参数。

```python
data = {
    "name": "张三",
    "age": 20
}

print("姓名：{name}，年龄：{age}".format(**data))
```

输出：

```text
姓名：张三，年龄：20
```

调用函数：

```python
def show(name, age):
    print(name, age)

data = {
    "name": "张三",
    "age": 20
}

show(**data)
```

相当于：

```python
show(name="张三", age=20)
```

字典中的键必须与函数参数名相匹配。

---

# 二十四、字典合并

## 24.1 使用 `update()`

```python
d1 = {"a": 1}
d2 = {"b": 2}

d1.update(d2)
```

会修改 `d1`。

## 24.2 使用 `|`

```python
d3 = d1 | d2
```

不会修改原字典。

## 24.3 使用字典拆包

```python
d3 = {
    **d1,
    **d2
}
```

如果有重复键，后面的字典覆盖前面的字典。

```python
d1 = {"a": 1, "b": 2}
d2 = {"b": 20, "c": 3}

d3 = {**d1, **d2}

print(d3)
```

输出：

```python
{'a': 1, 'b': 20, 'c': 3}
```

---

# 二十五、常见应用

## 25.1 统计元素出现次数

```python
text = "banana"

count = {}

for ch in text:
    if ch in count:
        count[ch] += 1
    else:
        count[ch] = 1

print(count)
```

输出：

```python
{'b': 1, 'a': 3, 'n': 2}
```

更简洁的写法：

```python
count = {}

for ch in text:
    count[ch] = count.get(ch, 0) + 1
```

执行逻辑：

```python
count.get(ch, 0)
```

- 字符已经存在：获取原来的次数
- 字符不存在：返回 0
- 最后统一加 1

## 25.2 按类别分组

```python
words = ["apple", "ant", "banana", "book"]

groups = {}

for word in words:
    first = word[0]
    groups.setdefault(first, []).append(word)

print(groups)
```

输出：

```python
{
    'a': ['apple', 'ant'],
    'b': ['banana', 'book']
}
```

## 25.3 保存对象信息

```python
student = {
    "name": "张三",
    "age": 20,
    "scores": {
        "语文": 90,
        "数学": 95
    }
}
```

## 25.4 建立映射关系

```python
month_days = {
    1: 31,
    2: 28,
    3: 31
}
```

---

# 二十六、时间复杂度

字典底层通常使用哈希表实现。

平均情况下：

| 操作 | 平均时间复杂度 |
|---|---:|
| 根据键查找值 | `O(1)` |
| 增加键值对 | `O(1)` |
| 修改键值对 | `O(1)` |
| 删除键值对 | `O(1)` |
| 判断键是否存在 | `O(1)` |
| 遍历整个字典 | `O(n)` |
| 判断值是否存在 | `O(n)` |

例如：

```python
key in d
```

平均时间复杂度是 `O(1)`。

而：

```python
value in d.values()
```

通常需要逐个检查，时间复杂度是 `O(n)`。

注意：以上是平均情况，极端情况下哈希冲突可能使性能下降。

---

# 二十七、常见错误与易错点

## 易错点 1：`in` 判断的是键

```python
d = {"name": "张三"}

print("张三" in d)
```

输出：

```text
False
```

因为 `"张三"` 是值，不是键。

正确写法：

```python
print("张三" in d.values())
```

## 易错点 2：键不存在时使用方括号会报错

```python
d["age"]
```

如果键不存在，会产生 `KeyError`。

安全写法：

```python
d.get("age")
```

## 易错点 3：字典不能使用位置索引

```python
d[0]
```

表示访问键 `0`，不是第 0 个元素。

## 易错点 4：重复键会被覆盖

```python
d = {
    "a": 1,
    "a": 2
}
```

结果：

```python
{'a': 2}
```

## 易错点 5：列表不能作为键

```python
d[[1, 2]] = 3
```

会报错，因为列表不可哈希。

## 易错点 6：遍历时不能修改字典大小

错误：

```python
for key in d:
    del d[key]
```

正确：

```python
for key in list(d):
    del d[key]
```

## 易错点 7：`get()` 的返回值不一定能判断键是否存在

```python
d = {"a": None}

print(d.get("a"))
print(d.get("b"))
```

两次输出都是：

```text
None
```

无法仅通过返回结果区分键是否存在。

应该使用：

```python
if "a" in d:
    print("键存在")
```

## 易错点 8：`setdefault()` 可能修改字典

```python
d = {}

d.setdefault("a", 1)

print(d)
```

结果：

```python
{'a': 1}
```

## 易错点 9：字典视图不是列表

```python
d.keys()[0]
```

会报错。

需要先转换：

```python
list(d.keys())[0]
```

不过通常不建议依赖“第几个键”来操作字典。

## 易错点 10：`pop()` 与 `del` 的区别

```python
value = d.pop("a")
```

会返回被删除的值。

```python
del d["a"]
```

只负责删除，不返回值。

## 易错点 11：字典视图是动态的

错误：

```python
for key in d.keys():
    del d[key]
```

正确：

```python
for key in list(d.keys()):
    del d[key]
```

## 易错点 12：`fromkeys()` 可能共享同一个可变对象

```python
d = dict.fromkeys(["a", "b"], [])
d["a"].append(1)

print(d)
```

输出：

```python
{'a': [1], 'b': [1]}
```

---

# 二十八、常用方法对比

## 28.1 `get()` 与方括号

| 情况 | `d[key]` | `d.get(key)` |
|---|---|---|
| 键存在 | 返回值 | 返回值 |
| 键不存在 | 报错 | 返回 `None` 或默认值 |
| 是否修改字典 | 否 | 否 |

## 28.2 `get()` 与 `setdefault()`

| 方法 | 键不存在时返回 | 是否添加键 |
|---|---|---|
| `get()` | 默认值 | 否 |
| `setdefault()` | 默认值 | 是 |

## 28.3 `del` 与 `pop()`

| 操作 | 是否返回被删除的值 | 键不存在 |
|---|---|---|
| `del d[key]` | 否 | 报错 |
| `d.pop(key)` | 是 | 报错 |
| `d.pop(key, default)` | 是 | 返回默认值 |

## 28.4 `clear()` 与重新赋值 `{}`

```python
d.clear()
```

清空原字典对象。

```python
d = {}
```

让变量 `d` 指向一个新的空字典。

例如：

```python
d1 = {"a": 1}
d2 = d1

d1.clear()

print(d2)
```

输出：

```python
{}
```

但：

```python
d1 = {"a": 1}
d2 = d1

d1 = {}

print(d2)
```

输出：

```python
{'a': 1}
```

## 28.5 `update()`、`|` 与 `|=`

| 写法 | 是否修改原字典 | 重复键处理 |
|---|---|---|
| `d1.update(d2)` | 修改 `d1` | `d2` 覆盖 `d1` |
| `d1 \| d2` | 不修改原字典 | 右边覆盖左边 |
| `d1 \|= d2` | 修改 `d1` | 右边覆盖左边 |

---

# 二十九、综合示例

## 学生成绩管理系统

```python
students = {}

while True:
    print("1. 添加学生")
    print("2. 查询学生")
    print("3. 删除学生")
    print("4. 显示所有学生")
    print("0. 退出")

    choice = input("请输入操作：")

    if choice == "1":
        name = input("请输入姓名：")
        score = float(input("请输入成绩："))

        students[name] = score
        print("添加成功")

    elif choice == "2":
        name = input("请输入姓名：")

        if name in students:
            print("成绩：", students[name])
        else:
            print("没有该学生")

    elif choice == "3":
        name = input("请输入姓名：")

        score = students.pop(name, None)

        if score is None:
            print("没有该学生")
        else:
            print("删除成功")

    elif choice == "4":
        for name, score in students.items():
            print(name, score)

    elif choice == "0":
        break

    else:
        print("输入错误")
```

说明：

- 使用学生姓名作为键
- 使用学生成绩作为值
- `students[name] = score` 可以完成添加或修改
- `name in students` 用于判断学生是否存在
- `students.pop(name, None)` 用于安全删除
- `students.items()` 用于同时遍历姓名和成绩

> 实际项目中，如果成绩可能是 `None`，就不应把 `None` 作为判断删除是否成功的唯一依据，应先用 `in` 判断键是否存在。

---

# 三十、核心知识总结

字典最重要的知识可以归纳为：

```text
1. 字典用于保存键值对。
2. 字典通过键访问值，而不是通过位置索引访问。
3. 键必须唯一，重复键会被覆盖。
4. 键必须可哈希，列表、字典、普通集合不能作为键。
5. 值可以是任意类型，也可以重复。
6. 字典是可变对象，可以增加、删除和修改。
7. Python 3.7 以后，字典保留插入顺序。
8. 直接遍历字典得到的是键。
9. keys()、values()、items() 分别获取键、值和键值对。
10. get() 可以避免键不存在时产生 KeyError。
11. update() 用于批量添加或修改键值对。
12. pop() 删除指定键，popitem() 删除最后一个键值对。
13. 字典可以嵌套，也可以保存列表等其他对象。
14. copy() 是浅拷贝，deepcopy() 是深拷贝。
15. 字典查找、添加和删除的平均时间复杂度为 O(1)。
```

## 字典最常见的基本操作模板

```python
d = {}

# 增加或修改
d["name"] = "张三"

# 获取
value = d["name"]
value = d.get("name", "默认值")

# 判断键是否存在
if "name" in d:
    print(d["name"])

# 删除
d.pop("name", None)

# 遍历
for key, value in d.items():
    print(key, value)
```

## 最需要掌握的 8 个操作

```python
d[key]                    # 访问值
d.get(key, default)       # 安全访问
d[key] = value            # 增加或修改
del d[key]                # 删除
d.pop(key, default)       # 安全删除并返回值
key in d                  # 判断键是否存在
d.items()                 # 获取键值对
for key, value in d.items():
    ...                   # 遍历键和值
```
