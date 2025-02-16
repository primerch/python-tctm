import pygame,sys,random

# 初始化
pygame.init()
pygame.mixer.init()
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

# 加载音乐

notifyNames = ['win', 'lose', 'explosion', 'fire', 'reload', 'start', 'transmit', 'restart']  
notify = []                   

def loadMusic():              
    for name in notifyNames:  
        sound = pygame.mixer.Sound('audio/' + name + '.mp3')    
        notify.append(sound)  

# 音乐播放
def playSound(name):                          
    if name in notifyNames:                   
        sound = notifyNames.index(name)       
        notify[sound].play()                  
    else:                                     
        pygame.mixer.music.load('audio/' + name + '.mp3')   
        pygame.mixer.music.play(-1)                         


loadMusic()                            
pygame.mixer.music.set_volume(0.5)     
playSound('BGM0')                      



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

xoffset1, yoffset1 = 0, 0
randNum1 = random.randint(-6, 6)
e1Life = True
lifeTime = 3000
startTime1 = 0
frm1 = 1
xoffset2, yoffset2 = 0, 0
randNum2 = random.randint(-6, 6)
e2Life = True
startTime2 = 0
frm2 = 0
def spawn(xoffset,yoffset,randNum,life,time,frame):
    x = bx + 1500 + xoffset
    y = by + 1100 + yoffset
    nowTime = pygame.time.get_ticks()
    if nowTime - time <= lifeTime and life:
        xoffset += randNum
        yoffset = yoffset - 2
        screen.blit(booms[0],(x,y))
    if not life:
        if frame <= 16:
            if frame == 1:                        
                playSound('explosion')            
            screen.blit(booms[frame], (x, y))
            frame += 1
    return xoffset,yoffset,frame

hits = [0, 0, 0, 0, 0, 0]                        
def score():                                     
    screen.blit(bgs[1],(bx,by))                
    screen.blit(bgs[2],(0,0))                  
    for count in range(6):                       
        if hits[count] == 1:                     
            screen.blit(scores[count],(0,0))   

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
fire = False
gunState = 'hold'
gunCount = 0
start = 0                             
doOnce1,doOnce2 = True, True
pygame.mouse.set_pos(WIDTH // 2,HEIGHT // 2)
while running:
    # 事件处理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and state == 'start':
                playSound('start')  
                pygame.time.delay(2000)  
                pygame.mixer.music.set_volume(0.15)  
                playSound('BGM1')  
                state = 'running'
            elif event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_r and state == 'running':
                playSound('reload')  
                bulFrm = 2
                gunState = 'reload'
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if state == 'running' and bulFrm > 0 :
                    playSound('fire')  
                    fire = True
                    bulFrm -= 1
                    x1 = bx + 1500 + xoffset1  
                    y1 = by + 1100 + yoffset1  
                    x2 = bx + 1500 + xoffset2  
                    y2 = by + 1100 + yoffset2  
                    e1 = (x1 + 12, y1 + 30, x1 + 71 + 12, y1 + 30 + 41)
                    e2 = (x2 + 12, y2 + 30, x2 + 71 + 12, y2 + 30 + 41)
                    sightRect = (489, 354, 489 + 5, 354 + 5)  
                    if checkHit(e1,sightRect) and e1Life:  
                        e1Life = False  
                        hits[2 * roundIndex] = 1  
                    if checkHit(e2,sightRect) and e2Life:  
                        e2Life = False  
                        hits[2 * roundIndex + 1] = 1
                if 455 < event.pos[0] < 545 and 480 < event.pos[1] < 510 and state == 'end':  
                    state = 'running'  
                    level = 'round'  
                    roundIndex = 0  
                    pygame.mouse.set_visible(False)  
                    hits = [0, 0, 0, 0, 0, 0]  
                    playSound('restart')  
                    pygame.time.delay(2000)  
                    playSound('BGM1')  
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
                    startTime1 = pygame.time.get_ticks()
                    startTime2 = pygame.time.get_ticks()  
            timeCount += 1
        elif level == 'shoot':
            if doOnce1:                                                                                           
                doOnce1 = False
                playSound('transmit')  
                start = pygame.time.get_ticks()                                                                   
            xoffset1,yoffset1,frm1 = spawn(xoffset1,yoffset1,randNum1,e1Life,startTime1,frm1)
            if pygame.time.get_ticks() - start > 500:
                if doOnce2:                   
                    doOnce2 = False           
                    playSound('transmit')     
                xoffset2,yoffset2,frm2 = spawn(xoffset2,yoffset2,randNum2,e2Life,startTime2,frm2)           
            if pygame.time.get_ticks() - start > 6000:                                                            
                doOnce1 = True
                doOnce2 = True  
                frm1, e1Life, xoffset1, yoffset1, randNum1 = 1, True, 0, 0, random.randint(-6, 6)  
                frm2, e2Life, xoffset2, yoffset2, randNum2 = 1, True, 0, 0, random.randint(-6, 6)                   
                roundIndex += 1      
                if roundIndex < 3:   
                    level = 'round'  
                else:                
                    state = 'end'
                    pygame.mouse.set_visible(True)      
                    if sum(hits) > 2:                   
                        playSound('win')                
                    else:                               
                        playSound('lose')               
                    pygame.mixer.music.stop()           
        screen.blit(sight,(0,0))
        if fire:
            screen.blit(flash,(0,0))
            fire = False
        if gunState == 'reload':
            if gunCount == 3:
                gunCount = 0
                gunFrm += 1
                if gunFrm == 6:
                    gunFrm = 0
                    gunState = 'hold'
            gunCount += 1
        screen.blit(guns[gunFrm],(0,0))
        screen.blit(bullets[bulFrm],(850,20))
    elif state == 'end':
        score()                               
    clock.tick(60)
    pygame.display.update()
pygame.quit()
sys.exit()