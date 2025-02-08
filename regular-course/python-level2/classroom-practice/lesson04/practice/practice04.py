# 课堂练习4
# 请完成如下功能：
# 手hand可以左右移动，接到金币后，金币消失
# 提示1：类比小车吃金币的效果；金币落下，需要改变y坐标
# 提示2：y坐标为一个碰撞范围，x坐标是判断相等即可。
# 提示3：碰撞后消失，移动到屏幕上方，y=-200的位置。

import pygame
import sys
import random

pygame.init()
screen = pygame.display.set_mode((500, 750))
bg = pygame.image.load("bg1.png")
hand = pygame.image.load("hand.png")
coin = pygame.image.load("coin.png")
screen.blit(bg, (0, 0))
pygame.display.update()

x = 100
x1 = 100
y1 = -200
while True:
    screen.blit(bg, (0, 0))
    screen.blit(hand, (x, 600))
    screen.blit(coin, (x1, y1))
    pygame.display.update()
    # 随机出现金币掉落，以及碰到后金币消失

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
        # 按下键盘的效果
