# Python 字符串处理方法大全

> 适用范围：Python 3.14  
> `str` 类型共有 **47 个不以下划线开头的公开方法**。

---

## 目录

1. [字符串方法概述](#一字符串方法概述)
2. [大小写转换方法：6 个](#二大小写转换方法6-个)
3. [字符串判断方法：12 个](#三字符串判断方法12-个)
4. [查找、计数与首尾判断方法：7 个](#四查找计数与首尾判断方法7-个)
5. [替换、删除前后缀与字符映射方法：5 个](#五替换删除前后缀与字符映射方法5-个)
6. [分割与拼接方法：6 个](#六分割与拼接方法6-个)
7. [清除、对齐、填充与制表符方法：8 个](#七清除对齐填充与制表符方法8-个)
8. [格式化与编码方法：3 个](#八格式化与编码方法3-个)
9. [47 个方法总表](#九47-个方法总表)
10. [常见易错点](#十常见易错点)
11. [快速选择指南](#十一快速选择指南)

---

# 一、字符串方法概述

## 1. 字符串是不可变对象

Python 字符串一旦创建，其内容不能被原地修改。

```python
s = "python"
s.upper()

print(s)          # python
print(s.upper())  # PYTHON
```

`upper()` 返回一个新字符串，原字符串 `s` 不变。

要保存处理结果，必须重新赋值：

```python
s = s.upper()
print(s)  # PYTHON
```

---

## 2. 字符串方法的基本调用形式

```python
字符串对象.方法名(参数)
```

例如：

```python
text = "Hello Python"

print(text.lower())
print(text.replace("Python", "World"))
```

也可以直接通过字符串字面量调用：

```python
print("Hello".upper())  # HELLO
```

---

## 3. 字符串方法的返回类型并不都是字符串

| 方法类型 | 常见返回值 |
|---|---|
| 大小写转换、替换、清除、对齐 | `str` |
| `is...()` 判断方法 | `bool` |
| `count()`、`find()`、`index()` | `int` |
| `split()`、`rsplit()`、`splitlines()` | `list` |
| `partition()`、`rpartition()` | `tuple` |
| `encode()` | `bytes` |

---

## 4. 以下操作不是字符串方法

下面这些也是常用字符串操作，但不属于 `str` 的 47 个公开方法：

```python
len(s)        # 求长度
s[0]          # 索引
s[1:4]        # 切片
"a" in s      # 成员判断
s1 + s2       # 拼接
s * 3         # 重复
```

---

# 二、大小写转换方法：6 个

## 1. `capitalize()`：首字符大写，其余字符小写

### 语法

```python
str.capitalize()
```

### 示例

```python
text = "hELLO PYTHON"
print(text.capitalize())
```

输出：

```text
Hello python
```

### 注意

它不只是将第一个字符大写，还会将其余字符全部转换为小写。

---

## 2. `casefold()`：用于不区分大小写的比较

### 语法

```python
str.casefold()
```

### 示例

```python
print("Straße".casefold())  # strasse
```

`casefold()` 比 `lower()` 转换得更加彻底，适合处理 Unicode 字符串的不区分大小写比较。

```python
a = "Straße"
b = "STRASSE"

print(a.casefold() == b.casefold())  # True
```

---

## 3. `lower()`：全部转换为小写

### 语法

```python
str.lower()
```

### 示例

```python
print("Hello PYTHON".lower())
```

输出：

```text
hello python
```

---

## 4. `upper()`：全部转换为大写

### 语法

```python
str.upper()
```

### 示例

```python
print("Hello Python".upper())
```

输出：

```text
HELLO PYTHON
```

---

## 5. `swapcase()`：大小写互换

### 语法

```python
str.swapcase()
```

### 示例

```python
print("Hello Python".swapcase())
```

输出：

```text
hELLO pYTHON
```

---

## 6. `title()`：每个单词的首字母大写

### 语法

```python
str.title()
```

### 示例

```python
print("hello python world".title())
```

输出：

```text
Hello Python World
```

### 注意

`title()` 按连续字母判断“单词”，在撇号等字符附近可能产生不符合自然语言习惯的结果：

```python
print("they're bill's friends".title())
```

输出：

```text
They'Re Bill'S Friends
```

---

# 三、字符串判断方法：12 个

字符串判断方法通常以 `is` 开头，返回布尔值 `True` 或 `False`。

---

## 1. `isalnum()`：是否全部由字母或数字组成

### 语法

```python
str.isalnum()
```

### 示例

```python
print("Python123".isalnum())  # True
print("Python 123".isalnum()) # False，包含空格
print("Python_123".isalnum()) # False，包含下划线
```

条件：

- 字符串至少包含一个字符；
- 每个字符都必须是字母或数字。

---

## 2. `isalpha()`：是否全部由字母组成

### 语法

```python
str.isalpha()
```

### 示例

```python
print("Python".isalpha())  # True
print("中国".isalpha())    # True
print("Python3".isalpha()) # False
```

这里的“字母”不限于英文字母，也包括 Unicode 中的其他字母字符。

---

## 3. `isascii()`：是否全部为 ASCII 字符

### 语法

```python
str.isascii()
```

### 示例

```python
print("Python123".isascii())  # True
print("中国".isascii())       # False
print("".isascii())           # True
```

ASCII 字符的码点范围为 `U+0000` 到 `U+007F`。

---

## 4. `isdecimal()`：是否全部为十进制数字字符

### 语法

```python
str.isdecimal()
```

### 示例

```python
print("123".isdecimal())  # True
print("²".isdecimal())    # False
print("Ⅳ".isdecimal())   # False
```

它的判断范围在三个数字判断方法中最严格。

---

## 5. `isdigit()`：是否全部为数字字符

### 语法

```python
str.isdigit()
```

### 示例

```python
print("123".isdigit())  # True
print("²".isdigit())    # True
print("Ⅳ".isdigit())   # False
```

`isdigit()` 除了普通十进制数字，还能识别某些上标数字等字符。

---

## 6. `isnumeric()`：是否全部为数值字符

### 语法

```python
str.isnumeric()
```

### 示例

```python
print("123".isnumeric())  # True
print("²".isnumeric())    # True
print("Ⅳ".isnumeric())   # True
print("四".isnumeric())   # True
```

三个数字判断方法的范围通常可以记为：

```text
isdecimal() ⊆ isdigit() ⊆ isnumeric()
```

即：

- `isdecimal()` 最严格；
- `isdigit()` 范围更大；
- `isnumeric()` 范围最大。

---

## 7. `isidentifier()`：是否为合法标识符形式

### 语法

```python
str.isidentifier()
```

### 示例

```python
print("student_name".isidentifier())  # True
print("_age".isidentifier())          # True
print("2name".isidentifier())         # False
print("user-name".isidentifier())     # False
```

### 重要注意

`isidentifier()` 只检查字符串形式是否符合标识符规则，不负责排除 Python 关键字：

```python
print("if".isidentifier())  # True
```

要判断是否能直接作为变量名，还应配合 `keyword.iskeyword()`：

```python
import keyword

name = "if"

print(name.isidentifier())       # True
print(keyword.iskeyword(name))   # True
```

完整判断：

```python
import keyword

name = "student_name"

valid = name.isidentifier() and not keyword.iskeyword(name)
print(valid)
```

---

## 8. `islower()`：是否所有有大小写的字符都是小写

### 语法

```python
str.islower()
```

### 示例

```python
print("python".islower())   # True
print("python123".islower()) # True
print("123".islower())      # False
```

数字、空格和标点不区分大小写，不会影响已有字母的判断；但字符串中必须至少有一个有大小写属性的字符。

---

## 9. `isupper()`：是否所有有大小写的字符都是大写

### 语法

```python
str.isupper()
```

### 示例

```python
print("PYTHON".isupper())    # True
print("PYTHON123".isupper()) # True
print("123".isupper())       # False
```

---

## 10. `istitle()`：是否符合标题格式

### 语法

```python
str.istitle()
```

### 示例

```python
print("Hello Python".istitle())  # True
print("Hello python".istitle())  # False
```

标题格式一般指：

- 每个单词的第一个有大小写属性的字符是大写；
- 后续有大小写属性的字符是小写。

---

## 11. `isprintable()`：是否全部为可打印字符

### 语法

```python
str.isprintable()
```

### 示例

```python
print("Hello Python!".isprintable())  # True
print("Hello\nPython".isprintable())  # False
print("".isprintable())               # True
```

换行符 `\n`、制表符 `\t` 等控制字符通常不是可打印字符。

---

## 12. `isspace()`：是否全部为空白字符

### 语法

```python
str.isspace()
```

### 示例

```python
print("   ".isspace())     # True
print("\t\n".isspace())    # True
print(" a ".isspace())     # False
print("".isspace())        # False
```

空白字符不只有普通空格，还包括制表符、换行符等。

---

## 空字符串的判断结果

```python
empty = ""
```

| 方法 | 结果 |
|---|---:|
| `empty.isascii()` | `True` |
| `empty.isprintable()` | `True` |
| 其他常见 `is...()` 方法 | `False` |

---

# 四、查找、计数与首尾判断方法：7 个

## 1. `count()`：统计子串出现次数

### 语法

```python
str.count(sub[, start[, end]])
```

### 示例

```python
text = "banana"

print(text.count("a"))       # 3
print(text.count("a", 2))    # 2
print(text.count("a", 2, 5)) # 1
```

`start` 和 `end` 的范围规则与切片相同：

```python
text[start:end]
```

### 注意：只统计不重叠出现

```python
print("aaaa".count("aa"))  # 2
```

统计的是：

```text
aa + aa
```

而不是三个相互重叠的 `"aa"`。

---

## 2. `find()`：从左向右查找子串位置

### 语法

```python
str.find(sub[, start[, end]])
```

### 示例

```python
text = "hello python"

print(text.find("python"))  # 6
print(text.find("java"))    # -1
```

找到时返回第一次出现的索引；找不到时返回 `-1`。

---

## 3. `rfind()`：从右向左查找子串位置

### 语法

```python
str.rfind(sub[, start[, end]])
```

### 示例

```python
text = "one two one"

print(text.find("one"))   # 0
print(text.rfind("one"))  # 8
```

返回子串最后一次出现的起始索引；找不到时返回 `-1`。

---

## 4. `index()`：从左向右查找，找不到则报错

### 语法

```python
str.index(sub[, start[, end]])
```

### 示例

```python
text = "hello python"

print(text.index("python"))  # 6
```

找不到时抛出 `ValueError`：

```python
text.index("java")
```

---

## 5. `rindex()`：从右向左查找，找不到则报错

### 语法

```python
str.rindex(sub[, start[, end]])
```

### 示例

```python
text = "one two one"

print(text.rindex("one"))  # 8
```

找不到时抛出 `ValueError`。

---

## `find()` 与 `index()` 的区别

| 方法 | 找到时 | 找不到时 |
|---|---|---|
| `find()` | 返回索引 | 返回 `-1` |
| `index()` | 返回索引 | 抛出 `ValueError` |
| `rfind()` | 返回最后一次出现的索引 | 返回 `-1` |
| `rindex()` | 返回最后一次出现的索引 | 抛出 `ValueError` |

通常：

- 不确定子串是否存在：优先使用 `find()`；
- 理论上必须存在，找不到就应视为程序错误：可以使用 `index()`；
- 只判断是否存在：优先使用 `in`，而不是 `find()`。

```python
text = "hello python"

print("python" in text)  # True
```

---

## 6. `startswith()`：判断是否以指定前缀开头

### 语法

```python
str.startswith(prefix[, start[, end]])
```

### 示例

```python
text = "Python programming"

print(text.startswith("Python"))  # True
print(text.startswith("programming", 7))  # True
```

前缀可以是一个元组：

```python
filename = "photo.png"

print(filename.startswith(("img_", "photo_", "photo")))  # True
```

只要匹配元组中的任意一个前缀，就返回 `True`。

---

## 7. `endswith()`：判断是否以指定后缀结尾

### 语法

```python
str.endswith(suffix[, start[, end]])
```

### 示例

```python
filename = "report.pdf"

print(filename.endswith(".pdf"))  # True
```

后缀也可以是元组：

```python
filename = "photo.jpg"

print(filename.endswith((".jpg", ".jpeg", ".png")))  # True
```

---

# 五、替换、删除前后缀与字符映射方法：5 个

## 1. `replace()`：替换子串

### 语法

```python
str.replace(old, new[, count])
```

### 示例

```python
text = "one one one"

print(text.replace("one", "two"))
```

输出：

```text
two two two
```

限制替换次数：

```python
print(text.replace("one", "two", 2))
```

输出：

```text
two two one
```

### 注意

字符串不可变，`replace()` 返回新字符串：

```python
text = "hello"
text.replace("h", "H")

print(text)  # hello
```

---

## 2. `removeprefix()`：删除指定前缀

### 语法

```python
str.removeprefix(prefix)
```

### 示例

```python
url = "https://example.com"

print(url.removeprefix("https://"))
```

输出：

```text
example.com
```

如果字符串不以该前缀开头，则返回原内容：

```python
print("example.com".removeprefix("https://"))
# example.com
```

---

## 3. `removesuffix()`：删除指定后缀

### 语法

```python
str.removesuffix(suffix)
```

### 示例

```python
filename = "report.pdf"

print(filename.removesuffix(".pdf"))
```

输出：

```text
report
```

如果不存在该后缀，则返回原内容。

---

## 4. `maketrans()`：创建字符转换表

### 常用语法一：两个等长字符串

```python
str.maketrans(x, y)
```

将 `x` 中的字符依次映射为 `y` 中对应位置的字符：

```python
table = str.maketrans("abc", "123")

print("apple banana".translate(table))
```

输出：

```text
1pple 21n1n1
```

### 常用语法二：指定要删除的字符

```python
str.maketrans(x, y, z)
```

其中：

- `x` 中字符映射为 `y` 中对应字符；
- `z` 中的字符会被删除。

```python
table = str.maketrans("abc", "123", " ")

print("a b c".translate(table))
```

输出：

```text
123
```

### 常用语法三：使用字典

```python
table = str.maketrans({
    "a": "1",
    "b": "2",
    " ": None
})
```

字典值为 `None` 表示删除该字符。

---

## 5. `translate()`：按照转换表转换字符串

### 语法

```python
str.translate(table)
```

### 示例

```python
table = str.maketrans({
    "a": "A",
    "b": "B",
    " ": None
})

text = "a b cab"
print(text.translate(table))
```

输出：

```text
ABcAB
```

### `replace()` 与 `translate()` 的选择

- 替换一个或少量子串：使用 `replace()`；
- 一次批量转换多个字符，或删除多个字符：使用 `translate()`；
- `translate()` 通常要与 `str.maketrans()` 配合。

---

# 六、分割与拼接方法：6 个

## 1. `split()`：从左向右分割字符串

### 语法

```python
str.split(sep=None, maxsplit=-1)
```

### 指定分隔符

```python
text = "apple,banana,orange"

print(text.split(","))
```

输出：

```python
['apple', 'banana', 'orange']
```

### 限制最大分割次数

```python
text = "a-b-c-d"

print(text.split("-", 2))
```

输出：

```python
['a', 'b', 'c-d']
```

`maxsplit=2` 表示最多切两刀，因此最多得到三个元素。

### 不指定分隔符

```python
text = "  Python   is\n easy  "

print(text.split())
```

输出：

```python
['Python', 'is', 'easy']
```

当 `sep=None` 时：

- 连续空白字符会被看成一个分隔区域；
- 字符串首尾空白不会产生空字符串元素；
- 空格、制表符、换行符等都可作为分隔符。

### 指定分隔符时会保留空字段

```python
print("a,,b,".split(","))
```

输出：

```python
['a', '', 'b', '']
```

---

## 2. `rsplit()`：从右向左分割字符串

### 语法

```python
str.rsplit(sep=None, maxsplit=-1)
```

### 示例

```python
path = "home/user/file.txt"

print(path.rsplit("/", 1))
```

输出：

```python
['home/user', 'file.txt']
```

### 注意

不设置 `maxsplit` 时，`split()` 和 `rsplit()` 的结果通常相同：

```python
"a-b-c".split("-")
"a-b-c".rsplit("-")
```

只有限制分割次数时，从左切还是从右切才有明显区别。

---

## 3. `splitlines()`：按照行边界分割

### 语法

```python
str.splitlines(keepends=False)
```

### 示例

```python
text = "第一行\n第二行\n第三行"

print(text.splitlines())
```

输出：

```python
['第一行', '第二行', '第三行']
```

保留换行符：

```python
print(text.splitlines(True))
```

输出：

```python
['第一行\n', '第二行\n', '第三行']
```

---

## 4. `partition()`：从左侧第一次出现处分成三部分

### 语法

```python
str.partition(sep)
```

返回一个三元素元组：

```text
(分隔符前面的内容, 分隔符本身, 分隔符后面的内容)
```

### 示例

```python
text = "name=Tom=20"

print(text.partition("="))
```

输出：

```python
('name', '=', 'Tom=20')
```

如果找不到分隔符：

```python
print("hello".partition("="))
```

输出：

```python
('hello', '', '')
```

---

## 5. `rpartition()`：从右侧第一次出现处分成三部分

### 语法

```python
str.rpartition(sep)
```

### 示例

```python
text = "name=Tom=20"

print(text.rpartition("="))
```

输出：

```python
('name=Tom', '=', '20')
```

如果找不到分隔符：

```python
print("hello".rpartition("="))
```

输出：

```python
('', '', 'hello')
```

---

## 6. `join()`：用指定字符串拼接多个字符串

### 语法

```python
separator.join(iterable)
```

### 示例

```python
words = ["Python", "is", "easy"]

result = " ".join(words)
print(result)
```

输出：

```text
Python is easy
```

使用其他连接符：

```python
print("-".join(["2026", "07", "14"]))
```

输出：

```text
2026-07-14
```

### 重要理解

调用 `join()` 的对象是“连接符”：

```python
"连接符".join(多个字符串)
```

而不是：

```python
多个字符串.join("连接符")
```

### 元素必须都是字符串

```python
numbers = [1, 2, 3]

# ",".join(numbers)  # TypeError
```

应先转换：

```python
numbers = [1, 2, 3]

print(",".join(map(str, numbers)))
```

输出：

```text
1,2,3
```

---

# 七、清除、对齐、填充与制表符方法：8 个

## 1. `strip()`：清除两端指定字符

### 语法

```python
str.strip(chars=None)
```

不传参数时，清除两端空白字符：

```python
text = "  hello \n"

print(text.strip())
```

输出：

```text
hello
```

指定字符集合：

```python
print("www.example.com".strip("w.com"))
```

输出：

```text
example
```

### 极重要：`chars` 是字符集合，不是一个完整前后缀

```python
"www.example.com".strip("w.com")
```

表示不断删除两端属于以下集合的字符：

```text
{'w', '.', 'c', 'o', 'm'}
```

它并不是精确删除字符串 `"w.com"`。

若要精确删除前缀或后缀，应使用：

```python
removeprefix()
removesuffix()
```

---

## 2. `lstrip()`：清除左端指定字符

### 语法

```python
str.lstrip(chars=None)
```

### 示例

```python
print("   hello   ".lstrip())
```

输出：

```text
hello   
```

指定字符集合：

```python
print("000123".lstrip("0"))
```

输出：

```text
123
```

---

## 3. `rstrip()`：清除右端指定字符

### 语法

```python
str.rstrip(chars=None)
```

### 示例

```python
print("   hello   ".rstrip())
```

输出：

```text
   hello
```

删除行尾换行符：

```python
line = "hello\n"
line = line.rstrip("\n")
```

---

## 4. `center()`：居中对齐

### 语法

```python
str.center(width, fillchar=" ")
```

### 示例

```python
print("Python".center(10))
```

输出：

```text
  Python  
```

指定填充字符：

```python
print("Python".center(10, "-"))
```

输出：

```text
--Python--
```

`fillchar` 必须是单个字符。

---

## 5. `ljust()`：左对齐

### 语法

```python
str.ljust(width, fillchar=" ")
```

### 示例

```python
print("Python".ljust(10, "-"))
```

输出：

```text
Python----
```

---

## 6. `rjust()`：右对齐

### 语法

```python
str.rjust(width, fillchar=" ")
```

### 示例

```python
print("Python".rjust(10, "-"))
```

输出：

```text
----Python
```

---

## 7. `zfill()`：左侧补零

### 语法

```python
str.zfill(width)
```

### 示例

```python
print("42".zfill(5))   # 00042
print("-42".zfill(5))  # -0042
print("+42".zfill(5))  # +0042
```

### 注意

当字符串以 `+` 或 `-` 开头时，零会填充在符号后面。

---

## 8. `expandtabs()`：将制表符展开为空格

### 语法

```python
str.expandtabs(tabsize=8)
```

### 示例

```python
text = "A\tB"

print(text.expandtabs(4))
```

输出效果类似：

```text
A   B
```

### 注意

它不是简单地将每个 `\t` 替换成固定数量的空格，而是根据当前列位置补到下一个制表位。

---

# 八、格式化与编码方法：3 个

## 1. `format()`：格式化字符串

### 语法

```python
format_string.format(*args, **kwargs)
```

### 按位置填充

```python
name = "Tom"
age = 20

print("姓名：{}，年龄：{}".format(name, age))
```

输出：

```text
姓名：Tom，年龄：20
```

### 使用参数序号

```python
print("{1}学习{0}".format("Python", "Tom"))
```

输出：

```text
Tom学习Python
```

### 使用参数名

```python
print("姓名：{name}，年龄：{age}".format(name="Tom", age=20))
```

### 使用格式控制标记

```python
pi = 3.1415926

print("{:.2f}".format(pi))  # 3.14
print("{:>10}".format("Hi"))
print("{:,}".format(1234567))
```

虽然现代 Python 中经常优先使用 f-string，但 `format()` 仍是正式的字符串方法。

---

## 2. `format_map()`：使用映射对象格式化字符串

### 语法

```python
format_string.format_map(mapping)
```

### 示例

```python
data = {
    "name": "Tom",
    "age": 20
}

text = "姓名：{name}，年龄：{age}".format_map(data)
print(text)
```

输出：

```text
姓名：Tom，年龄：20
```

### 与 `format(**mapping)` 的区别

以下两种写法效果通常相似：

```python
"{name}".format(**data)
"{name}".format_map(data)
```

区别在于：

- `format(**data)` 将字典作为关键字参数展开；
- `format_map(data)` 直接使用映射对象；
- 对自定义字典或自定义映射类型，`format_map()` 更灵活。

---

## 3. `encode()`：将字符串编码为字节串

### 语法

```python
str.encode(encoding="utf-8", errors="strict")
```

### 示例

```python
text = "你好"

data = text.encode("utf-8")

print(data)
print(type(data))
```

输出类似：

```text
b'\xe4\xbd\xa0\xe5\xa5\xbd'
<class 'bytes'>
```

### 编码与解码

```text
str --encode()--> bytes
bytes --decode()--> str
```

示例：

```python
text = "你好"

data = text.encode("utf-8")
new_text = data.decode("utf-8")

print(new_text)  # 你好
```

编码和解码必须使用相互兼容的字符编码。

---

# 九、47 个方法总表

| 序号 | 方法 | 主要作用 | 返回类型 |
|---:|---|---|---|
| 1 | `capitalize()` | 首字符大写，其余小写 | `str` |
| 2 | `casefold()` | Unicode 不区分大小写转换 | `str` |
| 3 | `center()` | 居中对齐 | `str` |
| 4 | `count()` | 统计子串出现次数 | `int` |
| 5 | `encode()` | 编码为字节串 | `bytes` |
| 6 | `endswith()` | 判断指定后缀 | `bool` |
| 7 | `expandtabs()` | 展开制表符 | `str` |
| 8 | `find()` | 从左查找，失败返回 `-1` | `int` |
| 9 | `format()` | 格式化字符串 | `str` |
| 10 | `format_map()` | 使用映射对象格式化 | `str` |
| 11 | `index()` | 从左查找，失败报错 | `int` |
| 12 | `isalnum()` | 判断是否全为字母或数字 | `bool` |
| 13 | `isalpha()` | 判断是否全为字母 | `bool` |
| 14 | `isascii()` | 判断是否全为 ASCII 字符 | `bool` |
| 15 | `isdecimal()` | 判断是否全为十进制数字字符 | `bool` |
| 16 | `isdigit()` | 判断是否全为数字字符 | `bool` |
| 17 | `isidentifier()` | 判断是否为合法标识符形式 | `bool` |
| 18 | `islower()` | 判断字母是否全为小写 | `bool` |
| 19 | `isnumeric()` | 判断是否全为数值字符 | `bool` |
| 20 | `isprintable()` | 判断是否全为可打印字符 | `bool` |
| 21 | `isspace()` | 判断是否全为空白字符 | `bool` |
| 22 | `istitle()` | 判断是否符合标题格式 | `bool` |
| 23 | `isupper()` | 判断字母是否全为大写 | `bool` |
| 24 | `join()` | 拼接多个字符串 | `str` |
| 25 | `ljust()` | 左对齐 | `str` |
| 26 | `lower()` | 全部转小写 | `str` |
| 27 | `lstrip()` | 清除左端字符 | `str` |
| 28 | `maketrans()` | 创建字符转换表 | `dict` |
| 29 | `partition()` | 从左按分隔符分成三部分 | `tuple` |
| 30 | `removeprefix()` | 删除指定前缀 | `str` |
| 31 | `removesuffix()` | 删除指定后缀 | `str` |
| 32 | `replace()` | 替换子串 | `str` |
| 33 | `rfind()` | 从右查找，失败返回 `-1` | `int` |
| 34 | `rindex()` | 从右查找，失败报错 | `int` |
| 35 | `rjust()` | 右对齐 | `str` |
| 36 | `rpartition()` | 从右按分隔符分成三部分 | `tuple` |
| 37 | `rsplit()` | 从右分割 | `list` |
| 38 | `rstrip()` | 清除右端字符 | `str` |
| 39 | `split()` | 从左分割 | `list` |
| 40 | `splitlines()` | 按行分割 | `list` |
| 41 | `startswith()` | 判断指定前缀 | `bool` |
| 42 | `strip()` | 清除两端字符 | `str` |
| 43 | `swapcase()` | 大小写互换 | `str` |
| 44 | `title()` | 每个单词首字母大写 | `str` |
| 45 | `translate()` | 按转换表转换字符 | `str` |
| 46 | `upper()` | 全部转大写 | `str` |
| 47 | `zfill()` | 左侧补零 | `str` |

分类数量：

```text
大小写转换：6 个
字符串判断：12 个
查找、计数与首尾判断：7 个
替换、前后缀与字符映射：5 个
分割与拼接：6 个
清除、对齐、填充与制表符：8 个
格式化与编码：3 个

总计：6 + 12 + 7 + 5 + 6 + 8 + 3 = 47 个
```

---

# 十、常见易错点

## 1. 字符串方法通常不会修改原字符串

错误理解：

```python
s = "hello"
s.upper()

print(s)  # 仍然是 hello
```

正确写法：

```python
s = s.upper()
```

---

## 2. `find()` 找不到返回 `-1`，`index()` 找不到会报错

```python
"abc".find("x")   # -1
"abc".index("x")  # ValueError
```

---

## 3. 不要用 `find()` 的返回值直接判断是否找到

错误写法：

```python
text = "python"

if text.find("p"):
    print("找到了")
```

`"p"` 位于索引 `0`，而整数 `0` 在布尔环境中为假，因此会错误地认为没有找到。

正确写法：

```python
if text.find("p") != -1:
    print("找到了")
```

更推荐：

```python
if "p" in text:
    print("找到了")
```

---

## 4. `strip(chars)` 的参数是字符集合

```python
"www.example.com".strip("w.com")
```

不是精确删除 `"w.com"`，而是从两端不断清除 `w`、`.`、`c`、`o`、`m` 中的任意字符。

精确删除前后缀：

```python
text.removeprefix(prefix)
text.removesuffix(suffix)
```

---

## 5. `split()` 不指定分隔符和指定空格并不相同

```python
text = "  a   b  "

print(text.split())
# ['a', 'b']

print(text.split(" "))
# ['', '', 'a', '', '', 'b', '', '']
```

---

## 6. `join()` 的调用者是连接符

正确：

```python
"-".join(["a", "b", "c"])
```

错误：

```python
# ["a", "b", "c"].join("-")
```

---

## 7. `join()` 中的元素必须都是字符串

```python
items = [1, 2, 3]

# ",".join(items)  # TypeError
```

正确：

```python
",".join(map(str, items))
```

---

## 8. `isidentifier()` 不排除 Python 关键字

```python
"if".isidentifier()  # True
```

完整判断：

```python
import keyword

name = "if"

result = name.isidentifier() and not keyword.iskeyword(name)
print(result)  # False
```

---

## 9. `isdecimal()`、`isdigit()`、`isnumeric()` 范围不同

```text
isdecimal() ⊆ isdigit() ⊆ isnumeric()
```

| 字符串 | `isdecimal()` | `isdigit()` | `isnumeric()` |
|---|---:|---:|---:|
| `"123"` | `True` | `True` | `True` |
| `"²"` | `False` | `True` | `True` |
| `"Ⅳ"` | `False` | `False` | `True` |
| `"四"` | `False` | `False` | `True` |

---

## 10. `replace()` 默认替换全部匹配项

```python
"aaa".replace("a", "b")
# 'bbb'
```

限制次数：

```python
"aaa".replace("a", "b", 1)
# 'baa'
```

---

## 11. `startswith()` 和 `endswith()` 可以接收元组

```python
filename = "photo.png"

filename.endswith((".jpg", ".jpeg", ".png"))
# True
```

适合一次判断多个可能的前缀或后缀。

---

## 12. `zfill()` 会正确处理正负号

```python
"-42".zfill(5)
# '-0042'
```

不是：

```text
00-42
```

---

# 十一、快速选择指南

| 需求 | 推荐方法 |
|---|---|
| 转换为小写 | `lower()` |
| 不区分大小写比较 | `casefold()` |
| 转换为大写 | `upper()` |
| 大小写互换 | `swapcase()` |
| 每个单词首字母大写 | `title()` |
| 判断是否全为字母 | `isalpha()` |
| 判断是否全为普通十进制数字 | `isdecimal()` |
| 判断是否为合法标识符形式 | `isidentifier()` |
| 判断子串是否存在 | `in` |
| 查找子串位置，不想报错 | `find()` |
| 查找子串位置，找不到应报错 | `index()` |
| 统计子串次数 | `count()` |
| 判断前缀 | `startswith()` |
| 判断后缀 | `endswith()` |
| 替换子串 | `replace()` |
| 精确删除前缀 | `removeprefix()` |
| 精确删除后缀 | `removesuffix()` |
| 清除两端空白 | `strip()` |
| 按分隔符切开 | `split()` |
| 从右侧限制次数分割 | `rsplit()` |
| 拆成“前、分隔符、后”三部分 | `partition()` |
| 拼接多个字符串 | `join()` |
| 居中对齐 | `center()` |
| 左对齐 | `ljust()` |
| 右对齐 | `rjust()` |
| 左侧补零 | `zfill()` |
| 批量转换多个字符 | `translate()` + `maketrans()` |
| 字符串转换为字节串 | `encode()` |
| 使用 `{}` 格式化 | `format()` |
| 使用字典格式化 | `format_map()` |

---

# 十二、在 Python 中查看全部公开字符串方法

```python
methods = [
    name
    for name in dir(str)
    if not name.startswith("_")
]

print(len(methods))
print(methods)
```

输出数量：

```text
47
```

方法列表：

```python
[
    'capitalize', 'casefold', 'center', 'count', 'encode',
    'endswith', 'expandtabs', 'find', 'format', 'format_map',
    'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal',
    'isdigit', 'isidentifier', 'islower', 'isnumeric',
    'isprintable', 'isspace', 'istitle', 'isupper', 'join',
    'ljust', 'lower', 'lstrip', 'maketrans', 'partition',
    'removeprefix', 'removesuffix', 'replace', 'rfind',
    'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip',
    'split', 'splitlines', 'startswith', 'strip', 'swapcase',
    'title', 'translate', 'upper', 'zfill'
]
```

---

# 十三、总结

Python 的 47 个字符串公开方法不需要一次全部死记。建议按使用频率分阶段掌握：

第一阶段重点掌握：

```text
lower()      upper()
strip()      split()
join()       replace()
find()       count()
startswith() endswith()
```

第二阶段掌握：

```text
isalpha()    isdecimal()
isdigit()    isidentifier()
partition()  removeprefix()
removesuffix()
```

第三阶段再学习：

```text
casefold()   translate()
maketrans()  format_map()
expandtabs()
```

核心原则：

```text
先理解方法解决什么问题，再通过代码练习记忆语法。
```

---

## 参考资料

- Python 3.14 官方文档：Built-in Types — Text Sequence Type `str`
- Python 3.14 官方文档：String Methods
