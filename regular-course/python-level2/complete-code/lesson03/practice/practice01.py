# 课堂练习1
# 编写代码，实现下方代码中的背景的循环连续向右移动
# 每次移动大小为10,移动延迟设置为40毫秒
import pygame
import sys

pygame.init()
# 图片加载
screen = pygame.display.set_mode((1000, 500))
bg = pygame.image.load('bg.jpg')
bx = 0
while True:
    screen.blit(bg, (bx, 0))
    screen.blit(bg, (bx - 1000, 0))
    pygame.display.update()
    bx = bx + 10
    if bx - 1000 == 0:
        bx = 0
    pygame.time.delay(40)
    # 事件获取
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
