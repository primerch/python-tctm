"""

这是我今天编写的代码：
```
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
            # 1.将食指指尖的x,y坐标分别扩大1100和600倍
            Game.knife.x = finger.x * 1100
            Game.knife.y = finger.y * 600
        cv2.namedWindow('AICam', cv2.WINDOW_NORMAL)
        aspect_ratio = frame.shape[1] / frame.shape[0]
        cv2.resizeWindow('AICam', 200, int(200 / aspect_ratio))
        cv2.moveWindow('AICam', 0, 0)
        cv2.imshow('AICam', frame)
        cv2.waitKey(1)
while True:
    AICam.recognize()

```
请根据代码详细总结今天学习的有关类和手势识别的知识点


"""
