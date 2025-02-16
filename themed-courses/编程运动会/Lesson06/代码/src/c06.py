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
    screen.blit(animations[frame], (x, y))
    if count >= delay:
        count = 0
        frame += 1
        if frame == len(animations):
            frame = 0
    count += 1
    return frame, count

# 事件获取
def getEvent():
    global running
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

# 游戏循环
running = True
clock = pygame.time.Clock()
# 动画帧变量
bgFrm = 0
bgCount = 0

while running:
    # 事件获取
    getEvent()
    # 绘制背景
    bgFrm, bgCount = Anim(bg, bgFrm, bgCount, y=100)
    # 全局更新及帧率
    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()


