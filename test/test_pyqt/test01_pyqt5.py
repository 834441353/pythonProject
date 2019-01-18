import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from mainWindow import *


# from PyQt5 import QtWidgets, QtCore


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.onCancleClicked)
        # self.pushButton.pressed.connect(self.onCancleClicked)

    def onCancleClicked(self):
        print('close')
        self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
