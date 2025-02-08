import pygame
import sys

# 初始化及背景显示
pygame.init()
screen = pygame.display.set_mode((1000, 700))

# 单人角色属性字典，
playerData = {
    'HP': 1000,
    'maxHP': 1000,
    'atk': 100,
    'def': 50,
    'addHP': 200,
    'addAtk': 200,
    'addDef': 100,
    'magic': 1000
}
# boss属性字典
bossData = {
    'atk': 300,
    'def': 50,
    'HP': 10000,
    's1': 100,
    's2': 200,
    's3': 300,
    's4': 400,
}

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
