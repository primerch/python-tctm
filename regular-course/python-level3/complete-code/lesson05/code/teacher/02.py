'''

这是我的授课思路：
问题:有些变量在类内，有些变量在类外，如何选择放在哪里
解决:面向对象编程，推荐变量都写在类中，便于查找和使用
问题:有些变量只需要保存一份,比如：knife,fruits...但是如果放在__init__中每个对象都会保存一份变量的副本，且必须先创建对象才能使用，反而繁琐
解决:放在类中，但放在__init__之外
使用类变量：优点是不需要创建对象，只需要类名就可以访问
注意:类外使用类变量时必须用 类名. 前缀
这是我的授课代码：
# 1. 定义Game类
class Game:
    # 2. 把类外边定义的全局变量bg，fruitImgs，fruits，bomb和knife移动到Game类中，定义成类变量
    bg = pygame.image.load("images/bg.png")
    fruitImgs = ['images/pineapple/full.png', 'images/orange/full.png',
                 'images/pitaya/full.png', 'images/kiwi/full.png']
    fruits = []
    bomb = Bomb('images/bomb/full.png', random.randint(100, 900), 600)
    knife = Knife('images/knife.png', 550, 300)
请帮我使用中文，根据以上内容出5道单选题，帮助学生理解什么是类变量何时应该使用类变量，不需要答案

'''
