# 课堂练习3
# 1、计算bean与pic的碰撞范围
# 2、设置在两张图片碰到以后，pic消失（被吃掉的感觉）
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1300, 600))
bg = pygame.image.load("bg2.png")
screen.blit(bg, (0, 0))
pygame.display.update()
pic = pygame.image.load("pic.png")
bean = pygame.image.load("0.png")
bean1 = pygame.image.load("1.png")
bean2 = pygame.image.load("2.png")
bean3 = pygame.image.load("3.png")
bean4 = pygame.image.load("4.png")
bean5 = pygame.image.load("5.png")
bean6 = pygame.image.load("6.png")
bean7 = pygame.image.load("7.png")
bean8 = pygame.image.load("8.png")
bean9 = pygame.image.load("9.png")
beans = [bean, bean1, bean2, bean3, bean4, bean5, bean6, bean7, bean8, bean9]
index = 0
x = 1400
while True:
    screen.blit(bg, (0, 0))
    screen.blit(pic, (x, 280))
    screen.blit(beans[index], (250, 150))
    pygame.display.update()
    index = index + 1
    if index == 10:
        index = 0
    x = x - 10
    if x < -150:
        x = 1400
    # 在这里判断范围

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
