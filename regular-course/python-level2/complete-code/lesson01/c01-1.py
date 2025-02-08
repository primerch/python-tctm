# 创建一个长1000宽700的游戏窗口
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1000, 700))
# 图片的加载
bg = pygame.image.load("bg.png")
car = pygame.image.load("car.png")
# 图片的绘制和显示
screen.blit(bg, (0, 0))
screen.blit(car, (400, 350))
pygame.display.update()
while True:
    # 事件的监听
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
