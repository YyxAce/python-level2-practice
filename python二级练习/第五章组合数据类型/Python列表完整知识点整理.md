# Python 列表完整知识点整理

## 一、列表的基本概念

列表 `list` 是 Python 中最常用的**组合数据类型**之一，同时属于：

- 序列类型
- 可变数据类型
- 有序容器

```python
a = [10, 20, 30]
```

列表的主要特点：

| 特点 | 说明 |
|---|---|
| 有序 | 每个元素都有固定位置和索引 |
| 可变 | 可以增加、删除、修改元素 |
| 可重复 | 相同元素可以出现多次 |
| 类型不限 | 一个列表中可以放不同类型的数据 |
| 可以嵌套 | 列表中可以继续包含列表 |

```python
data = [10, "hello", 3.14, True, [1, 2]]
```

> “有序”不是指元素会自动从小到大排列，而是指元素的**先后位置会被保留**。

---

## 二、创建列表

### 1. 使用方括号创建

```python
a = [1, 2, 3]
b = ["A", "B", "C"]
c = []
```

空列表：

```python
a = []
```

### 2. 使用 `list()` 创建

```python
a = list()
print(a)
```

结果：

```python
[]
```

将其他可迭代对象转换为列表：

```python
list("Python")
# ['P', 'y', 't', 'h', 'o', 'n']

list((1, 2, 3))
# [1, 2, 3]

list(range(5))
# [0, 1, 2, 3, 4]
```

注意：

```python
list(123)
```

会报错，因为整数不是可迭代对象。

### 3. 使用重复运算创建

```python
a = [0] * 5
print(a)
```

结果：

```python
[0, 0, 0, 0, 0]
```

### 4. 使用列表推导式创建

```python
a = [i for i in range(5)]
```

结果：

```python
[0, 1, 2, 3, 4]
```

---

## 三、列表索引

列表索引从 `0` 开始。

```python
a = ["A", "B", "C", "D"]
```

| 元素 | A | B | C | D |
|---|---:|---:|---:|---:|
| 正向索引 | 0 | 1 | 2 | 3 |
| 反向索引 | -4 | -3 | -2 | -1 |

### 1. 正向索引

```python
a[0]   # 'A'
a[2]   # 'C'
```

### 2. 反向索引

```python
a[-1]  # 'D'
a[-2]  # 'C'
```

### 3. 索引越界

```python
a[10]
```

会出现：

```text
IndexError: list index out of range
```

列表合法索引范围：

```text
-len(a) <= 索引 < len(a)
```

---

## 四、列表切片

基本格式：

```python
列表[start:stop:step]
```

含义：

- 从 `start` 开始；
- 到 `stop` 之前结束；
- 每次移动 `step`；
- 包含 `start`；
- 不包含 `stop`。

```python
a = [0, 1, 2, 3, 4, 5]
```

### 1. 普通切片

```python
a[1:4]
# [1, 2, 3]
```

### 2. 省略开始位置

```python
a[:3]
# [0, 1, 2]
```

### 3. 省略结束位置

```python
a[2:]
# [2, 3, 4, 5]
```

### 4. 复制整个列表

```python
b = a[:]
```

这会创建一个新的列表，但属于**浅拷贝**。

### 5. 设置步长

```python
a[::2]
# [0, 2, 4]
```

### 6. 倒序

```python
a[::-1]
# [5, 4, 3, 2, 1, 0]
```

### 7. 负步长

```python
a[4:1:-1]
# [4, 3, 2]
```

负步长时，一般需要满足：

```text
start > stop
```

例如：

```python
a[1:4:-1]
# []
```

因为从索引 `1` 开始向左走，不可能到达右边的索引 `4`。

### 8. 切片一般不会索引越界

```python
a[1:100]
```

不会报错，而是取到列表末尾。

这和单个索引不同：

```python
a[100]
```

会报错。

---

## 五、访问嵌套列表

```python
a = [
    [1, 2, 3],
    [4, 5, 6]
]
```

访问第一个子列表：

```python
a[0]
# [1, 2, 3]
```

访问数字 `2`：

```python
a[0][1]
# 2
```

