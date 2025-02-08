import pygame
import sys
import random

pygame.init()
# 图片加载
screen = pygame.display.set_mode((1000, 700))
car = pygame.image.load("car.png")
car1 = pygame.image.load("car1.png")
car2 = pygame.image.load("car2.png")
bg = pygame.image.load("bg.png")
block = pygame.image.load('block.png')
cars = [car, car1, car2]

x = 40
y = 300
bx = 0
x1 = 1250
y1 = 300
index = 0

coin = pygame.image.load('coin.png')
x2 = 1550
y2 = 300

while True:
    # 逐帧动画
    screen.blit(bg, (bx, 0))
    screen.blit(bg, (bx + 1000, 0))
    screen.blit(cars[index], (x, y))
    screen.blit(block, (x1, y1))

    screen.blit(coin, (x2, y2))

    pygame.display.update()
    pygame.time.delay(10)

    index += 1
    if index == 3:
        index = 0

    bx = bx - 10
    if bx + 1000 == 0:
        bx = 0

    x1 = x1 - 10
    if x1 < -150:
        x1 = 1250
        y1 = random.choice([150, 300, 450])

    x2 = x2 - 10
    if x2 < -150:
        x2 = 1550
        y2 = random.choice([150, 300, 450])

    ############碰撞检测#############
    if y == y1 and -50 < x1 < 375:
        print('撞到障碍物了！')
        x1 = 1250
        y1 = random.choice([150, 300, 450])

    if y == y2 and -50 < x2 < 375:
        print('撞到金币了！')
        x2 = 1550
        y2 = random.choice([150, 300, 450])
    #################################

    # 事件获取
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
        # 键盘事件
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_UP:
                y = y - 150
                if y == 0:
                    y = 150
            if e.key == pygame.K_DOWN:
                y = y + 150
                if y == 600:
                    y = 450
