# 课堂练习3
# 输入一个正整数，判断这个数字能不能作为二进制数字,如果不能，并输出判断结果
num = input('输入一个整数：')
a = 0
for i in num:
    if int(i) > 1:
        a += 1
if a == 0:
    print('能')
else:
    print('不能')
