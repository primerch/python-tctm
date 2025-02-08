# 课堂练习四
# 请完善drawPlant()函数，实现植物每隔两秒生长一次的效果
# 提示： 1.植物图片存储于images下的img04中，images中的图片已预留加载并存储在变量imgDict中
#       2.植物图片与背景图片尺寸相同，将其绘制在(0,0)位置即可

import pygame
import sys
import os
import time

pygame.init()
screen = pygame.display.set_mode((1200, 642))


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

# 初始时间
t = time.time()


# 绘制植物函数
def drawPlant():
    # 请在下方编写植物生长的代码
    level = (time.time() - t) // 2
    if level > 7:
        level = 7
    screen.blit(imgDict['img04'][int(level)], (0, 0))


while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
    screen.blit(imgDict['bg'][2], (0, 0))
    # 绘制植物
    drawPlant()
    pygame.display.update()
