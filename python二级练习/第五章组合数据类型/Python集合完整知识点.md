# Python 集合（set）完整知识点

## 1. 集合是什么

集合 `set` 是 Python 中的一种组合数据类型，用于存储**多个不重复的元素**。

```python
s = {1, 2, 3}
print(s)
```

集合具有四个核心特点：

| 特点 | 说明 |
|---|---|
| 元素不重复 | 相同元素只保留一个 |
| 无序 | 不能依赖集合中元素的排列顺序 |
| 可变 | 可以添加、删除元素 |
| 元素必须可哈希 | 一般要求元素是不可变对象 |

例如：

```python
s = {1, 2, 2, 3, 3, 3}
print(s)
```

结果中每个元素最多出现一次：

```python
{1, 2, 3}
```

---

## 2. 创建集合

### 2.1 使用花括号创建

```python
s = {1, 2, 3}
print(type(s))
```

输出：

```python
<class 'set'>
```

只有一个元素时：

```python
s = {1}
```

注意它和下面几种写法的区别：

```python
a = {1}      # 集合
b = (1)      # 整数
c = (1,)     # 元组
d = [1]      # 列表
```

### 2.2 创建空集合

空集合必须使用：

```python
s = set()
```

不能使用：

```python
s = {}
```

因为 `{}` 表示空字典。

```python
print(type(set()))   # set
print(type({}))      # dict
```

### 2.3 使用 `set()` 创建集合

语法：

```python
set(可迭代对象)
```

`set()` 最多接收一个参数。

#### 由列表创建

```python
s = set([1, 2, 2, 3])
print(s)
```

结果：

```python
{1, 2, 3}
```

#### 由元组创建

```python
s = set((1, 2, 3))
```

#### 由字符串创建

字符串会被拆分成单个字符：

```python
s = set("hello")
print(s)
```

集合中包含：

```python
{'h', 'e', 'l', 'o'}
```

其中重复的 `"l"` 只保留一个。

#### 由 `range` 创建

```python
s = set(range(5))
print(s)
```

结果：

```python
{0, 1, 2, 3, 4}
```

#### 由字典创建

将字典转换为集合时，默认只保留字典的键：

```python
d = {"name": "Tom", "age": 20}

s = set(d)
print(s)
```

集合中是：

```python
{'name', 'age'}
```

需要转换字典的值：

```python
s = set(d.values())
```

需要转换键值对：

```python
s = set(d.items())
```

### 2.4 `set()` 只能接收一个参数

错误写法：

```python
set(1, 2, 3)
```

会产生：

```python
TypeError
```

正确写法：

```python
set([1, 2, 3])
```

---

## 3. 集合元素的要求

### 3.1 集合元素必须可哈希

集合通过哈希机制保存元素，因此集合中的元素必须是可哈希对象。

通常可以简单理解为：

> 集合元素一般必须是不可变对象。

可以作为集合元素的常见类型：

```python
s = {
    10,
    3.14,
    True,
    "Python",
    (1, 2),
    frozenset({3, 4}),
    None
}
```

不能作为集合元素的常见类型：

```python
[1, 2]           # 列表
{"name": "Tom"}  # 字典
{1, 2}           # 普通集合
```

例如：

```python
s = {[1, 2], [3, 4]}
```

会报错：

```python
TypeError: unhashable type: 'list'
```

### 3.2 元组不一定能够作为集合元素

元组本身不可变，但元组内部的所有元素也必须可哈希。

可以：

```python
s = {(1, 2), (3, 4)}
```

不可以：

```python
s = {(1, [2, 3])}
```

因为元组内部包含列表，所以整个元组不可哈希。

### 3.3 集合本身不能嵌套普通集合

错误：

```python
s = {{1, 2}, {3, 4}}
```

因为内部的普通集合是可变对象。

需要使用不可变集合 `frozenset`：

