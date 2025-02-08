# 课堂练习1
# 请将以下小明的信息以字典的形式存储,并输出字典中的所有内容
'''
name：小明
sex：男
age：8
hobby：编程
'''
info = {
    'name': '小明',
    'sex': '男',
    'age': 8,
    'hobby': '编程'
}
for x, y in info.items():
    print(x, y)
