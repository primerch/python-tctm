# 课堂练习2
# 编写一个程序，能将输入的十六进制数字转换成二进制
num = input('输入一个十六进制的整数：')
num = int(num, 16)
num = bin(num)
print(num)
