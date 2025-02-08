# 课堂练习四
# 某商店在做水果的清仓处理，字典fruits存储的就是相应的水果信息
# 其中price表示水果的价格，quantity表示水果剩余的数量（库存）
# 现有预算 money=100，想要利用这100元购买尽可能多数量的水果
# 请应用贪心算法计算购买水果的最佳方案，将购买明细输出到控制台
# 示例：购买了5个apple，预算剩余75元
#      购买了4个pear，预算剩余51元
#      购买了5个banana，预算剩余11元
#      购买了1个strawberry，预算剩余0元

# 水果信息
fruits = {'apple': {'price': 5, 'quantity': 5},
          'pear': {'price': 6, 'quantity': 4},
          'banana': {'price': 8, 'quantity': 5},
          'strawberry': {'price': 11, 'quantity': 8},
          'cherry': {'price': 18, 'quantity': 10}
          }
# 预算
money = 100
# 遍历水果列表
for name, info in fruits.items():
    # 水果价格没有超过预算，可以购买
    if info['price'] <= money:
        # 请在下方编写代码
        # 计算购买数量
        pass
        # 判断购买数量是否超出库存，若超出则将库存视作购买数量

        # 更新剩余预算

        # 输出明细
