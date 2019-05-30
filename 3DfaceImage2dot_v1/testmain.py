from PyQt5 import QtWidgets, QtGui, QtCore
import test_ui01
import sys
import test_ui02


class AppMain(QtWidgets.QMainWindow, test_ui01.Ui_MainWindow):
    def __init__(self):
        super(AppMain, self).__init__()
        self.setupUi(self)

    def open(self):
        self.testui02 = test02init()
        self.gridLayout.addWidget(self.testui02)
        self.testui02.show()



class test02init(QtWidgets.QMainWindow, test_ui02.Ui_MainWindow):
    def __init__(self):
        super(test02init, self).__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    am = AppMain()
    am.show()
    sys.exit(app.exec_())
