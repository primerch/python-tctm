import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1100, 600))


class FlyObject:
    def __init__(self, img, x, y):
        self.img = pygame.image.load(img)
        w, h = self.img.get_size()
        self.centerX = x + w / 2
        self.centerY = y + h / 2
        self.speedY = random.randint(30, 48)
        self.speedX = random.randint(-10, 10)
        self.angle = 0
        self.imgParted = pygame.image.load(img.replace('full.png', 'parted.png'))
        typeName = type(self).__name__
        self.music = pygame.mixer.Sound('music/' + typeName + '.mp3')
        self.isCut = False

    def draw(self):
        if self.speedX < 0:
            self.angle -= 5
        else:
            self.angle += 5
        self.newImg = pygame.transform.rotate(self.img, self.angle)
        self.rect = self.newImg.get_rect(center=(self.centerX, self.centerY))
        screen.blit(self.newImg, self.rect)

    def move(self):
        self.centerY -= self.speedY
        self.speedY -= 2
        self.centerX -= self.speedX

    def bang(self):
        self.img = self.imgParted
        self.music.play()


class Juice:
    def __init__(self, img):
        self.img = pygame.image.load(img)
        self.centerX = None
        self.centerY = None

    def draw(self):
        rect = self.img.get_rect(center=(self.centerX, self.centerY))
        screen.blit(self.img, rect)


class Fruit(FlyObject):
    def __init__(self, img, x, y):
        super().__init__(img, x, y)
        self.juice = Juice(img.replace('full.png', 'juice.png'))

    def bang(self):
        super().bang()
        self.juice.centerX = self.centerX
        self.juice.centerY = self.centerY

    def draw(self):
        if self.isCut:
            self.juice.draw()
        super().draw()


class Bomb(FlyObject):
    pass


class Knife:
    def __init__(self, img, x, y):
        self.img = pygame.image.load(img)
        self.x = x
        self.y = y

    def draw(self):
        screen.blit(self.img, (self.x, self.y))

    def move(self):
        mouseX, mouseY = pygame.mouse.get_pos()
        self.x = mouseX - 60
        self.y = mouseY - 60

    def collide(self, fruit):
        if fruit.isCut:
            return
        knifeMask = pygame.mask.from_surface(self.img)
        fruitMask = pygame.mask.from_surface(fruit.newImg)
        offset = (fruit.rect.x - self.x, fruit.rect.y - self.y)
        result = knifeMask.overlap(fruitMask, offset)
        if result:
            fruit.bang()
            fruit.isCut = True


bg = pygame.image.load("images/bg.png")
fruitImgs = ['images/pineapple/full.png', 'images/orange/full.png',
             'images/pitaya/full.png', 'images/kiwi/full.png',
             'images/lemon/full.png', 'images/apple/full.png',
             'images/pomegranate/full.png', 'images/peach/full.png',
             'images/watermelon/full.png', 'images/banana/full.png',
             'images/coconut/full.png']
fruits = []
bomb = Bomb('images/bomb/full.png', random.randint(100, 900), 600)
knife = Knife('images/knife.png', 550, 300)

# 1. 定义Game类

# 2. 把类外边定义的全局变量bg，fruitImgs，fruits，bomb和knife移动到Game类中，定义成类变量

# 3. 把下方所有代码中使用的全局变量修改为类变量
for i in range(10):
    fruit = Fruit(random.choice(fruitImgs), random.randint(100, 900), 600)
    fruits.append(fruit)

while True:
    screen.blit(bg, (0, 0))
    for fruit in fruits:
        fruit.draw()
        fruit.move()
        knife.collide(fruit)
        if fruit.centerY > 700:
            i = fruits.index(fruit)
            fruits[i] = Fruit(random.choice(fruitImgs), random.randint(100, 900), 600)
    bomb.draw()
    bomb.move()
    knife.collide(bomb)
    if bomb.centerY > 700:
        bomb = Bomb('images/bomb/full.png', random.randint(100, 900), 600)
    knife.draw()
    knife.move()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
    pygame.time.delay(80)