```python
s = {
    frozenset({1, 2}),
    frozenset({3, 4})
}
```

---

## 4. 集合的“不重复”规则

集合判断重复元素时，不仅看类型，还会判断元素是否相等，以及哈希值是否相同。

例如：

```python
s = {1, 1.0, True}
print(s)
```

结果通常只有一个元素：

```python
{1}
```

因为：

```python
1 == 1.0 == True
```

同理：

```python
s = {0, 0.0, False}
print(s)
```

结果通常只有：

```python
{0}
```

所以集合中所谓的“不重复”，本质上是：

> 相等且哈希值相同的元素，会被视为同一个元素。

---

## 5. 集合是无序的

集合没有固定的索引顺序。

```python
s = {"A", "B", "C"}
print(s)
```

输出顺序可能不是创建时的顺序。

因此不能进行索引：

```python
s[0]
```

会报错：

```python
TypeError: 'set' object is not subscriptable
```

集合也不支持切片：

```python
s[1:3]
```

同样会报错。

### “无序”的准确含义

无序不代表每次操作都会随机打乱，而是：

> Python 不保证集合元素按照插入顺序、大小顺序或其他固定顺序排列。

因此不能编写依赖集合顺序的程序。

需要排序时，可以使用：

```python
s = {3, 1, 2}

result = sorted(s)
print(result)
```

结果：

```python
[1, 2, 3]
```

注意：`sorted()` 返回的是列表，不是集合。

---

## 6. 访问和遍历集合

集合没有索引，只能通过遍历访问元素。

```python
s = {"Python", "C", "Java"}

for item in s:
    print(item)
```

可以使用 `enumerate()` 添加计数：

```python
for index, item in enumerate(s):
    print(index, item)
```

但这个 `index` 只是遍历过程中的计数，不是集合真正拥有的固定索引。

---

## 7. 判断元素是否在集合中

使用：

```python
元素 in 集合
元素 not in 集合
```

例如：

```python
s = {10, 20, 30}

print(20 in s)       # True
print(50 in s)       # False
print(50 not in s)   # True
```

集合的成员判断平均效率很高，通常约为：

```text
O(1)
```

因此，当程序需要频繁判断某个元素是否存在时，集合通常比列表更合适。

---

## 8. 添加集合元素

### 8.1 `add()`：添加一个元素

语法：

```python
集合.add(元素)
```

例如：

```python
s = {1, 2}
s.add(3)

print(s)
```

结果：

```python
{1, 2, 3}
```

添加已经存在的元素，不会产生变化，也不会报错：

```python
s.add(2)
```

#### `add()` 添加的是一个整体

```python
s = {1, 2}
s.add((3, 4))

print(s)
```

结果中元组作为一个元素：

```python
{1, 2, (3, 4)}
```

但下面会报错：

```python
s.add([3, 4])
```

因为列表不可哈希。

### 8.2 `update()`：批量添加多个元素

语法：

```python
集合.update(可迭代对象)
```

例如：

```python
s = {1, 2}
s.update([2, 3, 4])

print(s)
```

结果：

```python
{1, 2, 3, 4}
```

#### `update()` 会拆分可迭代对象

```python
s = {1, 2}
s.update((3, 4))
```

会添加 `3` 和 `4` 两个元素。

```python
s = {1, 2}
s.update("abc")
```

会添加三个字符：

```python
'a'
'b'
'c'
```

#### `update()` 可以接收多个可迭代对象

```python
s = {1}

s.update([2, 3], (4, 5), "ab")

print(s)
```

### 8.3 `add()` 和 `update()` 的区别

| 方法 | 作用 | 参数处理 |
|---|---|---|
| `add(x)` | 添加一个元素 | 把参数作为整体 |
| `update(x)` | 批量添加元素 | 遍历并拆分参数 |

例如：

```python
s1 = {1}
s1.add((2, 3))
print(s1)
```

结果：

```python
{1, (2, 3)}
```

