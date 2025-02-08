# 课堂练习4
# 编写一个程序，随机生成5位八进制数字，并输出
# 提示：random.randint(a,b)函数可以随机选择一个大于等于小于等于b的整数
import random

a = ''
for i in range(5):
    a += str(random.randint(0, 7))
print(a)
