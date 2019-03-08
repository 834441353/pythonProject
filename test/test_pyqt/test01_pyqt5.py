import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from test01_pyqt5_ui import Ui_MainWindow
from test_pyqt.test01_pyqt5_ui02 import Ui_childFrom


class App(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(App, self).__init__(parent)
        self.setupUi(self)
        self.child = ChildrenFrom()
        self.addWinAction.triggered.connect(self.childshow)

    def childshow(self):
        self.gridLayout_2.addWidget(self.child)
        self.child.show()
        print('a')


class ChildrenFrom(QWidget, Ui_childFrom):
    def __init__(self):
        super(ChildrenFrom, self).__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myapp = App()
    myapp.show()
    sys.exit(app.exec_())
