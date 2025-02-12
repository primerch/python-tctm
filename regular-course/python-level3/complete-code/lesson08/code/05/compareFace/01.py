'''

我想使用deepface完成人脸信息识别比对。创建Compare类包含两个函数作为静态方法。
一个方法recognize_face负责使用deepface模块的represent进行人脸识别，将图像信息识别后，用numpy转换为数组，返回人脸数组数据，如果没有识别到人脸可以返回None，添加try避免未识别到人脸报错
另一个静态方法compare_face，用于对比人脸特征并返回匹配最佳的人名。方法接受一个包含人脸图片，使用上边的额recognize_face方法进行人脸识别。如果未检测到人脸，返回'未检测到人脸'；
当识别到人脸时，返回csv.reader读取data.csv文件中与识别目标最接近的人名。设定阈值为10，如果都未小于阈值则返回用户未识别。
注意，data.csv中每行是一个人的人脸信息，第一项是人名，后面是人脸数据

追问 ：
我发现recognize_face函数的返回值太复杂了，识别结果是一个列表，列表第一项是一个字典,
我只需要这个字典中embedding的值转换为数组返回就可以。请为我稍微修改下recognize_face函数

'''

import csv
import numpy as np
from deepface import DeepFace


class Compare:
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
    def compare_face(image_path):
        # 使用Recognize中的recognize_face方法进行人脸识别
        face_array = Compare.recognize_face(image_path)

        if face_array is None:
            return '未检测到人脸'

        min_distance = 10
        best_match = '用户未识别'

        with open('data.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                person_name = row[0]
                face_data = np.array(row[1:], dtype=float)

                # 计算人脸特征之间的欧氏距离
                distance = np.linalg.norm(face_array - face_data)

                if distance < min_distance:
                    min_distance = distance
                    best_match = person_name

        return best_match


# 测试代码
if __name__ == "__main__":
    # 测试代码
    result = Compare.compare_face("face/xiaolong2.jpg")
    print(f"最佳匹配的人名为：{result}")
