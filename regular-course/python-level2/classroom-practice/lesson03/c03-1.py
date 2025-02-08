import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1000, 700))
car = pygame.image.load("car.png")
car1 = pygame.image.load("car1.png")
car2 = pygame.image.load("car2.png")
bg = pygame.image.load("bg.png")
cars = [car, car1, car2]
x = 100
y = 200
index = 0
while True:
    # 逐帧动画
    screen.blit(bg, (0, 0))
    screen.blit(cars[index], (x, y))
    pygame.display.update()

    index += 1
    if index == 3:
        index = 0
    # 事件获取
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
        # 键盘事件
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_UP:
                y = y - 10
            if e.key == pygame.K_DOWN:
                y = y + 10
