import pygame
import sys

pygame.init()
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('滑板少年')
# 加载背景图
bg = pygame.image.load('images/bg.png').convert_alpha()
# 角色站立名称列表
stands = ['stand.png', 'stand1.png', 'stand2.png', 'stand3.png']


# 加载序列图函数
def loadImg(names):
    images = []
    for name in names:
        pic = pygame.image.load('images/' + name).convert_alpha()
        images.append(pic)
    return images


# 加载角色站立图
standList = loadImg(stands)
timer = pygame.time.Clock()
running = True
state = 'start'
bx = 0
index = 0
playerX = 40
playerY = 330
delay = 0
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
    if state == 'start':
        screen.blit(bg, (bx, 0))
        screen.blit(bg, (bx + 800, 0))
        screen.blit(standList[index], (playerX, playerY))
        bx -= 10
        if bx <= -800:
            bx = 0
        delay += 1
        if delay % 15 == 0:
            index += 1
            if index == 3:
                index = 0
    if state == 'end':
        pass
    pygame.display.update()
    timer.tick(60)
pygame.quit()
sys.exit()
