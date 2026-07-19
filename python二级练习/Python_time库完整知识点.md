# Python `time` 库完整知识点

> `time` 是 Python 标准库中用于处理**时间戳、时间转换、程序暂停和性能计时**的模块。

```python
import time
```

它主要适合：

- 获取当前时间戳
- 时间戳与本地时间、UTC 时间互相转换
- 格式化和解析时间字符串
- 暂停程序
- 测量程序运行时间和 CPU 时间

涉及日期加减、月份变化、复杂时区等操作时，通常使用 `datetime` 和 `zoneinfo` 更合适。

---

## 一、时间的三种表示形式

`time` 库主要使用三种时间表示形式：

1. 时间戳
2. 时间元组 `struct_time`
3. 格式化时间字符串

---

## 二、时间戳 `timestamp`

时间戳表示某个时刻距离 Unix 纪元的秒数。

Unix 纪元为：

```text
1970-01-01 00:00:00 UTC
```

获取当前时间戳：

```python
import time

timestamp = time.time()
print(timestamp)
```

可能输出：

```text
1784347200.123456
```

特点：

- 类型通常是 `float`
- 整数部分表示秒
- 小数部分表示不足一秒的部分
- 时间戳表示一个绝对时刻
- 时间戳本身不直接包含年月日
- 时间戳本身不属于某个特定时区

### 1. `time.time()`

获取当前时间戳，单位为秒。

```python
import time

now = time.time()

print(now)
print(type(now))
```

输出类型：

```text
<class 'float'>
```

### 2. `time.time_ns()`

获取当前时间戳，单位为纳秒，返回整数。

```python
import time

now_ns = time.time_ns()

print(now_ns)
print(type(now_ns))
```

换算关系：

```text
1 秒 = 1000 毫秒
1 秒 = 1,000,000 微秒
1 秒 = 1,000,000,000 纳秒
```

将纳秒时间戳转换为秒：

```python
seconds = time.time_ns() / 1_000_000_000
```

---

## 三、时间元组 `struct_time`

`struct_time` 是一种包含年月日、时分秒等信息的时间对象。

```python
import time

t = time.localtime()
print(t)
```

可能输出：

```text
time.struct_time(
    tm_year=2026,
    tm_mon=7,
    tm_mday=18,
    tm_hour=12,
    tm_min=30,
    tm_sec=45,
    tm_wday=5,
    tm_yday=199,
    tm_isdst=0
)
```

`struct_time` 同时具有：

- 元组特性：可以使用下标访问
- 对象特性：可以使用属性名访问

```python
print(t[0])
print(t.tm_year)
```

两种方式都能得到年份。

### `struct_time` 的核心字段

| 下标 | 属性 | 含义 | 取值范围 |
|---:|---|---|---|
| 0 | `tm_year` | 年份 | 如 `2026` |
| 1 | `tm_mon` | 月份 | `1~12` |
| 2 | `tm_mday` | 一个月中的第几天 | `1~31` |
| 3 | `tm_hour` | 小时 | `0~23` |
| 4 | `tm_min` | 分钟 | `0~59` |
| 5 | `tm_sec` | 秒 | 通常 `0~61` |
| 6 | `tm_wday` | 星期几 | `0~6`，星期一为 `0` |
| 7 | `tm_yday` | 一年中的第几天 | `1~366` |
| 8 | `tm_isdst` | 是否采用夏令时 | `1`、`0` 或 `-1` |

`tm_isdst` 的含义：

```text
1：处于夏令时
0：不处于夏令时
-1：未知，由系统判断
```

部分平台还提供：

```python
t.tm_zone       # 时区名称
t.tm_gmtoff     # 相对 UTC 的偏移秒数
```

---

## 四、格式化时间字符串

人们通常使用字符串表示时间：

```text
2026-07-18 12:30:45
```

可以使用 `strftime()` 将时间对象转换为字符串：

