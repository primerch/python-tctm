import cv2


class AICam:
    cap = cv2.VideoCapture(0)

    # 1.将recognize函数定义为AICam的类方法，并使用cls.访问类变量cap


def recognize():
    ret, frame = AICam.cap.read()
    frame = cv2.flip(frame, 1)
    cv2.imshow('AICam', frame)
    cv2.waitKey(1)


while True:
    # 2.使用AICam类调用recognize类方法
    recognize()
