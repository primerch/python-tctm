# 金币面额列表
d = [100, 50, 20, 10, 5, 1]
# 找零金额
money = 59
# 遍历金币面额列表
for i in d:
    if money >= i:
        n = money // i
        money = money % i
        print(f'需要{n}张{i}元纸币')
