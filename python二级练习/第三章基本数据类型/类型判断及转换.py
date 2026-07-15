# 类型判断及转换

# 类型判断使用 type()
a = 3
print(type(a))
print(type('Hello'))


# 数据类型转换函数

# complex(re,im)    函数返回值为 re+im*1j
# im省略时，默认虚部为0j
print(complex(a))

# float(x)
print(float(a))

# int(x)
print(int('1'))

# str(x)
print(str(a))

# 易错点
# int('3.14') 这种写法是错误的
# int(float('3.14'))    正确写法是先将字符串转换为浮点数，再将浮点数转换为整数
