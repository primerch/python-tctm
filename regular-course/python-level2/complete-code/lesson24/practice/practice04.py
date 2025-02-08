# 课堂练习四
# 实现背包的显示与关闭
# 提示：1.背包图片已经加载完毕并存入变量 bag
#      2.通过变量menu控制背包的显示与隐藏：menu值为0，隐藏；menu值为1，显示
#      3.通过点击背包按钮，让背包显示；点击叉号按钮，让背包隐藏

import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1000, 667))
bg = pygame.image.load('images/bg2.png')
# 背包图片加载
bag = pygame.image.load('images/bag.png')

# 添加代码：通过menu控制背包的显示与隐藏，默认隐藏状态
menu = 0
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
        elif e.type == pygame.MOUSEBUTTONDOWN:
            x = e.pos[0]
            y = e.pos[1]
            # 点击背包
            if 45 < x < 160 and 40 < y < 90:
                # 添加代码：让背包显示
                menu = 1
            # 点击叉号
            elif 800 < x < 860 and 70 < y < 130:
                # 添加代码：让背包隐藏
                menu = 0
    screen.blit(bg, (0, 0))
    # 添加代码：若menu为显示状态，绘制背包图片
    if menu == 1:
        screen.blit(bag, (0, 0))
    pygame.display.update()
