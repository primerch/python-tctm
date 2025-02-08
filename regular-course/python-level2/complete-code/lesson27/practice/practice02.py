# 课堂练习二
# 观察如下程序，然后通过异常处理捕获可能出现的异常，并且无论是否发生异常，都输出程序运行结束的提示语。
# 提示1：索引超出了列表范围造成的异常名为：IndexError
# 提示2：因不规范输入造成的异常名为：ValueError
try:
    list1 = [1, 2, 3, 4, 5]
    index = int(input("请输入一个索引值："))
    a = list1[index]
    print("索引%d对应的元素是：%s" % (index, a))
except IndexError:
    print("索引超出了列表范围")
except ValueError:
    print("请输入有效的索引")
finally:
    print('程序结束')
