# 课堂练习四
# 编写代码，将newData.pkl文件中的二进制数据转换成代码数据并更新到当前代码中,然后输出更新后的数据
# 提示：pickle.load()函数可以将python中代码数据转换成二进制数据


import pickle

name = '圣斗士'
stats = {'等级': 90,
         '称号': '荣誉将领',
         '攻击力': 16000,
         '防御力': 5000,
         '经验值': 57084 / 100000,
         }

with open('newData.pkl', 'wb') as f:
    data = [name, stats]
    pickle.dump(data, f)
