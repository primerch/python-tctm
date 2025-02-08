# 课堂练习三
# 完成点击选项卡切换菜单页的效果（底部的1 2 3表示选项卡）
# 提示： 1.三张菜单页的图片均加载好存入列表menu，默认显示第一张
#       2.请在鼠标点击事件中完成点击选项卡切换菜单页的功能
#       3.通过变量tab控制选项卡的切换

import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1200, 900))
# 菜单图片加载
menu = []
for i in range(3):
    menu.append(pygame.image.load('images/practice03/' + str(i) + '.jpg'))

tab = 0
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
        elif e.type == pygame.MOUSEBUTTONDOWN:
            x = e.pos[0]
            y = e.pos[1]
            # 请在下方完成点击选项卡切换菜单页
            # 选项卡1的坐标范围 x: 545~565 y:680~705
            # 选项卡2的坐标范围 x: 585~605 y:680~705
            # 选项卡3的坐标范围 x: 635~655 y:680~705

    screen.blit(menu[tab], (0, 0))
    pygame.display.update()
