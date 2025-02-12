import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1100, 600))
bg = pygame.image.load("images/bg.png")


class FlyObject:
    def __init__(self, img, x, y):
        self.img = pygame.image.load(img)
        self.x = x
        self.y = y
        self.speedY = random.randint(30, 48)
        self.speedX = random.randint(-10, 10)
        self.angle = 0

    def draw(self):
        # 1. 根据图像左右移动的方向来逆时针或顺时针旋转五度
        if self.speedX < 0:
            self.angle -= 5
        else:
            self.angle += 5
        self.newImg = pygame.transform.rotate(self.img, self.angle)
        screen.blit(self.newImg, (self.x, self.y))

    def move(self):
        self.y -= self.speedY
        self.speedY -= 2
        self.x -= self.speedX


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
    fruit = Fruit(random.choice(fruitImgs), random.randint(100, 500), 600)
    fruits.append(fruit)


class Bomb(FlyObject):
    pass


bomb1 = Bomb('images/bomb/full.png', random.randint(100, 900), 600)
bomb2 = Bomb('images/bomb/full.png', random.randint(100, 900), 600)

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
