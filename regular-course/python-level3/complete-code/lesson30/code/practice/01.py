# 1. 定义minCost函数和参数cost，计算整个路程的最小车费
def minCost(cost):
    # 2. 保存所有地点的最小车费，前两个点的最小车费已获得
    mins = [0, cost[0]]
    # 3. i从2开始到len(cost)反复执行三步计算
    for i in range(2, len(cost) + 1):
        # 4. 第一步: 前一站点出发车费+前一站点之前最小车费
        min1 = mins[i - 1] + cost[i - 1]
        # 5. 第二步: 前二站点出发车费+前二站点之前最小车费
        min2 = mins[i - 2] + cost[i - 2]
        # 6. 两个和取最小值，存入mins中当前i位置备用
        m = min(min1, min2)
        mins.append(m)
    # 7. 返回最后一次计算的最小车费
    return m


#  8. 终点之前每个站点出发的车费列表
cost = [20, 15, 5, 25, 16]
# 9. 调用函数计算整个路程的最小车费
m = minCost(cost)
print(m)
