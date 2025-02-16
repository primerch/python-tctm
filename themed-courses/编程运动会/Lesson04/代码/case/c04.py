import pygame
import sys
import random
pygame.init()
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('滑板少年')
# 加载背景图
bg = pygame.image.load('images/bg.png').convert_alpha()
# 角色站立名称列表
stands = ['stand.png', 'stand1.png', 'stand2.png', 'stand3.png']
# 角色下蹲名称列表
crouches = ['crouch.png', 'crouch1.png', 'crouch2.png', 'crouch3.png']
# 加载障碍图
block1 = pygame.image.load('images/barrier1.png').convert_alpha()
block2 = pygame.image.load('images/barrier2.png').convert_alpha()
# 生命名称列表
hps = ['hp.png', 'hp1.png', 'hp2.png', 'hp3.png']
# 进度条名称列表
bars = ['bar.png', 'bar1.png', 'bar2.png', 'bar3.png', 'bar4.png', 'bar5.png', 'bar6.png']
# 加载序列图函数
def loadImg(names):
    images = []
    for name in names:
        pic = pygame.image.load('images/' + name).convert_alpha()
        images.append(pic)
    return images


# 加载角色站立图
standList = loadImg(stands)
# 加载角色下蹲图
crouchList = loadImg(crouches)
# 加载血量图
hpList = loadImg(hps)
# 加载糖果图
gift = pygame.image.load('images/gift.png').convert_alpha()
# 加载进度条图
barList = loadImg(bars)

timer = pygame.time.Clock()
running = True
state = 'start'
bx = 0
index = 0
playerX = 40
playerY = 330
delay = 0
jump = False
jumpH = 25
currentState = standList
# 障碍物坐标
block1X = random.randint(2000, 2500)  # 新加
block1Y = 0
block2X = random.randint(1000, 1500)
block2Y = 450
# 开始时间
startTime = pygame.time.get_ticks()
distance = 0
hp = 3
# 加载结果图
bg2 = pygame.image.load('images/bg2.png').convert_alpha()
font = pygame.font.SysFont(None, 50)
giftX = random.randint(2000, 2500)
giftY = 450
candy = 0
invincible = False
mark = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_UP:
                jump = True
            if e.key == pygame.K_DOWN:
                currentState = crouchList
        if e.type == pygame.KEYUP:
            if e.key == pygame.K_DOWN:
                currentState = standList

    if state == 'start':
        screen.blit(bg, (bx, 0))
        screen.blit(bg, (bx + 800, 0))
        screen.blit(block1, (block1X, block1Y))
        screen.blit(block2, (block2X, block2Y))
        screen.blit(currentState[index], (playerX, playerY))
        screen.blit(hpList[hp], (625, 10))
        screen.blit(gift, (giftX, giftY))
        screen.blit(barList[candy], (0, 10))
        if not invincible:
            bx -= 10
            giftX -= 10
            block1X -= 10
            block2X -= 10
        else:
            bx -= 20
            giftX -= 20
            block1X -= 20
            block2X -= 20
            distance += 2
            if mark:
                tempTime = pygame.time.get_ticks()
                mark = False
            endTime = (pygame.time.get_ticks() - tempTime) // 1000
            if endTime == 3:
                candy = 0
                invincible = False
                mark = True
        if bx <= -800:
            bx = 0
        if block1X < -250:
            block1X = random.randint(2000, 2500)
        if block2X < -250:
            block2X = random.randint(1000, 1500)
        if giftX < -250:
            giftX = random.randint(2000, 2500)
        # block2碰撞检测
        if playerY + currentState[index].get_height() > block2Y:
            if playerX-block2.get_width() < block2X < playerX+currentState[index].get_width():
                print('撞到了障碍2')
                block2X = random.randint(1000, 1500)
                if not invincible:
                    hp -= 1
                if hp == 0:
                    state = 'end'
        # block1碰撞检测
        if playerX-block1.get_width() < block1X < playerX+currentState[index].get_width():
            if currentState == standList:
                y = playerY
            else:
                y = playerY + 10
            if y <= block1.get_height():
                print('撞到了障碍1')
                block1X = random.randint(2000, 2500)
                if not invincible:
                    hp -= 1
                if hp == 0:
                    state = 'end'
        # 糖果碰撞检测
        if playerX - gift.get_width() < giftX < playerX + currentState[index].get_width():
            if playerY + currentState[index].get_height() > giftY:
                print('撞到了糖果')
                giftX = random.randint(2000, 2500)
                if not invincible:
                    candy += 1
                if candy == 6:
                    invincible = True

        delay += 1
        if delay % 15 == 0:
            index += 1
            if index == 3:
                index = 0
        if jump:
            playerY -= jumpH
            jumpH -= 1
            if playerY >= 330:
                jump = False
                jumpH = 25
        # 计算滑行距离
        time = pygame.time.get_ticks() - startTime
        if time >= 1000:
            distance += 1
            print(distance)
            startTime = pygame.time.get_ticks()

    if state == 'end':
        screen.blit(bg2, (0, 0))
        text = 'Score: ' + str(distance)
        word = font.render(text, True, 'orange')
        screen.blit(word, (400 - word.get_width() / 2, 300 - word.get_height() / 2))
    pygame.display.update()
    timer.tick(60)
pygame.quit()
sys.exit()
