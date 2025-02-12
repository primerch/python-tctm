import pygame

pygame.init()
screen = pygame.display.set_mode((1100, 600))
bg = pygame.image.load("images/bg.png")


class Fruit:
    def __init__(self, img, x, y):
        self.img = pygame.image.load(img)
        self.x = x
        self.y = y

    # 1.定义draw方法，绘制水果图片
    def draw(self):
        screen.blit(self.img, (self.x, self.y))


apple = Fruit('images/apple/full.png', 100, 200)
banana = Fruit('images/banana/full.png', 300, 200)
orange = Fruit('images/orange/full.png', 500, 200)


class Bomb:
    def __init__(self, img, x, y):
        self.img = pygame.image.load(img)
        self.x = x
        self.y = y


bomb1 = Bomb('images/bomb/full.png', 200, 400)
bomb2 = Bomb('images/bomb/full.png', 500, 400)

while True:
    screen.blit(bg, (0, 0))
    # 2.水果对象调用draw方法，绘制图片
    apple.draw()
    banana.draw()
    orange.draw()
    screen.blit(bomb1.img, (bomb1.x, bomb1.y))
    screen.blit(bomb2.img, (bomb2.x, bomb2.y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
    pygame.time.delay(80)
