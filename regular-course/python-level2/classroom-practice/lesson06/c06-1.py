import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1000, 700))

# 图片名称列表
names = ['bg', 'for', 'list', 'random', 'function', 'box', 'lose', 'win', 'm0', 'm1']

# 游戏资源加载
screen.blit(bg, (0, 0))
pygame.display.update()
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
