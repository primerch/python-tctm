import pygame

pygame.init()
screen = pygame.display.set_mode((1100, 600))
bg = pygame.image.load('images/bg.png')


# 1. 定义一种水果类型，规定所有水果都包含三个属性
class Fruit:
    def __init__(self, img, x, y):
        self.img = img
        self.x = x
        self.y = y


# 2. 创建一个水果类型的对象apple，保存苹果的数据
apple = Fruit('images/apple/full.png', 100, 200)
print(apple.__dict__)
# 3. 创建一个水果类型的对象banana，保存香蕉的数据
banana = Fruit('images/banana/full.png', 300, 200)
print(banana.__dict__)
# 4. 创建一个水果类型的对象orange，保存橙子的数据
orange = Fruit('images/orange/full.png', 500, 200)
print(orange.__dict__)
while True:
    screen.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
    pygame.time.delay(80)
