# 课堂练习2
# 编写代码为下方窗口添加一个可以通过点击关闭按钮结束游戏的功能
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 500))
# 请在下方完成代码
import sys

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
