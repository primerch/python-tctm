# 21课
# 糖果生长动画及土壤点击
import pygame
import sys
import os
import time

# pygame初始化及设置
pygame.init()
screen = pygame.display.set_mode((1000, 700))


# 插入排序函数
def insertSort(mylist):
    for i in range(1, len(mylist)):
        for j in range(i, 0, -1):
            if mylist[j] < mylist[j - 1]:
                mylist[j], mylist[j - 1] = mylist[j - 1], mylist[j]
            else:
                break


# 构建动画字典，返回值是动画字典
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


# 资源加载
UIDict = createDict('images/UI/')
candyDict = createDict('images/candy/')
iconDict = createDict('images/icon/')

# 土壤种植信息字典
soilDict = {'soil1': {'name': 'blank', 'pos': (190, 330), 'time': 0},
            'soil2': {'name': 'blank', 'pos': (545, 330), 'time': 0},
            'soil3': {'name': 'blank', 'pos': (360, 240), 'time': 0},
            'soil4': {'name': 'blank', 'pos': (370, 425), 'time': 0}
            }

x, y = 0, 0
candyName = 'c0'
while True:

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
        elif e.type == pygame.MOUSEMOTION:
            x = e.pos[0]
            y = e.pos[1]
        elif e.type == pygame.MOUSEBUTTONDOWN:
            # 种植区域点击判断
            if 390 < y < 490:
                if 270 < x < 370:
                    print('点击了土地1')
                elif 615 < x < 715:
                    print('点击了土地2')
            elif 400 < x < 500:
                if 290 < y < 390:
                    print('点击了土地3')
                elif 480 < y < 580:
                    print('点击了土地4')
    # 绘制背景
    screen.blit(UIDict['map'][0], (0, 0))
    # 绘制糖果树
    pygame.display.update()
