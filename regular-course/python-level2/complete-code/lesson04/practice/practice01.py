# 课堂练习1
# 1、请你查看demo.jpg的宽高，并且根据宽高，设置对应大小的窗口
# 2、将demo.jpg作为背景，显示出来
# 注意：背景需要完整覆盖窗口
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((650, 365))
bg = pygame.image.load("demo.jpg")
screen.blit(bg, (0, 0))
pygame.display.update()
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
