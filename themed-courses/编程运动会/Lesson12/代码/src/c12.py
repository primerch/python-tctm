import pygame,sys

# 初始化
pygame.init()
# 窗口设置
WIDTH,HEIGHT = 1000,700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('飞碟射击')

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

clock = pygame.time.Clock()
running = True
state = 'start'
level = 'round'
bx = -1000
by = -700
gunFrm = 0
bulFrm = 2
while running:
    # 事件处理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and state == 'start':
                state = 'running'
    # 游戏状态
    if state == 'start':
        screen.blit(bgs[0],(0,0))
    elif state == 'running':
        screen.blit(bgs[1],(bx,by))
        if level == 'round':
            pass
        elif level == 'ready':
            pass
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