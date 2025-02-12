import pygame

pygame.init()
screen = pygame.display.set_mode((1100, 600))
bg = pygame.image.load('images/bg.png')
screen.blit(bg, (0, 0))
# 1. 请编写定目标对应的提示词
"""

一、立角色
使用python语言的pygame库编写游戏。
二、述已知 
程序中导入了pygame库并定义了游戏窗口对象screen。
三、定目标 
现在你需要完成如下要求：
1. 定义Fruit类，它有3个属性：img,x,y。其中，img是pygame加载的图片，x和y分别是传入的x，y坐标
2. 创建一个fruit对象，传入'images/banana/full.png'，100,100，并绘制在screen上
四、补规则
请只输出要求的代码块，不用输出已知的代码。

"""


# 2. 请使用上述提示词定义Fruit类，并创建一个对象
class Fruit:
    def __init__(self, img, x, y):
        self.img = pygame.image.load(img)
        self.x = x
        self.y = y


fruit = Fruit('images/banana/full.png', 100, 100)
screen.blit(fruit.img, (fruit.x, fruit.y))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
    pygame.time.delay(80)
