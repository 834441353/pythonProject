import os
import numpy

#验证码图片存放的路径
CAPTCHA_IMAGE_PATH = './captcha/image/'
CHAR_SET_LEN = 10
CAPTCHA_LEN = 4

def get_image_file_name(imgPath = CAPTCHA_IMAGE_PATH):
    filename = []
    total = 1
    for filePath in os.listdir(imgPath):
        captcha_name = filePath.split('/')[-1]
        filename.append(captcha_name)
        total+=1
    return filename,total

#件验证码转化为训练时用的标签向量，维度是40
def name2label(name):
    label = numpy.zeros(CHAR_SET_LEN*CAPTCHA_LEN)
    for i,c in enumerate(name):
        idx = i*CHAR_SET_LEN+ord(c)-ord('0')
        label[idx] = 1
    return label

#去的验证码图片得数据以及他的标签
def get_data_and_label(filename,filePath = CAPTCHA_IMAGE_PATH):
    

