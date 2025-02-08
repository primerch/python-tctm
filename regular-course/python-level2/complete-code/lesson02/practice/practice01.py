# 课堂练习1
# 请创建500*750的窗口，完成按下键盘上的任意键，控制台都可以输出A的效果。
# 提示1：创建窗口使用set_mode函数
# 提示2：pygame.KEYDOWN表示按下了键盘按键。


import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((500, 750))
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
        if e.type == pygame.KEYDOWN:
            print('A')
