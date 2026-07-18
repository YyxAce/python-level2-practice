# Python 文件与文件操作完整知识点

> 本文系统整理 Python 文件操作的核心知识，包括文件本质、打开模式、读写方法、文件指针、编码、路径、JSON、CSV、Pickle、异常处理及常见易错点。

---

## 目录

1. [文件的本质](#一文件的本质)
2. [Python 文件操作的底层结构](#二python-文件操作的底层结构)
3. [打开文件：open](#三打开文件open)
4. [文件打开模式](#四文件打开模式)
5. [关闭文件](#五关闭文件)
6. [推荐使用 with](#六推荐使用-with)
7. [读取文件](#七读取文件)
8. [read 方法](#八read读取内容)
9. [readline 方法](#九readline读取一行)
10. [readlines 方法](#十readlines读取所有行)
11. [遍历文件对象](#十一直接遍历文件对象)
12. [写入文件](#十二写入文件)
13. [write 方法](#十三write)
14. [writelines 方法](#十四writelines)
15. [文件指针](#十五文件指针)
16. [tell 方法](#十六tell查看当前位置)
17. [seek 方法](#十七seek移动文件指针)
18. [flush 方法](#十八刷新缓冲区flush)
19. [truncate 方法](#十九截断文件truncate)
20. [文件对象常用属性](#二十文件对象的常用属性)
21. [编码](#二十一编码)
22. [编码错误处理](#二十二编码错误处理errors)
23. [换行符](#二十三换行符)
24. [缓冲机制](#二十四缓冲机制)
25. [路径](#二十五路径)
26. [pathlib](#二十六推荐使用-pathlib)
27. [文件和目录操作](#二十七文件和目录操作)
28. [异常处理](#二十八异常处理)
29. [同时打开多个文件](#二十九同时打开多个文件)
30. [复制文本文件](#三十复制文本文件)
31. [复制二进制文件](#三十一复制二进制文件)
32. [JSON 文件](#三十二json-文件)
33. [CSV 文件](#三十三csv-文件)
34. [Pickle 文件](#三十四pickle-文件)
35. [临时文件](#三十五临时文件)
36. [文件对象与迭代器](#三十六文件对象是可迭代对象)
37. [大文件处理原则](#三十七大文件处理原则)
38. [常见实用案例](#三十八常见实用案例)
39. [常见易错点](#三十九文件操作常见易错点)
40. [.py 文件补充知识](#四十py-文件补充知识)
41. [核心方法总表](#四十一核心方法总表)
42. [核心结论](#四十二必须掌握的核心结论)

---

# 一、文件的本质

## 1. 文件本质上是一串字节

无论是：

- `.txt`
- `.py`
- `.jpg`
- `.mp3`
- `.json`
- `.xlsx`

在计算机磁盘中，本质上都是一串二进制数据，也就是字节：

```text
01001000 01100101 01101100 01101100 01101111
```

Python 根据文件的打开方式，将这些字节解释成不同的数据。

## 2. 文本文件与二进制文件

### 文本文件

文本文件中的字节会按照某种字符编码转换为字符串。

```text
磁盘字节 → 按 UTF-8 解码 → Python 字符串 str
```

```python
with open("test.txt", "r", encoding="utf-8") as f:
    content = f.read()

print(type(content))
```

输出：

```text
<class 'str'>
```

### 二进制文件

二进制模式不会进行字符编码转换，读取到的是原始字节。

```text
磁盘字节 → Python 字节对象 bytes
```

```python
with open("test.jpg", "rb") as f:
    content = f.read()

print(type(content))
```

输出：

```text
<class 'bytes'>
```

---

# 二、Python 文件操作的底层结构

Python 打开一个文本文件时，大致经过三层：

```text
磁盘文件
   ↓
原始文件层 FileIO
   ↓
缓冲层 BufferedReader / BufferedWriter
   ↓
文本转换层 TextIOWrapper
```

文本模式：

```python
f = open("test.txt", "r", encoding="utf-8")
print(type(f))
```

通常得到：

```text
<class '_io.TextIOWrapper'>
```

二进制模式：

```python
f = open("test.txt", "rb")
print(type(f))
```

通常得到：

```text
<class '_io.BufferedReader'>
```

因此：

- 文本模式会处理编码、解码和换行符。
- 二进制模式直接处理字节。
- 缓冲机制可以减少程序直接访问磁盘的次数，提高效率。

---

# 三、打开文件：`open()`

## 1. 基本格式

```python
文件对象 = open(文件路径, 打开模式)
```

例如：

```python
f = open("test.txt", "r", encoding="utf-8")
```

完整形式：

```python
open(
    file,
    mode="r",
    buffering=-1,
    encoding=None,
    errors=None,
    newline=None
)
```

常用参数：

| 参数 | 作用 |
|---|---|
| `file` | 文件路径 |
| `mode` | 打开模式 |
| `encoding` | 文本编码 |
| `errors` | 编码错误处理方式 |
| `newline` | 换行符处理方式 |
| `buffering` | 缓冲方式 |

---

# 四、文件打开模式

## 1. 基本模式

| 模式 | 含义 | 文件不存在 | 文件已存在 |
|---|---|---:|---|
| `r` | 只读 | 报错 | 从头读取 |
| `w` | 只写 | 创建 | 清空原内容 |
| `a` | 追加 | 创建 | 从末尾写入 |
| `x` | 独占创建 | 创建 | 报错 |

## 2. 辅助模式

| 模式 | 含义 |
|---|---|
| `t` | 文本模式，默认 |
| `b` | 二进制模式 |
| `+` | 同时支持读和写 |

## 3. 常见组合

| 模式 | 含义 |
|---|---|
| `r` | 文本只读 |
| `rt` | 文本只读，与 `r` 相同 |
| `rb` | 二进制只读 |
| `w` | 文本只写，清空原文件 |
| `wb` | 二进制只写 |
| `a` | 文本追加 |
| `ab` | 二进制追加 |
| `r+` | 读写，不清空文件 |
| `w+` | 读写，先清空文件 |
| `a+` | 读写，写入时追加到末尾 |
| `x` | 创建新文件并写入 |
| `x+` | 创建新文件并读写 |

## 4. `r` 模式

```python
f = open("test.txt", "r", encoding="utf-8")
```

特点：

- 只能读取。
- 文件必须存在。
- 文件指针初始位于开头。
- 不会修改原文件。

文件不存在时会抛出：

```text
FileNotFoundError
```

## 5. `w` 模式

```python
f = open("test.txt", "w", encoding="utf-8")
```

特点：

- 只能写入。
- 文件不存在时创建。
- 文件存在时立即清空。
- 文件指针位于开头。

注意，下面这行代码一执行，原文件就已经被清空：

```python
f = open("test.txt", "w", encoding="utf-8")
```

即使后面什么都不写，原内容也已经丢失。

## 6. `a` 模式

```python
f = open("test.txt", "a", encoding="utf-8")
```

特点：

- 文件不存在时创建。
- 文件存在时保留原内容。
- 新内容写在文件末尾。

```python
with open("test.txt", "a", encoding="utf-8") as f:
    f.write("新增内容\n")
```

## 7. `x` 模式

```python
f = open("test.txt", "x", encoding="utf-8")
```

特点：

- 只允许创建新文件。
- 文件已存在时抛出 `FileExistsError`。
- 适合防止意外覆盖文件。

## 8. `+` 模式

`+` 表示同时支持读取和写入。

```python
f = open("test.txt", "r+", encoding="utf-8")
```

需要特别注意文件指针的位置：

```python
with open("test.txt", "r+", encoding="utf-8") as f:
    content = f.read()
    f.write("hello")
```

执行完 `read()` 后，文件指针已经位于末尾，所以 `"hello"` 会写到文件末尾。

---

# 五、关闭文件

## 1. 使用 `close()`

```python
f = open("test.txt", "r", encoding="utf-8")

content = f.read()

f.close()
```

关闭文件的作用：

- 释放操作系统资源。
- 将缓冲区中的数据写入磁盘。
- 解除文件占用。
- 避免文件描述符耗尽。

关闭后再操作：

```python
f.read()
```

会报错：

```text
ValueError: I/O operation on closed file
```

## 2. 判断文件是否关闭

```python
print(f.closed)
```

返回 `True` 或 `False`。

---

# 六、推荐使用 `with`

## 1. 基本格式

```python
with open("test.txt", "r", encoding="utf-8") as f:
    content = f.read()
```

离开 `with` 代码块后，Python 会自动关闭文件。

它大致相当于：

```python
f = open("test.txt", "r", encoding="utf-8")

try:
    content = f.read()
finally:
    f.close()
```

## 2. 为什么推荐 `with`

即使代码发生异常，文件也会被正确关闭：

```python
with open("test.txt", "r", encoding="utf-8") as f:
    result = 1 / 0
```

虽然发生了除零错误，但文件仍会自动关闭。

---

# 七、读取文件

常用方法：

```python
read()
readline()
readlines()
```

也可以直接遍历文件对象。

---

# 八、`read()`：读取内容

## 1. 读取全部内容

```python
with open("test.txt", "r", encoding="utf-8") as f:
    content = f.read()

print(content)
```

返回值是一个字符串。

假设文件内容为：

```text
第一行
第二行
第三行
```

读取结果可以理解为：

```python
content == "第一行\n第二行\n第三行"
```

## 2. 读取指定数量的字符

```python
with open("test.txt", "r", encoding="utf-8") as f:
    content = f.read(3)
```

文本模式下，`3` 通常表示读取三个字符。

中文字符虽然在 UTF-8 中占多个字节，但文本模式读取的是字符。

## 3. 二进制模式下的 `read(n)`

```python
with open("test.txt", "rb") as f:
    data = f.read(3)
```

这里的 `3` 表示三个字节。

## 4. 连续调用 `read()`

```python
with open("test.txt", "r", encoding="utf-8") as f:
    print(f.read(2))
    print(f.read(2))
```

第二次读取会从第一次结束的位置继续。

## 5. 读取完后再次读取

```python
with open("test.txt", "r", encoding="utf-8") as f:
    print(f.read())
    print(f.read())
```

第二次返回：

```python
""
```

也就是空字符串，因为文件指针已经位于末尾。

二进制模式下返回：

```python
b""
```

---

# 九、`readline()`：读取一行

```python
with open("test.txt", "r", encoding="utf-8") as f:
    line = f.readline()
```

每次读取一行：

```python
with open("test.txt", "r", encoding="utf-8") as f:
    print(f.readline())
    print(f.readline())
```

`readline()` 通常会保留行末的换行符。

假设第一行是：

```text
hello
```

实际得到的可能是：

```python
"hello\n"
```

因此：

```python
print(f.readline())
```

有时看起来会多一个空行，因为：

- 文件内容中有一个 `\n`。
- `print()` 默认又添加一个 `\n`。

可以写成：

```python
print(f.readline(), end="")
```

## `readline(size)`

```python
f.readline(5)
```

最多读取指定数量的字符或字节，但实际开发中较少使用这个参数。

---

# 十、`readlines()`：读取所有行

```python
with open("test.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
```

返回一个列表：

```python
[
    "第一行\n",
    "第二行\n",
    "第三行"
]
```

遍历：

```python
for line in lines:
    print(line, end="")
```

缺点：

- 会一次性将所有行读入内存。
- 不适合特别大的文件。

---

# 十一、直接遍历文件对象

推荐写法：

```python
with open("test.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line, end="")
```

优点：

- 一次处理一行。
- 不需要一次加载整个文件。
- 内存占用较低。
- 适合大文件。

底层通常会使用缓冲区，并不是每次只从磁盘读取一个字符。

## 去除换行符

```python
with open("test.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.rstrip("\n")
        print(line)
```

也可以使用：

```python
line.strip()
```

但两者不同。

### `strip()`

删除字符串两端所有空白字符，包括：

- 空格
- `\n`
- `\t`
- `\r`

```python
line.strip()
```

### `rstrip("\n")`

只删除右侧换行符：

```python
line.rstrip("\n")
```

如果文件内容中的前后空格有实际意义，更推荐使用：

```python
line.rstrip("\n")
```

---

# 十二、写入文件

常用方法：

```python
write()
writelines()
```

---

# 十三、`write()`

## 1. 写入字符串

```python
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("hello")
```

文本模式下必须写入字符串。

错误：

```python
f.write(123)
```

正确：

```python
f.write(str(123))
```

## 2. `write()` 不会自动换行

```python
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("第一行")
    f.write("第二行")
```

文件内容：

```text
第一行第二行
```

需要自己添加 `\n`：

```python
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("第一行\n")
    f.write("第二行\n")
```

## 3. `write()` 的返回值

`write()` 返回成功写入的字符数：

```python
with open("test.txt", "w", encoding="utf-8") as f:
    result = f.write("hello")

print(result)
```

输出：

```text
5
```

文本模式下通常表示字符数，不一定等于磁盘字节数。

```python
with open("test.txt", "w", encoding="utf-8") as f:
    result = f.write("你好")
```

返回：

```text
2
```

但 UTF-8 编码下通常占 6 个字节。

## 4. 二进制模式写入

二进制模式必须写入 `bytes`：

```python
with open("test.bin", "wb") as f:
    f.write(b"hello")
```

字符串需要先编码：

```python
f.write("你好".encode("utf-8"))
```

---

# 十四、`writelines()`

```python
lines = ["第一行\n", "第二行\n", "第三行\n"]

with open("test.txt", "w", encoding="utf-8") as f:
    f.writelines(lines)
```

特点：

- 参数是可迭代对象。
- 每个元素必须是字符串。
- 不会自动添加换行符。
- 返回值通常为 `None`。

下面不会自动换行：

```python
lines = ["第一行", "第二行", "第三行"]
```

结果：

```text
第一行第二行第三行
```

可以这样添加换行：

```python
lines = ["第一行", "第二行", "第三行"]

with open("test.txt", "w", encoding="utf-8") as f:
    f.writelines(line + "\n" for line in lines)
```

---

# 十五、文件指针

文件对象内部维护一个当前位置：

```text
abcdefg
^
当前读取位置
```

读取或写入后，文件指针会向后移动。

```python
with open("test.txt", "r", encoding="utf-8") as f:
    print(f.read(2))
    print(f.read(2))
```

第一次读取前两个字符，第二次从第三个字符继续。

---

# 十六、`tell()`：查看当前位置

```python
with open("test.txt", "rb") as f:
    print(f.tell())
    f.read(3)
    print(f.tell())
```

输出：

```text
0
3
```

二进制模式中，位置通常可以理解为距离文件开头的字节数。

文本模式中，由于字符编码和换行转换，`tell()` 返回值不一定能简单理解为字符下标。

---

# 十七、`seek()`：移动文件指针

基本格式：

```python
文件对象.seek(offset, whence)
```

参数：

| `whence` | 含义 |
|---:|---|
| `0` | 从文件开头计算 |
| `1` | 从当前位置计算 |
| `2` | 从文件末尾计算 |

也可以使用常量：

```python
import os

os.SEEK_SET
os.SEEK_CUR
os.SEEK_END
```

## 1. 从文件开头移动

```python
with open("test.txt", "rb") as f:
    f.seek(3, 0)
    print(f.read())
```

表示从文件开头向后移动 3 个字节。

## 2. 从当前位置移动

```python
with open("test.txt", "rb") as f:
    f.read(3)
    f.seek(2, 1)
```

表示从当前位置再向后移动 2 个字节。

## 3. 从文件末尾移动

```python
with open("test.txt", "rb") as f:
    f.seek(-3, 2)
    print(f.read())
```

表示移动到文件末尾前 3 个字节的位置。

## 4. 回到文件开头

```python
f.seek(0)
```

常见用法：

```python
with open("test.txt", "r", encoding="utf-8") as f:
    print(f.read())

    f.seek(0)

    print(f.read())
```

## 5. 文本模式的限制

文本模式经过编码和换行转换，不能随意使用字节偏移。

下面操作在文本模式中可能报错：

```python
f.seek(-3, 2)
```

需要精确按字节移动时，应使用二进制模式：

```python
with open("test.txt", "rb") as f:
    f.seek(-3, 2)
```

---

# 十八、刷新缓冲区：`flush()`

写入文件时，数据可能暂时存放在内存缓冲区中，并没有立刻写入磁盘。

```python
f.write("hello")
f.flush()
```

`flush()` 会将 Python 缓冲区中的数据提交给底层文件系统。

常见场景：

- 日志文件。
- 实时输出。
- 多个程序共享文件。
- 长时间运行的程序。

```python
import time

with open("log.txt", "w", encoding="utf-8") as f:
    for i in range(5):
        f.write(f"当前值：{i}\n")
        f.flush()
        time.sleep(1)
```

注意：

`flush()` 不一定表示物理磁盘已经立即完成写入，因为操作系统本身也可能有缓存。

---

# 十九、截断文件：`truncate()`

```python
f.truncate(size)
```

将文件截断到指定大小。

```python
with open("test.txt", "rb+") as f:
    f.truncate(5)
```

文件只保留前 5 个字节。

省略参数：

```python
f.truncate()
```

通常会按照当前文件指针位置截断。

该方法具有破坏性，使用时要谨慎。

---

# 二十、文件对象的常用属性

```python
f.name
f.mode
f.closed
f.encoding
```

示例：

```python
with open("test.txt", "r", encoding="utf-8") as f:
    print(f.name)
    print(f.mode)
    print(f.closed)
    print(f.encoding)
```

可能输出：

```text
test.txt
r
False
utf-8
```

退出 `with` 后：

```python
print(f.closed)
```

输出：

```text
True
```

其他常用判断方法：

```python
f.readable()
f.writable()
f.seekable()
```

---

# 二十一、编码

## 1. 编码与解码

编码：

```text
字符串 str → 字节 bytes
```

```python
data = "你好".encode("utf-8")
print(data)
```

解码：

```text
字节 bytes → 字符串 str
```

```python
text = data.decode("utf-8")
print(text)
```

## 2. 文件读写中的编码过程

写入文本文件：

```text
Python 字符串
    ↓ encoding
字节
    ↓
磁盘文件
```

读取文本文件：

```text
磁盘字节
    ↓ decoding
Python 字符串
```

所以写入和读取时通常要使用相同的编码。

## 3. 推荐显式指定编码

```python
with open("test.txt", "r", encoding="utf-8") as f:
    content = f.read()
```

不要完全依赖系统默认编码，因为：

- Windows 某些环境可能使用 GBK。
- Linux 和 macOS 通常使用 UTF-8。
- 同一份代码换电脑后可能出错。

## 4. 常见编码

| 编码 | 特点 |
|---|---|
| `utf-8` | 通用，推荐 |
| `utf-8-sig` | UTF-8，可自动处理 BOM |
| `gbk` | 常见中文 Windows 编码 |
| `ascii` | 只支持基本英文字符 |
| `utf-16` | 常带 BOM，每个字符通常占更多字节 |

## 5. `UnicodeDecodeError`

文件实际是 GBK 编码，却按 UTF-8 读取：

```python
with open("test.txt", "r", encoding="utf-8") as f:
    print(f.read())
```

可能报错：

```text
UnicodeDecodeError
```

应该使用正确编码：

```python
with open("test.txt", "r", encoding="gbk") as f:
    print(f.read())
```

## 6. BOM 问题

某些 UTF-8 文件开头带有 BOM。

使用：

```python
encoding="utf-8"
```

读取后，字符串开头可能出现：

```python
"\ufeff"
```

可以改用：

```python
with open("test.txt", "r", encoding="utf-8-sig") as f:
    content = f.read()
```

---

# 二十二、编码错误处理：`errors`

```python
open(
    "test.txt",
    "r",
    encoding="utf-8",
    errors="strict"
)
```

常见值：

| 参数值 | 含义 |
|---|---|
| `strict` | 默认，遇到错误直接报错 |
| `ignore` | 忽略无法解码的内容 |
| `replace` | 使用替代字符 |
| `backslashreplace` | 使用反斜杠转义形式 |

例如：

```python
with open(
    "test.txt",
    "r",
    encoding="utf-8",
    errors="replace"
) as f:
    print(f.read())
```

不推荐为了“不报错”就盲目使用 `ignore`，因为它可能悄悄丢失数据。

---

# 二十三、换行符

不同系统的传统换行符不同：

| 系统 | 换行符 |
|---|---|
| Linux/macOS | `\n` |
| Windows | `\r\n` |
| 旧版 macOS | `\r` |

Python 文本模式通常会进行通用换行转换。

## `newline` 参数

```python
open("test.txt", "r", encoding="utf-8", newline=None)
```

### `newline=None`

启用通用换行处理。

读取时，不同系统换行符通常统一转换成：

```python
"\n"
```

### `newline=""`

识别各种换行符，但尽量保留原始换行形式。

### `newline="\n"`

只将 `\n` 视为换行符。

处理 CSV 文件时经常写：

```python
open("data.csv", "w", encoding="utf-8", newline="")
```

可以避免出现多余空行。

---

# 二十四、缓冲机制

```python
open("test.txt", "r", buffering=-1)
```

常见值：

| 值 | 含义 |
|---:|---|
| `-1` | 使用默认缓冲策略 |
| `0` | 不使用缓冲，只能用于二进制模式 |
| `1` | 行缓冲，主要用于文本写入 |
| 大于 `1` | 指定缓冲区大小 |

大多数情况下不需要手动修改。

---

# 二十五、路径

## 1. 相对路径

```python
open("test.txt", "r")
```

相对路径是相对于当前工作目录，而不一定是当前 `.py` 文件所在目录。

查看当前工作目录：

```python
import os

print(os.getcwd())
```

## 2. 绝对路径

Windows：

```python
path = r"D:\Python\data\test.txt"
```

Linux/macOS：

```python
path = "/home/user/data/test.txt"
```

## 3. Windows 路径的反斜杠问题

有风险的写法：

```python
path = "C:\new\test.txt"
```

其中 `\n` 会被解释为换行符。

解决方法一：原始字符串

```python
path = r"C:\new\test.txt"
```

解决方法二：双反斜杠

```python
path = "C:\\new\\test.txt"
```

解决方法三：正斜杠

```python
path = "C:/new/test.txt"
```

---

# 二十六、推荐使用 `pathlib`

```python
from pathlib import Path
```

## 1. 创建路径对象

```python
path = Path("data/test.txt")
```

## 2. 拼接路径

```python
path = Path("data") / "test.txt"
```

比字符串拼接更安全。

## 3. 读取文本

```python
from pathlib import Path

path = Path("test.txt")
content = path.read_text(encoding="utf-8")
```

相当于：

```python
with open("test.txt", "r", encoding="utf-8") as f:
    content = f.read()
```

## 4. 写入文本

```python
path.write_text("hello", encoding="utf-8")
```

注意：会覆盖原文件。

## 5. 读取和写入字节

```python
data = path.read_bytes()
```

```python
path.write_bytes(b"hello")
```

## 6. 判断路径状态

```python
path.exists()
path.is_file()
path.is_dir()
```

## 7. 获取路径组成部分

```python
path = Path("/home/user/test.txt")

print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)
```

| 属性 | 结果 |
|---|---|
| `name` | `test.txt` |
| `stem` | `test` |
| `suffix` | `.txt` |
| `parent` | `/home/user` |

多个后缀：

```python
path = Path("archive.tar.gz")

print(path.suffix)
print(path.suffixes)
```

结果：

```python
".gz"
[".tar", ".gz"]
```

## 8. 创建目录

```python
Path("data").mkdir()
```

目录已存在时不报错：

```python
Path("data").mkdir(exist_ok=True)
```

创建多级目录：

```python
Path("a/b/c").mkdir(parents=True, exist_ok=True)
```

## 9. 遍历目录

```python
for path in Path(".").iterdir():
    print(path)
```

匹配文件：

```python
for path in Path(".").glob("*.txt"):
    print(path)
```

递归匹配：

```python
for path in Path(".").rglob("*.py"):
    print(path)
```

---

# 二十七、文件和目录操作

## 1. 重命名

```python
from pathlib import Path

Path("old.txt").rename("new.txt")
```

## 2. 删除文件

```python
Path("test.txt").unlink()
```

文件不存在时不报错：

```python
Path("test.txt").unlink(missing_ok=True)
```

## 3. 删除空目录

```python
Path("data").rmdir()
```

只能删除空目录。

## 4. 复制文件

```python
import shutil

shutil.copy("source.txt", "target.txt")
```

保留更多元数据：

```python
shutil.copy2("source.txt", "target.txt")
```

## 5. 复制目录

```python
shutil.copytree("source_dir", "target_dir")
```

## 6. 移动文件

```python
shutil.move("source.txt", "data/source.txt")
```

## 7. 删除整个目录

```python
shutil.rmtree("data")
```

这是危险操作，会递归删除目录中的全部内容。

---

# 二十八、异常处理

常见异常：

| 异常 | 含义 |
|---|---|
| `FileNotFoundError` | 文件不存在 |
| `FileExistsError` | 文件已存在 |
| `PermissionError` | 没有访问权限 |
| `IsADirectoryError` | 把目录当文件打开 |
| `NotADirectoryError` | 路径中某部分不是目录 |
| `UnicodeDecodeError` | 解码失败 |
| `UnicodeEncodeError` | 编码失败 |
| `OSError` | 其他操作系统级错误 |

完整示例：

```python
try:
    with open("test.txt", "r", encoding="utf-8") as f:
        content = f.read()

except FileNotFoundError:
    print("文件不存在")

except PermissionError:
    print("没有权限访问文件")

except UnicodeDecodeError:
    print("文件编码不正确")

except OSError as error:
    print("文件操作失败：", error)

else:
    print(content)
```

---

# 二十九、同时打开多个文件

```python
with open("source.txt", "r", encoding="utf-8") as src, \
     open("target.txt", "w", encoding="utf-8") as dst:
    dst.write(src.read())
```

也可以使用括号：

```python
with (
    open("source.txt", "r", encoding="utf-8") as src,
    open("target.txt", "w", encoding="utf-8") as dst
):
    dst.write(src.read())
```

---

# 三十、复制文本文件

适合较小文件：

```python
with open("source.txt", "r", encoding="utf-8") as src:
    content = src.read()

with open("target.txt", "w", encoding="utf-8") as dst:
    dst.write(content)
```

适合大文件：

```python
with open("source.txt", "r", encoding="utf-8") as src, \
     open("target.txt", "w", encoding="utf-8") as dst:

    for line in src:
        dst.write(line)
```

---

# 三十一、复制二进制文件

图片、音频、视频、压缩包等必须使用二进制模式：

```python
with open("source.jpg", "rb") as src, \
     open("target.jpg", "wb") as dst:

    while True:
        block = src.read(1024 * 1024)

        if not block:
            break

        dst.write(block)
```

也可以使用：

```python
import shutil

shutil.copyfile("source.jpg", "target.jpg")
```

---

# 三十二、JSON 文件

JSON 是一种文本数据格式。

支持：

- 字符串
- 数字
- 布尔值
- `null`
- 数组
- 对象

Python 与 JSON 的对应关系：

| Python | JSON |
|---|---|
| `dict` | object |
| `list`、`tuple` | array |
| `str` | string |
| `int`、`float` | number |
| `True` | true |
| `False` | false |
| `None` | null |

## 1. 写入 JSON

```python
import json

data = {
    "name": "小明",
    "age": 20,
    "scores": [90, 85, 88]
}

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(
        data,
        f,
        ensure_ascii=False,
        indent=4
    )
```

参数：

- `ensure_ascii=False`：中文直接保存。
- `indent=4`：缩进四个空格，便于阅读。

## 2. 读取 JSON

```python
import json

with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(data)
print(type(data))
```

## 3. `dump()` 和 `dumps()`

```python
json.dump(data, 文件对象)
```

将 Python 对象写入文件。

```python
json.dumps(data)
```

将 Python 对象转换为 JSON 字符串。

## 4. `load()` 和 `loads()`

```python
json.load(文件对象)
```

从文件读取 JSON。

```python
json.loads(JSON字符串)
```

从字符串解析 JSON。

---

# 三十三、CSV 文件

CSV 是逗号分隔值文件。

```text
name,age,score
小明,20,90
小红,19,95
```

推荐使用标准库 `csv`，不要单纯使用 `split(",")`，因为字段本身可能包含逗号和引号。

## 1. 写入 CSV

```python
import csv

data = [
    ["姓名", "年龄", "成绩"],
    ["小明", 20, 90],
    ["小红", 19, 95]
]

with open(
    "data.csv",
    "w",
    encoding="utf-8-sig",
    newline=""
) as f:
    writer = csv.writer(f)
    writer.writerows(data)
```

在 Windows 中给 Excel 使用时，`utf-8-sig` 通常能减少中文乱码问题。

## 2. 读取 CSV

```python
import csv

with open(
    "data.csv",
    "r",
    encoding="utf-8-sig",
    newline=""
) as f:
    reader = csv.reader(f)

    for row in reader:
        print(row)
```

每一行得到一个列表。

## 3. 字典方式写入

```python
import csv

data = [
    {"name": "小明", "age": 20},
    {"name": "小红", "age": 19}
]

with open(
    "data.csv",
    "w",
    encoding="utf-8-sig",
    newline=""
) as f:
    writer = csv.DictWriter(
        f,
        fieldnames=["name", "age"]
    )

    writer.writeheader()
    writer.writerows(data)
```

## 4. 字典方式读取

```python
import csv

with open(
    "data.csv",
    "r",
    encoding="utf-8-sig",
    newline=""
) as f:
    reader = csv.DictReader(f)

    for row in reader:
        print(row["name"], row["age"])
```

注意：CSV 中的数据读出来通常都是字符串。

```python
age = int(row["age"])
```

---

# 三十四、Pickle 文件

`pickle` 可以将 Python 对象序列化成二进制数据。

## 写入

```python
import pickle

data = {
    "name": "小明",
    "scores": [90, 95, 88]
}

with open("data.pkl", "wb") as f:
    pickle.dump(data, f)
```

## 读取

```python
import pickle

with open("data.pkl", "rb") as f:
    data = pickle.load(f)
```

## 安全问题

不要加载来源不可信的 Pickle 文件：

```python
pickle.load(f)
```

因为恶意 Pickle 数据可能在加载时执行危险代码。

适合：

- 自己程序内部保存 Python 对象。
- 缓存中间结果。
- 可信环境的数据交换。

不适合：

- 接收陌生人提供的文件。
- 跨语言数据交换。
- 长期通用数据保存。

---

# 三十五、临时文件

```python
import tempfile
```

文本临时文件：

```python
import tempfile

with tempfile.NamedTemporaryFile(
    mode="w+",
    encoding="utf-8",
    delete=True
) as f:
    f.write("hello")
    f.seek(0)
    print(f.read())
```

退出 `with` 后通常自动删除。

---

# 三十六、文件对象是可迭代对象

文件对象可以直接用于 `for`：

```python
with open("test.txt", "r", encoding="utf-8") as f:
    iterator = iter(f)

    print(next(iterator))
    print(next(iterator))
```

说明：

```python
for line in f:
```

本质上是在反复调用：

```python
next(f)
```

直到抛出：

```text
StopIteration
```

---

# 三十七、大文件处理原则

不要直接：

```python
content = f.read()
```

因为整个文件会进入内存。

推荐逐行处理：

```python
with open("large.txt", "r", encoding="utf-8") as f:
    for line in f:
        process(line)
```

或者分块读取：

```python
with open("large.bin", "rb") as f:
    while block := f.read(1024 * 1024):
        process(block)
```

这里使用了海象运算符 `:=`。

等价写法：

```python
while True:
    block = f.read(1024 * 1024)

    if not block:
        break

    process(block)
```

---

# 三十八、常见实用案例

## 1. 统计文件行数

```python
count = 0

with open("test.txt", "r", encoding="utf-8") as f:
    for line in f:
        count += 1

print(count)
```

更简洁：

```python
with open("test.txt", "r", encoding="utf-8") as f:
    count = sum(1 for _ in f)
```

## 2. 统计单词数量

```python
with open("test.txt", "r", encoding="utf-8") as f:
    content = f.read()

words = content.split()

print(len(words))
```

## 3. 查找包含某个关键词的行

```python
keyword = "Python"

with open("test.txt", "r", encoding="utf-8") as f:
    for line_number, line in enumerate(f, start=1):
        if keyword in line:
            print(line_number, line.rstrip("\n"))
```

## 4. 给每行添加行号

```python
with open("source.txt", "r", encoding="utf-8") as src, \
     open("target.txt", "w", encoding="utf-8") as dst:

    for number, line in enumerate(src, start=1):
        dst.write(f"{number}: {line}")
```

## 5. 追加日志

```python
from datetime import datetime

message = "程序启动"

with open("app.log", "a", encoding="utf-8") as f:
    now = datetime.now()
    f.write(f"{now:%Y-%m-%d %H:%M:%S} {message}\n")
```

## 6. 安全保存文件

直接使用 `w` 写入时，如果程序中途崩溃，原文件可能被破坏。

更安全的方法：

1. 先写临时文件。
2. 写入成功后替换原文件。

```python
from pathlib import Path

target = Path("data.txt")
temporary = Path("data.tmp")

temporary.write_text(
    "新的文件内容",
    encoding="utf-8"
)

temporary.replace(target)
```

---

# 三十九、文件操作常见易错点

## 1. `w` 会清空原文件

```python
open("test.txt", "w")
```

打开瞬间就会截断原文件。

## 2. `write()` 不自动换行

```python
f.write("hello")
f.write("world")
```

结果：

```text
helloworld
```

## 3. `writelines()` 不自动添加换行符

```python
f.writelines(["a", "b", "c"])
```

结果：

```text
abc
```

## 4. `read()` 后文件指针在末尾

```python
content1 = f.read()
content2 = f.read()
```

第二次通常得到空字符串。

需要：

```python
f.seek(0)
```

## 5. 文本模式与二进制模式类型不同

文本模式读取结果：

```python
str
```

二进制模式读取结果：

```python
bytes
```

## 6. 文本模式不能写 `bytes`

错误：

```python
with open("test.txt", "w") as f:
    f.write(b"hello")
```

应该写：

```python
f.write("hello")
```

## 7. 二进制模式不能写 `str`

错误：

```python
with open("test.bin", "wb") as f:
    f.write("hello")
```

正确：

```python
f.write(b"hello")
```

或者：

```python
f.write("hello".encode("utf-8"))
```

## 8. 文件不存在时，`r` 会报错

```python
open("不存在.txt", "r")
```

产生：

```text
FileNotFoundError
```

## 9. `open()` 不会自动创建父目录

```python
open("data/result/test.txt", "w")
```

如果 `data/result` 不存在，会报错。

正确：

```python
from pathlib import Path

path = Path("data/result/test.txt")
path.parent.mkdir(parents=True, exist_ok=True)

with path.open("w", encoding="utf-8") as f:
    f.write("hello")
```

## 10. 相对路径相对于工作目录

```python
open("data.txt")
```

Python 查找的通常是：

```text
当前工作目录/data.txt
```

而不一定是：

```text
当前 .py 文件所在目录/data.txt
```

查看当前工作目录：

```python
import os

print(os.getcwd())
```

## 11. 不要使用 `eval()` 读取外部文件

危险写法：

```python
data = eval(f.read())
```

如果文件内容包含恶意代码，可能造成严重后果。

应根据格式使用：

- JSON：`json.load()`
- CSV：`csv.reader()`
- 普通文本：字符串处理
- Python 字面量：可以考虑 `ast.literal_eval()`

```python
import ast

data = ast.literal_eval(f.read())
```

---

# 四十、`.py` 文件补充知识

`.py` 文件本质上也是文本文件，只是里面按照 Python 语法保存源代码。

```python
print("hello")
```

## 1. 直接运行 `.py` 文件

```bash
python test.py
```

执行流程大致是：

```text
读取 test.py
    ↓
解析语法
    ↓
编译为字节码
    ↓
Python 虚拟机执行
```

## 2. `.pyc` 文件

Python 可能把编译后的字节码缓存在：

```text
__pycache__
```

目录中，例如：

```text
test.cpython-313.pyc
```

`.pyc` 不是机器码，而是供 Python 虚拟机执行的字节码缓存。

## 3. 导入 `.py` 文件

`tool.py`：

```python
def add(a, b):
    return a + b
```

其他文件中：

```python
import tool

print(tool.add(1, 2))
```

一个 `.py` 文件可以作为模块使用。

## 4. `__name__`

```python
print(__name__)
```

直接运行当前文件时：

```python
__name__ == "__main__"
```

被其他文件导入时：

```python
__name__ == "模块名"
```

常见写法：

```python
def main():
    print("主程序")


if __name__ == "__main__":
    main()
```

作用：

- 文件直接运行时执行 `main()`。
- 文件作为模块导入时，不自动执行 `main()`。

---

# 四十一、核心方法总表

| 方法或属性 | 作用 |
|---|---|
| `open()` | 打开文件 |
| `close()` | 关闭文件 |
| `read()` | 读取全部或指定数量内容 |
| `readline()` | 读取一行 |
| `readlines()` | 读取所有行并返回列表 |
| `write()` | 写入字符串或字节 |
| `writelines()` | 写入多个字符串 |
| `seek()` | 移动文件指针 |
| `tell()` | 获取当前指针位置 |
| `flush()` | 刷新缓冲区 |
| `truncate()` | 截断文件 |
| `f.name` | 文件名 |
| `f.mode` | 打开模式 |
| `f.closed` | 是否关闭 |
| `f.encoding` | 文本编码 |
| `f.readable()` | 是否可读 |
| `f.writable()` | 是否可写 |
| `f.seekable()` | 是否支持移动指针 |

---

# 四十二、必须掌握的核心结论

1. 文件在磁盘中本质上是一串字节。
2. 文本模式将字节解码为 `str`，二进制模式返回 `bytes`。
3. `r` 读取，`w` 覆盖，`a` 追加，`x` 独占创建。
4. `w` 模式打开文件时就会清空原内容。
5. `write()` 和 `writelines()` 都不会自动添加换行符。
6. 文件对象内部存在文件指针。
7. `read()` 后指针会移动，再次读取会从当前位置继续。
8. `seek(0)` 可以回到文件开头。
9. 推荐使用 `with open(...) as f` 自动关闭文件。
10. 文本文件推荐明确指定 `encoding="utf-8"`。
11. 图片、音频、视频和压缩包必须使用二进制模式。
12. 大文件应逐行或分块读取，不应一次性 `read()`。
13. 路径处理推荐使用 `pathlib.Path`。
14. JSON 使用 `json` 模块，CSV 使用 `csv` 模块。
15. 不要加载来源不可信的 Pickle 文件。
16. 不要使用 `eval()` 解析外部文件内容。
17. 相对路径是相对于当前工作目录，不一定是 `.py` 文件所在目录。
