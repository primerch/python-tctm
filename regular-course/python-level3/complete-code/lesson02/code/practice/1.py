"""

请使用pygame制作一个愤怒的小鸟游戏。
1.创建一个(1250,700)的窗口
2.加载images文件夹下的游戏背景图片bg.png和小鸟的图片bird.png
3.小鸟的初始位置为(135, 315)，初始垂直速度为33并递减2，初始水平速度为30，先向上飞再向下飞
4.每次延时30ms
请只输出可以复制的代码块

"""
# 使用以上提示词文本制作愤怒的小鸟游戏
import pygame

# 初始化
pygame.init()
# 创建窗口
window = pygame.display.set_mode((1250, 700))
# 加载图片
background = pygame.image.load('images/bg.png')
bird = pygame.image.load('images/bird.png')

# 小鸟的初始位置和速度
bird_x = 135
bird_y = 315
bird_velocity = 33
bird_gravity = 2
bird_horizontal_speed = 30

# 游戏循环
running = True
while running:
    # 绘制背景和小鸟
    window.blit(background, (0, 0))
    window.blit(bird, (bird_x, bird_y))

    # 更新小鸟的垂直位置和速度
    bird_y -= bird_velocity
    bird_velocity -= bird_gravity

    # 更新小鸟的水平位置
    bird_x += bird_horizontal_speed

    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 更新窗口
    pygame.display.update()

    # 延时
    pygame.time.delay(30)

# 退出游戏
pygame.quit()
