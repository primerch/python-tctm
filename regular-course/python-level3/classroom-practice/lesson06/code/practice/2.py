"""

编程题：
假设你正在为 "王者荣耀"游戏的英雄设计一个英雄类Hero，
类中含有一个类变量count，其初始值为0，用于记录创建的英雄数量。
每个Hero对象有name和skill两个属性，每当我们创建一个新的Hero对象时，count值增加1。
给定的代码如下：

class Hero:
    count = 0

    def __init__(self, name, skill):
        self.name = name
        self.skill = skill
        Hero.count += 1

你的任务是：
1. 为Hero类添加一个名为get_count的类方法。在该方法中输出当前已经创建的英雄数量。
2. 创建luban对象，保存名为"鲁班七号"且技能为"空中支援"的英雄，以及guanyu对象，保存名为"关羽"且技能为"青龙偃月"的英雄。
3. 使用Hero类来调用get_count方法

"""


# 请根据注释编写代码
class Hero:
    count = 0

    def __init__(self, name, skill):
        self.name = name
        self.skill = skill
        Hero.count += 1

    # 1. 定义类方法get_count, 在该方法中输出当前已经创建的英雄数量。

# 2. 创建luban对象，保存名为"鲁班"且技能为"空中支援"的英雄。

# 3. 创建guanyu对象，保存名为"关羽"且技能为"青龙偃月"的英雄。

# 4. 使用Hero类来调用get_count方法
