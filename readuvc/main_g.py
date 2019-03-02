from VideoCapture import Device
import cv2
import numpy
import os

path0 = os.getcwd()
father_path = os.path.abspath(os.path.dirname(path0) + os.path.sep + ".")

# cap = Device(0)
# cap.setResolution(1280, 720)

input_movie = cv2.VideoCapture(0)
input_movie.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
input_movie.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

fps = 1  # cap.get(cv2.CAP_PROP_FPS)
print(fps)

# saveimagepath = os.path.join(father_path, 'collectImagequick')
saveimagepath = './collectImage_g'
if not os.path.exists(saveimagepath):
    os.mkdir(saveimagepath)
    # os.makedirs()
# imagepathnum = 0

imagepathnum = len(os.listdir(saveimagepath))

'''
ret, frame = cap.read()
ret1, frame1 = cap1.read()
'''
diffperson = 0
showflag = 1


def savePicmethod():
    pic_num = 0

    # global ret,ret1,frame,frame1
    global imagepathnum, diffperson
    global saveimagepath
    '''
    if not ret :
        print('camera 1 is not OK!')
    if not ret1:
        print('camera 2 is not OK!')
    '''
    # while ret and ret1:
    while 1:
        '''
        ret, frame = cap.read()
        ret1, frame1 = cap1.read()
        '''
        # frame = cap.getImage()
        # frame = cv2.cvtColor(numpy.asarray(frame), cv2.COLOR_RGB2BGR)
        # frameor = frame
        # frame1 = cap1.getImage()
        # frame1 = cv2.cvtColor(numpy.asarray(frame1), cv2.COLOR_RGB2BGR)
        # frame1or = frame1
        ret, frame = input_movie.read()
        frame = cv2.flip(frame, 1)
        # gray_frame = cv2.cvtColor(frame_1, cv2.COLOR_RGB2BGR)


        save_color_path = os.path.join(saveimagepath, '%s/' % imagepathnum)
        if not os.path.exists(save_color_path):
            os.makedirs(save_color_path)
        # save_gray_path = os.path.join(saveimagepath, '%s/gray' % imagepathnum)
        # if not os.path.exists(save_gray_path):
        #     os.mkdir(save_gray_path)

        color_file = os.path.join(save_color_path, "%s.jpg" % pic_num)
        # gray_file = os.path.join(save_gray_path, "%s.jpg" % pic_num)

        cv2.imwrite(color_file, frame)
        cv2.imshow('clor', frame)
        # cv2.imshow('gray', frame1)
        cv2.waitKey(3)  #
        # cv2.imwrite(gray_file, frame1)
        pic_num += 1
        if pic_num > 600:
            pic_num = 0
            print('collect num %s OK!' % imagepathnum)
            print('\a')
            imagepathnum += 1
            break


closeflag = 1


def OnMouseAction(event, x, y, flags, param):
    global closeflag
    if event == cv2.EVENT_LBUTTONDOWN:
        print('\a')
        savePicmethod()
        print("左键点击")
    elif event == cv2.EVENT_RBUTTONDOWN:
        print("右键点击")
    elif flags == cv2.EVENT_FLAG_LBUTTON:
        print("左鍵拖曳")
    elif event == cv2.EVENT_MBUTTONDOWN:
        closeflag = 0
        print("中键点击")


if __name__ == "__main__":

    print('into while')
    cv2.namedWindow("OpenCV", cv2.WINDOW_NORMAL)
    Opencvimg = numpy.zeros((640, 480, 3), numpy.uint8)
    while closeflag:
        cv2.setMouseCallback('OpenCV', OnMouseAction)
        cv2.imshow('OpenCV', Opencvimg)
        cv2.waitKey(10)

    cv2.destroyAllWindows()
