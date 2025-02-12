'''
完成手势切水果游戏时要讲解试试识别，这是我的授课思路：
问题: 如何识别画面中的手势信息？
解决：可以使用mediapipe库，将手势识别的功能封装在hands类中，先导入Hands类
问题：有了手势识别的对象，如何检测每张图像上是否出现手呢
解决：需要借助手势识别对象hand的process方法，于是讲解process方法识别手势。
然后发现明明拍摄图像上出现手了，怎么依然输出大量的none呢？判断出计算机在读取摄像头拍摄的图像时，会先读取蓝色，然后再读取其他颜色，
图像中的手显示的很不清楚。需要通过使用cv2.cvtColor方法进行颜色转换，把蓝色移动到其他颜色后面。
接下来解析识别结果:
问题：识别结果是数字看不懂，将识别到的手势关键点信息输出在控制台，不方便观看识别结果
解决：讲解手势识别原理，并在显示的画面上绘制出手势特征点。通过在moveWithFinger方法中对识别结果hands进行判断，如果识别到手了，
就从手对象列表中，取出识别的手对象hands[0]，获取到手对象后，使用mediapipe库中的draw_landmarks方法进行标记特征点
之后获取手部关键点坐标，就是要根据识别出手的关键点位置，确定水果刀的位置。当手移动时，关键点位置发生变化，从而控制水果刀移动
问题 ： 该如何获取手的关键点的位置呢？
解决 ： landmark对应着手部的21关键点，每个关键点存储着自身的位置信息x,y。就需要先获取到该特征点，访问它的x,y属性（finge.x和finger.y）
就可以获取到它的特征点坐标。最后得到手指的坐标后就可以直接赋值给水果刀的x,y坐标，确定了水果刀的位置了，输出计算出的水果刀坐标

这是我的代码：
import cv2
from mediapipe.python.solutions.hands import Hands
from mediapipe.python.solutions.drawing_utils import draw_landmarks

cap = cv2.VideoCapture(0)
hand = Hands(1)

def recogine():
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    cvtframe = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    outputs = hand.process(cvtframe)
    hands = outputs.multi_hand_landmarks
    print(hands)

   if hands:
        draw_landmarks(frame, hands[0])
        finger = hands[0].landmark[8]
        print(finger.x, finger.y)

    cv2.imshow('AICamera', frame)
    cv2.waitKey(1)

while True:
    recogine()

请帮我使用中文，根据以上知识点出5道单选题，帮助学生理解，使用模块完成手势识别的过程，手势控制刀的基本原理，mediapipe模块中手势识别函数的功能等，不需要答案.
'''