理解过程：

```python
a[0]       # [1, 2, 3]
a[0][1]    # 2
```

多个中括号表示逐层访问。

---

## 六、修改列表元素

列表是可变对象，可以直接修改。

```python
a = [10, 20, 30]
a[1] = 200
print(a)
```

结果：

```python
[10, 200, 30]
```

### 1. 使用切片修改多个元素

```python
a = [1, 2, 3, 4, 5]
a[1:4] = [20, 30, 40]
```

结果：

```python
[1, 20, 30, 40, 5]
```

### 2. 切片赋值可以改变列表长度

```python
a = [1, 2, 3, 4]
a[1:3] = [10, 20, 30, 40]
```

结果：

```python
[1, 10, 20, 30, 40, 4]
```

原来替换两个元素，现在放入四个元素，所以列表变长。

### 3. 使用切片插入元素

```python
a = [1, 2, 3]
a[1:1] = [10, 20]
```

结果：

```python
[1, 10, 20, 2, 3]
```

### 4. 使用切片删除元素

```python
a = [1, 2, 3, 4]
a[1:3] = []
```

结果：

```python
[1, 4]
```

---

## 七、增加列表元素

### 1. `append()`：末尾追加一个元素

```python
a = [1, 2]
a.append(3)
print(a)
```

结果：

```python
[1, 2, 3]
```

`append()` 无论添加什么，都只添加为**一个元素**。

```python
a = [1, 2]
a.append([3, 4])
```

结果：

```python
[1, 2, [3, 4]]
```

### 2. `extend()`：一次添加多个元素

```python
a = [1, 2]
a.extend([3, 4])
```

结果：

```python
[1, 2, 3, 4]
```

`extend()` 会遍历参数，然后将其中的元素逐个加入。

```python
a = [1, 2]
a.extend("AB")
```

结果：

```python
[1, 2, 'A', 'B']
```

### 3. `insert()`：在指定位置插入

格式：

```python
列表.insert(索引, 元素)
```

例如：

```python
a = [1, 3]
a.insert(1, 2)
```

结果：

```python
[1, 2, 3]
```

插入位置是索引 `1`，原来索引 `1` 及后面的元素向右移动。

### 4. 三种方法的区别

```python
a = [1, 2]
```

```python
a.append([3, 4])
# [1, 2, [3, 4]]
```

```python
a.extend([3, 4])
# [1, 2, 3, 4]
```

```python
a.insert(1, [3, 4])
# [1, [3, 4], 2]
```

---

## 八、删除列表元素

### 1. `del`：根据位置删除

```python
a = [10, 20, 30]
del a[1]
```

结果：

```python
[10, 30]
```

删除切片：

```python
a = [1, 2, 3, 4, 5]
del a[1:4]
```

结果：

```python
[1, 5]
```

删除整个变量：

```python
del a
```

此后变量 `a` 不再存在。

### 2. `remove()`：根据值删除

```python
a = [10, 20, 30]
a.remove(20)
```

结果：

```python
[10, 30]
```

如果存在重复元素，只删除第一个：

```python
a = [1, 2, 2, 3]
a.remove(2)
```

结果：

```python
[1, 2, 3]
```

如果元素不存在，会抛出 `ValueError`。

安全写法：

```python
if 100 in a:
    a.remove(100)
```

### 3. `pop()`：删除并返回元素

不写索引时，删除最后一个元素：

```python
a = [10, 20, 30]
x = a.pop()
```

结果：

```python
x == 30
a == [10, 20]
```

指定索引：

```python
a = [10, 20, 30]
x = a.pop(1)
```

结果：

```python
x == 20
a == [10, 30]
```

空列表调用 `pop()` 会抛出 `IndexError`。

### 4. `clear()`：清空列表

```python
a = [1, 2, 3]
a.clear()
```

结果：

```python
[]
```

### 5. 删除方法对比

| 方法 | 根据什么删除 | 是否返回被删元素 |
|---|---|---|
| `del a[i]` | 索引 | 否 |
| `a.remove(x)` | 元素值 | 否 |
| `a.pop(i)` | 索引 | 是 |
| `a.clear()` | 全部元素 | 否 |

