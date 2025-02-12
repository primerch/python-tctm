"""
请使用pygame制作一个弹力球游戏，我已经在images文件夹中准备了如下资源：
1.在images文件夹中有一个张1400*600的游戏背景图bgjpg;
2.还有一个碗豆射手图片peashooter.png.
3.子弹图片bulletpng，
4.僵尸图片zombie.png，僵尸死亡图片die.png

我希望你创建僵尸类，豌豆射手类和子弹类，实现如下功能:
1.创建一个1400*600的游戏窗口，在主循环中绘制背景图片
2.在左上角坐标为(280,300)和(690,250)的位置分别绘制一个院豆射手和僵尸，他们都不移动
3.现豆射手每次间阳3秒向右发射一颗子弹，子弹的初始坐标为(350.300)
4.当子弹击中僵尸3次时，它就会死亡，此时僵尸图片切换为僵尸死亡图片
5.对子弹和僵尸进行精准碰撞检测时，请先使用pygame.mask.from_surface获取他们图片对应的mask对象，然后
计算两者的相对坐标，之后使用overlap方法判断两者是否重叠

请输出可以运行的代码
"""
# 请使用上述提示词，实现植物大战僵尸中的碰撞检测

import pygame
from pygame.locals import *
import time


class Zombie(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/zombie.png")
        self.dead_image = pygame.image.load("images/die.png")
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = (690, 250)
        self.mask = pygame.mask.from_surface(self.image)
        self.health = 3
        self.dead = False

    def update(self):
        if self.health <= 0:
            self.dead = True
            self.image = self.dead_image


class Peashooter(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/peashooter.png")
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = (280, 300)
        self.mask = pygame.mask.from_surface(self.image)


class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/bullet.png")
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = (350, 300)
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = 10

    def update(self):
        self.rect.left += self.speed


def main():
    pygame.init()
    screen = pygame.display.set_mode((1400, 600))
    pygame.display.set_caption("植物大战僵尸游戏")

    background = pygame.image.load("images/bg.jpg").convert()

    all_sprites = pygame.sprite.Group()
    zombies = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    pea_shooter = Peashooter()
    zombie = Zombie()

    all_sprites.add(pea_shooter)
    all_sprites.add(zombie)
    zombies.add(zombie)

    clock = pygame.time.Clock()
    last_shot_time = 0

    while True:
        screen.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return

        current_time = time.time()
        if current_time - last_shot_time >= 3:
            bullet = Bullet()
            all_sprites.add(bullet)
            bullets.add(bullet)
            last_shot_time = current_time

        for bullet in bullets:
            bullet.update()
            if pygame.sprite.spritecollide(bullet, zombies, False, pygame.sprite.collide_mask):
                bullet.kill()
                zombie.health -= 1

        for zombie in zombies:
            if not zombie.dead:
                all_sprites.draw(screen)
            zombie.update()

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
