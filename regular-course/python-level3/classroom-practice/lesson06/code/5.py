import cv2
from mediapipe.python.solutions.hands import Hands


class AICam:
    cap = cv2.VideoCapture(0)
    hand = Hands()

    @classmethod
    def recognize(cls):
        ret, frame = cls.cap.read()
        frame = cv2.flip(frame, 1)
        # 1. 将图像的颜色模式从BGR转换为RGB

        # 2. 使用转换后的图像cvtFrame进行手势识别
        outputs = cls.hand.process(frame)
        hands = outputs.multi_hand_landmarks
        print(hands)
        cv2.imshow('AICam', frame)
        cv2.waitKey(1)


while True:
    AICam.recognize()
