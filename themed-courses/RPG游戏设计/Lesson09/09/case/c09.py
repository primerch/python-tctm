import pygame
import sys
import os
import random
# 初始化pygame
pygame.init()

# 设置屏幕大小
WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# 设置标题
pygame.display.set_caption('精灵大乱斗')


# UI类
class UI(pygame.sprite.Sprite):
    def __init__(self, path, pos=(0, 0)):
        super(UI, self).__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()
        self.rect.topleft = pos


# 角色类
class Player(pygame.sprite.Sprite):
    def __init__(self, path='', anim='stand', pos=(0, 0), layer=2, dic=None):
        super(Player, self).__init__()
        self.animations = self.loadImages(path)
        self.anim = anim
        self.frame = 0
        self.image = self.animations[self.anim][self.frame]
        self.picNum = len(self.animations[self.anim])
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.layer = layer
        # 添加mask属性，设置遮罩层
        self.mask = pygame.mask.from_surface(self.image)
        # 添加战斗属性
        if dic:
            for k, v in dic.items():
                setattr(self, k, v)

    # 加载图片
    def loadImages(self, path):
        keys = os.listdir(f'images/{path}')
        gameDict = {}
        for key in keys:
            images = []
            names = os.listdir(f'images/{path}/{key}')
            for i in range(len(names)):
                p = f'images/{path}/{key}/{key}_{i}.png'
                image = pygame.image.load(p).convert_alpha()
                images.append(image)
            gameDict[key] = images
        return gameDict

    # 动画更新
    def update(self):
        self.frame = (self.frame + 1) % self.picNum
        self.image = self.animations[self.anim][self.frame]

        if self.frame == len(self.animations[self.anim]) - 1:
            self.notify = True
        else:
            self.notify = False

    # 动画切换
    def changeAnim(self, name):
        if name in self.animations and self.animations != name:
            self.anim = name
            self.frame = 0
            self.image = self.animations[self.anim][self.frame]
            self.picNum = len(self.animations[self.anim])

# 初始化变量来记录上一个精灵和动画类型
poinState = None

# 鼠标点击判断
def click(sprite, pos):
    if sprite.rect.collidepoint(pos):
        return True
    else:
        return False

# 角色名字
heroName = ''

# 宠物选择界面UI加载
def petUI():
    p1 = Player('choice/a0', pos=(270, 370))
    p2 = Player('choice/b0', pos=(500, 290))
    p3 = Player('choice/c0', pos=(900, 280))
    bg = UI('images/UI/bg1.png')
    c1 = UI('images/UI/choice1.png', pos=(120, 500))
    c2 = UI('images/UI/choice1.png', pos=(445, 500))
    c3 = UI('images/UI/choice1.png', pos=(745, 500))
    startSprites.empty()
    startSprites.add(bg, p1, p2, p3, c1, c2, c3)
    return p1, p2, p3, c1, c2, c3

# 地图类
class Map(pygame.sprite.Sprite):
    def __init__(self, mapName, layer, pos=(0, 0)):
        super(Map, self).__init__()
        # self.name = mapName   # 地图名
        self.note = 'block'
        self.image = pygame.image.load(f'images/map/{mapName}')
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.layer = layer
        # 添加mask属性，设置遮罩层
        self.mask = pygame.mask.from_surface(self.image)

# 敌人信息
mapEnemys = {
    'volcano':    {'e0': (620, 540), 'e5': (920, 540)},
    'crossroads': {'e0': (620, 540), 'e5': (920, 540)},
    'cave':       {'e0': (620, 540), 'e5': (920, 540)},
    'drylands':   {'e0': (620, 540), 'e5': (920, 540)},
    'icelands':   {'e0': (620, 540), 'e5': (920, 540)},
    'grasslands': {'e0': (620, 540), 'e5': (920, 540)}
}

