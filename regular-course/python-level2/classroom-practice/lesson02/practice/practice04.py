# 课堂练习4
# 按下空格键，可以让小人跳跃。
# 要求
# 1、所有图片都绘制在（0,0）的位置上
# 2、按下按键空格(K_SPACE),可以播放0,1,2三张图片
# 3、抬起按键（e.type == pygame.KEYUP）,可以播放3-12的图片
# 4、播放每张图片后，可以休眠0.1秒
# 提示：休眠可以先import time,再用time.sleep(休眠时间)
import pygame
import sys
import time

pygame.init()
screen = pygame.display.set_mode((400, 200))
bg = pygame.image.load("bg1.png")
screen.blit(bg, (0, 0))
pygame.display.update()
jump0 = pygame.image.load("0.png")
jump1 = pygame.image.load("1.png")
jump2 = pygame.image.load("2.png")
jump3 = pygame.image.load("3.png")
jump4 = pygame.image.load("4.png")
jump5 = pygame.image.load("5.png")
jump6 = pygame.image.load("6.png")
jump7 = pygame.image.load("7.png")
jump8 = pygame.image.load("8.png")
jump9 = pygame.image.load("9.png")
jump10 = pygame.image.load("10.png")
jump11 = pygame.image.load("11.png")
jump12 = pygame.image.load("12.png")
jump = [jump0, jump1, jump2, jump3, jump4, jump5, jump6, jump7, jump8, jump9, jump10, jump11, jump12]

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
    # 请在下方编写代码