而：

```python
s2 = {1}
s2.update((2, 3))
print(s2)
```

结果：

```python
{1, 2, 3}
```

---

## 9. 删除集合元素

### 9.1 `remove()`：删除指定元素

语法：

```python
集合.remove(元素)
```

例如：

```python
s = {1, 2, 3}
s.remove(2)

print(s)
```

如果元素不存在，会报错：

```python
s.remove(100)
```

产生：

```python
KeyError
```

### 9.2 `discard()`：安全删除指定元素

语法：

```python
集合.discard(元素)
```

例如：

```python
s = {1, 2, 3}
s.discard(2)
```

元素不存在时不会报错：

```python
s.discard(100)
```

程序仍然正常运行。

#### `remove()` 和 `discard()` 的区别

| 方法 | 元素存在 | 元素不存在 |
|---|---|---|
| `remove()` | 删除元素 | 抛出 `KeyError` |
| `discard()` | 删除元素 | 什么也不做 |

### 9.3 `pop()`：删除并返回一个元素

```python
s = {10, 20, 30}

x = s.pop()

print(x)
print(s)
```

由于集合无序，所以不能认为 `pop()` 一定删除“第一个”或“最后一个”元素。

准确说法是：

> `pop()` 删除并返回集合中的任意一个元素。

空集合调用 `pop()`：

```python
set().pop()
```

会抛出：

```python
KeyError
```

### 9.4 `clear()`：清空集合

```python
s = {1, 2, 3}
s.clear()

print(s)
```

结果：

```python
set()
```

`clear()` 是修改原集合，而不是创建一个新集合。

### 9.5 `del` 删除整个集合变量

```python
s = {1, 2, 3}
del s
```

此后变量 `s` 不再存在。

注意：

```python
del s[0]
```

不可以，因为集合没有索引。

---

## 10. 集合的四种基本运算

设有两个集合：

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
```

### 10.1 并集

并集表示属于 `A` 或属于 `B` 的所有元素。

使用 `|`：

```python
print(A | B)
```

结果：

```python
{1, 2, 3, 4, 5, 6}
```

使用 `union()`：

```python
print(A.union(B))
```

`union()` 不修改原集合，而是返回新集合。

```python
C = A.union(B)
```

还可以一次合并多个可迭代对象：

```python
C = A.union(B, [7, 8], (9, 10))
```

### 10.2 交集

交集表示同时属于 `A` 和 `B` 的元素。

使用 `&`：

```python
print(A & B)
```

结果：

```python
{3, 4}
```

使用 `intersection()`：

```python
print(A.intersection(B))
```

可以同时求多个集合的交集：

```python
A.intersection(B, C, D)
```

### 10.3 差集

差集 `A - B` 表示：

> 属于 A，但不属于 B 的元素。

```python
print(A - B)
```

结果：

```python
{1, 2}
```

注意差集具有方向性：

```python
print(B - A)
```

结果：

```python
{5, 6}
```

所以：

```python
A - B != B - A
```

方法形式：

```python
A.difference(B)
```

还可以依次减去多个可迭代对象：

```python
A.difference(B, C, D)
```

### 10.4 对称差集

对称差集表示：

> 只属于其中一个集合，但不同时属于两个集合的元素。

使用 `^`：

```python
print(A ^ B)
```

结果：

```python
{1, 2, 5, 6}
```

方法形式：

```python
A.symmetric_difference(B)
```

对称差集可以理解为：

```python
(A - B) | (B - A)
```

也可以表示为：

```python
(A | B) - (A & B)
```

---

## 11. 集合运算总结

| 运算 | 运算符 | 方法 |
|---|---:|---|
| 并集 | `A \| B` | `A.union(B)` |
| 交集 | `A & B` | `A.intersection(B)` |
| 差集 | `A - B` | `A.difference(B)` |
| 对称差集 | `A ^ B` | `A.symmetric_difference(B)` |

数学关系：

```text
并集：A ∪ B
交集：A ∩ B
差集：A - B
对称差集：A △ B
```

---

## 12. 运算符和方法的参数区别

运算符通常要求两边都是集合类型：

```python
{1, 2} & {2, 3}
```

正确。

但：

```python
{1, 2} & [2, 3]
```

会报错，因为右边是列表。

方法通常可以接收任意可迭代对象：

```python
{1, 2}.intersection([2, 3])
```

结果：

```python
{2}
```

因此：

```python
A & B
```

通常要求 `A`、`B` 都是集合。

而：

```python
A.intersection(B)
```

其中 `B` 可以是列表、元组、字符串等可迭代对象。

---

## 13. 原地集合运算

普通集合运算会创建新集合：

```python
A = {1, 2}
B = {2, 3}

