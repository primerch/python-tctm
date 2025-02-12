"""
练习题目:
已知定义了枪类Gun，在枪类中定义了两个属性:枪的名字name,子弹数量bullets；
还定义了一个射击方法shoot，发射子弹。
class Gun:
    def __init__(self, name, bullets):
        self.name = name
        self.bullets = bullets

    def shoot(self, num):
        self.bullets -= num
        print(self.name + '发射了' + str(num) + '颗子弹，还有' + str(self.bullets) + '发子弹')
请编写代码：
1. 创建手枪类HandGun继承枪类
2. 创建手枪对象handGun
3. 手枪对象handGun调用shoot方法，发射2颗子弹
"""


class Gun:
    def __init__(self, name, bullets):
        self.name = name
        self.bullets = bullets

    def shoot(self, num):
        self.bullets -= num
        print(self.name + '发射了' + str(num) + '颗子弹，还有' + str(self.bullets) + '发子弹')


# 1. 创建手枪类HandGun继承枪类
class HandGun(Gun):
    pass


# 2. 创建手枪对象handGun，名字为沙漠之鹰，子弹数量为7
handGun = Gun('沙漠之鹰', 7)
# 3. 手枪对象handGun调用shoot方法，发射2颗子弹
handGun.shoot(2)
