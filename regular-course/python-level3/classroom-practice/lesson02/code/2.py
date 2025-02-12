import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1100, 600))
bg = pygame.image.load("images/bg.png")


class Fruit:
    def __init__(self, img, x, y):
        self.img = pygame.image.load(img)
        self.x = x
        self.y = y
        # 1.定义speedY属性

    def draw(self):
        screen.blit(self.img, (self.x, self.y))

    # 2.定义move方法, 实现水果向上移动


apple = Fruit('images/apple/full.png', 100, 200)
banana = Fruit('images/banana/full.png', 300, 200)
orange = Fruit('images/orange/full.png', 500, 200)


class Bomb:
    def __init__(self, img, x, y):
        self.img = pygame.image.load(img)
        self.x = x
        self.y = y

    def draw(self):
        screen.blit(self.img, (self.x, self.y))


bomb1 = Bomb('images/bomb/full.png', 200, 400)
bomb2 = Bomb('images/bomb/full.png', 500, 400)

while True:
    screen.blit(bg, (0, 0))
    apple.draw()
    banana.draw()
    orange.draw()
    bomb1.draw()
    bomb2.draw()
    # 3.水果对象调用move方法

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
    pygame.time.delay(80)