C = A | B
```

此时 `A` 不变。

原地运算会直接修改左侧集合。

### 13.1 并集更新 `|=`

```python
A = {1, 2}
B = {2, 3}

A |= B

print(A)
```

结果：

```python
{1, 2, 3}
```

等价于：

```python
A.update(B)
```

### 13.2 交集更新 `&=`

```python
A &= B
```

等价于：

```python
A.intersection_update(B)
```

只保留公共元素。

### 13.3 差集更新 `-=`

```python
A -= B
```

等价于：

```python
A.difference_update(B)
```

删除 `A` 中所有同时存在于 `B` 的元素。

### 13.4 对称差集更新 `^=`

```python
A ^= B
```

等价于：

```python
A.symmetric_difference_update(B)
```

---

## 14. 更新类方法

### 14.1 `intersection_update()`

直接将原集合修改为交集：

```python
A = {1, 2, 3}
B = {2, 3, 4}

A.intersection_update(B)

print(A)
```

结果：

```python
{2, 3}
```

### 14.2 `difference_update()`

直接从原集合中删除指定集合里的元素：

```python
A = {1, 2, 3}
B = {2, 3, 4}

A.difference_update(B)

print(A)
```

结果：

```python
{1}
```

### 14.3 `symmetric_difference_update()`

直接将原集合修改为对称差集：

```python
A = {1, 2, 3}
B = {2, 3, 4}

A.symmetric_difference_update(B)

print(A)
```

结果：

```python
{1, 4}
```

---

## 15. 集合之间的包含关系

### 15.1 子集

如果集合 `A` 中的所有元素都在集合 `B` 中，那么 `A` 是 `B` 的子集。

```python
A = {1, 2}
B = {1, 2, 3}
```

判断方式：

```python
print(A <= B)
print(A.issubset(B))
```

结果：

```python
True
True
```

### 15.2 真子集

真子集要求：

1. `A` 的所有元素都在 `B` 中；
2. `A` 和 `B` 不相等。

```python
print(A < B)
```

结果：

```python
True
```

区别：

```python
A = {1, 2}
B = {1, 2}

print(A <= B)   # True，A 是 B 的子集
print(A < B)    # False，A 不是 B 的真子集
```

任何集合都是自己的子集：

```python
A <= A
```

结果为 `True`。

但集合不是自己的真子集：

```python
A < A
```

结果为 `False`。

### 15.3 超集

如果 `A` 包含 `B` 的所有元素，那么 `A` 是 `B` 的超集。

```python
A = {1, 2, 3}
B = {1, 2}

print(A >= B)
print(A.issuperset(B))
```

结果：

```python
True
True
```

### 15.4 真超集

```python
print(A > B)
```

要求 `A` 包含 `B`，并且两者不相等。

### 15.5 集合关系运算符总结

| 运算 | 含义 |
|---|---|
| `A <= B` | A 是 B 的子集 |
| `A < B` | A 是 B 的真子集 |
| `A >= B` | A 是 B 的超集 |
| `A > B` | A 是 B 的真超集 |
| `A == B` | A 和 B 的元素完全相同 |
| `A != B` | A 和 B 的元素不完全相同 |

注意：集合的 `<` 和 `>` 表示包含关系，不表示按照数值大小比较。

---

## 16. 判断两个集合是否不相交

使用：

```python
A.isdisjoint(B)
```

如果两个集合没有任何公共元素，返回 `True`。

```python
A = {1, 2}
B = {3, 4}

