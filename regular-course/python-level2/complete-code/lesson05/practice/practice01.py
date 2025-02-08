# 课堂练习1
# 完善程序，实现当按下任意键时画面由背景day.jpg变换成night.jpg
# 提示：可以设置'day'和’night‘两个状态来区分不同的场景
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1000, 700))
day = pygame.image.load('day.jpg')
night = pygame.image.load('night.jpg')
# 请在下方完善代码
state = 'day'
while True:
    if state == 'day':
        screen.blit(day, (0, 0))
    if state == 'night':
        screen.blit(night, (0, 0))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
        if e.type == pygame.KEYDOWN:
            state = 'night'
    pygame.display.update()
