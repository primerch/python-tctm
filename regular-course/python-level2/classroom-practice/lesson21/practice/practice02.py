# 课堂练习2
# 编写程序，为下方程序添加限时10秒的答题条件
n = input('请在10秒内说输入《静夜思》的作者:')
while True:
    if n == '李白':
        print('回答正确！')
        break
    else:
        print('挑战失败！')
        break
