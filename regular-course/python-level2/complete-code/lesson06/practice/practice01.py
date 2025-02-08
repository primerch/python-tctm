# 课堂练习一
# 利用pygame的image的load()函数，分别加载images文件夹下的图片：'tong.png'、'while.png'、及'bg.png'
# 在pygame 窗口同时显示背景、童童及while精灵
# 童童的参考坐标：(450,300)
# while精灵的参考坐标：(650,300)
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1000, 700))
# 图片加载
bg = pygame.image.load('images/bg.png')
actor1 = pygame.image.load('images/tong.png')
actor2 = pygame.image.load('images/while.png')
# 图片显示
screen.blit(bg, (0, 0))
screen.blit(actor1, (450, 300))
screen.blit(actor2, (650, 300))
# 刷新屏幕
pygame.display.update()
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
