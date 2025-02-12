class Knife:
    def __init__(self, img, x, y):
        self.img = img
        self.x = x
        self.y = y


class Game:
    knife = Knife('images/knife.png', 550, 300)


import cv2
from mediapipe.python.solutions.hands import Hands
from mediapipe.python.solutions.drawing_utils import draw_landmarks


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
        # 1. 判断是否识别出手

        # 2. 如果识别出手，绘制手部特征点

        # 3. 获取识别的第一只手的8号特征点对象

        # 4. 获取8号特征点的x,y坐标，赋值给刀的x,y坐标，并输出查看

        cv2.imshow('AICam', frame)
        cv2.waitKey(1)


while True:
    AICam.recognize()
