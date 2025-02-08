# 课堂练习二
# 请完善程序，实现按下空格键后发射炮弹的效果
# 提示：发射炮弹的代码已预留，只需完成按下空格键后，将游戏状态切换为炮弹发射状态（shoot）即可
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1000, 600))
# 加载背景图片
bg = pygame.image.load('image/bg1.png')
# 加载炮弹图片
ball = pygame.image.load('image/ball.png')
# 游戏状态
state = 'start'
# 炮弹的初始y坐标
y = 430

while True:
    screen.blit(bg, (0, 0))
    # 事件获取
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
        # 请在下方编写代码

    # 炮弹发射状态
    if state == 'shoot':
        screen.blit(ball, (475, y))
        y -= 5
        if y < 0:
            state = 'start'
            y = 430
    pygame.time.delay(15)
    pygame.display.update()
