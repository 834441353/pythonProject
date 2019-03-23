from PyQt5.QtCore import Qt
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize(477, 258)
        self.setWindowTitle('pyqt')
        self.setWindowFlags(Qt.FramelessWindowHint)
        rect = QApplication.desktop().availableGeometry()
        print(rect)
        self.setGeometry(rect)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # print('a')
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
