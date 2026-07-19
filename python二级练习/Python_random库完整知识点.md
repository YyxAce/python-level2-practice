# Python `random` 库完整知识点

`random` 是 Python 标准库中的**伪随机数模块**，可用于生成随机整数、随机小数、随机抽样、序列洗牌、概率模拟以及各种概率分布随机数。

```python
import random
```

---

## 一、什么是伪随机数

计算机通常不能凭空产生真正的随机数。`random` 模块根据内部状态，通过确定性的算法计算出一系列看起来随机的数字，因此称为：

> 伪随机数（Pseudo-random Number）

Python 的 `random` 模块默认采用 **Mersenne Twister（梅森旋转算法）**作为核心生成器。

主要特点：

- 周期很长，为 `2**19937 - 1`
- 生成速度快
- 适合模拟、抽样、游戏等普通场景
- 不适合密码、验证码、令牌等安全场景

`random.random()` 生成的随机小数范围为：

```text
0.0 <= x < 1.0
```

伪随机序列本质上是确定性计算的结果。因此，给定相同的随机种子和相同的调用顺序，通常可以重新生成相同的随机序列。

官方文档：

- <https://docs.python.org/3/library/random.html>

---

## 二、导入方式

### 1. 导入整个模块

推荐使用：

```python
import random

x = random.randint(1, 10)
```

优点是可以明确看出函数来自 `random` 模块。

### 2. 导入指定函数

```python
from random import randint, choice

x = randint(1, 10)
```

### 3. 导入全部函数

```python
from random import *
```

不推荐，因为容易和自己定义的变量、函数发生命名冲突。

---

## 三、核心函数分类

`random` 模块中的函数可以分为以下几类：

1. 随机种子和状态管理
2. 随机字节
3. 随机整数
4. 随机序列操作
5. 离散概率分布
6. 连续概率分布
7. 独立随机数生成器对象

---

# 第一部分：基础随机数

## 四、`random.random()`：生成 `[0, 1)` 的随机小数

语法：

```python
random.random()
```

返回范围：

```text
0.0 <= x < 1.0
```

示例：

```python
import random

print(random.random())
```

可能输出：

```text
0.7284159203
```

注意：

- 可能生成 `0.0`
- 一定小于 `1.0`
- 不接收任何参数

### 扩展到任意区间

若要生成 `[a, b)` 范围内的随机小数，可以写：

```python
a + (b - a) * random.random()
```

例如生成 `[10, 20)` 的随机小数：

```python
x = 10 + 10 * random.random()
```

实际编程中，一般直接使用 `uniform()`。

---

## 五、`random.uniform()`：生成指定范围的随机小数

语法：

```python
random.uniform(a, b)
```

返回 `a` 和 `b` 之间的随机浮点数。

```python
import random

print(random.uniform(1, 10))
```

大致范围：

```text
1 <= x <= 10
```

也允许 `a > b`：

```python
random.uniform(10, 1)
```

仍然会返回 `1` 和 `10` 之间的随机数。

其底层思想近似为：

```python
a + (b - a) * random.random()
```

由于浮点数舍入问题，右端点 `b` 是否可能出现并没有绝对保证。

---

# 第二部分：随机整数

## 六、`random.randint(a, b)`

语法：

```python
random.randint(a, b)
```

生成闭区间 `[a, b]` 中的随机整数：

```text
a <= x <= b
```

示例：

```python
import random

dice = random.randint(1, 6)
print(dice)
```

`randint(a, b)` 等价于：

```python
random.randrange(a, b + 1)
```

因此左右端点都可能取到。

### 常见误区

```python
random.randint(1, 6)
```

可能生成：

```text
1、2、3、4、5、6
```

不是只到 `5`。

---

## 七、`random.randrange()`

`randrange()` 的规则与 `range()` 基本一致，只是它会从 `range()` 表示的整数范围中随机选取一个数。

### 1. `randrange(stop)`

```python
random.randrange(stop)
```

从以下范围随机选择：

```python
range(stop)
```

示例：

```python
random.randrange(10)
```

可能结果：

```text
0、1、2、3、4、5、6、7、8、9
```

---

### 2. `randrange(start, stop)`

```python
random.randrange(start, stop)
```

候选范围为：

```python
range(start, stop)
```

特点：