---

## 九、查找和统计

### 1. `index()`：查找元素第一次出现的索引

```python
a = ["A", "B", "C", "B"]
a.index("B")
# 1
```

如果元素不存在，会抛出 `ValueError`。

安全写法：

```python
if "B" in a:
    print(a.index("B"))
```

可以指定查找范围：

```python
a.index("B", 2)
```

完整格式：

```python
a.index(元素, start, stop)
```

### 2. `count()`：统计出现次数

```python
a = [1, 2, 2, 2, 3]
a.count(2)
# 3
```

元素不存在时返回 `0`，不会报错：

```python
a.count(100)
# 0
```

### 3. `in` 和 `not in`

```python
2 in [1, 2, 3]
# True

5 not in [1, 2, 3]
# True
```

---

## 十、列表运算符

### 1. 拼接运算符 `+`

```python
[1, 2] + [3, 4]
# [1, 2, 3, 4]
```

`+` 不会修改原列表，而是创建新列表。

```python
a = [1, 2]
b = a + [3]
```

此时：

```python
a == [1, 2]
b == [1, 2, 3]
```

### 2. 重复运算符 `*`

```python
[1, 2] * 3
# [1, 2, 1, 2, 1, 2]
```

### 3. 成员运算符

```python
2 in [1, 2, 3]
2 not in [1, 2, 3]
```

### 4. 比较运算符

列表可以使用：

```text
==  !=  <  <=  >  >=
```

#### 相等比较

```python
[1, 2, 3] == [1, 2, 3]
# True
```

元素和顺序都必须一致。

```python
[1, 2, 3] == [3, 2, 1]
# False
```

#### 大小比较

列表按照从左到右的顺序逐个比较。

```python
[1, 5] < [2, 0]
# True
```

因为第一个元素比较时：

```python
1 < 2
```

已经可以确定结果，后面的元素不再比较。

```python
[1, 9] > [1, 5]
# True
```

第一个元素相等，继续比较第二个元素：

```python
9 > 5
```

前面的元素全部相同时，较短列表更小：

```python
[1, 2] < [1, 2, 0]
# True
```

不同且不可比较的类型可能报错：

```python
[1] < ["1"]
```

会抛出 `TypeError`。

---

## 十一、排序与反转

### 1. `sort()`：原地排序

```python
a = [3, 1, 2]
a.sort()
```

结果：

```python
[1, 2, 3]
```

降序排列：

```python
a.sort(reverse=True)
```

结果：

```python
[3, 2, 1]
```

按字符串长度排序：

```python
words = ["Python", "C", "Java"]
words.sort(key=len)
```

结果：

```python
['C', 'Java', 'Python']
```

按绝对值排序：

```python
a = [-10, 2, -3, 5]
a.sort(key=abs)
```

结果：

```python
[2, -3, 5, -10]
```

### 2. `sorted()`：返回新列表

```python
a = [3, 1, 2]
b = sorted(a)
```

结果：

```python
a == [3, 1, 2]
b == [1, 2, 3]
```

| 写法 | 是否修改原列表 | 返回值 |
|---|---|---|
| `a.sort()` | 是 | `None` |
| `sorted(a)` | 否 | 新列表 |

错误写法：

```python
a = a.sort()
```

执行后 `a` 会变成 `None`，因为 `sort()` 是原地修改，没有返回排序后的列表。

### 3. `reverse()`：原地反转

```python
a = [1, 2, 3]
a.reverse()
```

结果：

```python
[3, 2, 1]
```

注意：`reverse()` 只是反转原有顺序，不是降序排序。

```python
a = [3, 1, 2]
a.reverse()
```

结果：

```python
[2, 1, 3]
```

### 4. `reversed()`：返回反向迭代器

```python
a = [1, 2, 3]
b = reversed(a)
```

如果需要列表：

```python
b = list(reversed(a))
```

结果：

```python
[3, 2, 1]
```

---

## 十二、列表常用方法汇总

