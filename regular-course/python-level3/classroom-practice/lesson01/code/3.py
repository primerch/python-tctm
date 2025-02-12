import pygame

pygame.init()
screen = pygame.display.set_mode((1100, 600))
bg = pygame.image.load('images/bg.png')

# 1. 定义一种水果类型，规定所有水果都包含三个属性

# 2. 创建一个水果类型的对象apple，保存苹果的数据

# 3. 创建一个水果类型的对象banana，保存香蕉的数据

# 4. 创建一个水果类型的对象orange，保存橙子的数据

while True:
    screen.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
    pygame.time.delay(80)
