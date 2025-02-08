# 课堂练习3
# 完善程序，从坐标(100,50)的位置从上到下显示字典info中的信息
# 要求：每条信息左端对齐，上下间隔50，文字颜色为黑色
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1000, 625))
bg = pygame.image.load("pictures/bg.png")
screen.blit(bg, (0, 0))
font = pygame.font.SysFont('simhei', 25)
info = {
    '人物': '屈原',
    '所处时代': '战国末期',
    '出生地': '今湖北宣昌',
    '代表作': '《离骚》、《九歌》、《天问》'
}
# 显示人物信息
offset = 0
gap = 50
for x, y in info.items():
    words = x + '：' + y
    text = font.render(words, True, 'black')
    screen.blit(text, (100, 50 + offset * gap))
    offset += 1
while True:
    # 事件获取
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()
