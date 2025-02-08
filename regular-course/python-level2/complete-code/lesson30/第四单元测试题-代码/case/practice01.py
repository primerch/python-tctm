# 课堂练习1
# 编写程序，在控制台输出当前使用电脑的操作系统和电脑的本地时间，注意时间格式为XXXX-XX-XX h:m:s
# 要求：使用f-tring字符串格式化的方式输出内容"当前电脑系统为XX，当前电脑的本地时间为XX"
# 在下方编写你的代码
import platform, time

osName = platform.system()
t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
print(f'当前电脑系统为：{osName}', f'当前电脑的本地时间为：{t}')
