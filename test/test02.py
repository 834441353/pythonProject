#!/usr/bin/python
# -*- coding: UTF-8 -*-
import cv2

img1 = cv2.imread('a.jpg', 0)

for i in range(100):
    cv2.imshow("a", img1)
    waitkey_num = cv2.waitKeyEx()
    print(waitkey_num)

    if waitkey_num == 2490368:
        print("up")
    if waitkey_num == 2621440:
        print("down")
    if waitkey_num == 13:
        print("enter")
    if waitkey_num == 32:
        print("space")
