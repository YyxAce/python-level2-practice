# print() 进阶用法

# sep 和 end 参数
# separator 分隔符
# end 输出结束后的内容，默认为换行符

print(1,2,3,4,5,sep = '-',end = '！')

# 输出特殊字符，类似C语言中的转义字符

print("第一行\n第二行")     # 换行符\n
print("姓名\t年龄")         # 制表符\t
print("他说:\"你好\"")      # 输出引号
print("C:\\Users\\Desktop") # 输出反斜杠

# 格式化输出
# 方法一：使用逗号
name = '小明'
age = 20

print("姓名：", name, "年龄：", age)
# 方法二：使用f-string 目前最常用

print(f"姓名：{name}，年龄：{age}")

a = 10
b = 20

print(f"{a} + {b} = {a+b}") #大括号中也可写表达式

pi = 3.1415926

print(f"圆周率约为：{pi:.2f}")    # 控制小数位数


