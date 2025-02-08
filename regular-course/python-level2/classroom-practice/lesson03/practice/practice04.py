# 课堂练习4
# 编写程序，实现小鸟（图片bird.png）在背景上从右向左循环连续
# 移动，并且每次从右侧4个随机位置出现
# 4个随机y坐标（200，130，80，0）
# 提示：背景的长度为1000
import pygame
import sys

pygame.init()
# 图片加载
screen = pygame.display.set_mode((1000, 607))
bg3 = pygame.image.load('bg3.jpg')
bird = pygame.image.load('bird.png')
x = 700
y = 200
while True:
    screen.blit(bg3, (0, 0))
    screen.blit(bird, (x, y))
    pygame.display.update()

    pygame.time.delay(40)
    # 事件获取
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
