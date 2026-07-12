# eval() 处理函数

# eval() 会将字符串转化为表达式
# 可以理解为将字符串最外两侧的引号去掉，按照语法执行剩下内容

print(eval("1+2+3"))

a = "[1,2,3,4]"
b = eval(a)

print(a,type(a))
print(b,type(b))
