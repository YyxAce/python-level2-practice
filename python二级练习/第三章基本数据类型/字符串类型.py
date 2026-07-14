# 字符串类型

print('这是单引号字符串')
print("这是双引号字符串")
print('''这是三单引号字符串''')
print("""这是三双引号字符串""")

# 用三引号表示的字符串可以换行
print(
'''
Tom said,
"Let's go"
'''
)

# 转义字符

print('\b')
print('\n')
print('\r')
print('\t')
print('\\')
print('\'')
print('\"')
print('\v')

# 索引和切片

string = "hello python"

print(string[0])    # 字符序列的正向递增索引是从0开始的
print(string[-1])   # 字符序列的反向递增索引是从-1开始的
print(string[-len(string)]) # 第一个字符序号是-len(string)

# 切片 左闭右开

print(string[1:3])  # el
print(string[:3])   # hel
print(string[:-1])  # hello pytho
print(string[1:])   # ello python
print(string[:])    # hello python

print(string[-3:-1])

print(string[-1:-3])    # 为空字符，但系统不提示错误
print(string[2:0])      # 为空字符，但系统不提示错误


# 切片步长
print(string[::-1])     # nohtyp olleh  输出字符串的逆序
print(string[-1::-3])   # nt l
print(string[10:3:-2])  # otp

# format()的基本使用

x,y = 1,2

# 字符串中{}表示一个槽，这三个槽的顺序对应format参数的顺序，依次填充{}
print("{} 除以 {} 的商是 {}".format(x,y,x/y))

# 如果{}的数量和format参数的数量不一致
# 不指定序号可能会报错

# 只要在{}里填入数字就能指定序号
print("{0}是99%的{1}加1%的{2}".format("天才","汗水","灵感"))



# format()格式控制
# 格式为{<参数序号>:<格式控制标记>}
# 包含6个可选字段: <填充>、<对齐>、<宽度>、<数字分组符>、<精度>、<类型>
# <填充>、<对齐>、<宽度>一般一起使用

# <填充>  :后的字符为填充字符，只能是一个，默认为空格
# <对齐>  ^ < > = 分别对应 剧中 左对齐 右对齐 符号与数字之间填充
# <宽度>  当前槽指定输出宽度 如果实际大于指定 按实际宽度 如果小于 则以<填充>补足

print("{:*^10,}".format(1234.5))

# <数字分组符>

# 千分位分组符，使用逗号分隔
print("{:,}".format(1234.5))    

# 下划线分隔符

# 十进制 每三位分一组
print("{:_}".format(1234.5))
# 对于 二进制 八进制 十六进制 每四位分一组
print("{:_b}".format(255))
print("{:_x}".format(65535))

# <精度>

# 字符串
print("{:.5}".format("PYTHON")) # 字符串的精度表示输出最大长度

# 浮点数
print("{:.3f}".format(12.3456)) # 表示小数部分输出的有效位数



# <类型>

# 字符串输出类型 s
print("{:s}".format("hello"))   # s是字符串默认类型，可省略

# 整数输出类型 b c d o x X n
print("{:b}".format(42))    # 二进制
print("{:c}".format(65))    # 转换为字符
print("{:d}".format(42))    # 十进制整数
print("{:o}".format(42))    # 八进制
print("{:x}".format(42))    # 十六进制
print("{:X}".format(42))    # 十六进制  字母大写

# 浮点数输出类型   e E f F g G n %

# 科学计数法
print("{:e}".format(1234.5))    
print("{:E}".format(1234.5))    
# 定点小数  
print("{:f}".format(1234.5))    # f默认保留小数点后六位
print("{:.2f}".format(1234.5))
# 通用格式
print("{:g}".format(1234.5))    # 自动选择e或f，通常删除无意义的末尾0
# 百分数
print("{:%}".format(0.256))     # 将数值乘100然后加上百分号，默认保留六位小数


# n 表示根据当前地区设置输出数字
print("{:n}".format(1234567))


# 转换标志
# {参数序号!转换标志:格式控制标记}
# !s 实际调用str()      把对象转换为普通字符串
# !r 实际调用repr()     字符串外出现引号，会显示转义字符
# !a 实际调用ascii()    会把非ASCII字符转换为转义形式


