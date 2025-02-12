'''
我现在要讲继承知识点，让水果类和炸弹类继承FlyObject类。这是我的授课思路：
问题: 水果类和炸弹类除了类名不同外，在他们中定义的属性和方法代码都是一模一样的，这些代码被重复的书写了，那么如何避免这种类中重复的属性和方法定义
解决：使用类的继承技术
问题：水果类和炸弹类继承父类，讲解继承的概念，语法格式，以及特性，分析出定义父类FlyObject，然后举例强调继承特点，突出继承的好处，代码重用

这是我的代码：
# 1. 定义父类FlyObject
class FlyObject:
    def __init__(self, img, x, y):
        self.img = pygame.image.load(img)
        self.x = x
        self.y = y
        self.speedY = random.randint(30, 48)
        self.speedX = random.randint(-10, 10)

    def draw(self):
        screen.blit(self.img, (self.x, self.y))

    def move(self):
        self.y -= self.speedY
        self.speedY -= 2
        self.x += self.speedX

# 2. 水果类Fruit继承父类FlyObject
class Fruit(FlyObject):
    pass
# 3. 炸弹类Bomb继承父类FlyObject
class Bomb(FlyObject):
    pass
请帮我使用中文，根据以上知识点出5道单选题，帮助学生理解什么是继承，继承的作用、继承的语法、何时使用继承等，不需要答案.
'''
