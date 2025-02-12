# 开宝箱小游戏网址：http://l345.61it.cn:8080/l3/day28/game/index.html
# 1.创建排列函数，参数n表述元素个数，m表示需要排列的位置
def perm(n, m):
    # 2.定义变量保存累乘结果
    result = 1
    # 3.循环把每个排列位置的可能性相乘
    for i in range(m):
        result *= n
        n -= 1
    return result


# 4.分别计算9个点中选择2,3,4个点的排列数
print("选择2个点：", perm(9, 2))
print("选择3个点：", perm(9, 3))
print("选择4个点：", perm(9, 4))
