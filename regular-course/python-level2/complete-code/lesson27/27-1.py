# 27-01 异常处理的控制台练习,常见的异常类型
# '请输入第一个数字: '
# '请输入第二个数字: '
# '结果是:'
# '错误：不能除以零'
# '错误：无效的输入，请输入一个有效的数字。'
# '程序结束'

try:
    n1 = float(input('请输入第一个数字: '))
    n2 = float(input('请输入第二个数字: '))
    result = n1 / n2
except ValueError:
    print('错误：无效的输入，请输入一个有效的数字。')
except ZeroDivisionError:
    print('错误：除数不能为零。')
else:
    print('结果是：', result)
finally:
    print('程序结束！')
