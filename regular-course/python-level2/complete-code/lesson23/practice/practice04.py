# 课堂练习4
# 获取当前时间，并以 时：分：秒 的格式显示在界面中(300,300)的位置
import pygame
import sys
import time
import platform

# pygame初始化及设置
pygame.init()
screen = pygame.display.set_mode((1000, 700))
pygame.mouse.set_visible(False)
bg1 = pygame.image.load("img/bg.png")
# 字体设置
# windows字体    fangsong        simhei       kaiti
# macOS字体      arialunicode    pingfang     songti
osName = platform.system()
print(osName)

if osName == 'Windows':
    font = pygame.font.SysFont('simhei', 100)
elif osName == 'macOS':
    font = pygame.font.SysFont('songti', 100)


def showTime():
    datetime = time.strftime("%H:%M:%S", time.localtime())
    fs = font.render(datetime, True, 'white')
    screen.blit(fs, (300, 300))


while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
    screen.blit(bg1, (0, 0))
    showTime()
    pygame.display.update()
