# 数字类型的运算函数

# 这行命令列出所有的内置函数
# print(dir(__builtins__))


a = 1
b = -1
c = 3 + 4j
# abs(x) 返回x的绝对值 或 复数的模
print(abs(a),abs(b))
print(abs(c))

# x.conjugate() 返回x的共轭复数
print(c.conjugate())

# divmod(x,y) 返回一个由 x 整除 y 和 x 对 y 取余组成的元组
print(divmod(7,3))

# pow(x,y[,z]) 返回 x 的 y 次方 相当于 x**y
# 如果存在参数z 则返回 x 的 y 次方 除以 z 的余数

print(pow(2,3))
print(pow(2,3,3))

# round(x[,d]) 返回整数或浮点数x四舍五入到指定位数d的结果

# 四舍六入
print(round(3.16,1))
print(round(3.14,1))
# 五取偶
print(round(3.15,1))
# 这里的结果可能不是3.2,不是说round()违反规则
# 而是浮点数在计算机中通常不能精确存储
print(round(3.75,1))

# round只含一个参数
# 直接取整
print(round(3.4))
print(round(3.6))
print(round(3.5))
# d还可以是负数

print(round(1234,-2))

# 具体运算规则
# 先除以 10^(-d)
# 再按照"五取偶"舍入
# 最后乘回 10^(-d)

# max() 和 min() 分别用来计算列表、元组或其他可迭代对象的最大值和最小值 
a = [6,16,68,73,85,40,92,72,33,51]
print(max(a),min(a))
