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
        for i in range(len(names)):
            names[i] = int(names[i].replace('.png', ''))
        insertSort(names)
        # print(names)
        for name in names:
            # 把.png拼上
            img = pygame.image.load(path + key + '/' + str(name) + '.png')
            gameDict[key].append(img)
    return gameDict


# 游戏状态
state = 'loading'
# 区分双方回合
turn = 'player'
# 技能选择情况
choose = 'doing'
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
        # 监听键盘按下事件
        if e.type == pygame.KEYDOWN:
            # 按下Enter键进入游戏
            if e.key == pygame.K_RETURN:
                state = 'running'
            # 按下空格键发起攻击
            if e.key == pygame.K_SPACE:
                choose = 'done'
    # 加载状态
    if state == 'loading':
        # UI加载
        uiDict = createDict('UI/')
        screen.blit(uiDict['start'][0], (0, 0))
        pygame.display.update()
        # 玩家图片加载
        playerDict = createDict('animation/player/')
        screen.blit(uiDict['start'][1], (0, 0))
        pygame.display.update()
        # boss图片加载
        bossDict = createDict('animation/boss/')
        screen.blit(uiDict['start'][2], (0, 0))
        pygame.display.update()
        pygame.time.delay(500)
        state = 'start'
    # 开始状态
    elif state == 'start':
        screen.blit(uiDict['start'][3], (0, 0))
    # 进行状态
    elif state == 'running':
        screen.blit(uiDict['map'][0], (0, 0))
        # 玩家回合
        if turn == 'player':
            if choose == 'doing':
                print('技能选择中…')
            else:
                print('玩家开始攻击，boss不动')
                turn = 'boss'
        # boss回合
        elif turn == 'boss':
            print('boss开始攻击，玩家不动')
            turn = 'player'
        # 判断游戏是否结束
        if playerData['HP'] <= 0 or bossData['HP'] <= 0:
            state = 'end'
    # 结束状态
    elif state == 'end':
        print('游戏结束')

    pygame.display.update()
    pygame.time.delay(100)