| 方法 | 作用 |
|---|---|
| `append(x)` | 在末尾添加一个元素 |
| `extend(iterable)` | 在末尾添加多个元素 |
| `insert(i, x)` | 在指定位置插入元素 |
| `remove(x)` | 删除第一个值为 `x` 的元素 |
| `pop(i)` | 删除并返回指定位置元素 |
| `clear()` | 清空列表 |
| `index(x)` | 返回元素第一次出现的索引 |
| `count(x)` | 统计元素出现次数 |
| `sort()` | 原地排序 |
| `reverse()` | 原地反转 |
| `copy()` | 浅拷贝列表 |

大部分会修改原列表的方法返回值都是 `None`：

```text
append()
extend()
insert()
remove()
clear()
sort()
reverse()
```

`pop()` 比较特殊，它会返回被删除的元素。

---

## 十三、列表常用内置函数

### 1. `len()`：列表长度

```python
len([10, 20, 30])
# 3
```

### 2. `max()`：最大值

```python
max([3, 8, 2])
# 8
```

### 3. `min()`：最小值

```python
min([3, 8, 2])
# 2
```

### 4. `sum()`：求和

```python
sum([1, 2, 3])
# 6
```

列表元素必须是可以进行加法运算的数值。

### 5. `sorted()`：排序并返回新列表

```python
sorted([3, 1, 2])
```

### 6. `enumerate()`：同时获得索引和元素

```python
a = ["A", "B", "C"]

for index, value in enumerate(a):
    print(index, value)
```

输出：

```text
0 A
1 B
2 C
```

指定起始编号：

```python
for index, value in enumerate(a, start=1):
    print(index, value)
```

输出：

```text
1 A
2 B
3 C
```

### 7. `zip()`：将多个序列对应组合

```python
names = ["张三", "李四"]
scores = [90, 85]

for name, score in zip(names, scores):
    print(name, score)
```

输出：

```text
张三 90
李四 85
```

`zip()` 以最短的序列为准。

### 8. `any()`

只要有一个元素为真，结果就是 `True`。

```python
any([False, 0, 5])
# True
```

### 9. `all()`

所有元素都为真，结果才是 `True`。

```python
all([1, 2, 3])
# True

all([1, 0, 3])
# False
```

---

## 十四、遍历列表

### 1. 直接遍历元素

```python
a = [10, 20, 30]

for x in a:
    print(x)
```

### 2. 根据索引遍历

```python
for i in range(len(a)):
    print(i, a[i])
```

### 3. 使用 `enumerate()`

推荐写法：

```python
for i, x in enumerate(a):
    print(i, x)
```

### 4. 使用 `while` 遍历

```python
i = 0

while i < len(a):
    print(a[i])
    i += 1
```

---

## 十五、遍历过程中修改列表

这是列表最容易出错的部分之一。

### 1. 错误：遍历时直接删除

```python
a = [1, 2, 2, 2, 3]

for x in a:
    if x == 2:
        a.remove(x)

print(a)
```

结果可能是：

```python
[1, 2, 3]
```

仍然剩下一个 `2`。

原因：

1. 删除元素后，后面的元素整体向左移动；
2. `for` 循环继续移动到下一个位置；
3. 刚移动过来的元素被跳过。

### 2. 正确方法一：遍历副本

```python
a = [1, 2, 2, 2, 3]

for x in a[:]:
    if x == 2:
        a.remove(x)
```

### 3. 正确方法二：列表推导式

```python
a = [1, 2, 2, 2, 3]
a = [x for x in a if x != 2]
```

### 4. 正确方法三：倒序删除

```python
a = [1, 2, 2, 2, 3]

for i in range(len(a) - 1, -1, -1):
    if a[i] == 2:
        del a[i]
```

倒序删除时，前面尚未访问的元素索引不会发生变化。

---

## 十六、列表推导式

### 1. 基本形式

```python
[表达式 for 变量 in 可迭代对象]
```

例如：

```python
a = [i for i in range(5)]
# [0, 1, 2, 3, 4]
```

### 2. 对元素进行运算

```python
a = [i ** 2 for i in range(5)]
# [0, 1, 4, 9, 16]
```

### 3. 带筛选条件

格式：

```python
[表达式 for 变量 in 可迭代对象 if 条件]
```

例如，保留偶数：

