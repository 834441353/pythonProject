import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget, QPushButton,QHBoxLayout,QWidget
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.resize(400, 200)
        self.status = self.statusBar()
        self.status.showMessage('这是状态栏提示', 5000)
        self.setWindowTitle("Pyqt mainWindow例子")
        self.center()  # 窗口位移到显示屏的正中间

        self.button1 = QPushButton('关闭主窗口')
        self.button1.clicked.connect(self.onButtonClick)

        layout = QHBoxLayout()
        layout.addWidget(self.button1)

        main_frame = QWidget()
        main_frame.setLayout(layout)
        self.setCentralWidget(main_frame)

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

    def onButtonClick(self):
        sender = self.sender()  # sender 是发送信号的对象
        print(sender.text() + '被摁下了')
        qApp = QApplication.instance()
        qApp.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setWindowIcon(QIcon(""))
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())
