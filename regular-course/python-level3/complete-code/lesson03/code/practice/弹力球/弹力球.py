"""

请使用pygame制作一个弹力球游戏，我已经在images文件夹中准备了如下资源：
1. 游戏背景图bg.png
2. 弹力球图片ball.png
3. 砖块图片brick.png
4. 挡板图片baffle.png

我希望你使用面向对象的方式实现如下功能

1. 游戏窗口大小为（480,650），游戏帧率为60，在主循环中绘制背景，
2. 游戏得分初始为0，并绘制在10,10位置，文字颜色为黑色，它是全局变量
2. 绘制一个挡板，y坐标为600，x坐标为鼠标的x坐标，它的长度为100，
3. 绘制一个弹力球，初始位置在挡板上方，初始垂直移动方向向上，水平移动方向随机，水平和垂直移动速度为5，
5. 绘制5行8列个砖块，从坐标为(85, 100)的位置开始，并且他们上下左右之间的间隔为10
6. 当弹力球碰到挡板或者窗口左、右、上边界时反弹，碰到窗口下边界时游戏结束
7. 当弹力球碰到砖块时砖块就会消失，弹力球反弹，并且游戏得分加一

请只输出符合要求的代码块，且一定要在代码中添加每行注释

"""
import pygame
import random

# 初始化pygame
pygame.init()

# 游戏窗口大小
WIDTH = 480
HEIGHT = 650

# 颜色定义
BLACK = (0, 0, 0)

# 创建游戏窗口
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("弹力球游戏")

# 加载图片资源
bg_image = pygame.image.load("images/bg.png")
ball_image = pygame.image.load("images/ball.png")
brick_image = pygame.image.load("images/brick.png")
baffle_image = pygame.image.load("images/baffle.png")

# 设置游戏帧率
clock = pygame.time.Clock()
FPS = 60

# 定义全局变量
score = 0


# 绘制挡板的类
class Baffle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = baffle_image
        self.rect = self.image.get_rect()

    def update(self):
        # 挡板的位置跟随鼠标的x坐标
        self.rect.x = pygame.mouse.get_pos()[0]
        # 限制挡板在窗口范围内移动
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        self.rect.y = 600


# 绘制弹力球的类
class Ball(pygame.sprite.Sprite):
    def __init__(self, x_speed, y_speed):
        super().__init__()
        self.image = ball_image
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = 580
        self.x_speed = x_speed
        self.y_speed = y_speed

    def update(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

        # 检测弹力球是否碰到窗口边界
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.x_speed = -self.x_speed
        if self.rect.top <= 0:
            self.y_speed = -self.y_speed
        if self.rect.bottom >= HEIGHT:
            game_over()

        # 检测弹力球是否碰到挡板
        if pygame.sprite.collide_rect(self, baffle):
            self.y_speed = -self.y_speed

        # 检测弹力球是否碰到砖块
        for brick in brick_group:
            if pygame.sprite.collide_rect(self, brick):
                self.y_speed = -self.y_speed
                brick.kill()
                update_score()


# 绘制砖块的类
class Brick(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = brick_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


# 更新得分
def update_score():
    global score
    score += 1


# 绘制背景图和得分
def draw_background():
    screen.blit(bg_image, (0, 0))
    font = pygame.font.Font(None, 36)
    text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(text, (10, 10))


# 游戏结束
def game_over():
    pygame.quit()
    exit()


# 创建挡板和弹力球
baffle = Baffle()
ball = Ball(random.choice([-5, 5]), -5)

# 创建砖块组
brick_group = pygame.sprite.Group()
for row in range(5):
    for col in range(8):
        brick = Brick(85 + col * (brick_image.get_width() + 10), 100 + row * (brick_image.get_height() + 10))
        brick_group.add(brick)

# 游戏主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 绘制背景图和得分
    draw_background()

    # 更新挡板和弹力球
    baffle.update()
    ball.update()

    # 绘制挡板和弹力球
    screen.blit(baffle.image, baffle.rect)
    screen.blit(ball.image, ball.rect)

    # 绘制砖块
    brick_group.draw(screen)

    # 更新屏幕显示
    pygame.display.flip()

    # 控制游戏帧率
    clock.tick(FPS)

# 退出游戏
pygame.quit()
