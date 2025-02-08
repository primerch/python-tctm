# 课堂练习四
# 自定义插入排序函数，将列表numbers进行从小到大的顺序排序并将排好序的列表输出在控制台上
# 提示：
# （1）外层循环用来遍历未排序的元素
# （2）内层循环用来将当前要排序的元素正确归位
# （3）变量交换：a,b=b,a
# （4）break语句用于结束当前循环，跳出当前所在的循环结构
numbers = [500, 300, 900, 200, 800, 400, 100, 700, 600]


# 在下方编写你的代码
def insertSort(list):
    for i in range(1, len(list)):
        for j in range(i, 0, -1):
            if list[j] < list[j - 1]:
                list[j], list[j - 1] = list[j - 1], list[j]
            else:
                break


insertSort(numbers)
print(numbers)
