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
        for name in names:
            img = pygame.image.load(path + key + '/' + name)
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
