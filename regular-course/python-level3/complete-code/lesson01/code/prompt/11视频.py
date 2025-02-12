"""

这是我今天编写的代码：
```
import pygame

pygame.init()
screen = pygame.display.set_mode((1100, 600))
bg = pygame.image.load("images/bg.png")


class Fruit:
    def __init__(self, img, x, y):
        self.img = pygame.image.load(img)
        self.x = x
        self.y = y


apple = Fruit('images/apple/full.png', 100, 200)
banana = Fruit('images/banana/full.png', 300, 200)
orange = Fruit('images/orange/full.png', 500, 200)

# 1. 创建炸弹类Bomb
class Bomb:
    def __init__(self,img,x,y):
        self.img = pygame.image.load(img)
        self.x = x
        self.y = y
# 2. 创建炸弹对象bomb1, 坐标(200, 400)和bomb2, 坐标(500, 400)
bomb1 = Bomb('images/bomb/full.png', 200, 400)
bomb2 = Bomb('images/bomb/full.png', 500, 400)
while True:
    screen.blit(bg, (0, 0))
    screen.blit(apple.img, (apple.x, apple.y))
    screen.blit(banana.img, (banana.x, banana.y))
    screen.blit(orange.img, (orange.x, orange.y))
    # 3. 访问炸弹对象属性，绘制炸弹图片
    screen.blit(bomb1.img, (bomb1.x, bomb1.y))
    screen.blit(bomb2.img, (bomb2.x, bomb2.y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
    pygame.time.delay(80)

```
请详细总结今天学习的知识点


"""