```python
import time

result = time.strftime("%Y-%m-%d %H:%M:%S")
print(result)
```

---

## 五、三种形式之间的转换关系

```text
时间戳
  │
  ├── localtime() ──→ 本地时间 struct_time
  ├── gmtime() ─────→ UTC 时间 struct_time
  └── ctime() ──────→ 本地时间字符串

struct_time
  │
  ├── mktime() ─────→ 时间戳
  ├── strftime() ───→ 格式化字符串
  └── asctime() ────→ 固定格式字符串

格式化字符串
  │
  └── strptime() ───→ struct_time
```

这是整个 `time` 库最核心的知识结构。

---

# 六、时间戳转换为时间元组

## 1. `time.localtime()`

把时间戳转换为当前计算机所在时区的本地时间。

语法：

```python
time.localtime([seconds])
```

不传参数时，使用当前时间戳：

```python
import time

t = time.localtime()
print(t)
```

传入指定时间戳：

```python
print(time.localtime(0))
```

结果会受到当前计算机时区设置的影响。

---

## 2. `time.gmtime()`

把时间戳转换为 UTC 时间。

语法：

```python
time.gmtime([seconds])
```

示例：

```python
import time

t = time.gmtime()
print(t)
```

比较本地时间和 UTC 时间：

```python
import time

timestamp = time.time()

print("本地时间：", time.localtime(timestamp))
print("UTC 时间：", time.gmtime(timestamp))
```

对于中国、新加坡等 UTC+8 地区，本地时间通常比 UTC 时间快 8 小时。

### `localtime()` 和 `gmtime()` 的区别

| 函数 | 转换结果 |
|---|---|
| `localtime()` | 当前计算机设置的本地时间 |
| `gmtime()` | UTC 时间 |

它们接收的是同一个时间戳，表示的是同一个绝对时刻，只是显示时采用的时区不同。

---

# 七、时间元组转换为时间戳

## `time.mktime()`

把表示**本地时间**的 `struct_time` 或九元素元组转换为时间戳。

语法：

```python
time.mktime(tuple)
```

示例：

```python
import time

t = (2026, 7, 18, 12, 30, 0, 5, 199, -1)

timestamp = time.mktime(t)
print(timestamp)
```

常见写法：

```python
local_time = time.localtime()
timestamp = time.mktime(local_time)
```

转换关系：

```python
timestamp = time.time()

result = time.mktime(time.localtime(timestamp))
```

结果通常接近原来的时间戳。

### 重要注意

`mktime()` 会把参数当作本地时间。

因此下面这种写法通常不正确：

```python
time.mktime(time.gmtime())
```

原因：

- `gmtime()` 返回 UTC 时间
- `mktime()` 却会把它当成本地时间
- 最终可能产生时区偏差

UTC 时间元组转时间戳可以使用：

```python
import calendar

timestamp = calendar.timegm(utc_struct_time)
```

---

# 八、时间转换为字符串

## 1. `time.ctime()`

把时间戳转换为固定格式的本地时间字符串。

语法：

```python
time.ctime([seconds])
```

示例：

```python
import time

print(time.ctime())
```

可能输出：

```text
Sat Jul 18 12:30:45 2026
```

传入指定时间戳：

```python
print(time.ctime(0))
```

它大致等价于：

```python
time.asctime(time.localtime(seconds))
```

特点：

- 格式固定
- 使用本地时间
- 不适合自定义显示格式
- 适合快速查看时间戳

---

## 2. `time.asctime()`

把时间元组转换为固定格式字符串。

语法：

```python
time.asctime([tuple])
```

示例：

```python
import time

t = time.localtime()
result = time.asctime(t)

print(result)
```

不传参数时使用当前本地时间：

```python
print(time.asctime())
```

`ctime()` 和 `asctime()` 的区别：

```text
ctime()：主要接收时间戳
asctime()：主要接收 struct_time
```

---

## 3. `time.strftime()`

