import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1000, 700))

# 图片名称列表
names = ['bg', 'for', 'list', 'random', 'function', 'box', 'lose', 'win', 'm0', 'm1']
# 图片存储列表
plist = []

# 图片加载
for name in names:
    pic = pygame.image.load('images/%s.png' % (name))
    print('图片' + name + '加载完毕')
    plist.append(pic)

# 游戏资源加载
screen.blit(plist[0], (0, 0))
pygame.display.update()
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
        if e.type == pygame.MOUSEMOTION:
            screen.blit(plist[0], (0, 0))
            x = e.pos[0]
            y = e.pos[1]
            print('鼠标的x坐标是: % d, y坐标是 % s' % (x, y))
            if 130 < x < 200 and 300 < y < 400:
                screen.blit(plist[1], (0, 0))
            elif 220 < x < 320 and 80 < y < 180:
                screen.blit(plist[2], (0, 0))
            elif 650 < x < 750 and 150 < y < 210:
                screen.blit(plist[3], (0, 0))
            elif 720 < x < 820 and 320 < y < 420:
                screen.blit(plist[4], (0, 0))
            elif 400 < x < 620 and 300 < y < 450:
                screen.blit(plist[5], (0, 0))
            pygame.display.update()
