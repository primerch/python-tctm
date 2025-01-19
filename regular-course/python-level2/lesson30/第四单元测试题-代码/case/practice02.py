# 课堂练习2
# 编写程序，要求用户输入两个数字，并计算它们的整除的结果。
# 要求：
# 1.使用try/except语句来实现该程序
# 2.处理除数为零的情况，并给出相应的提示信息"除数不能为零，请重新输入"
# 3.处理输入的值错误的情况，并给出相应的提示信息"输入无效，请输入整数"
# 提示：
# 1.整除符号"//"
# 2.使用input输入的内容是字符串，需使用int()将其转换为整数
# 3.除数为零错误类型ZeroDivisionError，值错误类型ValueError
# 在下方编写你的代码
try:
    dividend = int(input("请输入被除数："))
    divisor = int(input("请输入除数："))
    result = dividend // divisor
    print("计算结果：", result)
except ZeroDivisionError:
    print("除数不能为零，请重新输入。")
except ValueError:
    print("输入无效，请输入整数。")