```python
a = [i for i in range(10) if i % 2 == 0]
# [0, 2, 4, 6, 8]
```

### 4. 带双分支表达式

格式：

```python
[条件成立时的值 if 条件 else 条件不成立时的值
 for 变量 in 可迭代对象]
```

例如：

```python
a = ["偶数" if i % 2 == 0 else "奇数" for i in range(5)]
```

结果：

```python
['偶数', '奇数', '偶数', '奇数', '偶数']
```

注意两个 `if` 的位置不同：

#### 筛选元素

```python
[i for i in range(10) if i % 2 == 0]
```

只保留满足条件的元素。

#### 二选一生成元素

```python
[i if i % 2 == 0 else -1 for i in range(10)]
```

每个元素都会生成，只是生成结果不同。

### 5. 嵌套列表推导式

```python
a = [[i, j] for i in range(2) for j in range(3)]
```

结果：

```python
[[0, 0], [0, 1], [0, 2],
 [1, 0], [1, 1], [1, 2]]
```

对应普通循环：

```python
a = []

for i in range(2):
    for j in range(3):
        a.append([i, j])
```

---

## 十七、列表赋值、引用和拷贝

### 1. 普通赋值不是复制

```python
a = [1, 2, 3]
b = a
```

这里 `a` 和 `b` 指向同一个列表对象。

```python
b[0] = 100
```

此时：

```python
a == [100, 2, 3]
b == [100, 2, 3]
```

关系可以理解为：

```text
a ─┐
   ├──> [1, 2, 3]
b ─┘
```

### 2. 判断是否是同一个对象

```python
a is b
# True
```

### 3. 浅拷贝

常见浅拷贝方式：

```python
b = a.copy()
b = a[:]
b = list(a)
```

对于一维列表：

```python
a = [1, 2, 3]
b = a.copy()

b[0] = 100
```

结果：

```python
a == [1, 2, 3]
b == [100, 2, 3]
```

### 4. 浅拷贝对嵌套列表的影响

```python
a = [[1, 2], [3, 4]]
b = a.copy()
```

外层列表不同：

```python
a is b
# False
```

但内部子列表仍然是同一个对象：

```python
a[0] is b[0]
# True
```

修改内部列表：

```python
b[0][0] = 100
```

此时：

```python
a == [[100, 2], [3, 4]]
b == [[100, 2], [3, 4]]
```

### 5. 深拷贝

深拷贝需要 `copy` 模块：

```python
import copy

a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)
```

现在内部嵌套对象也会复制。

```python
b[0][0] = 100
```

结果：

```python
a == [[1, 2], [3, 4]]
b == [[100, 2], [3, 4]]
```

### 6. `==` 和 `is` 的区别

| 运算符 | 比较内容 |
|---|---|
| `==` | 两个对象的值是否相等 |
| `is` | 是否是同一个对象 |

```python
a = [1, 2]
b = [1, 2]

a == b   # True
a is b   # False
```

---

## 十八、二维列表

### 1. 创建二维列表

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
```

### 2. 遍历二维列表

```python
for row in matrix:
    for value in row:
        print(value)
```

### 3. 根据索引遍历

```python
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j])
```

### 4. 创建固定大小的二维列表

正确写法：

```python
matrix = [[0 for j in range(3)] for i in range(2)]
```

简化：

```python
matrix = [[0] * 3 for _ in range(2)]
```

结果：

```python
[
    [0, 0, 0],
    [0, 0, 0]
]
```

### 5. 二维列表的经典错误

错误写法：

```python
matrix = [[0] * 3] * 2
```

表面上结果也是：

```python
[[0, 0, 0], [0, 0, 0]]
```

但两个子列表实际上是同一个对象。

```python
matrix[0][0] = 1
```

结果：

```python
[[1, 0, 0], [1, 0, 0]]
```

原因是：

```python
[[0] * 3] * 2
```

只是把同一个内部列表的引用重复了两次。

正确写法：

```python
matrix = [[0] * 3 for _ in range(2)]
```

---

## 十九、列表解包

### 1. 基本解包

```python
a = [10, 20, 30]
x, y, z = a
```

结果：

```python
x == 10
y == 20
z == 30
```

左右数量必须对应，否则会报错。

### 2. 使用星号收集剩余元素

```python
a = [1, 2, 3, 4, 5]
x, *middle, y = a
```

结果：

```python
x == 1
middle == [2, 3, 4]
y == 5
```

### 3. 交换变量

```python
a = 10
b = 20

