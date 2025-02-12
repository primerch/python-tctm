# 1. 基于分治法定义一个查找函数divide和其参数lst
def divide(lst):
    # 2. 判断查找范围内是否只有一个元素
    if len(lst) == 1:
        if lst[0] == target:
            return lst
        return []
    # 4. 计算中间位置mid
    mid = len(lst) // 2
    # 5. 递归查找左半部分和右半部分的target目标
    left = divide(lst[:mid])
    right = divide(lst[mid:])
    # 6. 返回左右两部分的结果合并的列表
    return left + right


# 7. 给定的奶茶商店列表shops
shops = ['蜜雪冰城', '喜茶', '蜜雪冰城', '茶百道', '喜茶', 'CoCo', '蜜雪冰城', '茶百道', 'CoCo']
target = '蜜雪冰城'
# 8. 调用divide函数，传入商店列表和其前后索引，获取查找结果result，并输出
result = divide(shops)
print(result)
