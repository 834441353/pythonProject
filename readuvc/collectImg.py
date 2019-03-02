import sys
import os
import numpy as np
import cv2
from VideoCapture import Device

outpath = "./collectImage_g"


def main(outpath):
    if not os.path.exists(outpath):
        os.makedirs(outpath)
    cam = Device(0)
    startflag = True
    head = False
    saveCount = 0
    book = 0
    savepicpath = os.path.join(outpath, "tests_%d" % book)
    if not os.path.exists(savepicpath):
        os.makedirs(savepicpath)
    page = 0
    savepicpath1 = os.path.join(savepicpath, "b_%d" % page)
    if not os.path.exists(savepicpath1):
        os.makedirs(savepicpath1)
    while 1:
        frame = cam.getImage()
        frame = cv2.cvtColor(np.asarray(frame), cv2.COLOR_RGB2BGR)
        cv2.imshow("window", frame)
        cv2.waitKey(1)
        k = cv2.waitKey(1) & 0xFF

        if k == ord('q'):
            break
        elif k == ord('c'):
            startflag = True
            saveCount = 0
            page += 1
            savepicpath1 = os.path.join(savepicpath, "b_%d" % page)
            if not os.path.exists(savepicpath1):
                os.makedirs(savepicpath1)
            print('c')
        elif k == ord('z'):
            startflag = True
            saveCount = 0
            book += 1
            page = 0
            savepicpath = os.path.join(outpath, "tests_%d" % book)
            if not os.path.exists(savepicpath):
                os.makedirs(savepicpath)
            savepicpath1 = os.path.join(savepicpath, "b_%d" % page)
            if not os.path.exists(savepicpath1):
                os.makedirs(savepicpath1)
            print('z')
        if saveCount > 60:
            startflag = False
            head = True

        if startflag:
            saveCount += 1
            if frame is None:
                break
            cv2.imwrite(os.path.join(savepicpath1, "%d.jpg" % (saveCount)), frame)
            print("save one img")


if __name__ == "__main__":
    main(outpath)
