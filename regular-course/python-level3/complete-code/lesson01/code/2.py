"""

使用Python语言中的pygame库创建游戏窗口，满足以下条件：
1、创建1100*600游戏窗口并存放在变量screen中
2、加载images/bg.png下的图片并存放在变量bg中
3、在主循环中绘制背景图片bg，处理退出事件，更新屏幕，并延时80毫秒
请输出可以直接复制的代码块

"""
# 1. 请使用上述提示词文本，创建游戏窗口
import pygame

# 初始化pygame
pygame.init()
# 创建游戏窗口
screen = pygame.display.set_mode((1100, 600))
# 加载背景图片
bg = pygame.image.load("images/bg.png")
# 游戏主循环
running = True
while running:
    # 绘制背景图片
    screen.blit(bg, (0, 0))
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # 更新屏幕
    pygame.display.update()
    # 延时80毫秒
    pygame.time.delay(80)
# 退出pygame
pygame.quit()