把时间元组格式化为指定格式的字符串。

`strftime` 可以理解为：

```text
string format time
字符串格式化时间
```

语法：

```python
time.strftime(format[, tuple])
```

示例：

```python
import time

t = time.localtime()

result = time.strftime("%Y-%m-%d %H:%M:%S", t)
print(result)
```

不传第二个参数时，使用当前本地时间：

```python
print(time.strftime("%Y-%m-%d"))
```

---

# 九、常用时间格式化符号

## 1. 年月日

| 格式符 | 含义 | 示例 |
|---|---|---|
| `%Y` | 四位年份 | `2026` |
| `%y` | 两位年份 | `26` |
| `%m` | 月份 | `07` |
| `%d` | 一个月中的第几天 | `18` |
| `%j` | 一年中的第几天 | `199` |

示例：

```python
time.strftime("%Y年%m月%d日")
```

可能输出：

```text
2026年07月18日
```

---

## 2. 时分秒

| 格式符 | 含义 | 示例 |
|---|---|---|
| `%H` | 24 小时制小时 | `00~23` |
| `%I` | 12 小时制小时 | `01~12` |
| `%M` | 分钟 | `00~59` |
| `%S` | 秒 | `00~61` |
| `%p` | 上午或下午标志 | `AM`、`PM` |

24 小时制：

```python
time.strftime("%H:%M:%S")
```

12 小时制：

```python
time.strftime("%I:%M:%S %p")
```

`%p` 通常配合 `%I` 使用。

---

## 3. 星期

| 格式符 | 含义 |
|---|---|
| `%a` | 星期名称缩写 |
| `%A` | 星期完整名称 |
| `%w` | 星期数字，星期日为 `0` |
| `%u` | ISO 星期数字，星期一为 `1` |

示例：

```python
time.strftime("%A")
```

可能输出：

```text
Saturday
```

注意三个不同规则：

```text
struct_time.tm_wday：星期一是 0
strftime("%w")：星期日是 0
strftime("%u")：星期一是 1
```

---

## 4. 月份名称

| 格式符 | 含义 |
|---|---|
| `%b` | 月份名称缩写 |
| `%B` | 月份完整名称 |

```python
time.strftime("%B")
```

可能输出：

```text
July
```

---

## 5. 星期编号

| 格式符 | 含义 |
|---|---|
| `%U` | 以星期日为一周第一天的周数 |
| `%W` | 以星期一为一周第一天的周数 |
| `%V` | ISO 8601 周数 |

对于 `%U` 和 `%W`，第一周开始前的日期属于第 `00` 周。

---

## 6. 本地化和时区格式

| 格式符 | 含义 |
|---|---|
| `%c` | 本地日期和时间 |
| `%x` | 本地日期 |
| `%X` | 本地时间 |
| `%Z` | 时区名称 |
| `%z` | UTC 偏移量 |
| `%%` | 普通百分号 `%` |

示例：

```python
print(time.strftime("%c"))
print(time.strftime("%x"))
print(time.strftime("%X"))
print(time.strftime("%Z"))
print(time.strftime("%z"))
```

这些格式的表现可能受到操作系统和语言区域设置影响。

---

## 7. 常用格式模板

```python
# 标准日期
"%Y-%m-%d"

# 标准时间
"%H:%M:%S"

# 日期和时间
"%Y-%m-%d %H:%M:%S"

# 中文日期
"%Y年%m月%d日"

# 文件名时间
"%Y%m%d_%H%M%S"

# 斜杠日期
"%Y/%m/%d"

# 12 小时制
"%Y-%m-%d %I:%M:%S %p"
```

生成带时间的文件名：

```python
filename = time.strftime("report_%Y%m%d_%H%M%S.txt")
print(filename)
```

可能输出：

```text
report_20260718_123045.txt
```

---

# 十、字符串转换为时间对象

## `time.strptime()`

把符合指定格式的字符串解析为 `struct_time`。

