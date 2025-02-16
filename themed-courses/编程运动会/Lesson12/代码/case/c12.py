import pygame,sys

# 初始化
pygame.init()
# 窗口设置
WIDTH,HEIGHT = 1000,700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('飞碟射击')
pygame.mouse.set_visible(False)
pygame.event.set_grab(True)

# 图片加载函数
def loadImg(path,num):
    imgs = []
    for n in range(num):
        frame = pygame.image.load(path + str(n) + '.png').convert_alpha()
        imgs.append(frame)
    return imgs

# 图片加载
rounds = loadImg('images/round/',3)
ready = loadImg('images/ready/',5)
scores = loadImg('images/score/',6)
bgs = loadImg('images/bg/',3)
guns = loadImg('images/guns/',6)
booms = loadImg('images/boom/',17)
bullets = loadImg('images/bullet/',3)
flash = pygame.image.load('images/flash/0.png')
sight = pygame.image.load("images/s.png")

# 矩形碰撞检测
def checkHit(rec1, rec2):
    if rec1[2] <= rec2[0]:
        return False
    if rec1[0] >= rec2[2]:
        return False
    if rec1[3] <= rec2[1]:
        return False
    if rec1[1] >= rec2[3]:
        return False
    return True

clock = pygame.time.Clock()
running = True
state = 'start'
level = 'round'
bx = -1000
by = -700
gunFrm = 0
bulFrm = 2
roundIndex = 0
timeCount = 0
readyIndex = 0

pygame.mouse.set_pos(WIDTH // 2,HEIGHT // 2)
while running:
    # 事件处理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and state == 'start':
                state = 'running'
            elif event.key == pygame.K_ESCAPE:
                running = False
    # 游戏状态
    if state == 'start':
        screen.blit(bgs[0],(0,0))
    elif state == 'running':
        mouseX, mouseY = pygame.mouse.get_pos()
        moveX = mouseX - WIDTH // 2
        moveY = mouseY - HEIGHT // 2
        bx -= moveX
        by -= moveY
        pygame.mouse.set_pos(WIDTH // 2,HEIGHT // 2)
        if bx >= 0:
            bx = 0
        if bx <= -2000:
            bx = -2000
        if by >= 0:
            by = 0
        if by <= -1050:
            by = -1050
        screen.blit(bgs[1],(bx,by))
        if level == 'round':
            screen.blit(rounds[roundIndex],(0,0))
            if timeCount == 60:
                timeCount = 0
                level = 'ready'
            timeCount += 1
        elif level == 'ready':
            screen.blit(ready[readyIndex],(0,0))
            if timeCount == 60:
                readyIndex += 1
                timeCount = 0
                if readyIndex == 5:
                    readyIndex = 0
                    level = 'shoot'
            timeCount += 1
        elif level == 'shoot':
            pass
        screen.blit(sight,(0,0))
        screen.blit(guns[gunFrm],(0,0))
        screen.blit(bullets[bulFrm],(850,20))
    elif state == 'end':
        pass
    clock.tick(60)
    pygame.display.update()
pygame.quit()
sys.exit()