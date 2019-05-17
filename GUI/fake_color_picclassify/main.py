# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
import os
from mainwindow_ui import *
import cv2
import json


class AppMain(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(AppMain, self).__init__()
        self.setupUi(self)
        self.tag = 0
        self.source = {}
        self.flag = True
        self.dir = ''
        my_regex = QtCore.QRegExp("[0-3]")
        my_validator = QtGui.QRegExpValidator(my_regex, self)
        self.type_1.setValidator(my_validator)
        self.type_2.setValidator(my_validator)
        self.type_3.setValidator(my_validator)
        self.menuactionopen.triggered.connect(self.opendir)
        self.type_1.textChanged.connect(self.t1changeFocus)
        self.type_2.textChanged.connect(self.t2changeFocus)
        self.labelshowpic(self.pic_1, 0)
        self.picname_1.setText('None')
        self.labelshowpic(self.pic_2, 0)
        self.picname_2.setText('None')
        self.labelshowpic(self.pic_3, 0)
        self.picname_3.setText('None')

    def opendir(self):
        self.tag = 0
        self.source = {}
        self.flag = True
        self.dir = ''
        self.dir = QtWidgets.QFileDialog.getExistingDirectory(self, "选取文件夹")  # 起始路径
        self.pathshow.setText(str(self.dir))
        self.dirlist = os.listdir(self.dir)
        self.dirlistlen = len(self.dirlist)
        self.dirlist.sort()
        print(self.dirlistlen)

        self.labelshowpic(self.pic_1, os.path.join(self.dir, self.dirlist[self.tag]))
        self.picname_1.setText(str(self.dirlist[self.tag]))
        self.tag += 1
        self.labelshowpic(self.pic_2, os.path.join(self.dir, self.dirlist[self.tag]))
        self.picname_2.setText(str(self.dirlist[self.tag]))
        self.tag += 1
        self.labelshowpic(self.pic_3, os.path.join(self.dir, self.dirlist[self.tag]))
        self.picname_3.setText(str(self.dirlist[self.tag]))
        self.tag += 1
        self.loadpicname.setText(str(self.dirlist[self.tag]))

    def labelshowpic(self, swidget, picurl):
        # print(picurl)
        if picurl == 0:
            pic = cv2.imread('None.jpg')
        else:
            pic = cv2.imread(picurl)
        if pic is None:
            print('pic is None')
        else:
            shrink = cv2.resize(pic, (240, 320), interpolation=cv2.INTER_AREA)
            shrink = cv2.cvtColor(shrink, cv2.COLOR_BGR2RGB)
            QtImg = QtGui.QImage(shrink.data,
                                 shrink.shape[1],
                                 shrink.shape[0],
                                 QtGui.QImage.Format_RGB888)
            swidget.setPixmap(QtGui.QPixmap.fromImage(QtImg))

    def loadpic(self):
        print('loadpic')
        if self.dir == '':
            QtWidgets.QMessageBox.critical(self, '错误', '请选择文件夹 ！！')
            return
        if self.type_1.text() == '':
            QtWidgets.QMessageBox.critical(self, '错误', '请分类 ' + self.picname_1.text())
            return
        elif self.type_2.text() == '':
            QtWidgets.QMessageBox.critical(self, '错误', '请分类 ' + self.picname_2.text())
            return
        elif self.type_3.text() == '':
            QtWidgets.QMessageBox.critical(self, '错误', '请分类 ' + self.picname_3.text())
            return

        self.source[os.path.join(self.dir, self.picname_1.text())] = self.type_1.text()
        self.source[os.path.join(self.dir, self.picname_2.text())] = self.type_2.text()
        self.source[os.path.join(self.dir, self.picname_3.text())] = self.type_3.text()

        if not self.flag:
            # self.writetxt()
            QtWidgets.QMessageBox.information(self, '提示', '当前文件夹分类完毕')
            return

        self.type_1.setText('')
        self.type_2.setText('')
        self.type_3.setText('')
        self.type_1.setFocus()
        if self.loadpicname.text() != self.dirlist[self.tag]:
            loadname = self.loadpicname.text()
            if loadname in self.dirlist:
                self.tag = self.dirlist.index(loadname)
            else:
                QtWidgets.QMessageBox.critical(self, '错误', '没有当前文件')
                return

        self.labelshowpic(self.pic_1, os.path.join(self.dir, self.dirlist[self.tag]))
        self.picname_1.setText(str(self.dirlist[self.tag]))
        # print(self.tag)
        if self.tag == self.dirlistlen - 1:
            self.labelshowpic(self.pic_2, 0)
            self.picname_2.setText('None')
            self.labelshowpic(self.pic_3, 0)
            self.picname_3.setText('None')
            self.flag = False
            return
        self.tag += 1
        self.labelshowpic(self.pic_2, os.path.join(self.dir, self.dirlist[self.tag]))
        self.picname_2.setText(str(self.dirlist[self.tag]))
        if self.tag == self.dirlistlen - 1:
            self.labelshowpic(self.pic_3, 0)
            self.picname_3.setText('None')
            self.flag = False
            return
        self.tag += 1
        self.labelshowpic(self.pic_3, os.path.join(self.dir, self.dirlist[self.tag]))
        self.picname_3.setText(str(self.dirlist[self.tag]))
        if self.tag == self.dirlistlen - 1:
            self.flag = False
            return
        self.tag += 1
        self.loadpicname.setText(str(self.dirlist[self.tag]))

    def t1changeFocus(self):
        self.type_2.setFocus()

    def t2changeFocus(self):
        self.type_3.setFocus()

    def savebut(self):
        self.writetxt()
        QtWidgets.QMessageBox.information(self, '提示', '保存成功')

    def writetxt(self):
        f = open('./source.txt', 'a', encoding="utf-8")
        # tiptxt = '红外图片->1  彩色图片->2  黑白图片->3\n'
        # f.write(tiptxt)
        for z in self.source:
            a = z + '  ' + self.source[z] + '\n'
            f.write(a)
        f.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    am = AppMain()
    am.show()
    sys.exit(app.exec_())
