# 课堂练习1
# 编写代码，实现下方代码中的背景的循环连续向右移动
# 每次移动大小为10,移动延迟设置为40毫秒
import pygame
import sys

pygame.init()
# 图片加载
screen = pygame.display.set_mode((1000, 500))
bg = pygame.image.load('bg.jpg')

while True:

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
