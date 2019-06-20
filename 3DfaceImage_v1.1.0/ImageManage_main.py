from PyQt5 import QtWidgets, QtCore, QtGui
import sys
import os
import ImageManage_main_ui
import ImageManage_mtcnndlib
import ImageManage_test
import cv2



class ImageManageMain(QtWidgets.QMainWindow, ImageManage_main_ui.Ui_MainWindow):
    def __init__(self):
        super(ImageManageMain, self).__init__()
        self.setupUi(self)
        self.facePath = ''  # 图片文件夹的根目录
        self.txtpath = ''  # txt文件（坐标文件）保存的路径
        self.facefeature = []  # 储存标记完成为图片路径和对应的特征点的字典
        self.historytem = [[0, 0], [0, 0]]  # 储存标记的历史记录字典
        self.tagfoldernum = 0  # 当前所要处理的文件夹的ID
        self.tagpicnum = 0  # 当前要处理的图片的ID
        self.picpath = []  # 储存当前所要处理de文件夹的图片的集合
        self.beingpicpath = ''  # 储存当前处理的图片文件地址(绝对路径)
        self.imgfixflag = 0  # 图片修改是否完成FLAG
        self.pointnum = -1
        self.puttype = 1
        self.tema = 0
        # self.ponitmax = 2
        self.x = 0
        self.y = 0
        self.tface = ImageManage_mtcnndlib.MtcnnDlib()
        self.labelshowpic(self.picshowLabel)
        self.savebutton.setEnabled(False)
        # self.testbutton.setEnabled(False)

    def loadOnclicked(self):
        self.picpath = []
        self.facePath = self.facepathEdit.text()
        self.txtpath = self.txtoutpathEdit.text()
        if self.facePath == '':
            QtWidgets.QMessageBox.critical(self, '错误', '请选择人脸目录')
            self.facepathEdit.setFocus()
            return
        if self.txtpath == '':
            QtWidgets.QMessageBox.critical(self, '错误', '请选择txt保存目录')
            self.txtoutpathEdit.setFocus()
            return
        if not os.path.exists(self.txtpath):
            os.makedirs(self.txtpath)
        self.rootpathlist = os.listdir(self.facePath)  # 总文件夹中的文件夹集合
        self.rootpathlistLen = len(self.rootpathlist)  # 总文件夹中的文件夹个数
        self.folderlenLabel.setText(str(self.rootpathlistLen))  # 文件夹个数
        self.tagfoldernum = self.startnumEdit.text()
        self.tagfolderLabel.setText(str(self.tagfoldernum))
        c = os.path.join(self.facePath, self.rootpathlist[int(self.tagfoldernum)])
        self.typefolderlsit = os.listdir(c)
        for i in self.typefolderlsit:
            tempath = os.path.join(self.facePath, self.rootpathlist[int(self.tagfoldernum)], i)
            a = os.listdir(tempath)
            for j in a:
                self.picpath.append(os.path.join(tempath, j))
        if self.picpath == []:
            a = self.nextdir()
            if a == 0:
                return
            self.loadOnclicked()
            print('jump')
            return

    def startOnclicked(self):
        if self.picpath == []:
            return 0
        self.tagpicnum = 0
        self.getpoint()
        # print(self.points)

    def nextdir(self):
        if self.tagfoldernum != self.rootpathlistLen:
            self.tagfoldernum = int(self.tagfoldernum) + 1
        if self.tagfoldernum + 1 > self.rootpathlistLen:
            print('over')
            QtWidgets.QMessageBox.information(self, '提示', '标注完毕')
            return 0
        self.startnumEdit.setText(str(self.tagfoldernum))
        self.picpath = []

    def labelshowpic(self, swidget, img=None):
        # print(picurl)
        if img is None:
            pic = cv2.imread('None.jpg')
        else:
            pic = img
        if pic is None:
            print('pic is None')
        else:
            shrink = cv2.resize(pic, (540, 640), interpolation=cv2.INTER_AREA)
            shrink = cv2.cvtColor(shrink, cv2.COLOR_BGR2RGB)
            QtImg = QtGui.QImage(shrink.data,
                                 shrink.shape[1],
                                 shrink.shape[0],
                                 QtGui.QImage.Format_RGB888)
            swidget.setPixmap(QtGui.QPixmap.fromImage(QtImg))

    def testOnclicked(self):
        ImageManage_test.testModule(self.txtpath)

    def saveOnclicked(self):
        print('save')

    def skipOnclicked(self):
        self.tagpicnum += 1
        self.historytem = [[0, 0], [0, 0]]

        if int(self.tagpicnum) + 1 > len(self.picpath):
            self.txtwrite()
            a = self.nextdir()
            if a == 0:
                return

            self.loadOnclicked()
            self.startOnclicked()
        else:
            self.getpoint()

    def OnMouseAction(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDBLCLK:
            self.lcbutton(x, y)
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
            if self.pointnum == 2:
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

    def drawcircle(self):
        i = -1
        self.beingimgcopy = self.beingimg.copy()
        for a in self.historytem:
            i += 1
            if a == []:
                continue
            cv2.circle(self.beingimgcopy, (a[0], a[1]), 2, (255, 0, 0), -1)
            cv2.putText(self.beingimgcopy, "%d" % (i), (a[0], a[1]), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (255, 0, 0))

    def fixOnclicked(self):
        a = 1
        self.beingimgcopy = self.beingimg.copy()
        closeflag = 1

        cv2.namedWindow('OpenCV', 0)
        cv2.setMouseCallback('OpenCV', self.OnMouseAction)
        if self.pointnum == 1:
            self.drawcircle()
        while closeflag:
            cv2.imshow('OpenCV', self.beingimgcopy)
            keyboard = cv2.waitKey(1) & 0xFF
            if keyboard == ord('q'):
                closeflag = 0
                cv2.destroyAllWindows()
        self.pointnum = -1

    # 获取图片和该图片的坐标信息
    def getpoint(self):
        self.beingpicpath = self.picpath[self.tagpicnum]
        self.beingimg, self.points = self.tface.detectFeature(self.beingpicpath)
        tempic = self.beingimg.copy()
        if len(self.points) == 0:

            self.labelshowpic(self.picshowLabel, tempic)
        else:
            self.historytem[0] = [int(round(self.points[0][0])), int(round(self.points[5][0]))]
            self.historytem[1] = [int(round(self.points[1][0])), int(round(self.points[6][0]))]
            i = -1
            self.pointnum = 1
            for a in self.historytem:
                i += 1
                if a == []:
                    continue
                cv2.circle(tempic, (a[0], a[1]), 3, (255, 0, 0), -1)
                cv2.putText(tempic, "%d" % (i), (a[0], a[1]), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (255, 0, 0))
            self.labelshowpic(self.picshowLabel, tempic)

    def nextOnclicked(self):
        self.tagpicnum += 1
        if self.historytem != [[0, 0], [0, 0]]:
            self.facefeature.append(
                [self.beingpicpath, int(round(self.historytem[0][0])), int(round(self.historytem[0][1])),
                 int(round(self.historytem[1][0])),
                 int(round(self.historytem[1][1]))])
        self.historytem = [[0, 0], [0, 0]]

        if int(self.tagpicnum) + 1 > len(self.picpath):
            self.txtwrite()
            a = self.nextdir()
            if a == 0:
                return

            self.loadOnclicked()
            self.startOnclicked()
        else:
            self.getpoint()

    def txtwrite(self):
        print(self.facefeature)
        txtname = str(self.rootpathlist[int(self.tagfoldernum)]) + '.txt'
        txtpathname = os.path.join(self.txtpath, txtname)

        with open(txtpathname, 'w') as f:
            for a in self.facefeature:
                context = str(a[0]) + ' ' + str(a[1]) + ' ' + str(a[2]) + ' ' + str(a[3]) + ' ' + str(a[4]) + '\r'
                f.writelines(context)
        self.facefeature = []

    def __del__(self):
        del self.tface


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    am = ImageManageMain()
    am.show()
    sys.exit(app.exec_())
