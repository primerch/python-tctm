"""

请使用pygame制作一个雷霆战机游戏。
我已经在images文件夹中准备了如下资源：

1. 游戏背景图bg.png，
2. 60*75大小的英雄飞机图片hero.png，
3. 9*21大小的子弹图片bullet.png，
4. 57*45大小的敌飞机图片enemy.png，和五张敌飞机爆炸图片down1.png,down2.png一直到down5.png

我希望你使用面向对象的方式实现如下功能：
1. 创建一个480, 650的游戏窗口，在主循环中绘制背景图片
2. 创建一个英雄飞机类，初始坐标为（240,550），实现绘制英雄飞机，跟随鼠标移动
3. 创建一个子弹类，实现绘制子弹和子弹竖直向上移动
4. 创建一个敌飞机类，它的初始x坐标随机产生，y坐标为-45，实现绘制敌飞机并竖直向下移动
5. 定义全局变量记录上一次产生敌飞机的时间，实现每次间隔1.5秒自动创建一个敌飞机，然后绘制并移动敌飞机。
6. 定义全局变量记录上一次发射子弹时间，实现每次间隔0.3秒自动产生一颗子弹，它的初始坐标由英雄飞机坐标决定，然后绘制并移动子弹。
7. 当子弹碰到敌飞机后，子弹直接消失，而每次更新屏幕时依次改为绘制敌飞机爆炸图片down1.png，一直到down5.png，绘制5张图片后消失。

请输出可以直接运行的代码块

"""
import pygame
import random

# 初始化pygame
pygame.init()

# 游戏窗口大小
WINDOW_WIDTH = 480
WINDOW_HEIGHT = 650

# 游戏窗口
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# 游戏标题
pygame.display.set_caption("雷霆战机")

# 加载背景图片
bg_img = pygame.image.load("images/bg.png")

# 加载英雄飞机图片
hero_img = pygame.image.load("images/hero.png")
hero_width = hero_img.get_width()
hero_height = hero_img.get_height()

# 加载子弹图片
bullet_img = pygame.image.load("images/bullet.png")
bullet_width = bullet_img.get_width()
bullet_height = bullet_img.get_height()

# 加载敌飞机图片
enemy_img = pygame.image.load("images/enemy.png")
enemy_width = enemy_img.get_width()
enemy_height = enemy_img.get_height()

# 加载敌飞机爆炸图片
enemy_down_imgs = []
for i in range(1, 6):
    enemy_down_imgs.append(pygame.image.load("images/down{}.png".format(i)))


# 定义英雄飞机类
class HeroPlane:
    def __init__(self):
        self.x = WINDOW_WIDTH // 2 - hero_width // 2  # 初始位置在窗口中央
        self.y = WINDOW_HEIGHT - hero_height - 50  # 初始位置在窗口底部靠上
        self.speed = 5

    def draw(self):
        window.blit(hero_img, (self.x, self.y))

    def move(self):
        self.x, self.y = pygame.mouse.get_pos()


# 定义子弹类
class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 7

    def draw(self):
        window.blit(bullet_img, (self.x, self.y))

    def move(self):
        self.y -= self.speed


# 定义敌飞机类
class EnemyPlane:
    def __init__(self):
        self.x = random.randint(0, WINDOW_WIDTH - enemy_width)  # 初始位置随机
        self.y = -enemy_height  # 初始位置在窗口顶部
        self.speed = 3

    def draw(self):
        window.blit(enemy_img, (self.x, self.y))

    def move(self):
        self.y += self.speed


# 创建英雄飞机对象
hero_plane = HeroPlane()

# 存储子弹的列表
bullets = []

# 存储敌飞机的列表
enemies = []

# 上一次产生敌飞机的时间
last_enemy_time = pygame.time.get_ticks()

# 上一次发射子弹的时间
last_bullet_time = pygame.time.get_ticks()

# 游戏主循环
running = True
while running:
    # 绘制背景图片
    window.blit(bg_img, (0, 0))

    # 事件处理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 绘制英雄飞机并跟随鼠标移动
    hero_plane.draw()
    hero_plane.move()

    # 创建子弹
    current_time = pygame.time.get_ticks()
    if current_time - last_bullet_time >= 300:
        bullet = Bullet(hero_plane.x + hero_width // 2 - bullet_width // 2, hero_plane.y)
        bullets.append(bullet)
        last_bullet_time = current_time

    # 绘制并移动子弹
    for bullet in bullets:
        bullet.draw()
        bullet.move()
        if bullet.y < -bullet_height:
            bullets.remove(bullet)

    # 创建敌飞机
    if current_time - last_enemy_time >= 1500:
        enemy = EnemyPlane()
        enemies.append(enemy)
        last_enemy_time = current_time

    # 绘制并移动敌飞机
    for enemy in enemies:
        enemy.draw()
        enemy.move()
        if enemy.y > WINDOW_HEIGHT:
            enemies.remove(enemy)

    # 子弹和敌飞机的碰撞检测
    for bullet in bullets:
        for enemy in enemies:
            if bullet.x + bullet_width > enemy.x and bullet.x < enemy.x + enemy_width and bullet.y < enemy.y + enemy_height:
                enemies.remove(enemy)
                bullets.remove(bullet)
                for i in range(5):
                    window.blit(enemy_down_imgs[i], (enemy.x, enemy.y))

    # 刷新屏幕
    pygame.display.flip()

# 退出pygame
pygame.quit()
