from PyQt5 import QtWidgets
from test05_pyqt5_ui import *
from test05_pyqt5_ui_dialog import *
import sys

class mainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.main_ui = Ui_MainWindow()
        self.main_ui.setupUi(self)

class dialogWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.dialog = Ui_Dialog()
        self.dialog.setupUi(self)


if __name__ == '__main__':
    Application = QtWidgets.QApplication(sys.argv)
    window = mainWindow()
    child = dialogWindow()

    window.main_ui.pushButton.clicked.connect(child.show)
    window.show()
    sys.exit(Application.exec_())

