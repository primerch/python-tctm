import pygame

pygame.init()
screen = pygame.display.set_mode((1100, 600))
bg = pygame.image.load("images/bg.png")


class Fruit:
    def __init__(self, img, x, y):
        # 1.修改img属性值为load方法加载的图片
        self.img = img
        self.x = x
        self.y = y


apple = Fruit('images/apple/full.png', 100, 200)
banana = Fruit('images/banana/full.png', 300, 200)
orange = Fruit('images/orange/full.png', 500, 200)

while True:
    screen.blit(bg, (0, 0))
    # 2.访问对象属性，绘制水果图片

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
    pygame.time.delay(80)
