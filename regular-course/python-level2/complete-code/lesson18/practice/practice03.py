# 课堂练习3
# 编写代码完成点击答案两个字，出现灯谜答案的效果
# 提示1：文字灯谜的x坐标范围为 420<x<560 y坐标范围为 400<y<472
# 提示2：图片bg2为灯谜答案图片，显示坐标为(0,0)
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1000, 602))
# 图片的加载
bg1 = pygame.image.load("pic/guess1.png")
bg2 = pygame.image.load("pic/guess2.png")
# 图片的绘制和显示
screen.blit(bg1, (0, 0))
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
        if e.type == pygame.MOUSEBUTTONDOWN:
            x = e.pos[0]
            y = e.pos[1]
            print(x, y)
            if 420 < x < 560 and 400 < y < 472:
                screen.blit(bg2, (0, 0))
    pygame.display.update()
