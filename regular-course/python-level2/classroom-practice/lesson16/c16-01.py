import pygame
import sys
import os

# 初始化及背景显示
pygame.init()
screen = pygame.display.set_mode((1000, 700))

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
                mylist[j - 1], mylist[j] = mylist[j], mylist[j - 1]
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
        pictures = []  # 临时列表，每次执行for时，会清空
        # 获取图片的名字（全名包括扩展名）
        names = os.listdir(path + key + '/')
        # 把图片变量存在picture列表中
        for i in range(len(names)):
            names[i] = int(names[i].replace('.png', ''))
        # print(names)
        insertSort(names)
        # print(names)
        for name in names:
            # 把.png拼上
            img = pygame.image.load(path + key + '/' + str(name) + '.png')  # convert可以去掉
            pictures.append(img)
        # 把动画序列帧列表存在字典相应的KEY值中
        gameDict[key] = pictures
    return gameDict


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
        # UI加载
        uiDict = createDict('UI/')
        screen.blit(uiDict['start'][0], (0, 0))
        pygame.display.update()

        # 玩家动画加载
        playerDict = createDict('animation/player/')
        screen.blit(uiDict['start'][1], (0, 0))
        pygame.display.update()

        # boss动画加载
        bossDict = createDict('animation/boss/')
        screen.blit(uiDict['start'][3], (0, 0))
        pygame.display.update()

        pygame.time.delay(500)
        state = 'start'
    # 游戏开始画面
    elif state == 'start':
        # 显示开始界面,按enter或者小键盘enter按键进入游戏
        screen.blit(uiDict['start'][4], (0, 0))
    # 游戏进行状态
    elif state == 'running':
        screen.blit(uiDict['map'][0], (0, 0))
        # 玩家回合
        if turn == 'player':
            # 技能选择
            if choose == 'doing':
                print('技能选择中…')
            else:
                print('玩家开始攻击')
                turn = 'boss'
                # boss回合
        elif turn == 'boss':
            print('boss开始攻击')
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
