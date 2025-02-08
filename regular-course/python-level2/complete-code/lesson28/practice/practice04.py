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
# 图片的加载
bg = pygame.image.load("pic/bg.png")
# 图片的绘制和显示
start = time.time()
while True:
    now = time.time()
    timeLeft = 10 - (now - start)
    if timeLeft <= 0:
        timeLeft = 0
    else:
        t = f'倒计时：{int(timeLeft)}秒'
        fs = font.render(t, True, 'white')
        screen.blit(bg, (0, 0))
        screen.blit(fs, (300, 200))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()
