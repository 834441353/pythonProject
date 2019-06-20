import os
import cv2


class testModule():
    def __init__(self, txtpath):
        if txtpath == '':
            return 0
        self.txtpath = txtpath
        self.filecontext = []
        self.piccontext = []
        print(txtpath)
        self.loadtxt()

    def loadtxt(self):
        txtfilelist = os.listdir(self.txtpath)
        for i in txtfilelist:  # 单个txt文件为i
            txtfile = os.path.join(self.txtpath, i)
            fb = open(txtfile, 'r+')
            print(txtfile)
            self.filecontext = []
            lines = fb.readlines()
            for j in range(len(lines)):  # 单个txt文件单行为j
                self.piccontext = lines[j].strip().split(' ')
                self.showpic()

    def showpic(self):
        picpath = self.piccontext[0]
        feature = []
        feature.append(self.piccontext[1:3])
        feature.append(self.piccontext[3:])
        print('-----')
        pic = self.drawcircle(picpath, feature)
        cv2.namedWindow(picpath, 0)
        cv2.imshow(picpath, pic)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def drawcircle(self, picpath, feature):
        i = -1
        pic = cv2.imread(picpath)
        for a in feature:
            i += 1
            if a == []:
                continue
            cv2.circle(pic, (int(a[0]), int(a[1])), 2, (255, 0, 0), -1)
            cv2.putText(pic, "%d" % (i), (int(a[0]), int(a[1])), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (255, 0, 0))
        return pic
