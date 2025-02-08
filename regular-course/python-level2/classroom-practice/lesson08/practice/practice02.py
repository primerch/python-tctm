# 课堂练习2
# 请完成如下效果：在键盘上输入数字以及小写字母，可以在控制台输出对应的值

# 提示1：键盘按键事件pygame.KEYDOWN
# 提示2：先通过e.key()获得按键的数值，再通过chr()将其转为ASCII码对应的字符，最后输出

import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((400, 400))
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
