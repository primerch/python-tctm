import pygame
import sys

# 初始化pygame
pygame.init()

# 设置屏幕大小
WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# 设置标题
pygame.display.set_caption('精灵大乱斗')


# UI类
class UI(pygame.sprite.Sprite):
    def __init__(self, ui_path, pos=(0, 0)):
        super(UI, self).__init__()
        self.image = pygame.image.load(ui_path)
        self.rect = self.image.get_rect()
        self.rect.topleft = pos


# 游戏状态
gameState = 'start'
startSprites = pygame.sprite.Group()
# 开始页精灵初始化
startPage = UI('images/UI/start.png')
startSprites.add(startPage)
# 游戏主循环
running = True
clock = pygame.time.Clock()
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(25)
    if gameState == 'start':
        startSprites.draw(screen)

pygame.quit()
sys.exit()
