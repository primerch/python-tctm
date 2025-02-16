import pygame
import sys

# 初始化Pygame
pygame.init()

# 定义窗口尺寸
WIDTH = 998
HEIGHT = 700

# 创建窗口
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# 加载动画
def loadAnim(path, num,zoom=1.6,flip=False):
    animFrames = []
    # 加载动画序列的图片文件
    for filename in range(num):
        frame = pygame.image.load(path + str(filename) + '.png').convert_alpha()
        width = frame.get_width()
        height = frame.get_height()
        frame = pygame.transform.scale(frame, (int(width * zoom), int(height * zoom)))
        # 图像水平翻转
        if flip:
            frame = pygame.transform.flip(frame, True, False)
        animFrames.append(frame)
    return animFrames

# 玩家的资源加载
plyAR = loadAnim('images/playerAnimation/attack/', 8, zoom=2)
plyAL = loadAnim('images/playerAnimation/attack/', 8, zoom=2, flip=True)
plyIR = loadAnim('images/playerAnimation/idle/', 8, zoom=2)
plyIL = loadAnim('images/playerAnimation/idle/', 8, zoom=2,flip=True)
plyMR = loadAnim('images/playerAnimation/move/', 8, zoom=2)
plyML = loadAnim('images/playerAnimation/move/', 8, zoom=2,flip=True)

# 敌人的资源加载
enemyAR = loadAnim('images/enemyAnimation/attack/', 8)
enemyAL = loadAnim('images/enemyAnimation/attack/', 8, flip=True)
enemyCR = loadAnim('images/enemyAnimation/crazy/', 8)
enemyCL = loadAnim('images/enemyAnimation/crazy/', 8, flip=True)
enemyIR = loadAnim('images/enemyAnimation/idle/', 8)
enemyIL = loadAnim('images/enemyAnimation/idle/', 8, flip=True)
enemyMR = loadAnim('images/enemyAnimation/move/', 8)
enemyML = loadAnim('images/enemyAnimation/move/', 8, flip=True)
enemyRR = loadAnim('images/enemyAnimation/run/', 8)
enemyRL = loadAnim('images/enemyAnimation/run/', 8, flip=True)
tigerL = loadAnim('images/particle/Tiger/', 8)
tigerR = loadAnim('images/particle/Tiger/', 8, flip=True)
# 背景加载
bg = loadAnim('images/maps/', 43)
bg1 = loadAnim('images/end/', 2, zoom=1)

# 动画播放函数
def Anim(animations, frame, count, delay=5, x=0, y=0):
    finished = False
    screen.blit(animations[frame], (x, y))
    if count >= delay:
        count = 0
        frame += 1
        if frame == len(animations):
            frame = 0
            finished = True
    count += 1
    return frame, count, finished

# 玩家动画
plyFrm = 0
plyC = 0
plyState = 'idle'
plyTurn = 'right'
x = 80
y = 500

def playerAnim():
    global plyFrm, plyC
    if plyState == 'idle':
        if plyTurn == 'left':
            plyFrm, plyC,plyEnd = Anim(plyIL, plyFrm, plyC, x=x, y=y)
        else:
            plyFrm, plyC,plyEnd = Anim(plyIR, plyFrm, plyC, x=x, y=y)
    elif plyState == 'moving':
        if plyTurn == 'left':
            plyFrm, plyC,plyEnd = Anim(plyML, plyFrm, plyC, x=x, y=y)
        else:
            plyFrm, plyC,plyEnd = Anim(plyMR, plyFrm, plyC, x=x, y=y)
    elif plyState == 'attack':
        if plyTurn == 'left':
            plyFrm, plyC,plyEnd= Anim(plyAL, plyFrm, plyC, x=x, y=y)
        else:
            plyFrm, plyC,plyEnd = Anim(plyAR, plyFrm, plyC, x=x, y=y)

# 玩家状态
speed = 2
up = False
down = False
left = False
right = False

# 敌人动画
enemyFrm, enemyC, = 0, 0
enemyState = 'special'
enemyTurn = 'left'
enemyX = 600
enemyY = 500
enemyNext = 0
tigerFrm, tigerC= 0, 0

