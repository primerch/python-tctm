# 课堂练习三
# 编写代码，将下方游戏中的关键数据以二进制形式保存在data.pkl文件中
# 提示1：pickle.dump()函数可以将python中代码数据转换成二进制数据
# 提示2：创建的文件可以打开本地文件查看

import pickle

name = '旋风小子'
stats = {'等级': 60,
         '称号': '荣誉战士',
         '攻击力': 8000,
         '防御力': 2000,
         '经验值': 8542 / 10000,
         }

with open('data.pkl', 'wb') as f:
    data = [name, stats]
    pickle.dump(data, f)
