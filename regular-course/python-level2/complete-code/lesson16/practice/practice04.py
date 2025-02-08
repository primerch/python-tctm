# 课堂练习4
# 通过等比缩放的形式将后边的那只燕子（bird2）缩小为长100，高100的大小
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1000, 625))
bg = pygame.image.load("pictures/bg1.png")
bird1 = pygame.image.load("pictures/bird1.png")
bird2 = pygame.image.load("pictures/bird2.png")
# 进行图像缩放
bird2 = pygame.transform.scale(bird2, (100, 100))

while True:
    screen.blit(bg, (0, 0))
    screen.blit(bird1, (400, 200))
    screen.blit(bird2, (500, 250))
    # 事件获取
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()
