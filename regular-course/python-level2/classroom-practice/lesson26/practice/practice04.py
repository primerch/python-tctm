# 课堂练习四
# 将有关家具的描述文字，分行显示在程序界面右上角的简介中
# 提示：1.要求每行最多显示15个字，超过15个字的部分换到下一行显示
#      2.描述文字存储在变量text中；字体已经加载好并存入变量font中
#      3.第一行文字的坐标为(770,220)，行与行之间y坐标相差30

import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1200, 656))
bg = pygame.image.load('images/practice04/0.png')
# 描述文字
text = '温馨粉色的梦幻床，给你带来极致的舒适。据说躺在上面，入眠如诗美梦连连，让你每晚都能享受到宛如仙境的甜美睡眠。'
# 字体
font = pygame.font.SysFont('simhei', 15)

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
        elif e.type == pygame.MOUSEBUTTONDOWN:
            x = e.pos[0]
            y = e.pos[1]
            print(x, y)
    screen.blit(bg, (0, 0))
    # 请在下方完成分行显示的代码

    pygame.display.update()