print(A.isdisjoint(B))
```

结果：

```python
True
```

如果存在公共元素：

```python
A = {1, 2}
B = {2, 3}

print(A.isdisjoint(B))
```

结果：

```python
False
```

等价判断：

```python
A & B == set()
```

但 `isdisjoint()` 表达更直接。

---

## 17. 集合的相等判断

集合相等只看元素，不看书写顺序：

```python
A = {1, 2, 3}
B = {3, 2, 1}

print(A == B)
```

结果：

```python
True
```

因为集合本身无序。

---

## 18. 集合推导式

集合推导式和列表推导式类似。

基本格式：

```python
{表达式 for 变量 in 可迭代对象}
```

例如：

```python
s = {x ** 2 for x in range(5)}
print(s)
```

集合中包含：

```python
{0, 1, 4, 9, 16}
```

添加条件：

```python
s = {x for x in range(10) if x % 2 == 0}
```

得到偶数集合：

```python
{0, 2, 4, 6, 8}
```

### 集合推导式会自动去重

```python
s = {x % 3 for x in range(10)}
print(s)
```

结果：

```python
{0, 1, 2}
```

### 和字典推导式的区别

集合推导式：

```python
{x for x in range(5)}
```

字典推导式：

```python
{x: x ** 2 for x in range(5)}
```

关键区别是字典推导式中存在冒号 `:`。

---

## 19. 集合常用内置函数

### 19.1 `len()`

返回集合元素个数：

```python
s = {1, 2, 3}
print(len(s))
```

结果：

```python
3
```

### 19.2 `max()` 和 `min()`

```python
s = {10, 30, 20}

print(max(s))   # 30
print(min(s))   # 10
```

### 19.3 `sum()`

```python
s = {1, 2, 3}

print(sum(s))
```

结果：

```python
6
```

### 19.4 `sorted()`

```python
s = {3, 1, 2}

print(sorted(s))
```

结果：

```python
[1, 2, 3]
```

降序：

```python
sorted(s, reverse=True)
```

### 19.5 `bool()`

空集合转换为布尔值是 `False`：

```python
bool(set())
```

结果：

```python
False
```

非空集合是 `True`：

```python
bool({1, 2})
```

结果：

```python
True
```

所以经常写成：

```python
if s:
    print("集合非空")
else:
    print("集合为空")
```

### 19.6 `list()`、`tuple()`

集合转列表：

```python
s = {1, 2, 3}
lst = list(s)
```

集合转元组：

```python
t = tuple(s)
```

注意转换后的顺序不能依赖集合原本的顺序。

---

## 20. 集合的复制

### 20.1 赋值不是复制

```python
A = {1, 2, 3}
B = A

B.add(4)

print(A)
```

结果：

```python
{1, 2, 3, 4}
```

因为 `A` 和 `B` 指向同一个集合对象。

### 20.2 使用 `copy()`

```python
A = {1, 2, 3}
B = A.copy()

B.add(4)

