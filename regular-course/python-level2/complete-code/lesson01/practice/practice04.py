# 课堂练习4
# 编写代码，将青蛙的图片frog.png绘制到背景图片bg2.jpg的合适位置
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((700, 400))
# 请在下方完成代码
bg2 = pygame.image.load("bg2.jpg")
frog = pygame.image.load("frog.png")
screen.blit(bg2, (0, 0))
screen.blit(frog, (470, 250))
pygame.display.update()
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
