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
index = 0
x1 = 550
y1 = 300

while True:
    screen.blit(bg, (bx, 0))
    screen.blit(bg, (bx + 1000, 0))
    screen.blit(cars[index], (x, y))
    screen.blit(block, (x1, y1))
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
        x1 = 1000
        y1 = random.choice([150, 300, 450])

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
