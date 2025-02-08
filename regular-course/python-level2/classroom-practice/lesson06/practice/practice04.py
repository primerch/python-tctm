# 课堂练习四
# 补全下列代码，实现移动鼠标，更换精灵照片的程序
# 提示：程序所需图片在images文件夹下

import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1000, 700))

# 图片存储列表
plist = []
key = 0


# 图片加载
def load_pic(path):
    # 图片加载功能，提示：图片名字是0-9，尝试用for i in range()
    pass


# 游戏资源加载，修改参数。
load_pic('images/pic')
bg = pygame.image.load('images/bg1.png')
screen.blit(plist[0], (0, 0))
screen.blit(bg, (0, 0))
pygame.display.update()

while True:

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
        if e.type == pygame.MOUSEMOTION:
            # 图片显示，完成点击鼠标更换精灵图片功能
            pass
