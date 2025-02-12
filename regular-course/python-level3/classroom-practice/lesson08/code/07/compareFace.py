import pygame
import sys
import cv2
import numpy as np
from deepface import DeepFace
import csv

pygame.init()
screen = pygame.display.set_mode((1100, 600))
bg = pygame.image.load("images/bg.png")
button_img = pygame.image.load("images/button.png")


class AICam:
    cap = cv2.VideoCapture(0)

    @staticmethod
    def show():
        ret, frame = AICam.cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = np.rot90(frame)
        frame = pygame.surfarray.make_surface(frame)
        screen.blit(frame, (0, 0))


class Utils:
    @staticmethod
    def drawText(text, pos):
        font = pygame.font.Font('fonts/WRYH.TTF', 40)
        textImg = font.render(str(text), True, 'orange')
        screen.blit(textImg, pos)


class Compare:

    @staticmethod
    def recognize_face(image_path):
        try:
            result = DeepFace.represent(image_path, model_name='Facenet')
            face_array = np.array(result[0]['embedding'])
            return face_array
        except:
            return None

    @staticmethod
    def compare_face(image_path):
        face_array = Compare.recognize_face(image_path)

        if face_array is None:
            return '未检测到人脸'

        min_distance = 10
        recognized_person = "用户未识别"

        with open('data.csv', 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                target_face = np.array(row[1:], dtype=np.float64)
                distance = np.linalg.norm(face_array - target_face)
                if distance < min_distance:
                    min_distance = distance
                    recognized_person = row[0]

        if min_distance <= 10:
            return recognized_person
        else:
            return '用户未识别'


result = ""

while True:
    screen.blit(bg, (0, 0))
    AICam.show()

    button_rect = button_img.get_rect(topleft=(600, 30))
    screen.blit(button_img, button_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            AICam.cap.release()
            cv2.destroyAllWindows()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                ret, frame = AICam.cap.read()
                cv2.imwrite('face/temp.jpg', frame)
                result = Compare.compare_face('face/temp.jpg')

    if result:
        Utils.drawText(result, (180, 500))

    pygame.display.update()
    pygame.time.delay(80)

'''

是我的代码，不需要解读代码，等待我的下一步指示

'''