- 包含 `start`
- 不包含 `stop`

例如：

```python
random.randrange(5, 10)
```

可能结果：

```text
5、6、7、8、9
```

---

### 3. `randrange(start, stop, step)`

```python
random.randrange(start, stop, step)
```

候选范围和以下代码完全一致：

```python
range(start, stop, step)
```

随机生成 `0～100` 之间的偶数：

```python
x = random.randrange(0, 101, 2)
```

可能结果：

```text
0、2、4、6、……、100
```

随机生成 `1～99` 之间的奇数：

```python
x = random.randrange(1, 100, 2)
```

倒序随机选择：

```python
random.randrange(10, 0, -1)
```

候选值为：

```text
10、9、8、……、1
```

### 注意事项

较新的 Python 版本要求参数是真正的整数，以下写法会报错：

```python
random.randrange(10.0)
```

即使 `10.0` 在数值上等于整数，也不能自动转换。

---

## 八、`random.getrandbits(k)`

语法：

```python
random.getrandbits(k)
```

生成一个具有 `k` 个随机二进制位的非负整数。

例如：

```python
import random

x = random.getrandbits(8)
print(x)
```

8 个二进制位可以表示：

```text
0～255
```

通用范围为：

```text
0 <= x < 2**k
```

示例：

```python
random.getrandbits(4)   # 0～15
random.getrandbits(16)  # 0～65535
random.getrandbits(32)  # 0～2**32 - 1
```

允许：

```python
random.getrandbits(0)
```

结果为：

```python
0
```

---

# 第三部分：序列随机操作

序列包括：

- 字符串
- 列表
- 元组
- `range` 对象

---

## 九、`random.choice(seq)`：随机选择一个元素

语法：

```python
random.choice(seq)
```

从非空序列中随机选择一个元素。

```python
import random

names = ["张三", "李四", "王五"]
name = random.choice(names)

print(name)
```

也可以用于字符串：

```python
random.choice("abcdef")
```

返回一个字符。

也可以用于元组：

```python
random.choice((10, 20, 30))
```

### 空序列错误

```python
random.choice([])
```

会抛出：

```text
IndexError
```

因为空序列中没有元素可以选择。

---

## 十、`random.choices()`：有放回随机抽样

语法：

```python
random.choices(
    population,
    weights=None,
    *,
    cum_weights=None,
    k=1
)
```

从总体中随机选择 `k` 个元素。

特点：

> 有放回抽样，同一个元素可以被多次选中。

示例：

```python
import random

result = random.choices(["A", "B", "C"], k=5)
print(result)
```

可能输出：

```python
['A', 'C', 'A', 'A', 'B']
```

即使默认 `k=1`，返回值也是列表：

```python
result = random.choices(["A", "B", "C"])
print(result)
```

结果形式：

```python
['B']
```

而不是：

```python
'B'
```

---

## 十一、`choices()` 的权重

### 1. 相对权重 `weights`

```python
random.choices(
    ["一等奖", "二等奖", "三等奖"],
    weights=[1, 3, 6],
    k=10
)
```

权重比例为：

```text
一等奖：1 / 10
二等奖：3 / 10
三等奖：6 / 10
```

权重不需要加起来等于 `1` 或 `100`。

以下两组权重效果相同：

```python
weights=[1, 2, 3]
weights=[10, 20, 30]
```

因为比例相同。

### 2. 累计权重 `cum_weights`

```python
random.choices(
    ["A", "B", "C"],
    cum_weights=[1, 4, 10],
    k=5
)
```

累计权重 `[1, 4, 10]` 对应普通权重：

```text
A：1
B：4 - 1 = 3
C：10 - 4 = 6
```

等价于：

```python
weights=[1, 3, 6]
```

### 3. 使用限制

不能同时使用：

```python
weights=
cum_weights=
```

错误示例：

```python
random.choices(
    ["A", "B"],
    weights=[1, 2],
    cum_weights=[1, 3]
)
```

会抛出：

```text
TypeError
```

所有权重都为零也会报错：

```python
random.choices(["A", "B"], weights=[0, 0])
```

权重应当满足：

- 非负
- 有限
- 与总体元素数量相同
- 至少有一个权重大于零

---

## 十二、`choice()` 和 `choices()` 的区别