`strptime` 可以理解为：

```text
string parse time
字符串解析为时间
```

语法：

```python
time.strptime(string, format)
```

示例：

```python
import time

text = "2026-07-18 12:30:45"

t = time.strptime(text, "%Y-%m-%d %H:%M:%S")
print(t)
```

进一步转换为时间戳：

```python
timestamp = time.mktime(t)
print(timestamp)
```

完整过程：

```text
字符串
  ↓ strptime()
struct_time
  ↓ mktime()
时间戳
```

---

## 格式必须与字符串对应

正确：

```python
time.strptime("2026-07-18", "%Y-%m-%d")
```

错误：

```python
time.strptime("2026/07/18", "%Y-%m-%d")
```

会抛出：

```text
ValueError
```

原因是字符串中的 `/` 与格式中的 `-` 不一致。

异常处理：

```python
import time

text = input("请输入日期：")

try:
    t = time.strptime(text, "%Y-%m-%d")
    print("解析成功：", t)
except ValueError:
    print("日期格式错误，应为 YYYY-MM-DD")
```

---

## `strftime()` 与 `strptime()` 对比

| 函数 | 转换方向 |
|---|---|
| `strftime()` | 时间对象 → 字符串 |
| `strptime()` | 字符串 → 时间对象 |

记忆方法：

```text
f = format：格式化输出
p = parse：解析输入
```

---

# 十一、程序暂停

## `time.sleep()`

让当前线程暂停指定秒数。

语法：

```python
time.sleep(seconds)
```

示例：

```python
import time

print("开始")
time.sleep(2)
print("两秒后执行")
```

参数可以是小数：

```python
time.sleep(0.5)
```

表示暂停约 0.5 秒。

倒计时：

```python
import time

for number in range(5, 0, -1):
    print(number)
    time.sleep(1)

print("时间到")
```

### 注意事项

`time.sleep(2)` 表示暂停大约 2 秒，但实际暂停时间可能略长，因为程序还会受到操作系统调度影响。

`sleep()` 只暂停当前执行线程，不会主动大量占用 CPU。

---

# 十二、程序性能计时

Python 提供了多种计时函数，它们的用途不同。

---

## 1. `time.perf_counter()`

用于测量一段程序实际经过的时间。

```python
import time

start = time.perf_counter()

total = sum(range(10_000_000))

end = time.perf_counter()

print(f"运行时间：{end - start:.6f} 秒")
```

特点：

- 单位为秒
- 返回浮点数
- 高分辨率
- 单调递增
- 包含程序暂停和等待时间
- 起点没有实际意义，只能比较两次调用的差值

适合：

- 算法测速
- 程序性能测试
- 代码段运行时间统计

通常是测量程序耗时的首选函数。

---

## 2. `time.perf_counter_ns()`

`perf_counter()` 的纳秒整数版本。

```python
start = time.perf_counter_ns()

total = sum(range(1_000_000))

end = time.perf_counter_ns()

print("耗时：", end - start, "纳秒")
```

转换为毫秒：

```python
elapsed_ms = (end - start) / 1_000_000
```

---

## 3. `time.monotonic()`

返回单调时钟值。

```python
import time

start = time.monotonic()

time.sleep(1)

end = time.monotonic()

print(end - start)
```

“单调”表示时钟值不会因为修改系统时间或网络校时而向后跳。

适合：

- 超时判断
- 定时任务
- 计算经过时间

示例：

```python
import time

deadline = time.monotonic() + 5

while time.monotonic() < deadline:
    print("任务执行中")
    time.sleep(1)
```

对应纳秒版本：

```python
time.monotonic_ns()
```

---

## 4. `time.process_time()`

返回当前进程消耗的 CPU 时间。

```python
import time

start = time.process_time()

total = sum(range(10_000_000))

end = time.process_time()

print("CPU 时间：", end - start)
```

它不统计程序睡眠时经过的时间：

