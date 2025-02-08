# 课堂练习1
# 编写代码获取鼠标点击游戏窗口时的坐标
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1000, 700))

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
