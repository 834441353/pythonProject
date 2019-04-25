import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from mainwindow import *
import os
import cv2
from multiprocessing import Pool
import time


def doing(cmd):
    # os.system(cmd)
    print(cmd)
    time.sleep(3)


class working(QtCore.QThread):
    def __init__(self, parent):
        super(working, self).__init__(parent)
        self.cmd = ''

    def run(self):
        print(self.cmd)
        os.system(self.cmd)


class AppMain(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(AppMain, self).__init__()
        self.setupUi(self)

        self.pool = Pool(10)
        self.dir = ''
        self.dirlist = ''
        self.tag = 0
        self.nextflag = 0
        self.openpath.triggered.connect(self.opendir)
        if self.dir == '':
            return

    def opendir(self):
        self.dir = QtWidgets.QFileDialog.getExistingDirectory(self, "选取文件夹")  # 起始路径
        # print('a' + self.dir)
        self.pathtext.setText(str(self.dir))
        self.dirlist = os.listdir(self.dir)
        if len(self.dirlist) < 2:
            print('no enough dir!')
            return

        self.dirlist = list(map(int, self.dirlist))
        self.dirlist.sort()
        print(self.dirlist)
        self.idtext1.setText(str(self.dirlist[self.tag]))
        self.tag += 1
        self.idtext2.setText(str(self.dirlist[self.tag]))
        self.loadimg1()
        self.loadimg2()

    def labelshowpic(self, swidget, picurl):
        # print(picurl)
        if picurl == 0:
            pic = cv2.imread('None.jpg')
        else:
            pic = cv2.imread(picurl)
        if pic is None:
            print('pic is None')
        else:
            shrink = cv2.resize(pic, (320, 240), interpolation=cv2.INTER_AREA)
            shrink = cv2.cvtColor(shrink, cv2.COLOR_BGR2RGB)
            QtImg = QtGui.QImage(shrink.data,
                                 shrink.shape[1],
                                 shrink.shape[0],
                                 QtGui.QImage.Format_RGB888)
            swidget.setPixmap(QtGui.QPixmap.fromImage(QtImg))

    def loadimg1(self):
        a = self.idtext1.text()
        path1 = os.path.join(self.dir, str(a))
        self.filelist1 = os.listdir(path1)
        # print(self.filelist1)
        filelen1 = len(self.filelist1)
        if filelen1 == 0:
            print('no pic')
            self.labelshowpic(self.pic1_1, 0)
            self.labelshowpic(self.pic1_2, 0)
            self.labelshowpic(self.pic1_3, 0)
        elif filelen1 == 1:
            self.labelshowpic(self.pic1_1, os.path.join(path1, self.filelist1[0]))
            self.labelshowpic(self.pic1_2, 0)
            self.labelshowpic(self.pic1_3, 0)
        elif filelen1 == 2:
            self.labelshowpic(self.pic1_1, os.path.join(path1, self.filelist1[0]))
            self.labelshowpic(self.pic1_2, os.path.join(path1, self.filelist1[1]))
            self.labelshowpic(self.pic1_3, 0)
        elif filelen1 > 2:
            self.labelshowpic(self.pic1_1, os.path.join(path1, self.filelist1[0]))
            self.labelshowpic(self.pic1_2, os.path.join(path1, self.filelist1[1]))
            self.labelshowpic(self.pic1_3, os.path.join(path1, self.filelist1[filelen1 - 1]))

    def loadimg2(self):
        a = self.idtext2.text()
        path2 = os.path.join(self.dir, str(a))
        self.filelist2 = os.listdir(path2)
        # print(self.filelist2)
        filelen2 = len(self.filelist2)
        if filelen2 == 0:
            print('no pic')
            self.labelshowpic(self.pic2_1, 0)
            self.labelshowpic(self.pic2_2, 0)
            self.labelshowpic(self.pic2_3, 0)
        elif filelen2 == 1:
            self.labelshowpic(self.pic2_1, os.path.join(path2, self.filelist2[0]))
            self.labelshowpic(self.pic2_2, 0)
            self.labelshowpic(self.pic2_3, 0)
        elif filelen2 == 2:
            self.labelshowpic(self.pic2_1, os.path.join(path2, self.filelist2[0]))
            self.labelshowpic(self.pic2_2, os.path.join(path2, self.filelist2[1]))
            self.labelshowpic(self.pic2_3, 0)
        elif filelen2 > 2:
            self.labelshowpic(self.pic2_1, os.path.join(path2, self.filelist2[0]))
            self.labelshowpic(self.pic2_2, os.path.join(path2, self.filelist2[1]))
            self.labelshowpic(self.pic2_3, os.path.join(path2, self.filelist2[filelen2 - 1]))

    def copyfile(self):
        print('copyfile')
        path = os.path.join(self.dir, str(self.dirlist[self.tag]))
        a = self.idtext1.text()
        b = self.idtext2.text()
        if a == self.dirlist[self.tag]:
            c = b
        else:
            c = a
        becppath = os.path.join(self.dir, str(c))
        cpfilelist = os.listdir(path)
        cpfilelistlen = len(cpfilelist)
        for i in range(cpfilelistlen):
            cpfile = os.path.join(path, cpfilelist[i])
            command = 'mv ' + cpfile + ' ' + becppath
            # self.pool.apply_async(doing, (command,))
            self.working1 = working(self)

            self.working1.cmd = command
            self.working1.start()
        if self.nextflag == 1:
            self.nextflag = 0
        elif self.nextflag == 0:
            self.nextflag = 1
        self.nextdir()

    def nextdir(self):
        print('nextdir')

        if self.tag == len(self.dirlist) - 1:
            print('over')
            return
        if self.nextflag == 0:
            self.tag += 1
            self.idtext1.setText(str(self.dirlist[self.tag]))
            self.nextflag = 1
            self.loadimg1()
        elif self.nextflag == 1:
            self.tag += 1
            self.idtext2.setText(str(self.dirlist[self.tag]))
            self.nextflag = 0
            self.loadimg2()

    def id1loadOnclick(self):
        print('id1loadOnclick')
        a = self.idtext1.text()
        self.tag = self.dirlist.index(int(a))
        # print(self.tag)
        self.loadimg1()
        self.nextflag == 1

    def id2loadOnclick(self):
        print('id2loadOnclick')
        a = self.idtext2.text()
        self.tag = self.dirlist.index(int(a))
        # print(self.tag)
        self.loadimg2()
        self.nextflag == 0

    def id1delOnclick(self):
        a = self.idtext1.text()
        path = os.path.join(self.dir, str(a))
        command = 'rm -r ' + path
        # self.pool.apply_async(doing, (command,))
        self.nextflag = 0
        self.nextdir()

    def id2delOnclick(self):
        a = self.idtext2.text()
        path = os.path.join(self.dir, str(a))
        command = 'rm -r ' + path
        # self.pool.apply_async(doing, (command,))
        self.nextflag = 1
        self.nextdir()

    def __del__(self):
        self.pool.close()
        self.pool.join()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    am = AppMain()
    am.show()
    sys.exit(app.exec_())
