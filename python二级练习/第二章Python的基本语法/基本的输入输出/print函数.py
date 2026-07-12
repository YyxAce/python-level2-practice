# print() 输出函数

# 一、仅输出字符串或单个变量的值
print("Welcome to Python")
print(123)

# 二、多个变量输出
print(1,2,3)    # 默认使用空格分隔
print(1,2,3,sep=",")    # 也可对sep参数进行赋值，自定义分隔符


# 三、混合输出字符串与变量值
x,y = 10.0,5.0
print("{}除以{}的商是{}".format(x,y,x/y))
