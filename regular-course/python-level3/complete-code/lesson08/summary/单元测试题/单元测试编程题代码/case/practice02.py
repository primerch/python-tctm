'''
编写一个Python程序，定义一个类Calculator，这个类有一个静态方法add，接收两个参数，
返回这两个参数的和。然后创建一个Calculator的实例，调用add方法计算5和3的和，并打印结果。

'''


# 定义Calculator类
class Calculator:
    # 定义静态方法add
    @staticmethod
    def add(a, b):
        return a + b


# 创建Calculator的实例，调用add方法计算5和3的和，并打印结果
calc = Calculator()
result = calc.add(5, 3)
print(result)
