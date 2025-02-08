# 课堂练习3
# 编写代码，完成按下键盘B键，烟花爆炸的效果。
# 要求：
# 1、加载boom1,boom2,boom3三张图片，绘制在150，150的位置上。
# 2、按下按键B(K_b),可以播放一次烟花效果，切换一次爆炸图片
# 3、按下B键后，让烟花动画播放21次
# 4、循环后，再绘制一个背景图片和爆竹图片。
# 提示：按下按键后再增加一个for循环，并在每次循环中增加一个延时效果，可以用time.sleep(0.05)实现
import pygame
import sys
import time

pygame.init()
screen = pygame.display.set_mode((500, 750))
bg = pygame.image.load("bg.png")
baozhu = pygame.image.load("baozhu.png")
screen.blit(bg, (0, 0))
screen.blit(baozhu, (180, 550))
pygame.display.update()
boom1 = pygame.image.load("boom1.png")
boom2 = pygame.image.load("boom2.png")
boom3 = pygame.image.load("boom3.png")

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
    # 请在下方编写代码
