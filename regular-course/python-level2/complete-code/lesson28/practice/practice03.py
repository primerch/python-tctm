# 课堂练习三
# 创建一个变量i,初始值为0，利用时间戳，让变量i每隔1秒增加1，直到增加到5为止，并输出i变化的过程。
import time

start = time.time()
i = 0
while i <= 5:
    now = time.time()
    interval = now - start
    if interval >= 1:
        print(i)
        i += 1
        start = time.time()