```python
start = time.process_time()

time.sleep(2)

end = time.process_time()

print(end - start)
```

结果通常接近 `0`，而不是 `2`。

对应纳秒版本：

```python
time.process_time_ns()
```

---

## 5. `time.thread_time()`

返回当前线程消耗的 CPU 时间。

```python
import time

start = time.thread_time()

total = sum(range(1_000_000))

end = time.thread_time()

print(end - start)
```

对应纳秒版本：

```python
time.thread_time_ns()
```

该函数在部分平台上可能不可用。

---

## 各类时钟对比

| 函数 | 测量内容 | 包含 `sleep()` | 会受系统时间修改影响 |
|---|---|---:|---:|
| `time()` | 当前系统日历时间 | 是 | 可能 |
| `perf_counter()` | 实际经过时间 | 是 | 通常不会 |
| `monotonic()` | 单调经过时间 | 是 | 不会回退 |
| `process_time()` | 当前进程 CPU 时间 | 否 | 不受影响 |
| `thread_time()` | 当前线程 CPU 时间 | 否 | 不受影响 |

选择原则：

```text
显示当前日期时间 → time()
测试程序真实耗时 → perf_counter()
处理超时和截止时间 → monotonic()
分析进程 CPU 消耗 → process_time()
分析线程 CPU 消耗 → thread_time()
```

这些计时函数的起点通常没有实际意义，必须计算两次调用之差。

---

# 十三、查看时钟信息

## `time.get_clock_info()`

查询某个时钟的底层特性。

```python
import time

info = time.get_clock_info("perf_counter")
print(info)
```

可以查询：

```python
"time"
"monotonic"
"perf_counter"
"process_time"
"thread_time"
```

返回对象的主要属性：

```python
info.adjustable      # 时钟是否可以被系统调整
info.implementation  # 底层实现
info.monotonic       # 是否保证单调
info.resolution      # 时钟分辨率，单位为秒
```

示例：

```python
import time

for name in ["time", "monotonic", "perf_counter", "process_time"]:
    info = time.get_clock_info(name)

    print(name)
    print("底层实现：", info.implementation)
    print("是否可调整：", info.adjustable)
    print("是否单调：", info.monotonic)
    print("分辨率：", info.resolution)
    print()
```

---

# 十四、时区相关变量

## 1. `time.tzname`

当前系统定义的时区名称。

```python
import time

print(time.tzname)
```

通常返回二元素元组：

```text
('标准时间名称', '夏令时间名称')
```

---

## 2. `time.timezone`

本地标准时间与 UTC 之间的偏移秒数。

```python
print(time.timezone)
```

注意它的符号方向比较特殊，表示的是：

```text
UTC = 本地时间 + time.timezone 秒
```

对于 UTC+8 地区，可能得到：

```text
-28800
```

---

## 3. `time.altzone`

采用夏令时时，本地时间与 UTC 的偏移秒数。

只在系统定义了夏令时时有意义。

---

## 4. `time.daylight`

如果当前系统时区定义了夏令时规则，通常为非零值。

```python
print(time.daylight)
```

它不一定表示当前时刻正在采用夏令时，而是表示当前时区是否定义了夏令时规则。

---

## 5. `time.tzset()`

根据环境变量 `TZ` 重新初始化时区设置。

```python
import os
import time

os.environ["TZ"] = "UTC"
time.tzset()

print(time.strftime("%Y-%m-%d %H:%M:%S %Z"))
```

`tzset()` 主要在 Unix 系统上可用，Windows 通常不支持。

复杂跨地区时区转换建议使用：

```python
from datetime import datetime
from zoneinfo import ZoneInfo
```

---

# 十五、底层系统时钟函数

这些函数比较底层，初学阶段了解即可。

## 1. `time.clock_gettime()`

读取指定系统时钟。

```python
time.clock_gettime(time.CLOCK_MONOTONIC)
```

