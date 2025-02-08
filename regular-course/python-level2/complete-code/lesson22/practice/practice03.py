# 课堂练习三
# 完善程序，实现点击工具栏选择防御塔，并让鼠标变成相应样式的效果
# 提示： 1.鼠标图片存储于images下的img03中，images中的图片已预留加载并存储在变量imgDict中
#       2.工具栏中的四个防御塔图标 y坐标范围均在 540-620之间
#         防御塔 1 x范围：285-365   防御塔 2 x范围：400-480
#         防御塔 3 x范围：520-600   防御塔 4 x范围：625-705
#       3.变量pointer用来存储鼠标图片
import pygame
import sys
import os

pygame.init()
screen = pygame.display.set_mode((1000, 667))
pygame.mouse.set_visible(False)


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
# 默认鼠标样式
pointer = imgDict['img03'][0]
x, y = 0, 0
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
        elif e.type == pygame.MOUSEMOTION:
            x = e.pos[0]
            y = e.pos[1]
        elif e.type == pygame.MOUSEBUTTONDOWN:
            if 540 < y < 620:
                if 285 < x < 365:
                    # 请在下方将鼠标切换为防御塔1的图片
                    pointer = imgDict['img03'][1]
                elif 400 < x < 480:
                    # 请在下方将鼠标切换为防御塔2的图片
                    pointer = imgDict['img03'][2]
                elif 520 < x < 600:
                    # 请在下方将鼠标切换为防御塔3的图片
                    pointer = imgDict['img03'][3]
                elif 625 < x < 705:
                    # 请在下方将鼠标切换为防御塔4的图片
                    pointer = imgDict['img03'][4]

    screen.blit(imgDict['bg'][1], (0, 0))
    screen.blit(pointer, (x - 30, y - 30))
    pygame.display.update()
