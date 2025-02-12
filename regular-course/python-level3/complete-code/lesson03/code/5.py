import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1100, 600))
bg = pygame.image.load("images/bg.png")


class FlyObject:
    def __init__(self, img, x, y):
        self.img = pygame.image.load(img)
        w, h = self.img.get_size()
        self.centerX = x + w / 2
        self.centerY = y + h / 2
        self.speedY = random.randint(30, 48)
        self.speedX = random.randint(-10, 10)
        self.angle = 0

    def draw(self):
        if self.speedX < 0:
            self.angle -= 5
        else:
            self.angle += 5
        self.newImg = pygame.transform.rotate(self.img, self.angle)
        self.rect = self.newImg.get_rect(center=(self.centerX, self.centerY))
        screen.blit(self.newImg, self.rect)

    def move(self):
        self.centerY -= self.speedY
        self.speedY -= 2
        self.centerX -= self.speedX


class Fruit(FlyObject):
    pass


fruitImgs = ['images/pineapple/full.png', 'images/orange/full.png',
             'images/pitaya/full.png', 'images/kiwi/full.png',
             'images/lemon/full.png', 'images/apple/full.png',
             'images/pomegranate/full.png', 'images/peach/full.png',
             'images/watermelon/full.png', 'images/banana/full.png',
             'images/coconut/full.png']
fruits = []
for i in range(10):
    fruit = Fruit(random.choice(fruitImgs), random.randint(100, 900), 600)
    fruits.append(fruit)


class Bomb(FlyObject):
    pass


bomb1 = Bomb('images/bomb/full.png', random.randint(100, 900), 600)
bomb2 = Bomb('images/bomb/full.png', random.randint(100, 900), 600)

"""

使用pygame库编写游戏，已知程序中导入了pygame库并定义了游戏窗口对象screen。
现在你需要使用Python面向对象编程定义一个水果刀类Knife，满足如下要求：
Knife类包含三个属性：img、x、y；其中img是pygame.image.load方法加载的图片。
Knife类包含一个draw方法，在该方法中直接使用全局变量screen绘制水果刀图片。
然后调用水果刀类，传入"images/knife.png"，550和300，来创建水果刀对象knife。
最后输出它的属性结构__dict__并调用draw方法。
请只输出满足要求的代码块，不要输出已知的代码。

"""


# 1. 请使用上述提示词，定义水果刀类并创建水果刀对象
class Knife:
    def __init__(self, img_path, x, y):
        self.img = pygame.image.load(img_path)
        self.x = x
        self.y = y

    def draw(self):
        screen.blit(self.img, (self.x, self.y))


knife = Knife("images/knife.png", 550, 300)
print(knife.__dict__)
knife.draw()

while True:
    screen.blit(bg, (0, 0))
    for fruit in fruits:
        fruit.draw()
        fruit.move()
    bomb1.draw()
    bomb2.draw()
    bomb1.move()
    bomb2.move()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
    pygame.time.delay(80)
