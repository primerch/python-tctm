import random
import time


# 第一种方法
def missNum1(lst):
    for i in range(len(lst)):
        for j in range(len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    for i in range(len(lst)):
        if lst[i] != i:
            return i


# 第二种方法
def missNum2(lst):
    n = len(lst)
    lst2 = [-1] * (n + 1)
    for num in lst:
        lst2[num] = num
    result = lst2.index(-1)
    return result


# 生成一个包含0-20000的所有整数的列表，但是列表中缺少一个未知的数字，整个列表乱序排列。
nums = random.sample(range(0, 20000), 20000)
nums.remove(random.choice(nums))

# 计算第一种方法耗时
start = time.time()
print("第一种方法：", missNum1(nums))
print("耗时：", time.time() - start, "秒")

# 计算第二种方法耗时
start = time.time()
print("第二种方法：", missNum2(nums))
print("耗时：", time.time() - start, "秒")
