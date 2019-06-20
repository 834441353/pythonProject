import os
import cv2
import numpy


# img = cv2.imread('./sampletestdata2/1/color/data_6.bmp')
img = cv2.imread('./sampletestdata2/1/color/data_6.bmp')
# img = cv2.imread('./sampletestdata2/1/gray/data_1.bmp',cv2.IMREAD_UNCHANGED)
channel = len(img.shape)
print(channel)
cv2.namedWindow('opencv', 0)
# cv2.setMouseCallback('opencv', self.OnMouseAction)
cv2.imshow('opencv', img)
a = cv2.waitKey(0)
print(a)
cv2.destroyAllWindows()