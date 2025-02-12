"""

下面定义了鱼类Fish和鸟类Bird，并创建了两个对象animal1，animal2:
class Fish:
    def __init__(self, species, color):
        self.species = species
        self.color = color

    def swim(self):
        return "这只鱼正在水中游泳"

class Bird:
    def __init__(self, species, color):
        self.species = species
        self.color = color

    def fly(self):
        return "这只鸟正在空中飞翔"

animal1 = Fish("金鱼", "金色")
animal2 = Bird("燕子", "灰色")

你的任务：
编写一段Python代码，获取animal1和animal2对象所属类的类名,并输出在控制台上。

"""


class Fish:
    def __init__(self, species, color):
        self.species = species
        self.color = color

    def swim(self):
        return "这只鱼正在水中游泳"


class Bird:
    def __init__(self, species, color):
        self.species = species
        self.color = color

    def fly(self):
        return "这只鸟正在空中飞翔"


animal1 = Fish("金鱼", "金色")
animal2 = Bird("燕子", "灰色")
# 1. 获取animal1和animal2对象所属类的类名,并输出在控制台上
print(type(animal1).__name__)
print(type(animal2).__name__)