print(A)   # {1, 2, 3}
print(B)   # {1, 2, 3, 4}
```

也可以：

```python
B = set(A)
```

集合的 `copy()` 属于浅拷贝。

不过由于普通集合不能直接包含列表、字典等可变对象，集合的浅拷贝问题通常没有列表那么常见。

---

## 21. 集合方法完整表

### 21.1 修改原集合的方法

| 方法 | 作用 | 返回值 |
|---|---|---|
| `add(x)` | 添加一个元素 | `None` |
| `update(iterable)` | 批量添加元素 | `None` |
| `remove(x)` | 删除指定元素，不存在则报错 | `None` |
| `discard(x)` | 删除指定元素，不存在不报错 | `None` |
| `pop()` | 删除并返回任意元素 | 被删除的元素 |
| `clear()` | 清空集合 | `None` |
| `intersection_update()` | 原地更新为交集 | `None` |
| `difference_update()` | 原地更新为差集 | `None` |
| `symmetric_difference_update()` | 原地更新为对称差集 | `None` |

注意：

```python
s = {1, 2}
result = s.add(3)

print(result)
```

输出：

```python
None
```

因此不能写：

```python
s = s.add(3)
```

这样会让 `s` 变成 `None`。

### 21.2 返回新集合的方法

| 方法 | 作用 |
|---|---|
| `copy()` | 浅复制集合 |
| `union()` | 返回并集 |
| `intersection()` | 返回交集 |
| `difference()` | 返回差集 |
| `symmetric_difference()` | 返回对称差集 |

### 21.3 判断关系的方法

| 方法 | 返回值 |
|---|---|
| `issubset()` | 是否为子集 |
| `issuperset()` | 是否为超集 |
| `isdisjoint()` | 是否没有公共元素 |

---

## 22. 不可变集合 `frozenset`

普通集合 `set` 是可变的：

```python
s = {1, 2}
s.add(3)
```

`frozenset` 是不可变集合，创建之后不能添加或删除元素。

```python
fs = frozenset([1, 2, 3])
print(fs)
```

输出形式：

```python
frozenset({1, 2, 3})
```

下面这些操作不允许：

```python
fs.add(4)
fs.remove(1)
fs.clear()
```

因为 `frozenset` 没有修改类方法。

### 22.1 `frozenset` 支持的操作

虽然不能修改，但仍然可以进行集合运算：

```python
A = frozenset({1, 2, 3})
B = frozenset({3, 4, 5})

print(A | B)
print(A & B)
print(A - B)
print(A ^ B)
```

也可以判断包含关系：

```python
A <= B
A.isdisjoint(B)
```

### 22.2 `frozenset` 可以作为集合元素

```python
s = {
    frozenset({1, 2}),
    frozenset({3, 4})
}
```

### 22.3 `frozenset` 可以作为字典键

```python
d = {
    frozenset({1, 2}): "A组",
    frozenset({3, 4}): "B组"
}
```

普通集合不能作为字典键：

```python
d = {
    {1, 2}: "A组"
}
```

这会报错。

### 22.4 `set` 和 `frozenset` 对比

| 特点 | `set` | `frozenset` |
|---|---|---|
| 是否可变 | 可变 | 不可变 |
| 可以添加、删除 | 可以 | 不可以 |
| 可以作为字典键 | 不可以 | 可以 |
| 可以作为集合元素 | 不可以 | 可以 |
| 支持集合运算 | 支持 | 支持 |

---

## 23. 集合的常见应用

### 23.1 列表去重

```python
lst = [1, 2, 2, 3, 3, 3]

result = list(set(lst))

print(result)
```

结果中没有重复元素。

但是：

> `list(set(lst))` 不能保证保留原列表顺序。

需要在保留顺序的同时去重，可以使用：

```python
lst = [3, 1, 3, 2, 1]

result = list(dict.fromkeys(lst))

print(result)
```

结果：

```python
[3, 1, 2]
```

### 23.2 判断是否存在重复元素

```python
lst = [1, 2, 3, 2]

if len(lst) == len(set(lst)):
    print("没有重复元素")
else:
    print("存在重复元素")
```

### 23.3 找出两个列表的公共元素

```python
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

common = set(list1) & set(list2)

print(common)
```

结果：

```python
{3, 4}
```

### 23.4 找出两个列表中不同的元素

```python
different = set(list1) ^ set(list2)
```

得到只存在于其中一个列表中的元素。

### 23.5 判断一个列表是否包含另一个列表的全部元素

```python
required = [1, 2]
actual = [1, 2, 3, 4]

