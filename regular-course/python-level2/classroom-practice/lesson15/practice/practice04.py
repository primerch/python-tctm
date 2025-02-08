# 课堂练习四
# 请完善程序，实现通过按下空格键控制游戏（小派/童童）回合的切换
# 提示：小派回合（pai）与童童回合（tong）的代码需要自行编写，所需图片已在第10、12行加载完毕
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((900, 422))
# 加载小派回合图片
pai = pygame.image.load('image/turn1.png')
# 加载童童回合图片
tong = pygame.image.load('image/turn2.png')
# 回合（默认是小派回合）
turn = 'pai'

while True:
    # 事件获取
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
        # 请在下方编写代码

    # 请在下方编写双方回合的代码

    pygame.time.delay(15)
    pygame.display.update()
