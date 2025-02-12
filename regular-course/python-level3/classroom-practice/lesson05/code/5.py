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


四、补规则
请只输出要求的代码块，不用输出已知的代码。

"""
# 2. 请使用上述提示词定义Fruit类，并创建一个对象

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
    pygame.time.delay(80)
