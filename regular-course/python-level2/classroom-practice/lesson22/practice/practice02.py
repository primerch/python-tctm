# 课堂练习二
# 请为本程序的开始界面设置相应的鼠标样式
# 提示： 1.鼠标图片存储于images下的img02中，images中的图片已预留加载并存储在变量imgDict中
#       2.代码注释中会给出相应提示

import pygame
import sys
import os

pygame.init()
screen = pygame.display.set_mode((1280, 610))


# 请在下方隐藏鼠标箭头


def insertSort(mylist):
    for i in range(1, len(mylist)):
        for j in range(i, 0, -1):
            if mylist[j] < mylist[j - 1]:
                mylist[j], mylist[j - 1] = mylist[j - 1], mylist[j]
            else:
                break


def createDict(path):
    keys = os.listdir(path)
    gameDict = dict.fromkeys(keys)
    for key in keys:
        gameDict[key] = []
        names = os.listdir(path + key + '/')
        for i in range(len(names)):
            names[i] = int(names[i].replace('.png', ''))
        insertSort(names)
        for name in names:
            img = pygame.image.load(path + key + '/' + str(name) + '.png')
            gameDict[key].append(img)
    return gameDict


# 图片加载
imgDict = createDict('images/')

x, y = 0, 0
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
        elif e.type == pygame.MOUSEMOTION:
            # 请在鼠标移动事件中，实时获取鼠标的x、y坐标
            pass
    screen.blit(imgDict['bg'][0], (0, 0))
    # 请在下方绘制鼠标箭头

    pygame.display.update()
