# 课堂练习1
# 请完成按下鼠标的任意键，控制台都可以输出“点击了鼠标”的效果。

# 提示1：按下鼠标会触发pygame.MOUSEBUTTONDOWN事件。


import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((400, 400))
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
        if e.type == pygame.MOUSEBUTTONDOWN:
            print('点击了鼠标')