a, b = b, a
```

结果：

```python
a == 20
b == 10
```

右侧先整体计算，再分别赋值给左侧。

---

## 二十、列表与其他类型转换

### 1. 字符串转列表

```python
list("abc")
# ['a', 'b', 'c']
```

如果按指定分隔符拆分：

```python
"1,2,3".split(",")
# ['1', '2', '3']
```

转成整数：

```python
a = list(map(int, "1,2,3".split(",")))
# [1, 2, 3]
```

### 2. 列表转字符串

元素必须是字符串：

```python
a = ["A", "B", "C"]
"-".join(a)
# 'A-B-C'
```

数字列表需要先转换：

```python
a = [1, 2, 3]
",".join(map(str, a))
# '1,2,3'
```

### 3. 元组转列表

```python
list((1, 2, 3))
```

### 4. 列表转元组

```python
tuple([1, 2, 3])
# (1, 2, 3)
```

### 5. 集合转列表

```python
list({1, 2, 3})
```

注意：集合本身无固定顺序，所以转换后的顺序不应依赖。

### 6. 字典转列表

```python
d = {"name": "Tom", "age": 20}
```

```python
list(d)
# ['name', 'age']
```

获取键：

```python
list(d.keys())
```

获取值：

```python
list(d.values())
```

获取键值对：

```python
list(d.items())
# [('name', 'Tom'), ('age', 20)]
```

---

## 二十一、列表作为函数参数

列表是可变对象。

```python
def change(data):
    data.append(100)

a = [1, 2, 3]
change(a)

print(a)
```

结果：

```python
[1, 2, 3, 100]
```

因为函数中的 `data` 和外部的 `a` 指向同一个列表。

如果不希望修改原列表，可以传入副本：

```python
change(a.copy())
```

或者在函数内部创建新列表：

```python
def change(data):
    data = data + [100]
    return data
```

---

## 二十二、列表能否作为字典键或集合元素

列表是可变对象，因此通常不可哈希。

所以列表不能作为字典键：

```python
d = {[1, 2]: "value"}
```

会报错：

```text
TypeError: unhashable type: 'list'
```

列表也不能直接作为集合元素：

```python
s = {[1, 2]}
```

同样报错。

可以改成元组：

```python
d = {(1, 2): "value"}
s = {(1, 2)}
```

但是，列表内部可以包含列表：

```python
a = [[1, 2], [3, 4]]
```

---

## 二十三、常见算法

### 1. 求列表和

```python
a = [1, 2, 3]
total = sum(a)
```

手动计算：

```python
total = 0

for x in a:
    total += x
```

### 2. 求平均值

```python
a = [1, 2, 3]
average = sum(a) / len(a)
```

需要注意空列表不能除以 `0`：

```python
if a:
    average = sum(a) / len(a)
```

### 3. 找最大值及其索引

```python
a = [3, 8, 2, 8]

max_value = max(a)
max_index = a.index(max_value)
```

结果：

```python
max_value == 8
max_index == 1
```

只能得到第一个最大值的位置。

### 4. 去重但保持原顺序

```python
a = [1, 2, 1, 3, 2]
result = []

for x in a:
    if x not in result:
        result.append(x)
```

结果：

```python
[1, 2, 3]
```

也可以：

```python
result = list(dict.fromkeys(a))
```

### 5. 统计频率

```python
a = ["A", "B", "A", "C", "A"]
count = {}

for x in a:
    count[x] = count.get(x, 0) + 1
```

结果：

```python
{'A': 3, 'B': 1, 'C': 1}
```

### 6. 查找所有指定元素的索引

```python
a = [1, 2, 1, 3, 1]

indexes = [
    i for i, x in enumerate(a)
    if x == 1
]
```

结果：

```python
[0, 2, 4]
```

### 7. 将二维列表展开为一维列表

```python
matrix = [[1, 2], [3, 4], [5, 6]]

