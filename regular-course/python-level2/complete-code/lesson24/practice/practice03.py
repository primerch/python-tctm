# 课堂练习三
# 请完成打砖块游戏中，滑动鼠标滚轮控制底部滑板移动的效果
# 要求：1.每向下滑动滚轮一次，滑板x坐标增加30
#      2.每向上滑动滚轮一次，滑板x坐标减少30

import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1000, 600))
bg = pygame.image.load('images/bg.png')
# 滑板图片加载
board = pygame.image.load('images/board.png')

x = 392
y = 500
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
        elif e.type == pygame.MOUSEBUTTONDOWN:
            # 添加代码：向下滑动滚轮，x增加30；向上滑动滚轮，x减小30
            if e.button == 5:
                x += 30
            elif e.button == 4:
                x -= 30

    screen.blit(bg, (0, 0))
    screen.blit(board, (x, y))
    pygame.display.update()