## 2. `time.clock_gettime_ns()`

纳秒整数版本。

```python
time.clock_gettime_ns(time.CLOCK_MONOTONIC)
```

## 3. `time.clock_getres()`

查询时钟分辨率。

```python
time.clock_getres(time.CLOCK_MONOTONIC)
```

## 4. `time.clock_settime()`

设置指定系统时钟，通常需要管理员权限。

```python
time.clock_settime(clock_id, seconds)
```

## 5. 常见时钟常量

```python
time.CLOCK_REALTIME
time.CLOCK_MONOTONIC
time.CLOCK_PROCESS_CPUTIME_ID
time.CLOCK_THREAD_CPUTIME_ID
```

这些接口和常量具有平台差异，并非所有操作系统都支持。

---

# 十六、常见应用

## 1. 显示当前时间

```python
import time

now = time.strftime("%Y-%m-%d %H:%M:%S")
print("当前时间：", now)
```

---

## 2. 数字时钟

```python
import time

while True:
    current = time.strftime("%Y-%m-%d %H:%M:%S")
    print("\r" + current, end="", flush=True)
    time.sleep(1)
```

其中：

```text
\r
```

表示把光标移动到当前行开头。

---

## 3. 倒计时

```python
import time

seconds = 10

while seconds > 0:
    minute, second = divmod(seconds, 60)

    print(
        f"\r剩余时间：{minute:02d}:{second:02d}",
        end="",
        flush=True
    )

    time.sleep(1)
    seconds -= 1

print("\n倒计时结束")
```

---

## 4. 计算两个时间相差多少秒

```python
import time

start_text = "2026-07-18 08:00:00"
end_text = "2026-07-18 12:30:00"

start_tuple = time.strptime(
    start_text,
    "%Y-%m-%d %H:%M:%S"
)

end_tuple = time.strptime(
    end_text,
    "%Y-%m-%d %H:%M:%S"
)

start_timestamp = time.mktime(start_tuple)
end_timestamp = time.mktime(end_tuple)

difference = end_timestamp - start_timestamp

print("相差秒数：", difference)
print("相差小时：", difference / 3600)
```

简单时间差可以这样计算。

涉及跨时区、夏令时、月份或日期加减时，更推荐使用 `datetime`。

---

## 5. 装饰器统计函数运行时间

```python
import time
from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()

        result = func(*args, **kwargs)

        end = time.perf_counter()

        print(
            f"{func.__name__} 运行耗时："
            f"{end - start:.6f} 秒"
        )

        return result

    return wrapper


@timer
def calculate():
    return sum(range(10_000_000))


answer = calculate()
```

---

## 6. 超时判断

```python
import time

timeout = 5
start = time.monotonic()

while True:
    elapsed = time.monotonic() - start

    if elapsed >= timeout:
        print("操作超时")
        break

    print("正在等待……")
    time.sleep(1)
```

这里使用 `monotonic()` 比 `time()` 更合理，因为修改系统时间不会导致计时回退。

---

# 十七、常见错误与陷阱

## 1. 把 `time.time()` 当作年月日

错误理解：

```python
print(time.time())
```

它不会直接得到：

```text
2026-07-18
```

而是得到一个时间戳。

正确转换：

```python
timestamp = time.time()
t = time.localtime(timestamp)
text = time.strftime("%Y-%m-%d", t)

print(text)
```

---

## 2. 混淆 `strftime()` 和 `strptime()`

```text
strftime：时间对象 → 字符串
strptime：字符串 → 时间对象
```

---

## 3. 使用 `time.time()` 测量程序性能

虽然可以：

```python
start = time.time()

# 执行代码

end = time.time()
```

但更推荐：

```python
start = time.perf_counter()

# 执行代码

end = time.perf_counter()
```

因为 `perf_counter()` 专门用于高精度耗时测量。

---

## 4. 认为 `sleep(1)` 一定精确等待一秒

