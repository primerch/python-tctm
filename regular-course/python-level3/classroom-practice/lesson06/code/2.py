import cv2


class AICam:
    cap = cv2.VideoCapture(0)


def regonize():
    ret, frame = AICam.cap.read()
    # 1. 设置拍摄图像水平翻转

    cv2.imshow('AICam', frame)
    # 2. 设置程序延时1ms


while True:
    regonize()
