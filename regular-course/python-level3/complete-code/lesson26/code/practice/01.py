# 1. 基于分治法定义一个查找函数divide和其参数lst
def divide(lst):
    # 2. 如果列表只有一个元素，返回该列表
    if len(lst) == 1:
        return lst

    # 3.计算中间位置mid
    mid = len(lst) // 2

    # 4. 递归获得左半部分和右半部分列表
    left = divide(lst[:mid])
    right = divide(lst[mid:])

    # 5. 使用merge函数将左右两部分合并成一个有序列表
    return merge(left, right)


# 6. 定义merge函数将两个有序列表合并，参数left和right
def merge(left, right):
    # 7. 创建一个空列表result，设置i j初始为0 分别指向left,right第一个元素
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # 8.判断如果是i等于left长度，将right剩余元素加到result后面，返回相加后的列表。否则加left返回
    if i == len(left):
        result += right[j:]
        return result
    else:
        result += left[i:]
        return result


# 9.定义nums列表，调用divide函数对数字进行归并排序并打印结果
nums = [38, 27, 43, 3, 9, 82, 10]
print(divide(nums))
