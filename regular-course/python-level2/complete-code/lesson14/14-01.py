import pygame
import sys
import os

# 初始化及背景显示
pygame.init()
screen = pygame.display.set_mode((1000, 700))

# 单人角色属性字典，
playerData = {
    'HP': 1000,
    'maxHP': 1000,
    'atk': 100,
    'def': 50,
    'addHP': 200,
    'addAtk': 200,
    'addDef': 100,
    'magic': 1000
}
# boss属性字典
bossData = {
    'atk': 300,
    'def': 50,
    'HP': 10000,
    's1': 100,
    's2': 200,
    's3': 300,
    's4': 400,
}


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
    # 获取文件夹名字
    keys = os.listdir(path)
    # 以文件夹名字列表构建字典
    gameDict = dict.fromkeys(keys)
    # 字典赋值
    for key in keys:
        gameDict[key] = []
        # 获取图片的名字（全名包括扩展名）
        names = os.listdir(path + key + '/')
        # 把图片变量存在picture列表中
        for i in range(len(names)):
            names[i] = int(names[i].replace('.png', ''))
        insertSort(names)
        print(names)
        for name in names:
            # 把.png拼上
            img = pygame.image.load(path + key + '/' + str(name) + '.png')
            gameDict[key].append(img)
    return gameDict


# 构建角色字典
playerDict = createDict('animation/player/')
bg = pygame.image.load('bg.png')

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
    # 测试动画序列
    for img in playerDict['attack']:
        screen.blit(bg, (0, 0))
        screen.blit(img, (0, 150))
        pygame.display.update()
        pygame.time.delay(100)