result = set(required) <= set(actual)

print(result)
```

结果：

```python
True
```

### 23.6 高效成员查找

```python
allowed_users = {"Tom", "Jack", "Alice"}

name = input("请输入用户名：")

if name in allowed_users:
    print("允许访问")
else:
    print("拒绝访问")
```

当数据量较大且需要反复查找时，集合通常比列表效率高。

---

## 24. 集合的时间复杂度

集合底层主要基于哈希表。

| 操作 | 平均时间复杂度 |
|---|---:|
| `x in s` | `O(1)` |
| `add(x)` | `O(1)` |
| `remove(x)` | `O(1)` |
| `discard(x)` | `O(1)` |
| 遍历集合 | `O(n)` |
| 创建集合 | `O(n)` |
| 并集 | 约 `O(n + m)` |
| 交集 | 通常与较小集合规模相关 |

这里的 `O(1)` 是平均情况，不代表任何情况下都绝对只执行一步。

---

## 25. 集合操作的优先级

集合运算符沿用 Python 原有运算符优先级。

例如：

```python
A | B & C
```

先计算：

```python
B & C
```

再计算：

```python
A | 结果
```

即：

```python
A | (B & C)
```

差集使用减号，减法的优先级又高于 `&`、`^`、`|`。

为了防止理解错误，复杂集合表达式建议主动添加括号：

```python
(A - B) | (C & D)
```

不要过度依赖优先级记忆。

---

## 26. 集合遍历时不能修改集合大小

错误示例：

```python
s = {1, 2, 3, 4}

for x in s:
    if x % 2 == 0:
        s.remove(x)
```

通常会产生：

```python
RuntimeError: Set changed size during iteration
```

原因是遍历集合时，同时改变了集合大小。

### 正确方法一：遍历集合副本

```python
s = {1, 2, 3, 4}

for x in s.copy():
    if x % 2 == 0:
        s.remove(x)

print(s)
```

结果：

```python
{1, 3}
```

### 正确方法二：使用集合推导式

```python
s = {1, 2, 3, 4}

s = {x for x in s if x % 2 != 0}
```

### 正确方法三：使用差集

```python
s = {1, 2, 3, 4}

s -= {x for x in s if x % 2 == 0}
```

---

## 27. 集合和其他组合数据类型的区别

| 特点 | 列表 `list` | 元组 `tuple` | 集合 `set` | 字典 `dict` |
|---|---|---|---|---|
| 是否有序 | 有序 | 有序 | 无序 | 按插入顺序 |
| 是否可变 | 可变 | 不可变 | 可变 | 可变 |
| 是否允许重复 | 允许 | 允许 | 不允许 | 键不允许重复 |
| 是否支持索引 | 支持 | 支持 | 不支持 | 通过键访问 |
| 表示形式 | `[1, 2]` | `(1, 2)` | `{1, 2}` | `{"a": 1}` |
| 主要用途 | 顺序数据 | 固定数据 | 去重、集合运算 | 键值映射 |

---

## 28. 常见易错点

### 易错点一：空集合写成 `{}`

```python
s = {}
```

这是字典，不是集合。

正确：

```python
s = set()
```

### 易错点二：认为集合支持索引

```python
s[0]
```

错误，集合没有索引。

### 易错点三：认为集合保持插入顺序

```python
s = {"A", "B", "C"}
```

不能保证输出顺序一定是：

```python
{'A', 'B', 'C'}
```

### 易错点四：使用 `add()` 添加列表

```python
s.add([1, 2])
```

错误，因为列表不可哈希。

### 易错点五：混淆 `add()` 和 `update()`

```python
s.add("abc")
```

添加一个字符串元素：

```python
"abc"
```

而：

```python
s.update("abc")
```

添加三个字符：

```python
'a'
'b'
'c'
```

### 易错点六：混淆 `remove()` 和 `discard()`

```python
s.remove(x)
```

元素不存在会报错。

```python
s.discard(x)
```

元素不存在不会报错。

### 易错点七：认为 `pop()` 删除最后一个元素

集合没有“最后一个元素”的概念。

```python
s.pop()
```

删除任意一个元素。

### 易错点八：把修改方法的返回值赋给集合

错误：

```python
s = {1, 2}
s = s.add(3)
```

执行后：

```python
s is None
```

正确：

```python
s = {1, 2}
s.add(3)
```

### 易错点九：使用集合去重后还要求保留原顺序

```python
list(set(lst))
```

只能保证去重，不能保证原顺序。

保序去重：

```python
list(dict.fromkeys(lst))
```

### 易错点十：遍历集合时删除元素

```python
for x in s:
    s.remove(x)
