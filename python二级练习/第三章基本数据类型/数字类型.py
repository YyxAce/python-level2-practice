# 整数

# 整数可以表示为 二进制、八进制、十进制和十六进制
print(0b001111101000,0B001111101000)
print(0o1750,0O1750)
print(0x3e8,0X3e8)

# bin() oct() hex()     将整数转换为对应进制，且为字符串形式

print(f"bin({10}) = {bin(10)}",type(bin(10)))
print(f"oct({10}) = {oct(10)}",type(oct(10)))
print(f"hex({10}) = {hex(10)}",type(hex(10)))

# Python没有限制整数类型的大小，
# 但实际由于计算机内存有限，整数类型不可能无限大或无限小

# 浮点数

pi = 3.1415926  # 小数表示法
a = 125e10      # 科学计数法 数字部分 + e或E + 可选正负号 + 整数指数

print(pi,a)
print()
# 易错点
print("(0.1 + 0.2 == 0.3) is", 0.1 + 0.2 == 0.3) 
print("(1.5 + 2.1 == 3.6) is", 1.5 + 2.1 == 3.6)


# 复数

# 一般形式为 x + yj

# 如果省略实数部分，python 会自动添加一个0.0的实数部分

fushu = 1j  # 即使 y = 1，也不可省略，因为省略后，python 会将j识别为一个变量 

# 可以使用.real和.imag 取出实数部分和虚数部分

print(fushu.real)
print(fushu.imag)
print(fushu.conjugate())    # 返回共轭复数
