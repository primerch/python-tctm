# 颜色叠加实验：http://l345.61it.cn:8080/l3/day29/color/index.html

# 排列函数
def perm(n, m):
    result = 1
    for i in range(m):
        result *= n
        n -= 1
    return result


def comb(n, m):
    return perm(n, m) // perm(m, m)


print(comb(256 * 3, 3))

# 1.计算3种颜色各取一种叠加，一共可以组成多少种颜色。用comb(256 * 3, 3)减去一种颜色去了3个的情况，再减去一种颜色取了2个的情况
