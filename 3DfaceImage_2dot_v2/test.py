import os
import cv2
import numpy


# img = cv2.imread('./sampletestdata2/1/color/data_6.bmp')
img = cv2.imread('./sampletestdata2/1/color/data_6.bmp',cv2.IMREAD_UNCHANGED)
# img = cv2.imread('./sampletestdata2/1/gray/data_1.bmp',cv2.IMREAD_UNCHANGED)
channel = len(img.shape)
print(channel)