def createMap(name, pos1=(0, 0), pos2=(120, 500), anim='standRight'):
    mapNames = os.listdir(f'images/map/{name}') # grasslands
    maps = {}
    for n in mapNames:
        n = n.split('.')[0]
        if n == 'bg':
            layer = 1
        elif n == 'mask':
            layer = 3
        else:
            layer = 0
        s = Map(f'{name}/{n}.png', layer, pos1)
        maps[n] = s
    maps['hero'] = Player(f'Hero/{heroName}', anim, pos2)
    # 添加两个敌人对象
    if mapName in mapEnemys:
        for k, v in mapEnemys[name].items():
            enemy = Player(f'Hero/{k}', 'stand', v)
            maps[k] = enemy
    return maps

# 地图界面的精灵的组
mapSprites = pygame.sprite.LayeredUpdates()
mapName = 'grasslands'
# 地图关系字典
mapConnections = {
    'cave': {
        'left': 'volcano',
        'leftpos': (-618, -145),  # 切换地图后，背景volcano的坐标
        'leftheroPos': (660, 470)  # 切换地图后，角色的坐标

    },
    'crossroads': {
        'up': 'icelands',
        'down': 'drylands',
        'left': 'grasslands',
        'right': 'volcano',
        'rightpos': (0, -240),  # 切换地图后，背景volcano的坐标
        'rightheroPos': (160, 350),  # 切换地图后，角色的坐标
        'uppos': (-365, -324),  # 切换地图后，背景icelands的坐标
        'upheroPos': (315, 480),  # 切换地图后，角色的坐标
        'downpos': (-365, 0),  # 切换地图后，背景drylands的坐标
        'downheroPos': (315, 120),  # 切换地图后，角色的坐标
        'leftpos': (-365, -140),  # 切换地图后，背景grasslands的坐标
        'leftheroPos': (890, 350)  # 切换地图后，角色的坐标
    },
    'drylands': {
        'up': 'crossroads',
        'uppos': (-365, -324),  # 切换地图后，背景crossroads的坐标
        'upheroPos': (315, 520)  # 切换地图后，角色的坐标
    },
    'icelands': {
        'down': 'crossroads',
        'downpos': (-365, 0),  # 切换地图后，背景crossroads的坐标
        'downheroPos': (315, 95)  # 切换地图后，角色的坐标
    },
    'grasslands': {
        'right': 'crossroads',
        'rightpos': (0, -125),  # 切换地图后，背景crossroads的坐标
        'rightheroPos': (130, 365),  # 切换地图后，角色的坐标
    },
    'volcano': {
        'left': 'crossroads',
        'right': 'cave',
        'leftpos': (-365, -140),  # 切换地图后，背景crossroads的坐标
        'leftheroPos': (860, 370),  # 切换地图后，角色的坐标
        'rightpos': (0, -125),  # 切换地图后，背景cave的坐标
        'rightheroPos': (130, 365),  # 切换地图后，角色的坐标
    }
}

# 碰撞检测
def collision():
    # 角色与地图空气墙的碰撞
    if pygame.sprite.collide_mask(maps['hero'], maps['block']):
        return 'block'
    # 角色与传送块
    elif maps.get('left') and pygame.sprite.collide_mask(maps['hero'], maps['left']):
        return 'left'
    elif maps.get('right') and pygame.sprite.collide_mask(maps['hero'], maps['right']):
        return 'right'
    elif maps.get('up') and pygame.sprite.collide_mask(maps['hero'], maps['up']):
        return 'up'
    elif maps.get('down') and pygame.sprite.collide_mask(maps['hero'], maps['down']):
        return 'down'
    # 单独提取敌人对象，存入字典
    enemyDict = {k: v for k, v in maps.items() if k.startswith('e')}
    # 角色与敌人的碰撞检测
    for k in enemyDict:
        if pygame.sprite.collide_mask(maps['hero'], maps[k]):
            return k
    return 'No collsion'