| 特点 | `choice()` | `choices()` |
|---|---|---|
| 一次选择数量 | 一个 | `k` 个 |
| 返回类型 | 单个元素 | 列表 |
| 是否有放回 | 一次选择无所谓 | 有放回 |
| 是否支持权重 | 不支持 | 支持 |
| 是否可能重复 | 不涉及 | 可能重复 |

示例：

```python
random.choice([1, 2, 3])
```

可能返回：

```python
2
```

而：

```python
random.choices([1, 2, 3], k=3)
```

可能返回：

```python
[2, 2, 1]
```

即使不设置权重，在相同随机种子下，多次调用 `choice()` 与一次调用 `choices()`，也不一定得到相同结果，因为二者内部使用的算法不同。

---

## 十三、`random.shuffle()`：原地打乱列表

语法：

```python
random.shuffle(x)
```

随机打乱可变序列中的元素顺序。

```python
import random

numbers = [1, 2, 3, 4, 5]

random.shuffle(numbers)

print(numbers)
```

可能输出：

```python
[4, 1, 5, 2, 3]
```

### 关键特点：原地修改

`shuffle()` 会直接修改原列表，不会创建并返回一个新列表。

返回值是：

```python
None
```

错误写法：

```python
numbers = [1, 2, 3]

result = random.shuffle(numbers)

print(result)
```

输出：

```python
None
```

正确写法：

```python
random.shuffle(numbers)
print(numbers)
```

### 为什么字符串和元组不能直接打乱

字符串和元组是不可变对象：

```python
random.shuffle("abc")      # 错误
random.shuffle((1, 2, 3))  # 错误
```

可以先转换为列表：

```python
text = "abcdef"

chars = list(text)
random.shuffle(chars)

result = "".join(chars)
print(result)
```

也可以使用：

```python
random.sample(text, k=len(text))
```

生成新的随机排列。

---

## 十四、`random.sample()`：无放回随机抽样

语法：

```python
random.sample(population, k)
```

从总体中随机抽取 `k` 个不同位置的元素。

特点：

> 无放回抽样，同一个位置不会被重复选择。

示例：

```python
import random

numbers = [1, 2, 3, 4, 5]

result = random.sample(numbers, 3)

print(result)
print(numbers)
```

可能输出：

```text
[4, 1, 5]
[1, 2, 3, 4, 5]
```

原序列不会改变。

### `k` 不能超过总体大小

```python
random.sample([1, 2, 3], 4)
```

会抛出：

```text
ValueError
```

### 抽取全部元素：生成随机排列

```python
numbers = [1, 2, 3, 4]

new_numbers = random.sample(numbers, k=len(numbers))
```

会生成一个新的随机排列，原列表保持不变。

### 大范围抽样

推荐直接使用 `range`：

```python
result = random.sample(range(10_000_000), k=60)
```

不需要先创建一个包含一千万个整数的列表，因此更节省内存。

---

## 十五、`sample()` 中的重复元素

`sample()` 保证的是：

> 不重复选择同一个位置。

它并不保证返回值中的数值一定不同。

例如：

```python
population = ["A", "A", "B"]

result = random.sample(population, 2)
```

可能得到：

```python
["A", "A"]
```

因为两个 `"A"` 位于不同位置，属于两个独立候选项。

---

## 十六、`sample()` 的 `counts` 参数

语法：

```python
random.sample(population, k, *, counts=None)
```

`counts` 用于表示每种元素的重复数量。

```python
result = random.sample(
    ["红球", "蓝球"],
    counts=[4, 2],
    k=5
)
```

等价于：

```python
result = random.sample(
    ["红球", "红球", "红球", "红球", "蓝球", "蓝球"],
    k=5
)
```

这样可以避免手动建立包含大量重复元素的列表。

---

## 十七、`sample()` 与集合

较新的 Python 版本中，`sample()` 的总体必须是序列，不能直接传入集合：

```python
s = {1, 2, 3, 4}

random.sample(s, 2)  # TypeError
```

需要先转换：

```python
random.sample(list(s), 2)
```

但集合本身无固定顺序。因此即使设置相同种子，跨环境使用集合转换后的结果，也不适合作为严格复现依据。

---

## 十八、有放回和无放回抽样

假设盒子里有三个球：

```python
balls = ["红", "蓝", "绿"]
```

### 1. 有放回抽样

