# 课堂练习1
# 完成程序中暗号的输入，然后计算并输出代码一共执行的时间
import time

startTime = time.time()

print('守卫：天王盖地虎')
cipher = input('请输入暗号：')
while True:
    if cipher == '宝塔镇河妖':
        print('守卫：自己人，随我来！')
        break
    else:
        cipher = input('请输入暗号：')

endTime = time.time()
interval = endTime - startTime
print('用时', interval, '秒')
