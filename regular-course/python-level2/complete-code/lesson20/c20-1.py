import pygame
import sys
import os
import random

pygame.init()
screen = pygame.display.set_mode((1000, 700))
font = pygame.font.SysFont('simhei', 18)

# 塔影守卫属性字典，
playerData = {
    'def': 50,
    'atk': 100,
    'HP': 1000,
    'maxHP': 1000,
}

# 魔兽属性字典
bossData = {
    'def': 50,
    'magic': 150,
    'cards': 200,
    'grab': 250,
    'bow': 300,
    'HP': 10000,
}


# 插入排序
def insertSort(mylist):
    for i in range(1, len(mylist)):
        for j in range(i, 0, -1):
            if mylist[j] < mylist[j - 1]:
                mylist[j - 1], mylist[j] = mylist[j], mylist[j - 1]
            else:
                break


# 加载图片，构建动画字典
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
            img = pygame.image.load(path + key + '/' + str(name) + '.png')
            pictures.append(img)
        gameDict[key] = pictures
    return gameDict


# 背景控制
def bgControl():
    global index, angerAnimation
    if angerSkill and not angerAnimation:
        screen.blit(uiDict['map'][3], (0, 0))
        screen.blit(uiDict['anger1'][index], (0, 0))
        index += 1
        if index == 10:
            index = 0
            angerAnimation = True
    elif angerAnimation:
        screen.blit(uiDict['map'][3], (0, 0))
        screen.blit(uiDict['anger2'][index], (0, 0))
        index += 1
        if index == 12:
            index = 0
    else:
        screen.blit(uiDict['map'][skill], (0, 0))


# 绘制血条
def showHP(x, y, hp, name):
    if name == 'player':
        ratio = int(0.25 * hp)
    elif name == 'boss':
        ratio = int(0.025 * hp)
    if ratio < 0:
        ratio = 0
    bar = pygame.transform.scale(uiDict['HPbar'][0], (ratio, 13))
    screen.blit(bar, (x, y))


# 绘制角色
def showActor(dict, file, pos=(0, 0)):
    global player, boss
    list = dict[file]
    num = len(list)
    if dict == playerDict:
        if player >= num:
            player = 0
        screen.blit(list[player], pos)
        player += 1
    else:
        if boss >= num:
            boss = 0
        screen.blit(list[boss], pos)
        boss += 1


# 显示人物属性
def showData(dict):
    global offset
    row = 1
    if dict == playerData:
        x = 190
        gap = 30
    else:
        x = 620
        gap = 29
        distance = 138
    for k, v in dict.items():
        if k != 'maxHP':
            if row > 3:
                row = 1
                offset = 0
                x += distance
            words = k + ':' + str(v)
            text = font.render(words, True, 'white')
            screen.blit(text, (x, 42 + offset * gap))
            row += 1
            offset += 1
    offset = 0


# 塔影守卫技能
def playerSkill(playerState):
    global anger
    if playerState == 'attack':
        damage = (playerData['atk'] - bossData['def'])
        bossData['HP'] -= damage
        anger = 0
    elif playerState == 'defense':
        playerData['def'] += 150
    elif playerState == 'anger':
        bossData['HP'] -= 10000


# 魔兽技能
def bossSkill():
    global anger, angerSkill
    damage = (bossData[randomSkill] - playerData['def'])
    if damage > 0:
        playerData['HP'] -= damage
    if playerState == 'defense':
        anger += 10
        if anger >= 100:
            angerSkill = True


# 技能选择
def skillChoose(e):
    global playerState, skill
    x = e.pos[0]
    y = e.pos[1]
    if 290 < x < 440 and 605 < y < 675:
        playerState = 'attack'
        skill = 1
    elif 560 < x < 710 and 605 < y < 675:
        playerState = 'defense'
        skill = 2
    elif 420 < x < 570 and 540 < y < 700 and angerSkill:
        playerState = 'anger'
        skill = 3


# 动画状态帧
player = 0
boss = 0
index = 0
# 游戏状态
state = 'loading'
# 塔影守卫状态
playerState = 'idle'
# 游戏回合
turn = 'player'
# 技能选择
choose = 'doing'
# 塔影守卫技能
skill = 0
# 魔兽随机技能
randomSkill = 'magic'
# 位置计数
offset = 0
# 怒气值
anger = 0
# 烈焰狂怒技能
angerSkill = False
# 烈焰狂怒动画
angerAnimation = False

while True:
    # 加载状态
    if state == 'loading':
        # 图片加载
        uiDict = createDict('UI/')
        screen.blit(uiDict['start'][0], (0, 0))
        pygame.display.update()
        playerDict = createDict('animation/player/')
        screen.blit(uiDict['start'][1], (0, 0))
        pygame.display.update()
        bossDict = createDict('animation/boss/')
        screen.blit(uiDict['start'][2], (0, 0))
        pygame.display.update()
        pygame.time.delay(500)
        state = 'start'
    # 开始状态
    if state == 'start':
        screen.blit(uiDict['start'][3], (0, 0))
    # 进行状态
    if state == 'running':
        bgControl()
        # 显示血条和属性值
        showHP(161, 12, playerData['HP'], 'player')
        showHP(589, 12, bossData['HP'], 'boss')
        showData(playerData)
        showData(bossData)
        # 玩家回合
        if turn == 'player':
            # 选择技能
            if choose == 'doing':
                showActor(playerDict, 'idle')
                showActor(bossDict, 'idle')
            # 发动攻击
            else:
                showActor(bossDict, 'idle')
                showActor(playerDict, playerState)
                num = len(playerDict[playerState])
                if player >= num:
                    playerSkill(playerState)
                    randomSkill = random.choice(['magic', 'grab', 'cards', 'bow'])
                    turn = 'boss'
        # boss回合
        elif turn == 'boss':
            if playerState == 'defense':
                showActor(playerDict, 'idle2')
            else:
                showActor(playerDict, 'idle')
            showActor(bossDict, randomSkill)
            num = len(bossDict[randomSkill])
            if boss >= num:
                bossSkill()
                choose = 'doing'
                turn = 'player'
                playerData['def'] = 50
        if playerData['HP'] <= 0 or bossData['HP'] <= 0:
            state = 'end'
    # 结束状态
    if state == 'end':
        if playerData['HP'] <= 0:
            screen.blit(uiDict['end'][0], (0, 0))
        elif bossData['HP'] <= 0:
            screen.blit(uiDict['end'][1], (0, 0))
    # 刷新屏幕
    pygame.display.update()
    pygame.time.delay(100)
    # pygame事件
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_KP_ENTER or e.key == pygame.K_RETURN:
                state = 'running'
            if e.key == pygame.K_SPACE:
                choose = 'done'
                player = 0
                if skill == 3:
                    angerAnimation = False
                    angerSkill = False
        if e.type == pygame.MOUSEBUTTONDOWN:
            if choose == 'doing':
                skillChoose(e)
