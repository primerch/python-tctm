import pygame
import sys
import os
import time

# pygame初始化及设置
pygame.init()
screen = pygame.display.set_mode((1000, 700))
pygame.mouse.set_visible(False)


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

# 土地字典
soilDict = {'soil1': {'name': 'blank', 'pos': (190, 330), 'time': 0},
            'soil2': {'name': 'blank', 'pos': (545, 330), 'time': 0},
            'soil3': {'name': 'blank', 'pos': (360, 240), 'time': 0},
            'soil4': {'name': 'blank', 'pos': (370, 425), 'time': 0}
            }

# 仓库字典
plygoods = {'c0': 100, 'c1': 3, 'c2': 3, 'c3': 3, 'c4': 3, 'c5': 3, 'c6': 3}

# 糖果信息字典
candyUI = {
    'c0': {'name': '棉花糖', 'pic': iconDict['big'][0], 'pic1': iconDict['small'][0],
           'text': '甜美柔软的棉花状糖果,入口即化。', 'price': 10},
    'c1': {'name': '棒棒糖', 'pic': iconDict['big'][1], 'pic1': iconDict['small'][1],
           'text': '五颜六色的糖果，口味丰富。', 'price': 9},
    'c2': {'name': '彩虹糖', 'pic': iconDict['big'][2], 'pic1': iconDict['small'][2],
           'text': '五彩缤纷的小糖果，味道鲜美。', 'price': 8},
    'c3': {'name': '流心面包', 'pic': iconDict['big'][3], 'pic1': iconDict['small'][3],
           'text': '鲜奶油和巧克力混合的面包，外酥里软。', 'price': 7},
    'c4': {'name': '生巧泡芙', 'pic': iconDict['big'][4], 'pic1': iconDict['small'][4],
           'text': '口感轻盈的泡芙，内陷丝滑的巧克力酱。', 'price': 6},
    'c5': {'name': '樱桃蛋糕', 'pic': iconDict['big'][5], 'pic1': iconDict['small'][5],
           'text': '口感细腻的蛋糕，上面点缀着美味的樱桃。', 'price': 5},
    'c6': {'name': '焦糖布丁', 'pic': iconDict['big'][6], 'pic1': iconDict['small'][6],
           'text': '香气四溢的甜点，带有焦糖的独特风味。', 'price': 4}
}


# 绘制糖果树
def drawCandy():
    for crop in soilDict.values():
        k = crop['name']
        p = crop['pos']
        # 作物生长
        lv = (time.time() - crop['time']) // 2
        if lv > 3:
            lv = 3
        screen.blit(candyDict[k][int(lv)], p)


# 道具功能
candyName = 'c0'
pointer = UIDict['pointer'][0]
tool = ''


def prop(n):
    global pointer, tool
    if soilDict[n]['name'] == 'blank':
        if tool == '糖果':
            soilDict[n]['name'] = candyName
            soilDict[n]['time'] = time.time()
            plygoods[candyName] -= 1
            pointer = UIDict['pointer'][0]
            tool = ''
    else:
        if tool == '铲子':
            soilDict[n]['name'] = 'blank'
        elif tool == '手':
            lv = (time.time() - soilDict[n]['time']) // 2
            if lv >= 3:
                plygoods[soilDict[n]['name']] += 4
                soilDict[n]['name'] = 'blank'
    print(plygoods)


x, y = 0, 0
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
                    prop('soil1')
                elif 615 < x < 715:
                    prop('soil2')
            elif 400 < x < 500:
                if 290 < y < 390:
                    prop('soil3')
                elif 480 < y < 580:
                    prop('soil4')
            # 工具区域判断
            elif 610 < y < 670:
                if 660 < x < 720:
                    pointer = UIDict['pointer'][1]
                    tool = '铲子'
                elif 765 < x < 825:
                    pointer = UIDict['pointer'][2]
                    tool = '手'
                elif 870 < x < 930:
                    if plygoods[candyName] > 0:
                        pointer = candyUI[candyName]['pic1']
                        tool = '糖果'
    # 绘制背景
    screen.blit(UIDict['map'][0], (0, 0))
    # 绘制糖果树
    drawCandy()
    # 绘制右下糖果图标
    screen.blit(candyUI[candyName]['pic1'], (860, 595))
    # 绘制鼠标样式
    screen.blit(pointer, (x - 30, y - 30))
    pygame.display.update()
