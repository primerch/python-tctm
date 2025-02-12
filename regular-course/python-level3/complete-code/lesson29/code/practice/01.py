# 颜色叠加实验：http://l345.61it.cn:8080/l3/day29/color/index.html

# 排列函数
def perm(n, m):
    result = 1
    for i in range(m):
        result *= n
        n -= 1
    return result


# 1.创建组合函数，参数n表述元素个数，m表示取出多少个元素
def comb(n, m):
    # 2.n个原色中取m个的排列数除以m个元素的排列数
    return perm(n, m) // perm(m, m)


# 3.计算三种颜色所有的度中选3个有多少情况
print(comb(256 * 3, 3))
