import cv2
import os
import numpy as np


def to_rgb(img):
    w, h = img.shape
    ret = np.empty((w, h, 3), dtype=np.uint8)
    ret[:, :, 0] = ret[:, :, 1] = ret[:, :, 2] = img
    return ret


if __name__ == '__main__':
    # img = cv2.imread('./pic/2.jpeg', cv2.IMREAD_COLOR)
    # # w,h = img .shape
    #
    # img1 = img[:, :, 0:3]
    # print(img)
    #
    # cv2.imshow('as1', img1)
    # cv2.imshow('as', img)
    #
    # cv2.waitKey(0)
    # np.round(2.33333, 3)

    # img = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9], [11, 22, 33, 44, 55, 66, 77, 88, 99],
    #                 [111, 222, 333, 444, 555, 666, 777, 888, 999]])
    # img = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    # w, h = img.shape
    # ret = np.empty((w, h, 3), dtype=np.uint8)
    # print(ret[:, :, 0])

    img = cv2.imread('./pic/cat01.jpg', cv2.IMREAD_COLOR)
    n_img = img[900:1200, 1800:2100]
    cv2.imshow('n_img', n_img)
    cv2.waitKey(0)
