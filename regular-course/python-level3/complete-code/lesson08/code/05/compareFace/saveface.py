'''
预留代码用于拍照保存照片，然后对这部分测试
'''

import pygame
import sys
import cv2
import numpy as np
import os
import csv
from deepface import DeepFace


class Recognize:
    @staticmethod
    def recognize_face(image_path):
        try:
            # 使用DeepFace进行人脸识别
            result = DeepFace.represent(image_path, model_name='Facenet')
            face_array = np.array(result[0]['embedding'])
            return face_array
        except:
            return None

    @staticmethod
    def store_face(name, image_path):
        # 调用人脸识别函数
        face_array = Recognize.recognize_face(image_path)

        if face_array is not None:
            # 将人名和对应图像转换后的数组数据写入data.csv文件
            with open('data.csv', mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([name] + face_array.tolist())
            print("人脸数据已成功保存到data.csv文件中。")
        else:
            print("未能识别到人脸，请检查输入的图像。")


pygame.init()
screen = pygame.display.set_mode((1100, 600))
bg = pygame.image.load("images/bg.png")
play_button = pygame.image.load("images/play.png")


class AICam:
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    @staticmethod
    def show(screen):
        ret, frame = AICam.cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = np.rot90(frame)
        frame = pygame.surfarray.make_surface(frame)
        screen.blit(frame, (0, 0))


while True:
    screen.blit(bg, (0, 0))
    screen.blit(play_button, (800, 200))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Click the close button
            pygame.quit()
            AICam.cap.release()
            cv2.destroyAllWindows()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if 800 <= x <= 1000 and 200 <= y <= 400:
                name = input("Enter name: ")
                ret, frame = AICam.cap.read()
                cv2.imwrite(os.path.join("face", "temp.jpg"), frame)
                Recognize.store_face(name, "face/temp.jpg")

    AICam.show(screen)

    pygame.display.update()
    pygame.time.delay(80)