# 控制角色移动速度
speedX, speedY = 0, 0
# 控制水平方向背景的移动状态
horiz = False
# 控制竖直方向背景的移动状态
vert = True
# 下个地图的初始坐标
bgPos = (0, 0)
# 下个地图角色的初始坐标
heroPos = (0, 0)
# 下个地图角色的初始动画
heroAnmi = 'standDown'
# 敌人名字
enemyName = ''
# 所有精灵的移动函数
def move(dx, dy):
    global horiz, vert, bgPos, heroPos, heroAnmi, gameState, mapName, speedX, speedY, enemyName
    # 水平方向背景可以移动
    if horiz:
        # 存储地图中所有对象碰撞前的x坐标
        old_x = {k: v.rect.x for k, v in maps.items()}
        # 遍历maps列表，控制除hero外的所有物体一起移动
        for k, m in maps.items():
            if k != 'hero':
                m.rect.x -= dx
        # 发生碰撞，将除角色以外所有对象还原到碰撞前的位置
        if collision() == 'block':
            for k, v in old_x.items():
                if k != 'hero':
                    maps[k].rect.x = v
        # 地图到达左边界
        if maps['bg'].rect.left > 0:
            maps['bg'].rect.left = 0
            horiz = False
        # 地图到达右边界
        elif maps['bg'].rect.right < WIDTH:
            maps['bg'].rect.right = WIDTH
            horiz = False
    # 水平方向背景不可以移动
    else:
        # 记录碰撞前的位置
        old_rect = maps['hero'].rect.copy()
        # 人物角色移动
        maps['hero'].rect.centerx += dx
        # 角色移动到屏幕中心
        if maps['hero'].rect.centerx == WIDTH / 2:
            horiz = True
        # 角色的左边缘检测
        if maps['hero'].rect.centerx < 0:
            maps['hero'].rect.centerx = 0
        # 角色的右边缘检测
        if maps['hero'].rect.centerx > WIDTH:
            maps['hero'].rect.centerx = WIDTH
        # 发生碰撞，还原到碰撞前的位置
        if collision() == 'block':
            maps['hero'].rect = old_rect
    # 竖直方向背景可以移动
    if vert:
        # 存储地图中所有对象碰撞前的y坐标
        old_y = {k: v.rect.y for k, v in maps.items()}
        # 遍历maps列表，控制除hero外的所有物体一起移动
        for k, m in maps.items():
            if k != 'hero':
                m.rect.y -= dy
        # 发生碰撞，将除角色以外所有对象还原到碰撞前的位置
        if collision() == 'block':
            for k, v in old_y.items():
                if k != 'hero':
                    maps[k].rect.y = v
        # 地图到达上边界
        if maps['bg'].rect.top > 0:
            maps['bg'].rect.top = 0
            vert = False
        # 地图到达下边界
        elif maps['bg'].rect.bottom < HEIGHT:
            maps['bg'].rect.bottom = HEIGHT
            vert = False
    # 竖直方向背景不可以移动
    else:
        # 记录碰撞前的位置
        old_rect = maps['hero'].rect.copy()
        # 人物角色移动
        maps['hero'].rect.centery += dy
        # 角色移动到屏幕中心
        if maps['hero'].rect.centery == HEIGHT / 2:
            vert = True
        # 角色的上边缘检测
        if maps['hero'].rect.centery < 0:
            maps['hero'].rect.centery = 0
        # 角色的下边缘检测
        if maps['hero'].rect.centery > HEIGHT:
            maps['hero'].rect.centery = HEIGHT
        # 发生碰撞，还原到碰撞前的位置
        if collision() == 'block':
            maps['hero'].rect = old_rect
    # 让除角色图片以外的其它图片坐标与背景图片保持相同
    for k, v in maps.items():
        if k != 'hero':
            # 当前精灵对象是敌人
            if k.startswith('e'):
                v.rect.x = maps['bg'].rect.x + mapEnemys[mapName][k][0]
                v.rect.y = maps['bg'].rect.y + mapEnemys[mapName][k][1]
            # 当前精灵对象不是敌人
            else:
                v.rect.x = maps['bg'].rect.x
                v.rect.y = maps['bg'].rect.y
    # 如果碰撞到传送块，获取要切换的地图信息，进入加载状态
    if collision() in ('left', 'right', 'up', 'down'):
        bgPos = mapConnections[mapName][f"{collision()}pos"]
        heroPos = mapConnections[mapName][f"{collision()}heroPos"]
        mapName = mapConnections[mapName][collision()]
        heroAnmi = f"stand{collision().capitalize()}"
        gameState = 'maploading'
    # 如果检测到角色与敌人发生碰撞
    elif collision().startswith('e'):
        print('碰到敌人了')
        enemyName = collision()
        speedX, speedY = 0, 0
        gameState = 'loading'
