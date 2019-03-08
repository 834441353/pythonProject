from PyQt5 import QtWidgets
import sys
from PyQt5.QtCore import pyqtSlot


class App(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'ss'
        self.left = 100
        self.top = 100
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.statusBar().showMessage('asdf')
        self.button1 = QtWidgets.QPushButton('botton1', self)
        self.button1.setToolTip('this is a button called button1')
        self.setObjectName('button1')
        self.button1.clicked.connect(self.on_click)

        self.messageBox1 = QtWidgets.QMessageBox.question(self, 'a message', 'Do you like me?')
        if self.messageBox1 == QtWidgets.QMessageBox.Yes:
            print('a')
        else:
            print('b')

        self.show()

    # @pyqtSlot()
    def on_click(self):
        print('PyQt5 button1 clicked')
        self.messageBox1 = QtWidgets.QMessageBox.question(self, 'a message', 'Do you like me?',QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Cancel, QtWidgets.QMessageBox.Cancel)
        if self.messageBox1 == QtWidgets.QMessageBox.Yes:
            print('a')
        else:
            print('b')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    a = App()
    sys.exit(app.exec_())
