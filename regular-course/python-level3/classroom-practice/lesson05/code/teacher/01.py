'''

这是我的授课思路：
因为水果需要果汁属性，炸弹不需要果汁属性，所以不能在父类FlyObject中加果汁属性？
解决：在水果类的__init__()中添加果汁属性即可
在创建水果对象时子类会调用使用自己的__init__方法，丢失父类属性，如何让对象同时拥有父类的属性和子类的属性？
解决：在子类型的初始化方法中使用super()获得父类型，通过点init调用父类的__init__()方法，super().__init__()给对象先添加父类中的属性，然后再由子类的__init__（）方法给子类添加属性
这是我的授课代码：
class Fruit(FlyObject):
    # 1. 子类Fruit重写父类FlyObject的__init__方法
    def __init__(self, img, x, y):
        # 2. 使用super()函数调用父类的__init__方法继承父类的属性
        super().__init__(img, x, y)
        # 3. 子类添加独有的果汁属性juice
        self.juice = Juice(img.replace('full.png', 'juice.png'))
请帮我使用中文，根据以上内容出5道单选题，帮助学生理解和消化Python的重写，不需要答案

'''