每次抽完后把球放回：

```python
random.choices(balls, k=5)
```

可能结果：

```python
["红", "红", "蓝", "红", "绿"]
```

同一个元素可以重复出现。

### 2. 无放回抽样

抽完后不放回：

```python
random.sample(balls, k=3)
```

同一个位置不会被重复选择。

核心对应关系：

```text
有放回：choices()
无放回：sample()
```

---

# 第四部分：随机种子和状态

## 十九、`random.seed()`：设置随机种子

语法：

```python
random.seed(a=None, version=2)
```

随机种子决定伪随机数生成器的初始状态。

### 1. 不设置种子

```python
import random

print(random.randint(1, 100))
```

程序每次运行时，通常会得到不同结果。

### 2. 设置固定种子

```python
import random

random.seed(10)

print(random.randint(1, 100))
print(random.randint(1, 100))
print(random.randint(1, 100))
```

每次重新运行程序，通常都会得到相同的随机序列。

需要注意：

> 相同种子得到的是相同的随机序列，不是所有调用都得到同一个数字。

---

## 二十、不要在循环中反复设置同一个种子

错误示例：

```python
import random

for i in range(5):
    random.seed(10)
    print(random.randint(1, 100))
```

每次循环都把生成器恢复到同一个初始状态，所以会连续输出相同的数字。

正确方式：

```python
random.seed(10)

for i in range(5):
    print(random.randint(1, 100))
```

---

## 二十一、可用的种子类型

现代 Python 中，种子可以是：

```text
None
int
float
str
bytes
bytearray
```

例如：

```python
random.seed(100)
random.seed("Python")
random.seed(b"Python")
```

较新的 Python 版本不再允许任意可哈希对象作为种子。

---

## 二十二、默认种子

```python
random.seed()
```

等价于：

```python
random.seed(None)
```

Python 会优先使用操作系统提供的随机源；无法使用时，才会参考当前系统时间。

---

## 二十三、`version` 参数

```python
random.seed(a, version=2)
```

通常保持默认值 `2` 即可。

```python
random.seed("Python", version=2)
```

`version=1` 主要用于复现旧版本 Python 对字符串或字节种子的随机序列，新程序一般不使用。

---

## 二十四、随机状态管理

### 1. `getstate()`

```python
state = random.getstate()
```

保存当前随机数生成器的内部状态。

### 2. `setstate()`

```python
random.setstate(state)
```

恢复之前保存的状态。

示例：

```python
import random

random.seed(100)

print(random.randint(1, 100))

state = random.getstate()

print(random.randint(1, 100))
print(random.randint(1, 100))

random.setstate(state)

print(random.randint(1, 100))
print(random.randint(1, 100))
```

恢复状态后，后面的两个数字会重新生成一次。

可以把它理解为：

```text
随机生成器内部有一个“进度”
getstate() 保存进度
setstate() 恢复进度
```

---

# 第五部分：随机字节和概率分布

## 二十五、`random.randbytes(n)`

语法：

```python
random.randbytes(n)
```

生成长度为 `n` 的随机字节对象。

```python
import random

data = random.randbytes(8)

print(data)
print(type(data))
```

返回类型为：

```python
bytes
```

注意：

```python
random.randbytes()
```

不适合用于生成安全令牌、密码或验证码。

安全场景应使用：

```python
import secrets

secrets.token_bytes()
```

---

## 二十六、`random.binomialvariate()`

较新的 Python 版本提供：

```python
random.binomialvariate(n=1, p=0.5)
```

表示进行 `n` 次相互独立的试验，每次成功概率为 `p`，返回最终成功的次数。

例如抛硬币 10 次，正面概率为 `0.5`：

```python
import random

heads = random.binomialvariate(n=10, p=0.5)

print(heads)
```

返回范围：

```text
0 <= heads <= 10
```

数学思想近似为：

```python
sum(random.random() < 0.5 for _ in range(10))
```

参数要求：

```text
n 是非负整数
0 <= p <= 1
```

---

# 第六部分：连续概率分布函数

这些函数主要用于概率统计、数学建模、仿真和蒙特卡洛模拟。

## 二十七、均匀分布

```python
random.uniform(a, b)
```

区间内各位置具有相同概率密度。

```python
x = random.uniform(0, 100)
```

---

