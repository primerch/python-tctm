import cv2
from mediapipe.python.solutions.hands import Hands


class AICam:
    cap = cv2.VideoCapture(0)

    # 1. 定义类变量hand，存储创建的手势识别对象

    @classmethod
    def recognize(cls):
        ret, frame = cls.cap.read()
        frame = cv2.flip(frame, 1)
        # 2. 对拍摄图像进行手势识别

        # 3. 获取识别的手对象，并输出查看

        cv2.imshow('AICam', frame)
        cv2.waitKey(1)


while True:
    AICam.recognize()