```

会改变集合大小，导致运行错误。

应遍历副本：

```python
for x in s.copy():
    s.remove(x)
```

---

## 29. Python 二级考试常见题型

### 题型一：集合自动去重

```python
s = {1, 2, 2, 3}
print(len(s))
```

结果：

```python
3
```

### 题型二：字符串转换为集合

```python
s = set("banana")
print(len(s))
```

不同字符有：

```python
'b', 'a', 'n'
```

所以结果：

```python
3
```

### 题型三：`add()` 和 `update()`

```python
s = {1}
s.add((2, 3))
s.update([4, 5])

print(len(s))
```

集合元素为：

```python
1
(2, 3)
4
5
```

所以长度为：

```python
4
```

### 题型四：集合关系

```python
A = {1, 2}
B = {1, 2, 3}

print(A < B)
print(A <= B)
print(B > A)
```

结果：

```python
True
True
True
```

### 题型五：交集和并集

```python
A = {1, 2, 3}
B = {2, 3, 4}

print(len(A | B))
print(len(A & B))
```

并集：

```python
{1, 2, 3, 4}
```

长度为 `4`。

交集：

```python
{2, 3}
```

长度为 `2`。

### 题型六：集合推导式

```python
s = {x % 4 for x in range(10)}
print(len(s))
```

`x % 4` 只可能得到：

```python
0, 1, 2, 3
```

所以集合长度：

```python
4
```

### 题型七：真假值

```python
s = set()

if s:
    print("A")
else:
    print("B")
```

空集合为假，输出：

```python
B
```

---

## 30. 集合知识框架总结

```text
Python 集合 set
│
├─ 基本特点
│  ├─ 元素不重复
│  ├─ 无序
│  ├─ 集合可变
│  └─ 元素必须可哈希
│
├─ 创建
│  ├─ {1, 2, 3}
│  ├─ set()
│  ├─ set(列表)
│  ├─ set(元组)
│  └─ set(字符串)
│
├─ 添加
│  ├─ add()
│  └─ update()
│
├─ 删除
│  ├─ remove()
│  ├─ discard()
│  ├─ pop()
│  └─ clear()
│
├─ 集合运算
│  ├─ 并集：|
│  ├─ 交集：&
│  ├─ 差集：-
│  └─ 对称差集：^
│
├─ 集合关系
│  ├─ 子集：<=
│  ├─ 真子集：<
│  ├─ 超集：>=
│  ├─ 真超集：>
│  └─ 不相交：isdisjoint()
│
├─ 常用功能
│  ├─ 去重
│  ├─ 成员判断
│  ├─ 寻找公共元素
│  └─ 比较数据差异
│
└─ 不可变集合
   └─ frozenset
```

## 最核心的记忆口诀

```text
集合无序不重复，元素必须能哈希；
单个添加用 add，批量添加用 update；
remove 不在会报错，discard 不在也没事；
并交差对称差，分别是 | & - ^；
普通集合能修改，frozenset 不可变。
```
