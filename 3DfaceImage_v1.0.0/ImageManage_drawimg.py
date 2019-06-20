import cv2


def drawcircle(img, x, y):
    cv2.circle(img, (x, y), 3, (255, 0, 0), -1)

# if __name__ == '__main__':
#     img = cv2.imread('None.jpg')
#     drawcircle(img,20,20)
#     cv2.imshow('a',img)
#     cv2.waitKey(0)
