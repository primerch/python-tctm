import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1100, 600))
bg = pygame.image.load("images/bg.png")


class Fruit:
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
        self.x -= self.speedX


# 不同种类的水果图片路径列表
fruitImgs = ['images/pineapple/full.png', 'images/orange/full.png',
             'images/pitaya/full.png', 'images/kiwi/full.png',
             'images/lemon/full.png', 'images/apple/full.png',
             'images/pomegranate/full.png', 'images/peach/full.png',
             'images/watermelon/full.png', 'images/banana/full.png',
             'images/coconut/full.png']

# 1. 循环创建10个随机的水果对象
fruits = []
for i in range(10):
    fruit = Fruit(random.choice(fruitImgs), random.randint(100, 900), 600)
    fruits.append(fruit)


class Bomb:
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
        self.x -= self.speedX


bomb1 = Bomb('images/bomb/full.png', random.randint(100, 900), 600)
bomb2 = Bomb('images/bomb/full.png', random.randint(100, 900), 600)

while True:
    screen.blit(bg, (0, 0))
    # 2. 循环遍历水果对象列表，并调用draw和move方法
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
