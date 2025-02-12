"""
AI小助手：https://gpt.dnzx.com/

使用AI小助手的提示词示例：
1. 请出10个谜语
2. 请使用python制作一个贪吃蛇游戏
3. 请帮我制作一份3天的北京旅行计划
4. 我想要学习打篮球，请给出一些学习教程
5. 请使用python制作一个程序生成九九乘法表
...

"""
# 1. 复制、粘贴AI小助手生成的代码
import pygame
import random

# 初始化游戏
pygame.init()

# 设置游戏窗口的尺寸
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# 定义颜色
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
green = pygame.Color(0, 255, 0)
red = pygame.Color(255, 0, 0)

# 定义蛇的初始位置和大小
snake_x = screen_width // 2
snake_y = screen_height // 2
snake_size = 20

# 定义蛇的移动速度和方向
snake_speed = 15
snake_direction = 'RIGHT'

# 定义食物的位置和大小
food_x = random.randint(0, screen_width // snake_size - 1) * snake_size
food_y = random.randint(0, screen_height // snake_size - 1) * snake_size
food_size = 20

# 初始化蛇的身体
snake_body = []
snake_length = 1

# 游戏循环
while True:
    # 处理游戏退出事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # 处理按键事件
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != 'DOWN':
                snake_direction = 'UP'
            if event.key == pygame.K_DOWN and snake_direction != 'UP':
                snake_direction = 'DOWN'
            if event.key == pygame.K_LEFT and snake_direction != 'RIGHT':
                snake_direction = 'LEFT'
            if event.key == pygame.K_RIGHT and snake_direction != 'LEFT':
                snake_direction = 'RIGHT'

    # 移动蛇的位置
    if snake_direction == 'UP':
        snake_y -= snake_size
    if snake_direction == 'DOWN':
        snake_y += snake_size
    if snake_direction == 'LEFT':
        snake_x -= snake_size
    if snake_direction == 'RIGHT':
        snake_x += snake_size

    # 判断是否吃到食物
    if snake_x == food_x and snake_y == food_y:
        food_x = random.randint(0, screen_width // snake_size - 1) * snake_size
        food_y = random.randint(0, screen_height // snake_size - 1) * snake_size
        snake_length += 1

    # 判断蛇是否碰到边界
    if snake_x >= screen_width or snake_x < 0 or snake_y >= screen_height or snake_y < 0:
        pygame.quit()
        quit()

    # 判断蛇是否碰到自身
    for segment in snake_body[:-1]:
        if segment == (snake_x, snake_y):
            pygame.quit()
            quit()

    # 更新蛇的身体
    snake_body.append((snake_x, snake_y))
    if len(snake_body) > snake_length:
        del snake_body[0]

    # 绘制游戏界面
    screen.fill(black)
    for segment in snake_body:
        pygame.draw.rect(screen, green, (segment[0], segment[1], snake_size, snake_size))
    pygame.draw.rect(screen, red, (food_x, food_y, food_size, food_size))

    # 更新帧并刷新画面
    pygame.display.update()
    pygame.time.Clock().tick(snake_speed)
