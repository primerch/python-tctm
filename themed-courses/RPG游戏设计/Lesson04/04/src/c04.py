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
    def __init__(self, path='', anim='stand', pos=(0, 0)):
        super(Player, self).__init__()
        self.animations = self.loadImages(path)
        self.anim = anim
        self.frame = 0
        self.image = self.animations[self.anim][self.frame]
        self.picNum = len(self.animations[self.anim])
        self.rect = self.image.get_rect()
        self.rect.center = pos

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
        self.frame = (self.frame + 1) % len(self.animations[self.anim])
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

# 新增
heroName = ''

# 新增 宠物选择界面UI加载
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
                    if poinState is not None:
                        poinState = None  # 重置记录的动画类型为 None
                        boy.changeAnim('stand')
                        girl.changeAnim('stand')
        # 新增
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



    pygame.display.flip()
    clock.tick(25)
    if gameState == 'start':
        startSprites.draw(screen)

    elif gameState == 'hero':
        startSprites.draw(screen)
        startSprites.update()
    # 新增
    elif gameState == 'pet':
        startSprites.draw(screen)
        startSprites.update()

pygame.quit()
sys.exit()