# 地图加载动画的精灵组
loadIMG = UI('images/UI/loading.png')
loadSprites = pygame.sprite.Group(loadIMG)

# 精灵属性
petData = {
    # b0 小火龙 b1 火恐龙 b2 喷火龙
    'b0': {'HP': 1000, 'MP': 100, 'Def': 50, 'skill1': 150, 'skill2': 200, 'Atk': 100},
    'b1': {'HP': 1500, 'MP': 100, 'Def': 50, 'skill1': 150, 'skill2': 200, 'Atk': 100},
    'b2': {'HP': 2000, 'MP': 100, 'Def': 50, 'skill1': 150, 'skill2': 200, 'Atk': 100},
    # c0 杰尼龟 c1 卡咪龟 c2 水箭龟
    'c0': {'HP': 1000, 'MP': 100, 'Def': 50, 'skill1': 150, 'skill2': 200, 'Atk': 100},
    'c1': {'HP': 1500, 'MP': 100, 'Def': 50, 'skill1': 150, 'skill2': 200, 'Atk': 100},
    'c2': {'HP': 2000, 'MP': 100, 'Def': 50, 'skill1': 150, 'skill2': 200, 'Atk': 100},
    # a0 妙蛙种子 a1 妙蛙草 a2 妙蛙花
    'a0': {'HP': 1000, 'MP': 100, 'Def': 50, 'skill1': 150, 'skill2': 200, 'Atk': 100111},
    'a1': {'HP': 1500, 'MP': 100, 'Def': 50, 'skill1': 150, 'skill2': 200, 'Atk': 100111},
    'a2': {'HP': 2000, 'MP': 100, 'Def': 50, 'skill1': 150, 'skill2': 200, 'Atk': 100111},
    # 敌人
    'e0': {'HP': 1000, 'MP': 100, 'Def': 50, 'skill1': 150, 'skill2': 200, 'Atk': 10000},
    'e1': {'HP': 1500, 'MP': 100, 'Def': 50, 'skill1': 150, 'skill2': 200, 'Atk': 100},
    'e2': {'HP': 2000, 'MP': 100, 'Def': 50, 'skill1': 150, 'skill2': 200, 'Atk': 100},
    'e3': {'HP': 1000, 'MP': 100, 'Def': 50, 'skill1': 150, 'skill2': 200, 'Atk': 100},
    'e4': {'HP': 1500, 'MP': 100, 'Def': 50, 'skill1': 150, 'skill2': 200, 'Atk': 100},
    'e5': {'HP': 2000, 'MP': 100, 'Def': 50, 'skill1': 150, 'skill2': 200, 'Atk': 100},
}

skill = 'attack'
enemySkill = 'attack'
gameRound = 'hero'
gameState = ''
count = 0
flag = False
def fight(sp, s):
    global count, gameRound, fightState, enemySkill, gameState, flag
    if sp.notify:  # 判断动画是否播放完毕
        count += 1
        if count == 1:

            if sp == pet:
                fight_sprites.change_layer(pet, 3)
            else:
                fight_sprites.change_layer(pet, 0)

            sp.changeAnim(s)
            flag = True
        elif count == 2:
            pet.changeAnim('stand')
            enemy.changeAnim('stand')
            if sp == enemy:
                gameRound = 'hero'
                fightState = 'choose'
                count = 0
            else:
                gameRound = 'enemy'
                enemySkill = random.choice(['attack', 'skill1', 'skill2'])
                count = 0
    # 受击动画
    if flag:
        if sp.frame == sp.picNum - 13:  #
            if sp == enemy:
                pet.changeAnim('hit')

            else:
                enemy.changeAnim('hit')
            flag = False

