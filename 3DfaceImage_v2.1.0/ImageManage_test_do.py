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
        self.temp = []
        self.historytem = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        self.pointnum = -1
        self.puttype = 1
        self.tema = 0

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
                    souce = z[0] + ' ' + z[1] + ' ' + z[2] + ' ' + z[3] + ' ' + z[4] + ' ' + z[5] + ' ' + z[6] + ' ' + \
                            z[7] + ' ' + z[8] + ' ' + z[9] + ' ' + z[10] + '\n'
                    # print(souce)
                    fa.writelines(souce)

        print('over')

    def showpic(self):
        self.picpath = self.piccontext[0]
        self.feature = []
        self.historytem = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        # self.feature.append(self.piccontext[1:3])
        # self.feature.append(self.piccontext[3:5])
        self.feature.append(self.piccontext[5:7])
        self.feature.append(self.piccontext[7:9])
        self.feature.append(self.piccontext[9:11])
        self.feature.append(self.piccontext[11:13])
        self.feature.append(self.piccontext[13:])
        self.historytem = self.feature
        self.pointnum = 4
        self.puttype = 1
        # print('-----')
        print(self.picpath)
        self.drawcircle()
        cv2.namedWindow('opencv', 0)
        cv2.setMouseCallback('opencv', self.OnMouseAction)
        while 1:
            # print('1')
            cv2.imshow('opencv', self.pic)
            key = cv2.waitKey(1) & 0xFF
            if key == 32:  # keyword = space  保存
                self.temp.append(self.picpath)
                self.temp.append(self.historytem[0][0])
                self.temp.append(self.historytem[0][1])
                self.temp.append(self.historytem[1][0])
                self.temp.append(self.historytem[1][1])
                self.temp.append(self.historytem[2][0])
                self.temp.append(self.historytem[2][1])
                self.temp.append(self.historytem[3][0])
                self.temp.append(self.historytem[3][1])
                self.temp.append(self.historytem[4][0])
                self.temp.append(self.historytem[4][1])
                self.filecontext.append(self.temp)
                self.temp = []
                print(self.filecontext)
                print('save')
                cv2.destroyAllWindows()
                break
            elif key == 48:  # keyword = 0 放弃
                self.piccontext = []
                print('del')
                cv2.destroyAllWindows()
                break

    def drawcircle(self):
        i = -1
        self.pic = cv2.imread(self.picpath)
        # if pic.ndim == 2:
        #     pic = to_rgb(pic)
        for a in self.historytem:
            i += 1
            if a == []:
                continue
            cv2.circle(self.pic, (int(a[0]), int(a[1])), 2, (255, 0, 0), -1)
            cv2.putText(self.pic, "%d" % i, (int(a[0]), int(a[1])), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (255, 0, 0))

    def OnMouseAction(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDBLCLK:
            self.lcbutton(x, y)
            # print('aaa')
        elif event == cv2.EVENT_LBUTTONDOWN:
            self.lbutton(x, y)
        elif event == cv2.EVENT_RBUTTONDOWN:
            self.rbutton(x, y)

    def lbutton(self, x, y):
        if self.puttype == 2:
            self.puttype = 1
            self.historytem[self.tema] = [x, y]
            self.drawcircle()
        elif self.puttype == 1:
            self.pointnum += 1
            if self.pointnum == 5:
                self.pointnum -= 1
                return

            self.historytem[self.pointnum] = [x, y]
            self.drawcircle()

    def rbutton(self, x, y):

        if self.pointnum != -1:
            self.historytem[self.pointnum] = [0, 0]
            self.pointnum -= 1
            self.drawcircle()
        elif self.pointnum == -1:
            return

    def lcbutton(self, x, y):
        if self.historytem.count([x, y]) == 1:
            self.tema = self.historytem.index([x, y])
            self.historytem[self.tema] = [0, 0]
            self.puttype = 2
            # print('puttype ==2 ')
            self.drawcircle()
        elif self.historytem.count([x, y - 1]) == 1:
            self.tema = self.historytem.index([x, y - 1])
            self.historytem[self.tema] = [0, 0]
            self.puttype = 2
            # print('puttype ==2 ')
            self.drawcircle()
        elif self.historytem.count([x, y + 1]) == 1:
            self.tema = self.historytem.index([x, y + 1])
            self.historytem[self.tema] = [0, 0]
            self.puttype = 2
            # print('puttype ==2 ')
            self.drawcircle()
        elif self.historytem.count([x - 1, y]) == 1:
            self.tema = self.historytem.index([x - 1, y])
            self.historytem[self.tema] = [0, 0]
            self.puttype = 2
            # print('puttype ==2 ')
            self.drawcircle()
        elif self.historytem.count([x - 1, y - 1]) == 1:
            self.tema = self.historytem.index([x - 1, y - 1])
            self.historytem[self.tema] = [0, 0]
            self.puttype = 2
            # print('puttype ==2 ')
            self.drawcircle()
        elif self.historytem.count([x - 1, y + 1]) == 1:
            self.tema = self.historytem.index([x - 1, y + 1])
            self.historytem[self.tema] = [0, 0]
            self.puttype = 2
            # print('puttype ==2 ')
            self.drawcircle()
        elif self.historytem.count([x + 1, y + 1]) == 1:
            self.tema = self.historytem.index([x + 1, y + 1])
            self.historytem[self.tema] = [0, 0]
            self.puttype = 2
            # print('puttype ==2 ')
            self.drawcircle()
        elif self.historytem.count([x + 1, y]) == 1:
            self.tema = self.historytem.index([x + 1, y])
            self.historytem[self.tema] = [0, 0]
            self.puttype = 2
            # print('puttype ==2 ')
            self.drawcircle()
        elif self.historytem.count([x + 1, y - 1]) == 1:
            self.tema = self.historytem.index([x + 1, y - 1])
            self.historytem[self.tema] = [0, 0]
            self.puttype = 2
            # print('puttype ==2 ')
            self.drawcircle()

        elif self.historytem.count([x - 2, y - 2]) == 1:
            self.tema = self.historytem.index([x - 2, y - 2])
            self.historytem[self.tema] = [0, 0]
            self.puttype = 2
            # print('puttype ==2 ')
            self.drawcircle()
        elif self.historytem.count([x - 2, y - 1]) == 1:
            self.tema = self.historytem.index([x - 2, y - 1])
            self.historytem[self.tema] = [0, 0]
            self.puttype = 2
            # print('puttype ==2 ')
            self.drawcircle()
        elif self.historytem.count([x - 2, y]) == 1:
            self.tema = self.historytem.index([x - 2, y])
            self.historytem[self.tema] = [0, 0]
            self.puttype = 2
            # print('puttype ==2 ')
            self.drawcircle()
        elif self.historytem.count([x - 2, y + 1]) == 1:
            self.tema = self.historytem.index([x - 2, y + 1])
            self.historytem[self.tema] = [0, 0]
            self.puttype = 2
            # print('puttype ==2 ')
            self.drawcircle()
        elif self.historytem.count([x - 2, y + 2]) == 1:
            self.tema = self.historytem.index([x - 2, y + 2])
            self.historytem[self.tema] = [0, 0]
            self.puttype = 2
            # print('puttype ==2 ')
            self.drawcircle()
        elif self.historytem.count([x - 1, y + 2]) == 1:
            self.tema = self.historytem.index([x - 1, y + 2])
            self.historytem[self.tema] = [0, 0]
            self.puttype = 2
            # print('puttype ==2 ')
            self.drawcircle()
        elif self.historytem.count([x - 1, y - 2]) == 1:
            self.tema = self.historytem.index([x - 1, y + 2])
            self.historytem[self.tema] = [0, 0]
            self.puttype = 2
            # print('puttype ==2 ')
            self.drawcircle()
        elif self.historytem.count([x, y - 2]) == 1:
            self.tema = self.historytem.index([x, y - 2])
            self.historytem[self.tema] = [0, 0]
            self.puttype = 2
            # print('puttype ==2 ')
            self.drawcircle()
        elif self.historytem.count([x, y + 2]) == 1:
            self.tema = self.historytem.index([x, y + 2])
            self.historytem[self.tema] = [0, 0]
            self.puttype = 2
            # print('puttype ==2 ')
            self.drawcircle()
        elif self.historytem.count([x + 1, y - 2]) == 1:
            self.tema = self.historytem.index([x + 1, y - 2])
            self.historytem[self.tema] = [0, 0]
            self.puttype = 2
            # print('puttype ==2 ')
            self.drawcircle()
        elif self.historytem.count([x + 1, y + 2]) == 1:
            self.tema = self.historytem.index([x + 1, y + 2])
            self.historytem[self.tema] = [0, 0]
            self.puttype = 2
            # print('puttype ==2 ')
            self.drawcircle()
        elif self.historytem.count([x + 2, y - 2]) == 1:
            self.tema = self.historytem.index([x + 2, y - 2])
            self.historytem[self.tema] = [0, 0]
            self.puttype = 2
            # print('puttype ==2 ')
            self.drawcircle()
        elif self.historytem.count([x + 2, y + 2]) == 1:
            self.tema = self.historytem.index([x + 2, y + 2])
            self.historytem[self.tema] = [0, 0]
            self.puttype = 2
            # print('puttype ==2 ')
            self.drawcircle()
        elif self.historytem.count([x + 2, y - 1]) == 1:
            self.tema = self.historytem.index([x + 2, y - 1])
            self.historytem[self.tema] = [0, 0]
            self.puttype = 2
            # print('puttype ==2 ')
            self.drawcircle()
        elif self.historytem.count([x + 2, y + 1]) == 1:
            self.tema = self.historytem.index([x + 2, y + 1])
            self.historytem[self.tema] = [0, 0]
            self.puttype = 2
            # print('puttype ==2 ')
            self.drawcircle()
        elif self.historytem.count([x + 2, y]) == 1:
            self.tema = self.historytem.index([x + 2, y])
            self.historytem[self.tema] = [0, 0]
            self.puttype = 2
            # print('puttype ==2 ')
            self.drawcircle()


if __name__ == '__main__':
    a = testModule('F:\\demores_s\\pythonProject\\test\\txtdoing\\txt')
    a.loadtxt()
