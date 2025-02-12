import cv2


# 1. 定义AICam类，并创建类变量cap存储摄像头对象
class AICam:
    cap = cv2.VideoCapture(0)


# 2. 定义手势识别函数recognize
def recognize():
    # 3. 获取拍摄图像数据，并显示在AICam窗口上
    ret, frame = AICam.cap.read()
    cv2.imshow('AICam', frame)


# 6. 在while True循环中调用recognize函数
while True:
    recognize()
