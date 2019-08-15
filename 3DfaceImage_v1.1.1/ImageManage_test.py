import os
import cv2
import numpy as np

def to_rgb(img):
    w, h = img.shape
    ret = np.empty((w, h, 3), dtype=np.uint8)
    ret[:, :, 0] = ret[:, :, 1] = ret[:, :, 2] = img
    return ret

class testModule():
    def __init__(self, txtpath):
        if txtpath == '':
            self.txtpath = ''
            return None
        self.txtpath = txtpath
        self.filecontext = []
        self.piccontext = []
        # print(txtpath)
        # a = self.loadtxt()
        # if a == 0:
        #     return None

    def loadtxt(self):
        if self.txtpath == '':
            return 0
        txtfilelist = os.listdir(self.txtpath)
        if len(txtfilelist) == 0:
            return 0
        for i in txtfilelist:  # 单个txt文件为i
            txtfile = os.path.join(self.txtpath, i)
            fb = open(txtfile, 'r+')
            print(txtfile)
            self.filecontext = []
            lines = fb.readlines()
            for j in range(len(lines)):  # 单个txt文件单行为j
                self.piccontext = lines[j].strip().split(' ')
                # print(self.piccontext)
                self.showpic()
            with open(txtfile, 'w') as fa:

                for z in self.filecontext:
                    souce = z[0] + ' ' + z[1] + ' ' + z[2] + ' ' + z[3] + ' ' + z[4] + '\n'
                    # print(souce)
                    fa.writelines(souce)
        print('over')

    def showpic(self):
        picpath = self.piccontext[0]
        feature = []
        feature.append(self.piccontext[1:3])
        feature.append(self.piccontext[3:])
        # print('-----')
        pic = self.drawcircle(picpath, feature)
        cv2.namedWindow('opencv', 0)
        # cv2.setMouseCallback(picpath, self.OnMouseAction)
        while 1:
            cv2.imshow('opencv', pic)
            key = cv2.waitKey(0)
            if key == 32:  # keyword = space  保存
                self.filecontext.append(self.piccontext)
                print('save')
                cv2.destroyAllWindows()
                break
            elif key == 48:  # keyword = 0 放弃
                self.piccontext = []
                print('del')
                cv2.destroyAllWindows()
                break




    def drawcircle(self, picpath, feature):
        i = -1
        pic = cv2.imread(picpath)
        if pic.ndim == 2:
            pic = to_rgb(pic)
        for a in feature:
            i += 1
            if a == []:
                continue
            cv2.circle(pic, (int(a[0]), int(a[1])), 2, (255, 0, 0), -1)
            cv2.putText(pic, "%d" % i, (int(a[0]), int(a[1])), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (255, 0, 0))
        return pic
