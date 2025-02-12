from PIL import Image
import numpy as np

# 求汉明距离，定义函数，参数是两个正整数

# 两个数字异或操作

# 统计异或结果中有多少个1


'''
这是我定义好的一个函数，请为我写一个程序，利用这个函数定义新函数compare_images，判断两个图片中的指纹是否一致。将两个图片内容转换为数组后，对数组中的数逐一比对汉明距离，如果比对不一致则累计加1，最终累计结果小于10则认为两张图片中的指纹一致，否则不一致
'''


def compare_images(img1_path, img2_path):
    # 打开图片
    img1 = Image.open(img1_path)
    img2 = Image.open(img2_path)

    # 将图片转换为8位整型的numpy数组
    img1_data = np.array(img1, dtype=np.uint8)
    img2_data = np.array(img2, dtype=np.uint8)

    # 将图片数据扁平化
    img1_data_flat = img1_data.flatten()
    img2_data_flat = img2_data.flatten()

    # 检验两图片的shape是否一样
    if img1_data_flat.shape != img2_data_flat.shape:
        print("两图片形状不一样，进行像素比较可能存在问题")
        return False

    # 对数组中的数逐一比对汉明距离
    total_difference = 0
    for i in range(len(img1_data_flat)):
        diff = hamming(img1_data_flat[i], img2_data_flat[i])
        total_difference += diff

    # 最终判断
    if total_difference < 10:
        print("两图片指纹一致")
        return True
    else:
        print("两图片指纹不一致")
        return False


compare_images("./fingerprint.png", "true.png")