## 二十八、三角分布

语法：

```python
random.triangular(low, high, mode)
```

参数：

- `low`：最小值，默认 `0`
- `high`：最大值，默认 `1`
- `mode`：最可能出现的位置，默认区间中点

示例：

```python
x = random.triangular(0, 100, 70)
```

含义：

- 结果范围为 `0～100`
- `70` 附近出现的概率最高

适合只有最小值、最大值和最可能值的简单估计模型。

---

## 二十九、正态分布：`gauss()`

语法：

```python
random.gauss(mu=0.0, sigma=1.0)
```

参数：

- `mu`：均值
- `sigma`：标准差

标准正态分布：

```python
x = random.gauss(0, 1)
```

例如模拟平均身高为 `170`、标准差为 `6`：

```python
height = random.gauss(170, 6)
```

`gauss()` 通常比 `normalvariate()` 略快。

在多线程共享同一个随机生成器时，`gauss()` 需要注意缓存问题。可以让每个线程使用独立的 `Random` 实例，或者改用 `normalvariate()`。

---

## 三十、正态分布：`normalvariate()`

语法：

```python
random.normalvariate(mu=0.0, sigma=1.0)
```

示例：

```python
x = random.normalvariate(100, 15)
```

与 `gauss()` 的主要区别：

| 特点 | `gauss()` | `normalvariate()` |
|---|---|---|
| 分布 | 正态分布 | 正态分布 |
| 速度 | 略快 | 略慢 |
| 多线程共享调用 | 需注意缓存问题 | 更稳妥 |

---

## 三十一、对数正态分布

语法：

```python
random.lognormvariate(mu, sigma)
```

如果随机变量 `X` 服从对数正态分布，那么：

```text
ln(X)
```

服从均值为 `mu`、标准差为 `sigma` 的正态分布。

示例：

```python
x = random.lognormvariate(0, 1)
```

通常要求：

```text
sigma > 0
```

---

## 三十二、指数分布

语法：

```python
random.expovariate(lambd=1.0)
```

通常用于模拟：

- 顾客到达时间间隔
- 设备故障间隔
- 电话呼入间隔
- 排队系统事件间隔

其中：

```text
lambd = 1 / 平均值
```

假设平均每 5 秒到达一个顾客：

```python
interval = random.expovariate(1 / 5)
```

当：

```text
lambd > 0
```

结果范围为：

```text
0～正无穷
```

`lambd` 不能为 `0`。

---

## 三十三、Gamma 分布

语法：

```python
random.gammavariate(alpha, beta)
```

参数：

- `alpha`：形状参数
- `beta`：尺度参数

要求：

```text
alpha > 0
beta > 0
```

常用于：

- 等待时间
- 寿命分析
- 降雨量
- 排队模型

注意：这里的 Gamma 分布不是数学中的 Gamma 函数。

---

## 三十四、Beta 分布

语法：

```python
random.betavariate(alpha, beta)
```

返回范围：

```text
0～1
```

要求：

```text
alpha > 0
beta > 0
```

常用于描述：

- 比例
- 概率
- 成功率
- 转化率

示例：

```python
p = random.betavariate(2, 5)
```

---

## 三十五、冯·米塞斯分布

语法：

```python
random.vonmisesvariate(mu, kappa)
```

主要用于圆周方向数据。

参数：

- `mu`：平均角度，使用弧度
- `kappa`：集中程度，要求 `kappa >= 0`

当：

```python
kappa == 0
```

结果相当于在 `0～2π` 范围内均匀选择角度。

适用于：

- 风向
- 朝向
- 圆周运动
- 动物迁徙方向

---

## 三十六、Pareto 分布

语法：

```python
random.paretovariate(alpha)
```

`alpha` 是形状参数。

常用于描述少数占据多数的长尾现象，例如：

- 财富分布
- 文件大小
- 城市人口
- 网络流量

---

## 三十七、Weibull 分布

语法：

```python
random.weibullvariate(alpha, beta)
```

参数：

- `alpha`：尺度参数
- `beta`：形状参数

常用于：

- 设备可靠性
- 元件寿命
- 故障时间
- 生存分析

---

## 三十八、概率分布函数总结

