import time
import pygame
import random
import cv2
from mediapipe.python.solutions.hands import Hands
from mediapipe.python.solutions.drawing_utils import draw_landmarks
from mediapipe.python.solutions.face_mesh import FaceMesh

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
        self.isCut = False
        if type(self) == Fruit:
            self.music = pygame.mixer.Sound('music/fruit.mp3')
        else:
            self.music = pygame.mixer.Sound('music/bomb.mp3')

    def draw(self):
        if self.speedX > 0:
            self.angle += 5
        else:
            self.angle -= 5
        self.newImg = pygame.transform.rotate(self.img, self.angle)
        self.rect = self.newImg.get_rect(center=(self.centerX, self.centerY))
        screen.blit(self.newImg, self.rect)

    def move(self):
        self.centerY -= self.speedY
        self.speedY -= 2
        self.centerX += self.speedX

    def bang(self):
        self.img = self.imgParted
        self.isCut = True
        self.music.play()


class Fruit(FlyObject):

    def __init__(self, img, x, y):
        super().__init__(img, x, y)
        self.juice = Juice(img.replace('full.png', 'juice.png'))

    def bang(self):
        super().bang()
        self.juice.centerX = self.centerX
        self.juice.centerY = self.centerY
        Game.score += 1

    def draw(self):
        if self.isCut:
            self.juice.draw()
        super().draw()


class Juice:
    def __init__(self, img):
        self.img = pygame.image.load(img)
        self.centerX = 0
        self.centerY = 0
        self.alpha = 255

    def draw(self):
        rect = self.img.get_rect(center=(self.centerX, self.centerY))
        screen.blit(self.img, rect)
        self.alpha -= 5
        self.img.set_alpha(self.alpha)


class Bomb(FlyObject):

    def bang(self):
        super().bang()
        Game.score -= 3
        if Game.score < 0:
            Game.score = 0
        Game.life -= 1
        if Game.life <= 0:
            Game.state = "END"


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
        offset = fruit.rect.x - self.x, fruit.rect.y - self.y
        result = knifeMask.overlap(fruitMask, offset)
        if result:
            fruit.bang()

    def moveWithMark(self, hands, n):
        if hands:
            lm = hands[0].landmark[n]
            self.x = (1 - lm.x) * 1100
            self.y = lm.y * 600


class AICamera:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.frame = None
        self.hand = Hands()
        self.faceMesh = FaceMesh()

    def take(self):
        ret, image = self.cap.read()
        self.frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    def draw(self):
        img = pygame.surfarray.make_surface(self.frame)
        img = pygame.transform.rotate(img, -90)
        w, h = img.get_size()
        s = w / h
        img = pygame.transform.scale(img, (200, 200 / s))
        screen.blit(img, (870, 10))

    def recognize(self):
        outputs = self.hand.process(self.frame)
        hands = outputs.multi_hand_landmarks
        return hands

    def mark(self, hands):
        if hands:
            for hand in hands:
                draw_landmarks(self.frame, hand)

    def recogFace(self):
        outputs = self.faceMesh.process(self.frame)
        faces = outputs.multi_face_landmarks
        return faces


class Game:
    bg = pygame.image.load("images/bg.png")
    knife = Knife('images/knife.png', 550, 300)
    bomb = Bomb('images/bomb/full.png', random.randint(100, 900), 600)
    fruitImgs = ['images/pineapple/full.png', 'images/orange/full.png',
                 'images/pitaya/full.png', 'images/kiwi/full.png',
                 'images/lemon/full.png', 'images/apple/full.png',
                 'images/pomegranate/full.png', 'images/peach/full.png',
                 'images/watermelon/full.png', 'images/banana/full.png',
                 'images/coconut/full.png']
    fruits = []
    scoreBoard = pygame.image.load("images/scoreBoard.png")
    score = 0
    state = 'START'
    startBg = pygame.image.load("images/startBg.png")
    life = 3
    heart = pygame.image.load('images/heart.png')
    endBg = pygame.image.load("images/endBg.png")
    cameraBoard = pygame.image.load('images/cameraBoard.png')
    camera = AICamera()
    challenge = pygame.time.get_ticks()
    keydown = []

    @classmethod
    def createObj(cls):
        for i in range(10):
            fruit = Fruit(random.choice(cls.fruitImgs), random.randint(100, 900), 600)
            cls.fruits.append(fruit)

    @classmethod
    def regen(cls):
        for fruit in cls.fruits:
            if fruit.centerY > 700:
                i = cls.fruits.index(fruit)
                cls.fruits[i] = Fruit(random.choice(cls.fruitImgs), random.randint(100, 900), 600)
        if cls.bomb.centerY > 700:
            cls.bomb = Bomb('images/bomb/full.png', random.randint(100, 900), 600)

    @classmethod
    def action(cls):
        screen.blit(cls.bg, (0, 0))
        for fruit in cls.fruits:
            fruit.draw()
            fruit.move()
            cls.knife.collide(fruit)
        cls.bomb.draw()
        cls.bomb.move()
        cls.knife.collide(cls.bomb)
        cls.knife.draw()
        cls.knife.move()
        screen.blit(cls.scoreBoard, (0, 0))
        cls.fillText(str(cls.score), (115, 20))
        screen.blit(cls.heart, (80, 100))
        cls.fillText(str(cls.life), (155, 90))
        cls.camera.take()
        # 面部识别
        # faces = cls.camera.recogFace()
        # cls.camera.mark(faces)
        # cls.knife.moveWithMark(faces, 1)
        # 手势识别
        hands = cls.camera.recognize()
        cls.camera.mark(hands)
        cls.knife.moveWithMark(hands, 8)
        cls.camera.draw()
        screen.blit(cls.cameraBoard, (840, 0))

    @staticmethod
    def fillText(text, pos):
        textFont = pygame.font.Font('fonts/WRYH.ttf', 40)
        newText = textFont.render(str(text), True, 'orange')
        screen.blit(newText, pos)

    @classmethod
    def handleEvent(cls):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if cls.state == 'START':
                    cls.state = 'RUNNING'
            elif event.type == pygame.KEYDOWN:
                cls.keydown.append(event.key)
                if cls.challenge is None and event.key == pygame.K_UP:
                    cls.challenge = pygame.time.get_ticks()
        pygame.display.update()
        pygame.time.delay(80)
        # AI 生成代码：实现2秒内按完上下左右键生命值变为30
        if cls.challenge is not None:
            challenge_time = pygame.time.get_ticks() - cls.challenge
            if challenge_time < 2000:
                if cls.keydown == [pygame.K_UP, pygame.K_UP, pygame.K_DOWN, pygame.K_DOWN, pygame.K_LEFT, pygame.K_LEFT,
                                   pygame.K_RIGHT, pygame.K_RIGHT]:
                    cls.life = 30
            else:
                cls.challenge = None
                cls.keydown = []

    @classmethod
    def getScore(cls):
        with open('utils/score.txt', 'r') as f:
            highestScore = f.read()
        if cls.score > int(highestScore):
            with open('utils/score.txt', 'w') as f:
                f.write(str(cls.score))
            return cls.score
        return highestScore

    @classmethod
    def run(cls):
        screen.blit(cls.startBg, (0, 0))
        cls.createObj()
        while True:
            if cls.state == 'RUNNING':
                cls.action()
                cls.regen()
            elif cls.state == 'END':
                screen.blit(cls.endBg, (0, 0))
                cls.fillText(cls.score, (600, 390))
                cls.fillText(cls.getScore(), (600, 330))
            cls.handleEvent()


Game.run()