# 游戏状态
gameState = 'start'
startSprites = pygame.sprite.Group()
# 开始页精灵初始化
startPage = UI('images/UI/start.png')
startSprites.add(startPage)
# 游戏主循环
running = True
clock = pygame.time.Clock()
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        elif e.type == pygame.KEYDOWN:
            if gameState == 'start':
                startSprites.remove(startPage)
                # 角色选择页，角色、背景
                bg = UI('images/UI/bg.png')
                startSprites.add(bg)
                boy = Player('choice/boy', pos=(300, 400))
                girl = Player('choice/girl', pos=(700, 400))
                cursor = UI('images/UI/choice.png', pos=(-1000, -1000))
                startSprites.add(bg, cursor, boy, girl)
                gameState = 'hero'  # 选择男女
            # 按键控制角色移动
            if gameState == 'map':
                if e.key == pygame.K_a:
                    maps['hero'].changeAnim('moveLeft')
                    speedX = -5
                elif e.key == pygame.K_d:
                    maps['hero'].changeAnim('moveRight')
                    speedX = 5
                elif e.key == pygame.K_w:
                    maps['hero'].changeAnim('moveUp')
                    speedY = -5
                elif e.key == pygame.K_s:
                    maps['hero'].changeAnim('moveDown')
                    speedY = 5
        # 松开按键，角色停止移动
        elif e.type == pygame.KEYUP:
            if gameState == 'map':
                if e.key == pygame.K_a:
                    maps['hero'].changeAnim('standLeft')
                    speedX, speedY = 0, 0
                elif e.key == pygame.K_d:
                    maps['hero'].changeAnim('standRight')
                    speedX, speedY = 0, 0
                elif e.key == pygame.K_w:
                    maps['hero'].changeAnim('standUp')
                    speedX, speedY = 0, 0
                elif e.key == pygame.K_s:
                    maps['hero'].changeAnim('standDown')
                    speedX, speedY = 0, 0
        elif e.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            # 人物选择
            if gameState == 'hero':
                if click(boy, pos):
                    cursor.rect.topleft = (70, 380)
                    if poinState != 'boy':
                        boy.changeAnim('win')
                        poinState = 'boy'
                        if boy.anim == girl.anim:
                            girl.changeAnim('stand')
                elif click(girl, pos):
                    cursor.rect.topleft = (455, 380)
                    if poinState != 'girl':  # 只有当动画类型不同时才调用 changeAnim 方法
                        girl.changeAnim('win')
                        poinState = 'girl'  # 记录当前动画类型
                        if boy.anim == girl.anim:
                            boy.changeAnim('stand')
                else:
                    cursor.rect.topleft = (-1000, -1000)
                    if poinState is not None:  # 只有当上一次记录的动画类型不为 None 时才调用 changeAnim 方法
                        poinState = None  # 重置记录的动画类型为 None
                        boy.changeAnim('stand')
                        girl.changeAnim('stand')
            # 宠物选择
            elif gameState == 'pet':
                if click(c1, pos):
                    if poinState != 'a0':
                        p1.changeAnim('win')
                        poinState = 'a0'
                elif click(c2, pos):
                    if poinState != 'b0':
                        p2.changeAnim('win')
                        poinState = 'b0'
                elif click(c3, pos):
                    if poinState != 'c0':
                        p3.changeAnim('win')
                        poinState = 'c0'
                else:
                    if poinState is not None:
                        poinState = None
                        p1.changeAnim('stand')
                        p2.changeAnim('stand')
                        p3.changeAnim('stand')
        elif e.type == pygame.MOUSEBUTTONDOWN:
            if e.button == 1:
                pos = pygame.mouse.get_pos()
                if gameState == 'hero':
                    if click(boy, pos):
                        gameState = 'pet'
                        heroName = 'boy'
                        # 宠物选择页，宠物背景
                        p1, p2, p3, c1, c2, c3 = petUI()
                    elif click(girl, pos):
                        gameState = 'pet'
                        heroName = 'girl'
                        # 宠物选择页，宠物背景
                        p1, p2, p3, c1, c2, c3 = petUI()
                elif gameState == 'pet':
                    # 进入地图函数
                    def enterMap():
                        global maps
                        maps = createMap(mapName)
                        for n, s in maps.items():
                            mapSprites.add(s, layer=s.layer)
                    if click(c1, pos):
                        petName = 'a0'
                        gameState = 'map'
                        # 调用进入地图函数
                        enterMap()
                    elif click(c2, pos):
                        petName = 'b0'
                        gameState = 'map'
                        # 调用进入地图函数
                        enterMap()
                    elif click(c3, pos):
                        petName = 'c0'
                        gameState = 'map'
                        # 调用进入地图函数
                        enterMap()

    pygame.display.flip()
    clock.tick(25)
    if gameState == 'start':
        startSprites.draw(screen)
    elif gameState == 'hero':
        startSprites.draw(screen)
        startSprites.update()
    elif gameState == 'pet':
        startSprites.draw(screen)
        startSprites.update()
    elif gameState == 'map':
        move(speedX, speedY)
        mapSprites.update()
        mapSprites.draw(screen)
    elif gameState == 'maploading':
        loadSprites.draw(screen)
        pygame.display.flip()
        maps = createMap(mapName, bgPos, heroPos, heroAnmi)
        for i in mapSprites:
            i.kill()
        for n, s in maps.items():
            mapSprites.add(s, layer=s.layer)
        gameState = 'map'
        speedY, speedX = 0, 0
    elif gameState == 'loading':
        loadSprites.draw(screen)
        pygame.display.flip()
        pet = Player(f'pets/{petName}', pos=(500, 350), dic=petData[petName])
        enemy = Player(f'enemy/{enemyName}', pos=(500, 350), dic=petData[enemyName])
        btnAtk = UI('images/UI/attack.png', pos=(350, 580)) # 技能一
        btnSkill1 = UI('images/UI/skill1.png', pos=(445, 580)) # 技能二
        btnSkill2 = UI('images/UI/skill2.png', pos=(540, 580)) # 技能三
        fightUI = UI('images/UI/fightUI.png', pos=(25, 550)) # 精灵状态框
        enemyIcon = UI(f'images/UI/icon/{enemyName}.png', pos=(2, 40)) # 敌人头像
        enemyHP = UI('images/UI/enemyHP.png', pos=(720, 597)) # 敌人HP
        enemyMP = UI('images/UI/enemyMP.png', pos=(720, 626)) # 敌人MP
        petIcon = UI(f'images/UI/icon/{petName}.png', pos=(2, 40)) # 宠物头像
        petHP = UI('images/UI/petHP.png', pos=(182, 597)) # 宠物HP
        petMP = UI('images/UI/petMP.png', pos=(182, 626)) # 宠物MP
        map1 = UI(f'images/map/fight/{mapName}.png') # 战斗界面背景
        win = UI('images/UI/win.png', pos=(0, 0)) # 胜利图片
        # UI精灵组，控制基本UI元素
        UI_sprites = pygame.sprite.Group(fightUI, enemyIcon, enemyHP, enemyMP, petIcon, petHP, petMP)
        # 战斗地图精灵组，控制地图背景
        fightMap = pygame.sprite.Group(map1)
        # 按钮精灵组，控制技能按钮
        btn_sprites = pygame.sprite.Group(btnAtk, btnSkill1, btnSkill2)
        # 战斗对象精灵组，控制战斗的精灵（需要区分图层）
        fight_sprites = pygame.sprite.LayeredUpdates(pet, enemy)
        # 将游戏状态切换为战斗状态
        gameState = 'fight'
        # 战斗状态默认进入到技能选择阶段
        fightState = 'choose'
        # 重置移动速度
        speedX, speedY = 0, 0
    elif gameState == 'fight':
        # 显示战斗界面背景
        fightMap.draw(screen)
        # 显示战斗界面的精灵和敌人
        fight_sprites.draw(screen)
        # 执行精灵组中所有精灵对象的update()，实现动画的切换
        fight_sprites.update()
        # 新增
        if fightState == 'choose':
            UI_sprites.draw(screen)
            btn_sprites.draw(screen)
            fightState = 'done'
        # 新增
        elif fightState == 'done':
            if gameRound == "hero":
                fight(pet, skill)
            elif gameRound == 'enemy':
                fight(enemy, enemySkill)

pygame.quit()
sys.exit()
