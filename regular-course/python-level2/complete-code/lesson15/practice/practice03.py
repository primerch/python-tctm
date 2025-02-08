# 课堂练习三
# 请完善程序，实现通过按下Enter键控制游戏（进行/暂停）状态的切换
# 提示：进行状态（running）与暂停状态（pause）的代码已预留，只需完成按下Enter键后，切换游戏状态即可
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 450))
# 加载背景图片
bg = pygame.image.load('image/bg2.png')
# 加载飞机图片
plane = pygame.image.load('image/plane.png')
# 加载暂停图片
pause = pygame.image.load('image/pause.png')
# 游戏状态
state = 'running'
# 第一张背景图片的x坐标
x1 = 0
# 第二张背景图片的x坐标
x2 = 800

while True:
    # 事件获取
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
        # 请在下方编写代码
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_RETURN:
                if state == 'running':
                    state = 'pause'
                else:
                    state = 'running'
    # 进行状态
    if state == 'running':
        screen.blit(bg, (x1, 0))
        screen.blit(bg, (x2, 0))
        screen.blit(plane, (100, 200))
        x1 -= 3
        x2 -= 3
        if x1 < -800:
            x1 = 800
        if x2 < -800:
            x2 = 800
    # 暂停状态
    elif state == 'pause':
        screen.blit(bg, (x1, 0))
        screen.blit(bg, (x2, 0))
        screen.blit(plane, (100, 200))
        screen.blit(pause, (10, 10))

    pygame.time.delay(15)
    pygame.display.update()
