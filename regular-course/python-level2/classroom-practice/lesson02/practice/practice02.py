# 课堂练习2
# 请编写代码，实现按下键盘数字1键，控制台输出  '1键被按下'  的效果。
# 提示1：具体的键盘按键使用e.key进行判断，按键1的表示方式为pygame.K_1

import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((500, 750))
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()

    # 请在下方编写代码
