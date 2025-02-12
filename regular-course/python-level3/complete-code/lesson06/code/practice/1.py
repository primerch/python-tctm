"""

使用python的opencv和mediapipe库编写一个实时显示试穿T恤的程序。
已经准备好了一个T恤图片shirt.png。你需要编写程序满足如下要求：
1. 加载具有透明度的shirt.png图片
2. 打开摄像头，拍摄画面，并将拍摄图像转换为RGB颜色模式，再进行人体识别。
3. 如果识别出人体，就计算出上半身对应的11,12,13,14,15,16,23,24号特征点的坐标，
4. 并根据拍摄图像的大小计算出这些特征点对应的像素坐标，并让y坐标都减少40像素，然后计算出最小最大的xy像素坐标
5. 修改T恤图片的宽高为最大最小xy坐标的差值
6. 然后将T恤图片逐像素替换上半身对应的像素，需要满足以下条件：x，y坐标大于0且分别小于拍摄图像的宽和高，另外只有T恤非透明的部分才覆盖
7. 实时显示出T恤覆盖后的画面
请输出要求的代码，并在代码中添加每行注释

"""
# 请使用上述提示词生成一个AI试衣程序
import cv2
import mediapipe as mp
import numpy as np

# 加载T恤图片
shirt_img = cv2.imread('shirt.png', cv2.IMREAD_UNCHANGED)
shirt_h, shirt_w, _ = shirt_img.shape

# 打开摄像头
cap = cv2.VideoCapture(0)
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

# 创建姿势检测模型
pose = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5, min_tracking_confidence=0.5)

while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("无法获取视频帧")
        break

    # 转换图像为RGB颜色模式
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # 进行人体识别
    results = pose.process(image_rgb)

    if results.pose_landmarks:
        # 获取上半身特征点坐标
        landmarks = results.pose_landmarks.landmark
        upper_body_landmarks = [landmarks[11], landmarks[12], landmarks[13], landmarks[14], landmarks[15],
                                landmarks[16],
                                landmarks[23], landmarks[24]]

        # 根据拍摄图像的大小计算特征点的像素坐标并修改y坐标
        heights, widths, _ = image.shape
        upper_body_pixel_coords = [(int(l.x * widths), int(l.y * heights) - 40) for l in upper_body_landmarks]

        # 计算最小最大xy像素坐标
        min_x = min(upper_body_pixel_coords, key=lambda x: x[0])[0]
        min_y = min(upper_body_pixel_coords, key=lambda x: x[1])[1]
        max_x = max(upper_body_pixel_coords, key=lambda x: x[0])[0]
        max_y = max(upper_body_pixel_coords, key=lambda x: x[1])[1]

        # 修改T恤图片的宽高为最大最小xy坐标的差值
        new_shirt_w = max_x - min_x + 1
        new_shirt_h = max_y - min_y + 1

        # 调整T恤图片的大小
        resized_shirt = cv2.resize(shirt_img, (new_shirt_w, new_shirt_h))

        # 遍历T恤图片的每个像素
        for i in range(new_shirt_h):
            for j in range(new_shirt_w):
                # 计算当前像素在拍摄图像中的坐标
                y = min_y + i
                x = min_x + j

                # 确保坐标在图像范围内
                if 0 <= x < widths and 0 <= y < heights:
                    # 获取T恤图片中对应像素的RGBA值
                    shirt_pixel = resized_shirt[i, j]
                    # 如果T恤像素不是透明的
                    if shirt_pixel[3] != 0:
                        # 将T恤像素覆盖在拍摄图像上
                        image[y, x] = shirt_pixel[:3]

    # 实时显示图像
    cv2.imshow("Virtual Try On", image)

    # 按下q键退出程序
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放资源
cap.release()
cv2.destroyAllWindows()
