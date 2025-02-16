import pygame
import sys
import os
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
    def __init__(self, path='', anim='stand', pos=(0, 0), layer=2):
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
            layer = 5
        s = Map(f'{name}/{n}.png', layer, pos1)
        maps[n] = s
    maps['hero'] = Player(f'Hero/{heroName}', anim, pos2)
    return maps

# 地图界面的精灵的组
mapSprites = pygame.sprite.LayeredUpdates()
mapName = 'grasslands'

# 碰撞检测
def collision():
    # 角色与地图空气墙的碰撞
    if pygame.sprite.collide_mask(maps['hero'], maps['block']):
        return 'block'

# 控制角色移动速度
speedX, speedY = 0, 0
# 控制水平方向背景的移动状态
horiz = False
# 控制竖直方向背景的移动状态
vert = True
# 所有精灵的移动函数
def move(dx, dy):
    global horiz,vert
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
            v.rect.x = maps['bg'].rect.x
            v.rect.y = maps['bg'].rect.y

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

pygame.quit()
sys.exit()
