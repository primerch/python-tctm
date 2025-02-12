import pygame
import random
import cv2
from mediapipe.python.solutions.hands import Hands
from mediapipe.python.solutions.drawing_utils import draw_landmarks

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
    # 1. 重写bang()方法，并使用super()函数调用父类的bang()方法
    def bang(self):
        super().bang()
        # 2. 当切到炸弹时，生命值减1
        Game.life -= 1


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


class AICam:
    cap = cv2.VideoCapture(0)
    hand = Hands()

    @classmethod
    def recognize(cls):
        ret, frame = cls.cap.read()
        frame = cv2.flip(frame, 1)
        cvtFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        outputs = cls.hand.process(cvtFrame)
        hands = outputs.multi_hand_landmarks
        if hands:
            draw_landmarks(frame, hands[0])
            finger = hands[0].landmark[8]
            Game.knife.x = finger.x * 1100
            Game.knife.y = finger.y * 600
        cv2.namedWindow('AICam', cv2.WINDOW_NORMAL)
        aspect_ratio = frame.shape[1] / frame.shape[0]
        cv2.resizeWindow('AICam', 200, int(200 / aspect_ratio))
        cv2.moveWindow('AICam', 0, 0)
        cv2.imshow('AICam', frame)
        cv2.waitKey(1)


class Game:
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
    life = 3
    heart = pygame.image.load('images/heart.png')


for i in range(10):
    fruit = Fruit(random.choice(Game.fruitImgs), random.randint(100, 900), 600)
    Game.fruits.append(fruit)


class Utils:
    @staticmethod
    def drawText(text, pos):
        font = pygame.font.Font('fonts/WRYH.ttf', 40)
        textImg = font.render(str(text), True, 'orange')
        screen.blit(textImg, pos)


while True:
    screen.blit(Game.bg, (0, 0))
    screen.blit(Game.heart, (970, 40))
    Utils.drawText(Game.life, (1050, 30))
    AICam.recognize()
    for fruit in Game.fruits:
        fruit.draw()
        fruit.move()
        Game.knife.collide(fruit)
        if fruit.centerY > 700:
            i = Game.fruits.index(fruit)
            Game.fruits[i] = Fruit(random.choice(Game.fruitImgs), random.randint(100, 900), 600)
    Game.bomb.draw()
    Game.bomb.move()
    Game.knife.collide(Game.bomb)
    if Game.bomb.centerY > 700:
        Game.bomb = Bomb('images/bomb/full.png', random.randint(100, 900), 600)
    Game.knife.draw()
    Game.knife.move()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            AICam.cap.release()
            cv2.destroyAllWindows()
            exit()
    pygame.display.update()
    pygame.time.delay(80)
