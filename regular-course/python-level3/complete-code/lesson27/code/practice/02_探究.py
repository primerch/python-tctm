'''
提示词1：

我是一名6年级小学生，现有完成一个题目要求：数组nums包含从0到n的所有整数，但其中缺了一个。
请编写代码找出那个缺失的整数。你有办法在尽量少的时间空间内完成吗？ 我有两种方法：
def missNum1(lst):
    for i in range(len(lst)):
        for j in range(len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    for i in range(len(lst)):
        if lst[i] != i:
            return i

def missNum2(lst):
    n = len(lst)
    lst2 = [-1] * (n + 1)
    for num in lst:
        lst2[num] = num
    result = lst2.index(-1)
    return result
为什么第一种方法速度慢，第二种方法速度快？语言通俗，只说明原因即可。
'''

'''
提示词2：

那是不是说明方法2就是最好的方法呢？能用类比的方式通俗的帮我解释一下什么是时间复杂度的概念么？

'''
