# 课堂练习3
# 编写代码将文件名称为：bg.jpg的图片加载并显示在下方
# 窗口中作为窗口的背景
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 500))
# 请在下方完成代码


while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
