import cv2
import numpy
import os
from VideoCapture import Device

# input_movie = cv2.VideoCapture(0)
# input_movie.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# input_movie.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cam = Device(0)

saveimagepath = './collectImage_g'
if not os.path.exists(saveimagepath):
    os.mkdir(saveimagepath)



def savePicmethod():
    pic_num = 0
    global imagepathnum, diffperson
    global saveimagepath

    imagepathnum = len(os.listdir(saveimagepath))
    while flag:

        # ret, frame = input_movie.read()
        # frame = cv2.flip(frame, 1)
        frame = cam.getImage()
        frame = cv2.cvtColor(numpy.asarray(frame),cv2.COLOR_RGB2BGR)

        save_color_path = os.path.join(saveimagepath, '%s/' % imagepathnum)
        if not os.path.exists(save_color_path):
            os.makedirs(save_color_path)

        color_file = os.path.join(save_color_path, "%s.jpg" % pic_num)

        cv2.imwrite(color_file, frame)
        cv2.imshow('clor', frame)

        cv2.waitKey(3)  #

        pic_num += 1
        # if pic_num > 600:
        #     pic_num = 0
        #     print('collect num %s OK!' % imagepathnum)
        #     print('\a')
        #     imagepathnum += 1
        #     break


closeflag = 1


def onMouseAction(event, x, y, flags, param):
    global closeflag, flag
    if event == cv2.EVENT_LBUTTONDOWN:
        print('start')
        flag = 1
        savePicmethod()
    elif event == cv2.EVENT_RBUTTONDOWN:
        flag = 0
        print('EVENT_RBUTTONDOWN')
    elif event == cv2.EVENT_MBUTTONDOWN:
        closeflag = 0
        print("中键点击")


if __name__ == '__main__':
    print('into while')
    cv2.namedWindow('OpenCv', cv2.WINDOW_NORMAL)
    Opencvimg = numpy.zeros((640, 480, 3), numpy.uint8)
    while closeflag:
        cv2.setMouseCallback('OpenCv', onMouseAction)
        cv2.imshow('OpenCv', Opencvimg)
        cv2.waitKey(10)
    cv2.destroyAllWindows()
