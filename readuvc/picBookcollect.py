import cv2
import numpy
import os
def onMouseAction(event,x,y,flags,param):
    global closeflag
    if event == cv2.EVENT_LBUTTONDOWN:
        print('start')



if __name__ == '__main__':
    print('into while')
    cv2.namedWindow('OpenCv', cv2.WINDOW_NORMAL)
    Opencvimg = numpy.zeros((640, 480, 3), numpy.uint8)
    while closeflag:
        cv2.setMouseCallback('OpenCv',onMouseAction)
        cv2.imshow('OpenCv',Opencvimg)
        cv2.waitKey(10)
    cv2.destroyAllWindows()
