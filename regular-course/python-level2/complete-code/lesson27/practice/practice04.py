# 课堂练习四
# 请按以下要求完成对下列两个列表的操作
# 要求：1. 将列表bonus中数字，按从大到小的顺序排列
#      2. 将names列表中的元素顺序随机打乱
#      3. 将两个列表中的对应位置的元素以元组的形式一一结合，并逐个输出

import random

bonus = [100, 5, 10, 50, 20]
names = ['张三', '李四', '王五', '赵二', '孙六']
bonus.sort(reverse=True)
random.shuffle(names)
result = zip(names, bonus)
for i in result:
    print(i)
