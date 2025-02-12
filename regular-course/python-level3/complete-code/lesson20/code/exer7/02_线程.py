import threading
import time


def father(task):
    for i in range(5):
        print('爸爸正在做%s' % task)
        time.sleep(1)


t1 = threading.Thread(target=father, args=['扫地'])
t1.start()


# 1. 定义son函数，实现儿子正在做的任务
def son(task):
    for i in range(5):
        print('儿子正在做%s' % task)
        time.sleep(1)


# 2. 创建子线程t2，执行son函数，传入参数：擦桌子，并启动t2子线程
t2 = threading.Thread(target=son, args=['擦桌子'])
t2.start()
# 3. 输出：主线程结束
print('主线程结束')