result = [
    x
    for row in matrix
    for x in row
]
```

结果：

```python
[1, 2, 3, 4, 5, 6]
```

---

## 二十四、列表操作的时间复杂度

常见操作的大致效率：

| 操作 | 平均时间复杂度 |
|---|---:|
| `a[i]` 索引访问 | `O(1)` |
| `a[i] = x` 修改 | `O(1)` |
| `append()` | `O(1)` |
| `pop()` 删除末尾 | `O(1)` |
| `insert(0, x)` | `O(n)` |
| `pop(0)` | `O(n)` |
| `remove(x)` | `O(n)` |
| `x in a` | `O(n)` |
| `index(x)` | `O(n)` |
| `sort()` | `O(n log n)` |
| 切片 | 与切片长度有关 |

列表适合：

- 根据索引快速访问；
- 在末尾添加、删除元素。

列表不适合频繁在开头插入或删除，因为后面的所有元素都需要移动。

---

## 二十五、常见错误总结

### 错误一：把修改方法的返回值重新赋值

```python
a = [3, 1, 2]
a = a.sort()
```

结果：

```python
a is None
```

正确写法：

```python
a.sort()
```

或者：

```python
a = sorted(a)
```

### 错误二：混淆 `append()` 和 `extend()`

```python
a.append([3, 4])
# [1, 2, [3, 4]]
```

```python
a.extend([3, 4])
# [1, 2, 3, 4]
```

### 错误三：遍历列表时删除元素

```python
for x in a:
    if 条件:
        a.remove(x)
```

可能跳过元素。

推荐：

```python
a = [x for x in a if not 条件]
```

### 错误四：二维列表使用乘法复制

```python
a = [[0] * 3] * 2
```

多个子列表引用同一对象。

正确写法：

```python
a = [[0] * 3 for _ in range(2)]
```

### 错误五：认为 `b = a` 是复制列表

```python
b = a
```

只是增加了一个指向同一列表的变量。

需要复制时：

```python
b = a.copy()
```

### 错误六：混淆 `remove()` 和 `pop()`

```python
a.remove(2)
```

删除值为 `2` 的元素。

```python
a.pop(2)
```

删除索引为 `2` 的元素。

### 错误七：切片方向与步长不匹配

```python
a[1:5:-1]
```

结果为空，因为负步长向左走，但结束位置在右边。

### 错误八：字符串不能直接和数字列表拼接

```python
[1, 2] + "34"
```

会报错。

需要类型相同：

```python
[1, 2] + list("34")
# [1, 2, '3', '4']
```

---

## 二十六、列表核心方法分类记忆

### 增

```text
append()
extend()
insert()
```

### 删

```text
remove()
pop()
clear()
del
```

### 改

```python
a[index] = value
a[start:stop] = values
```

### 查

```text
index()
count()
in
not in
```

### 排序与反转

```text
sort()
reverse()
sorted()
reversed()
```

### 复制

```python
copy()
a[:]
list(a)
```

---

## 二十七、考试常考结论

1. 列表是**有序、可变、允许重复**的序列。
2. 列表索引从 `0` 开始，最后一个元素索引是 `-1`。
3. 切片包含开始位置，不包含结束位置。
4. `append()` 添加一个整体，`extend()` 添加多个元素。
5. `remove()` 按值删除，`pop()` 按索引删除并返回元素。
6. `sort()` 修改原列表，`sorted()` 返回新列表。
7. `reverse()` 修改原列表，没有返回反转后的列表。
8. `b = a` 不会复制列表，两个变量指向同一对象。
9. `copy()`、`[:]`、`list()` 都是浅拷贝。
10. 遍历列表时直接删除元素可能造成元素跳过。
11. 列表可以包含列表，但列表不能作为字典键或集合元素。
12. `[[0] * n] * m` 会造成多个子列表共享同一对象。
13. 单个索引越界会报错，切片越界通常不会报错。
14. 列表比较时，从左向右逐个元素比较。
15. 原地修改列表的方法通常返回 `None`。
