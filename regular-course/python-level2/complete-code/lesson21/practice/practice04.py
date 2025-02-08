# 课堂练习4
# 某电商双11促销，想将以下3款产品统一999出售，
# 请遍历这3款产品的价格并统一修改为999，并输出价格更改后的字典products
products = {
    'p1': {
        'name': 'iPhone',
        'price': 1111,
        'color': 'silver'
    },
    'p2': {
        'name': 'MacBook',
        'price': 1299,
        'color': 'gray'
    },
    'p3': {
        'name': 'iPad',
        'price': 1028,
        'color': 'gold'
    }
}

for i in products.values():
    i['price'] = 999
print(products)
