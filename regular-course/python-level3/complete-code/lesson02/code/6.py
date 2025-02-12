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


apple = Fruit('images/apple/full.png', random.randint(100, 900), 600)
banana = Fruit('images/banana/full.png', random.randint(100, 900), 600)
orange = Fruit('images/orange/full.png', random.randint(100, 900), 600)


class Bomb:
    def __init__(self, img, x, y):
        self.img = pygame.image.load(img)
        self.x = x
        self.y = y
        # 1.定义speedX和SpeedY属性，添加水平和垂直方向的随机初始速度
        self.speedY = random.randint(30, 48)
        self.speedX = random.randint(-10, 10)

    def draw(self):
        screen.blit(self.img, (self.x, self.y))

    # 2.在炸弹类中定义move方法
    def move(self):
        self.y -= self.speedY
        self.speedY -= 2
        self.x -= self.speedX


# 3. 修改炸弹初始x坐标为100-900范围内的随机值，y坐标为600
bomb1 = Bomb('images/bomb/full.png', random.randint(100, 900), 600)
bomb2 = Bomb('images/bomb/full.png', random.randint(100, 900), 600)

while True:
    screen.blit(bg, (0, 0))
    apple.draw()
    banana.draw()
    orange.draw()
    bomb1.draw()
    bomb2.draw()
    apple.move()
    banana.move()
    orange.move()
    # 4.炸弹对象bomb1,bomb2分别调用move方法
    bomb1.move()
    bomb2.move()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
    pygame.time.delay(80)