| 函数 | 分布 | 主要参数 | 常见用途 |
|---|---|---|---|
| `random()` | `[0,1)` 均匀分布 | 无 | 基础随机小数 |
| `uniform()` | 区间均匀分布 | `a, b` | 区间随机值 |
| `triangular()` | 三角分布 | 最小值、最大值、众数 | 项目估计 |
| `binomialvariate()` | 二项分布 | 次数、成功概率 | 多次独立试验 |
| `gauss()` | 正态分布 | 均值、标准差 | 自然测量数据 |
| `normalvariate()` | 正态分布 | 均值、标准差 | 多线程场景 |
| `lognormvariate()` | 对数正态分布 | `mu, sigma` | 收入、价格等 |
| `expovariate()` | 指数分布 | 发生率 | 到达间隔 |
| `gammavariate()` | Gamma 分布 | 形状、尺度 | 等待时间 |
| `betavariate()` | Beta 分布 | `alpha, beta` | 概率、比例 |
| `vonmisesvariate()` | 圆周分布 | 均值角、集中度 | 方向数据 |
| `paretovariate()` | Pareto 分布 | 形状参数 | 长尾数据 |
| `weibullvariate()` | Weibull 分布 | 尺度、形状 | 寿命分析 |

---

# 第七部分：随机生成器对象

## 三十九、独立随机数生成器 `Random`

模块中的普通函数实际上使用一个隐藏的全局 `Random` 对象。

例如：

```python
random.randint(1, 10)
```

本质上相当于调用全局随机生成器对象的方法。

也可以自己创建独立生成器：

```python
import random

r1 = random.Random(100)
r2 = random.Random(200)

print(r1.randint(1, 10))
print(r2.randint(1, 10))
```

两个生成器各自拥有独立状态，互不影响。

```python
r1 = random.Random(10)
r2 = random.Random(10)

print(r1.randint(1, 100))
print(r2.randint(1, 100))
```

因为种子相同，二者会生成相同的随机序列。

适用场景：

- 不同模拟任务需要独立随机序列
- 多线程中每个线程使用自己的生成器
- 不希望修改全局随机状态
- 单元测试需要稳定复现

---

## 四十、`SystemRandom`

语法：

```python
random.SystemRandom()
```

它使用操作系统提供的随机源，而不是普通的 Mersenne Twister 状态。

```python
import random

secure_random = random.SystemRandom()

print(secure_random.randint(1, 100))
```

特点：

- 使用操作系统随机源
- 序列不可通过固定种子复现
- `seed()` 没有实际效果
- `getstate()` 和 `setstate()` 不可用

```python
r = random.SystemRandom()

r.seed(100)   # 没有实际作用
r.getstate()  # NotImplementedError
```

安全相关代码通常更推荐直接使用：

```python
import secrets
```

---

# 第八部分：安全随机数

## 四十一、`random` 与 `secrets` 的区别

### 普通随机场景

使用：

```python
random
```

适用于：

- 游戏随机事件
- 随机抽样
- 洗牌
- 数学模拟
- 测试数据
- 蒙特卡洛方法

### 安全随机场景

使用：

```python
secrets
```

适用于：

- 密码
- 验证码
- 重置令牌
- 会话密钥
- API Token
- 邀请码

错误示例：

```python
password = "".join(
    random.choices("abcdefghijklmnopqrstuvwxyz0123456789", k=16)
)
```

这种方法不适合生成真正的安全密码。

更合适的写法：

```python
import secrets
import string

chars = string.ascii_letters + string.digits
password = "".join(secrets.choice(chars) for _ in range(16))
```

---

# 第九部分：常见编程案例

## 四十二、模拟掷骰子

```python
import random

dice = random.randint(1, 6)
print(dice)
```

---

## 四十三、模拟抛硬币

```python
import random

result = random.choice(["正面", "反面"])
print(result)
```

也可以写成：

```python
if random.random() < 0.5:
    print("正面")
else:
    print("反面")
```

---

## 四十四、按概率执行事件

假设事件有 `30%` 的概率发生：

```python
import random

if random.random() < 0.3:
    print("事件发生")
else:
    print("事件没有发生")
```

原理：

```text
random.random() 均匀生成 [0,1) 中的小数
落入 [0,0.3) 的概率约为 30%
```

---

## 四十五、生成随机验证码

普通练习场景：

