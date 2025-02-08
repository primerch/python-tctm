import pygame
import sys
import os

# 初始化
pygame.init()
screen = pygame.display.set_mode((1000, 700))


# 插入排序
def insertSort(mylist):
    for i in range(1, len(mylist)):
        for j in range(i, 0, -1):
            if mylist[j] < mylist[j - 1]:
                mylist[j - 1], mylist[j] = mylist[j], mylist[j - 1]
            else:
                break


# 构建动画字典，返回值是动画字典
def createDict(path):
    keys = os.listdir(path)
    gameDict = dict.fromkeys(keys)
    for key in keys:
        pictures = []
        names = os.listdir(path + key + '/')
        for i in range(len(names)):
            names[i] = int(names[i].replace('.png', ''))
        insertSort(names)
        for name in names:
            img = pygame.image.load(path + key + '/' + str(name) + '.png')  # convert可以去掉
            pictures.append(img)
        gameDict[key] = pictures
    return gameDict


# 加载机甲图片
robotDict = createDict('../src/robot/')
# 初始y坐标
y = 0
# 步长
step = 1
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
    screen.blit(robotDict['bg'][0], (0, 0))
    # 请在下方编写代码
    screen.blit(robotDict['blue'][0], (0, y))  # 左臂
    screen.blit(robotDict['blue'][1], (0, y))  # 左腿
    screen.blit(robotDict['blue'][2], (0, y))  # 身体
    screen.blit(robotDict['blue'][3], (0, y))  # 头
    screen.blit(robotDict['blue'][4], (0, y))  # 右腿
    screen.blit(robotDict['blue'][5], (0, y))  # 右臂
    y += step
    if y >= 10:
        step = -1
    elif y <= 0:
        step = 1

    pygame.display.update()
    pygame.time.delay(25)
