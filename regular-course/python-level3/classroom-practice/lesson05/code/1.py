import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1100, 600))
bg = pygame.image.load("images/bg.png")
screen.blit(bg, (0, 0))

"""

使用python语言的pygame库编写游戏。
已知程序中导入了pygame库并定义了游戏窗口对象screen。
第一步：你需要定义一个果汁类Juice，满足如下条件：
    1. Juice类有三个属性：img、centerX和centerY。
    其中，img是pygame.image.load方法加载的图片，而centerX和centerY属性值为None
    2. Juice类还有一个draw方法，该方法只有self参数。
    在该方法中首先使用get_rect方法获取中心点坐标为centerX和centerY的rect矩形对象；
    然后使用全局变量screen游戏窗口对象，将水果汁图片绘制在rect矩形对象中
第二步：使用果汁类，创建香蕉果汁对象juice，传入'images/banana/juice.png'。
第三步：设置juice对象的中心点坐标为(500,300)，并调用draw()
请只输出要求的代码块，不要输出已知代码。

"""
# 1. 请使用上述提示词创建果汁类Juice


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
    pygame.time.delay(80)