```python
import random
import string

characters = string.ascii_uppercase + string.digits

code = "".join(random.choices(characters, k=6))

print(code)
```

真正的安全验证码应改用 `secrets`。

---

## 四十六、随机点名

```python
import random

students = ["张三", "李四", "王五", "赵六"]

student = random.choice(students)

print(student)
```

---

## 四十七、随机抽取多名学生且不重复

```python
import random

students = ["张三", "李四", "王五", "赵六", "孙七"]

selected = random.sample(students, k=3)

print(selected)
```

---

## 四十八、随机打乱题目

```python
import random

questions = ["题目1", "题目2", "题目3", "题目4"]

random.shuffle(questions)

for question in questions:
    print(question)
```

---

## 四十九、生成随机 RGB 颜色

```python
import random

r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)

print(r, g, b)
```

生成十六进制颜色：

```python
color = "#{:02X}{:02X}{:02X}".format(r, g, b)
print(color)
```

---

## 五十、生成不重复随机整数

从 `1～100` 中随机选择 10 个不同整数：

```python
numbers = random.sample(range(1, 101), k=10)
```

不应使用：

```python
random.choices(range(1, 101), k=10)
```

因为 `choices()` 可能产生重复数字。

---

## 五十一、加权抽奖

```python
import random

prize = random.choices(
    ["一等奖", "二等奖", "三等奖", "未中奖"],
    weights=[1, 5, 20, 74],
    k=1
)[0]

print(prize)
```

使用 `[0]` 是因为 `choices()` 返回列表。

---

## 五十二、模拟多次掷骰子

```python
import random

counts = [0] * 6

for _ in range(10000):
    dice = random.randint(1, 6)
    counts[dice - 1] += 1

for number, count in enumerate(counts, start=1):
    print(number, count)
```

试验次数足够多时，每个点数出现次数大约接近：

```text
10000 / 6
```

但不一定完全相等。

---

## 五十三、蒙特卡洛估算圆周率

```python
import random

inside = 0
total = 1_000_000

for _ in range(total):
    x = random.random()
    y = random.random()

    if x * x + y * y <= 1:
        inside += 1

pi = 4 * inside / total

print(pi)
```

原理：

```text
四分之一圆面积 / 正方形面积 = π / 4
```

所以：

```text
π ≈ 4 × 落入圆内的点数 / 总点数
```

---

# 第十部分：常见错误与易错点

## 五十四、混淆 `randint()` 和 `randrange()`

```python
random.randint(1, 10)
```

范围：

```text
1～10
```

而：

```python
random.randrange(1, 10)
```

范围：

```text
1～9
```

---

## 五十五、认为 `shuffle()` 会返回新列表

错误：

```python
new_list = random.shuffle(old_list)
```

此时：

```python
new_list is None
```

正确：

```python
random.shuffle(old_list)
```

或者：

```python
new_list = random.sample(old_list, len(old_list))
```

---

## 五十六、混淆 `choice()` 和 `choices()`

```python
random.choice(data)
```

返回单个元素。

```python
random.choices(data, k=1)
```

返回只包含一个元素的列表。

---

## 五十七、混淆有放回和无放回

```python
random.choices(data, k=5)
```

可能重复。

```python
random.sample(data, k=5)
```

不会重复选择同一个位置。

---

## 五十八、`sample()` 的 `k` 过大

```python
random.sample([1, 2, 3], 4)
```

会抛出：

```text
ValueError
```

---

## 五十九、对不可变对象使用 `shuffle()`

```python
random.shuffle("abc")
random.shuffle((1, 2, 3))
```

都会失败，因为字符串和元组不能原地修改。

---

## 六十、把随机种子理解成随机结果

```python
random.seed(10)
```

`10` 不是接下来一定生成的数字，而是随机生成器的初始条件。

---

## 六十一、在循环中反复设置相同种子

```python
for _ in range(10):
    random.seed(100)
    print(random.randint(1, 10))
```

会反复得到相同结果。

---

## 六十二、使用 `random` 生成安全密码

`random` 是确定性的伪随机生成器，不适合安全用途。

应当使用：

```python
secrets
```

---

## 六十三、误认为随机结果短期内一定平均

随机抛十次硬币，完全可能出现连续八次正面。

随机性表示每次试验遵循对应概率，并不表示短期结果一定平均。

试验次数越多，统计频率才越可能接近理论概率。

