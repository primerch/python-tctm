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
        self.speedY = random.randint(30, 48)

    def draw(self):
        screen.blit(self.img, (self.x, self.y))

    def move(self):
        self.y -= self.speedY


# 1.修改水果初始x坐标为100-900范围内的随机值，y坐标为600
apple = Fruit('images/apple/full.png', random.randint(100, 900), 600)
banana = Fruit('images/banana/full.png', random.randint(100, 900), 600)
orange = Fruit('images/orange/full.png', random.randint(100, 900), 600)


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
    apple.move()
    banana.move()
    orange.move()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
    pygame.time.delay(80)
