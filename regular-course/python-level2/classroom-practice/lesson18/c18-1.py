import pygame
import sys
import os
import random

# 初始化及背景显示
pygame.init()
screen = pygame.display.set_mode((1000, 700))
# 字体设置
# windows字体    fangsong        simhei       kaiti
# macOS字体      arialunicode    pingfang     songti

font = pygame.font.SysFont('simhei', 20)

#######单人角色属性字典，
playerData = {
    'def': 50,
    'atk': 100,
    'magic': 1000,
    'addHP': 200,
    'addAtk': 200,
    'addDef': 100,
    'HP': 1000,
    'maxHP': 1000,
}
# boss属性字典
bossData = {
    'def': 50,
    'ice': 100,
    'earth': 200,
    'fire': 300,
    'wind': 400,
    'HP': 10000,
}


# 插入排序
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
    keys = os.listdir(path)  # print()列表
    # 以文件夹名字列表构建字典
    gameDict = dict.fromkeys(keys)  # print()空字典
    # 字典赋值
    for key in keys:
        pictures = []
        # 获取图片的名字（全名包括扩展名）
        names = os.listdir(path + key + '/')
        # 把图片变量存在picture列表中
        for i in range(len(names)):
            names[i] = int(names[i].replace('.png', ''))
        insertSort(names)
        for name in names:
            # 把.png拼上
            img = pygame.image.load(path + key + '/' + str(name) + '.png')  # convert可以去掉
            pictures.append(img)
        gameDict[key] = pictures
    return gameDict


# 绘制单独角色UI函数，角色字典名，坐标x，y
def showHP(x, y, hp, name):  # x,y固定值
    if name == 'player':
        length = int(0.1 * hp)
    elif name == 'boss':
        length = int(0.01 * hp)
    # 保证血条，不能为负值。
    if length < 0:
        length = 0
    # 缩放图片，参数：图片变量；缩放的像素大小
    bar = pygame.transform.scale(uiDict['HPbar'][0], (length, 13))
    screen.blit(bar, (x, y))


# 显示人物属性
offset = 0


def showData(d):
    global offset
    if d == playerData:
        x = 260
        gap = 21
    else:
        x = 700
        gap = 25
    for k, v in d.items():
        if k != 'maxHP':
            words = k + ':' + str(v)
            text = font.render(words, True, 'black')
            screen.blit(text, (x, 516 + offset * gap))
            offset += 1
    offset = 0


# 动画状态帧
player = 0
boss = 0


def showActor(dict, file, pos=(0, 0)):
    global player, boss
    if dict == playerDict:
        if player >= len(dict[file]):
            player = 0
        screen.blit(dict[file][player], pos)
        player += 1
    else:
        if boss >= len(dict[file]):
            boss = 0
        screen.blit(dict[file][boss], pos)
        boss += 1


state = 'loading'
turn = 'player'
choose = 'doing'

while True:
    # 事件获取
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
        # 键盘按下事件
        if e.type == pygame.KEYDOWN:
            # 回车键进入游戏
            if e.key == pygame.K_KP_ENTER or e.key == pygame.K_RETURN:
                state = 'running'
            # 空格键选择完毕
            if e.key == pygame.K_SPACE:
                choose = 'done'
    # 资源加载
    if state == 'loading':
        # 资源加载（更换图片）
        uiDict = createDict('UI/')
        screen.blit(uiDict['start'][0], (0, 0))
        pygame.display.update()

        playerDict = createDict('animation/player/')
        screen.blit(uiDict['start'][1], (0, 0))
        pygame.display.update()

        bossDict = createDict('animation/boss/')
        screen.blit(uiDict['start'][3], (0, 0))
        pygame.display.update()

        pygame.time.delay(500)
        state = 'start'
    # 游戏开始画面
    elif state == 'start':
        # 显示开始界面,按enter
        screen.blit(uiDict['start'][4], (0, 0))
    # 游戏进行状态
    elif state == 'running':
        # 绘制背景
        screen.blit(uiDict['map'][0], (0, 0))
        # 显示面板UI
        showHP(86, 642, playerData['HP'], 'player')
        showHP(818, 642, bossData['HP'], 'boss')
        # 显示属性
        showData(playerData)
        showData(bossData)
        # 玩家回合
        if turn == 'player':
            # 技能选择
            if choose == 'doing':
                # 双方闲置动画
                showActor(playerDict, 'idle')
                showActor(bossDict, 'idle')

            else:
                # BOSS为闲置动画
                showActor(bossDict, 'idle')
                showActor(playerDict, 'magic')
                # 玩家技能播放
                num = len(playerDict['magic'])
                if player >= num:
                    randomSkill = random.choice(['ice', 'earth', 'fire', 'wind'])
                    turn = 'boss'
        # boss回合
        elif turn == 'boss':
            # player为闲置动画
            showActor(playerDict, 'idle')
            showActor(bossDict, randomSkill)
            num = len(bossDict[randomSkill])
            if boss >= num:
                choose = 'doing'
                turn = 'player'
            # 游戏结束状态，显示胜利或者失败
        if playerData['HP'] <= 0 or bossData['HP'] <= 0:
            # 双方任意一方没血，结束游戏
            state = 'end'
    elif state == 'end':
        pass
    # 全局更新
    pygame.display.update()
    pygame.time.delay(100)
