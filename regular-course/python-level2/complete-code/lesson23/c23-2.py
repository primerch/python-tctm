import time

while True:
    n = input('时间的输出格式是否为24小时制：')
    if n == '是':
        t = time.strftime("%H:%M:%S", time.localtime())
        print(t)
    else:
        t = time.strftime("%p-%I:%M:%S", time.localtime())
        print(t)