---

# 第十一部分：底层原理

## 六十四、随机生成器是“有状态”的

假设执行：

```python
random.seed(100)
```

随机生成器内部形成初始状态：

```text
状态 S₀
```

第一次调用：

```python
random.random()
```

可以理解为：

```text
根据 S₀ 生成输出 X₁
同时更新为状态 S₁
```

第二次调用：

```text
根据 S₁ 生成输出 X₂
同时更新为状态 S₂
```

整体过程：

```text
S₀ → X₁ → S₁ → X₂ → S₂ → X₃ → S₃
```

因此：

- 相同种子意味着相同初始状态
- 相同初始状态和相同调用顺序意味着相同随机序列
- 中途多调用一次随机函数，后续所有结果都可能改变
- 随机生成器本质上是一个有内部状态的对象

示例：

```python
random.seed(10)

a = random.randint(1, 100)
b = random.randint(1, 100)
```

与：

```python
random.seed(10)

a = random.randint(1, 100)
random.random()  # 中间多调用了一次
b = random.randint(1, 100)
```

其中的 `b` 通常不同，因为第二段代码的随机状态多向前推进了一次。

---

## 六十五、随机序列的可复现性

固定种子常用于：

- 调试程序
- 单元测试
- 数据分析实验
- 机器学习实验
- 数学建模
- 科研结果复现

示例：

```python
import random

random.seed(42)

data = [random.randint(1, 100) for _ in range(10)]

print(data)
```

注意：

- 相同 Python 版本、相同调用顺序下通常可以复现
- 不同随机函数内部算法可能随 Python 版本变化
- 中间多调用一次随机函数，后续序列就会发生变化
- 多线程调用时，实际调用顺序可能不稳定

---

## 六十六、线程安全

Python 官方实现中的全局随机生成器和 `Random` 实例通常是线程安全的。

但多个线程同时调用同一个生成器时，可能产生锁竞争，影响性能。

大量并发随机数生成时，更适合让每个线程使用自己的 `Random` 实例：

```python
import random

generator = random.Random(100)
```

每个线程分别创建自己的生成器对象。

---

# 第十二部分：核心总结

## 六十七、核心函数速查表

| 函数 | 作用 | 是否可能重复 | 是否修改原对象 |
|---|---|---:|---:|
| `random()` | 生成 `[0,1)` 随机小数 | — | 否 |
| `uniform(a, b)` | 生成区间随机小数 | — | 否 |
| `randint(a, b)` | 生成 `[a,b]` 随机整数 | — | 否 |
| `randrange()` | 从 `range()` 中随机选择 | — | 否 |
| `getrandbits(k)` | 生成 `k` 位随机整数 | — | 否 |
| `choice(seq)` | 随机选择一个元素 | — | 否 |
| `choices(seq, k=n)` | 有放回抽取多个元素 | 是 | 否 |
| `sample(seq, k=n)` | 无放回抽取多个位置 | 否 | 否 |
| `shuffle(list)` | 原地随机打乱列表 | — | 是 |
| `seed()` | 设置随机种子 | — | 修改生成器状态 |
| `getstate()` | 保存随机状态 | — | 否 |
| `setstate()` | 恢复随机状态 | — | 修改生成器状态 |
| `randbytes(n)` | 生成随机字节 | — | 否 |
| `binomialvariate()` | 生成二项分布随机变量 | — | 否 |

---

## 六十八、必须重点掌握的函数

学习和考试中，优先掌握：

```python
random.random()
random.uniform()
random.randint()
random.randrange()
random.choice()
random.choices()
random.sample()
random.shuffle()
random.seed()
```

---

## 六十九、必须重点区分

```text
randint(a, b)       包含 b
randrange(a, b)     不包含 b

choice()            返回一个元素
choices()           返回列表，有放回
sample()            返回列表，无放回

shuffle()           修改原列表，返回 None
sample()            不修改原序列，返回新列表

random              普通随机和模拟
secrets             安全随机
```

---

## 七十、最终记忆框架

```text
随机小数：random、uniform
随机整数：randint、randrange
随机选一个：choice
有放回抽多个：choices
无放回抽多个：sample
原地打乱：shuffle
固定随机序列：seed
保存状态：getstate
恢复状态：setstate
安全随机：secrets
```
