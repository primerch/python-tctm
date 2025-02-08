# 课堂练习四
# 利用时间戳，在窗口背景中实现一个倒计时10秒的程序
import pygame
import sys
import platform

pygame.init()
import time

osName = platform.system()
screen = pygame.display.set_mode((1000, 571))
if osName == 'Windows':
    font = pygame.font.SysFont('simhei', 70)
elif osName == 'Darwin':
    font = pygame.font.SysFont('songti', 70)
bg = pygame.image.load("pic/bg.png")

while True:
    screen.blit(bg, (0, 0))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()
