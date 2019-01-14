from PyQt5 import QtWidgets, QtGui, QtCore
import sys
from test03_pyqt5_ui import *
import cv2


class app(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.actionopen = QtWidgets.QAction('openfile', self)
        self.SHADOW_WIDTH = 0  # 边框距离
        self.actionopen.triggered.connect(self.OnOpenClicked)
        self.actionExit.triggered.connect(self.close)

        # img = cv2.imread('C:/Users/Administrator/Desktop/ascii.jpg')

    def OnOpenClicked(self):
        path, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, '请选择图片', QtCore.QStandardPaths.writableLocation(QtCore.QStandardPaths.DesktopLocation),
            '图片文件(*.jpg *.png)')
        print(path)
        if not path:
            return
        img = cv2.imread(path)
        sp = img.shape
        # image_height, image_width, image_depth = img.shape
        Qimg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        Qimg = QtGui.QImage(Qimg.data, sp[1], sp[0], sp[1] * sp[2], QtGui.QImage.Format_RGB888)
        self.resize(sp[1], sp[0]+50)
        # self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, sp[1], sp[0]))

        # self.label.setGeometry(QtCore.QRect(0, 0, sp[1], sp[0]))

        self.label.setPixmap(QtGui.QPixmap.fromImage(Qimg))
        self.label.setScaledContents(True)
    # def loadImage(self):


if __name__ == '__main__':
    application = QtWidgets.QApplication(sys.argv)
    window = app()
    window.show()
    sys.exit(application.exec_())
    # img = cv2.imread('C:/Users/Administrator/Desktop/ascii.jpg')
    # img = cv2.imread('C:/Users/Administrator/Desktop/QQ20181122110425.png')
    # cv2.imshow('dd',img)
    # cv2.waitKey(0)