```python
time.sleep(1)
```

它表示暂停大约一秒，实际暂停时间可能略长。

它不适合高精度实时控制。

---

## 5. 混淆星期编号

`tm_wday`：

```python
time.localtime().tm_wday
```

规则：

```text
星期一 = 0
星期日 = 6
```

`%w`：

```python
time.strftime("%w")
```

规则：

```text
星期日 = 0
星期六 = 6
```

---

## 6. 将 UTC 时间传给 `mktime()`

```python
utc_time = time.gmtime()
timestamp = time.mktime(utc_time)
```

这种写法通常会产生时区误差。

正确处理 UTC 时间元组：

```python
import calendar

timestamp = calendar.timegm(utc_time)
```

---

## 7. 直接使用时间戳计算日历日期

下面的写法只是增加了 86400 秒：

```python
tomorrow = time.time() + 24 * 60 * 60
```

对于采用夏令时的地区，一天不一定始终是 24 小时。

日历日期加减更适合：

```python
from datetime import datetime, timedelta

tomorrow = datetime.now() + timedelta(days=1)
```

---

## 8. 在 `time.strftime()` 中误用 `%f`

`%f` 表示微秒，主要由 `datetime` 使用。

普通 `struct_time` 只保存到秒，因此 `time.strftime()` 不能可靠输出真实微秒。

需要微秒时使用：

```python
from datetime import datetime

print(
    datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S.%f"
    )
)
```

---

# 十八、`time` 和 `datetime` 的区别

| 需求 | 推荐模块 |
|---|---|
| 获取时间戳 | `time` |
| 程序暂停 | `time` |
| 测量代码耗时 | `time` |
| 年月日对象 | `datetime` |
| 日期加减 | `datetime` |
| 计算日期差 | `datetime` |
| 跨时区转换 | `datetime` + `zoneinfo` |
| 底层系统时钟 | `time` |

简单理解：

```text
time：偏底层、偏时间戳和计时
datetime：偏日历、偏年月日运算
```

---

# 十九、重点函数速查表

| 函数 | 作用 | 返回值 |
|---|---|---|
| `time()` | 获取当前时间戳 | `float` |
| `time_ns()` | 获取纳秒时间戳 | `int` |
| `localtime()` | 时间戳转本地时间 | `struct_time` |
| `gmtime()` | 时间戳转 UTC 时间 | `struct_time` |
| `mktime()` | 本地时间元组转时间戳 | `float` |
| `ctime()` | 时间戳转固定格式字符串 | `str` |
| `asctime()` | 时间元组转固定格式字符串 | `str` |
| `strftime()` | 时间元组转自定义字符串 | `str` |
| `strptime()` | 时间字符串转时间元组 | `struct_time` |
| `sleep()` | 暂停当前线程 | `None` |
| `perf_counter()` | 高精度实际耗时计时 | `float` |
| `monotonic()` | 单调时钟 | `float` |
| `process_time()` | 当前进程 CPU 时间 | `float` |
| `thread_time()` | 当前线程 CPU 时间 | `float` |
| `get_clock_info()` | 查询时钟信息 | 命名空间对象 |

---

# 二十、必须掌握的核心内容

学习和考试时，优先掌握：

```python
import time

# 当前时间戳
time.time()

# 时间戳转本地时间
time.localtime()

# 时间戳转 UTC 时间
time.gmtime()

# 本地时间元组转时间戳
time.mktime()

# 时间格式化
time.strftime("%Y-%m-%d %H:%M:%S")

# 时间字符串解析
time.strptime("2026-07-18", "%Y-%m-%d")

# 程序暂停
time.sleep(1)

# 程序性能计时
time.perf_counter()
```

最终记住这一条主线：

```text
时间戳
  ↓ localtime() / gmtime()
struct_time
  ↓ strftime()
字符串

字符串
  ↓ strptime()
struct_time
  ↓ mktime()
时间戳
```