def enemyAnim():
    global enemyFrm, enemyC,enemyNext,tigerFrm,tigerC,enemyEnd
    if enemyState == 'idle':
        if enemyTurn == 'left':
            enemyFrm, enemyC, enemyEnd = Anim(enemyIL, enemyFrm, enemyC, 5, enemyX, enemyY)
        else:
            enemyFrm, enemyC, enemyEnd = Anim(enemyIR, enemyFrm, enemyC, 5, enemyX, enemyY)
    elif enemyState == 'move':
        if enemyTurn == 'left':
            enemyFrm, enemyC, enemyEnd = Anim(enemyML, enemyFrm, enemyC, 7, enemyX, enemyY)
        else:
            enemyFrm, enemyC, enemyEnd = Anim(enemyMR, enemyFrm, enemyC, 7, enemyX, enemyY)
    elif enemyState == 'attack':
        if enemyTurn == 'left':
            if enemyNext == 0:
                enemyFrm, enemyC, enemyEnd = Anim(enemyIL, enemyFrm, enemyC, 5, enemyX, enemyY)
            elif enemyNext == 1:
                enemyFrm, enemyC, enemyEnd = Anim(enemyAL, enemyFrm, enemyC, 5, enemyX - 70, enemyY)
            elif enemyNext == 2:
                enemyFrm, enemyC, enemyEnd = Anim(enemyIL, enemyFrm, enemyC, 5, enemyX, enemyY)
        else:
            if enemyNext == 0:
                enemyFrm, enemyC, enemyEnd = Anim(enemyIR, enemyFrm, enemyC, 5, enemyX, enemyY)
            elif enemyNext == 1:
                enemyFrm, enemyC, enemyEnd = Anim(enemyAR, enemyFrm, enemyC, 5, enemyX + 10, enemyY)
            elif enemyNext == 2:
                enemyFrm, enemyC, enemyEnd = Anim(enemyIR, enemyFrm, enemyC, 5, enemyX, enemyY)
        if enemyEnd:
            enemyNext += 1
            if enemyNext == 3:
                enemyNext = 0
    elif enemyState == 'special':
        if enemyTurn == 'left':
            if enemyNext <=3:
                enemyFrm, enemyC, enemyEnd = Anim(enemyCL, enemyFrm, enemyC, 5, enemyX, enemyY)
            elif enemyNext == 4:
                enemyFrm, enemyC, enemyEnd = Anim(enemyRL, enemyFrm, enemyC, 8, enemyX - 40, enemyY)
                tigerFrm, tigerC, tigerEnd = Anim(tigerL, tigerFrm, tigerC, 8, enemyX - 235, enemyY - 20)
            elif 7 > enemyNext > 4:
                enemyFrm, enemyC, enemyEnd = Anim(enemyIL, enemyFrm, enemyC, 10, enemyX, enemyY)
        else:
            if enemyNext <=3:
                enemyFrm, enemyC, enemyEnd = Anim(enemyCR, enemyFrm, enemyC, 5, enemyX, enemyY)
            elif enemyNext == 4:
                enemyFrm, enemyC, enemyEnd = Anim(enemyRR, enemyFrm, enemyC, 8, enemyX + 10, enemyY)
                tigerFrm, tigerC, tigerEnd = Anim(tigerR, tigerFrm, tigerC, 8, enemyX - 135, enemyY - 20)
            elif 7 > enemyNext > 4:
                enemyFrm, enemyC, enemyEnd = Anim(enemyIR, enemyFrm, enemyC, 10, enemyX, enemyY)
        if enemyEnd:
            enemyNext += 1
            if enemyNext == 7:
                enemyNext = 0

# 绘制角色血条框
font = pygame.font.SysFont('simhei', 40)
plyHP = 600
enemyHP = 600

def drawUI():
    # 黑色背景框
    color = (0, 0, 0)
    pos = (0, 0)
    size = (998, 100)
    pygame.draw.rect(screen, color, (pos, size))
    # 玩家 名字
    t = font.render('PLAYER', True, 'white')
    screen.blit(t, (40, 5))
    # 敌人 名字
    t = font.render('ENEMY', True, 'white')
    screen.blit(t, (40, 45))
    # 玩家 血条框
    color = (255, 255, 255)
    pos = (196, 8)
    size = (604, 34)
    pygame.draw.rect(screen, color, (pos, size), 2)
    # 敌人 血条框
    color = (255, 255, 255)
    pos = (196, 8 + 40)
    size = (604, 34)
    pygame.draw.rect(screen, color, (pos, size), 2)
    # 玩家 血条
    color = (200, 200, 200)
    pos = (198, 10)
    size = (plyHP, 30)
    pygame.draw.rect(screen, color, (pos, size))
    # 敌人 血条
    color = (200, 200, 200)
    pos = (198, 10 + 40)
    size = (enemyHP, 30)
    pygame.draw.rect(screen, color, (pos, size))

# 事件获取
def getEvent():
    global running, up, down, left, right, plyTurn, plyState
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_w:
                up = True
            elif e.key == pygame.K_s:
                down = True
            elif e.key == pygame.K_a:
                plyTurn = 'left'
                left = True
            elif e.key == pygame.K_d:
                plyTurn = 'right'
                right = True
            elif e.key == pygame.K_j:
                plyState = 'attack'
        elif e.type == pygame.KEYUP:
            if e.key == pygame.K_w:
                up = False
                plyState = 'idle'
            elif e.key == pygame.K_s:
                down = False
                plyState = 'idle'
            elif e.key == pygame.K_a:
                left = False
                plyState = 'idle'
            elif e.key == pygame.K_d:
                right = False
                plyState = 'idle'
            elif e.key == pygame.K_j:
                plyState = 'idle'

#  角色的移动
def playerMove():
    global x, y, plyState
    if up:
        y -= speed
        if y <= 476:
            y = 476
        plyState = 'moving'
    elif down:
        y += speed
        if y >= 566:
            y = 566
        plyState = 'moving'
    elif left:
        x -= speed
        if x <= 80:
            x = 80
        plyState = 'moving'
    elif right:
        x += speed
        if x >= 800:
            x = 800
        plyState = 'moving'

# 游戏循循环
running = True
clock = pygame.time.Clock()
# 动画帧变量
bgFrm = 0
bgCount = 0

while running:
    # 事件获取
    getEvent()
    # 运动计算
    playerMove()
    # 绘制背景
    bgFrm, bgCount, bgEnd = Anim(bg, bgFrm, bgCount, y=100)
    # 绘制UI
    drawUI()
    # 根据前后关系绘制玩家和对手
    if y > enemyY + 30:
        enemyAnim()
        playerAnim()
    else:
        playerAnim()
        enemyAnim()
    # 全局更新及帧率
    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
