# 课堂练习2
# 让飞机可以循环发射子弹，当子弹移出到屏幕外以后，继续从飞机处发射子弹。
# 提示：1.设置子弹的初始坐标 2.让子弹的y坐标不断减小，并且达到屏幕外以后，重新设置为初始坐标的位置
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((500, 850))
bg = pygame.image.load("bg.png")
bullet = pygame.image.load("bullet.png")
plane = pygame.image.load("plane.png")
screen.blit(bg, (0, 0))
pygame.display.update()

# 设置子弹的初始y坐标
y = 670

while True:
    screen.blit(bg, (0, 0))
    screen.blit(plane, (200, 680))
    screen.blit(bullet, (225, y))
    pygame.display.update()

    # 子弹移动
    y = y - 10
    if y < -150:
        y = 670

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
