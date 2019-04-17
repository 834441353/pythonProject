import sys
from PyQt5 import QtWidgets, QtCore


class AppMain(QtWidgets.QMainWindow):
    def __init__(self):
        super(AppMain, self).__init__()

        self.dir = ''
        self.initUI()
        # self.button = QtWidgets.QPushButton(self)
        # self.setGeometry(300, 100, 600, 900)
        self.setWindowTitle('人工聚类')

    def initUI(self):
        # menubar
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 26))
        self.menubar.setObjectName("menubar")
        self.menufile = self.menubar.addMenu('file')
        self.menuopendiraction = QtWidgets.QAction('open', self)
        self.menuopendiraction.setStatusTip('打开需要处理的文件夹')
        self.menuopendiraction.triggered.connect(self.opendir)

        self.menufile.addAction(self.menuopendiraction)

        # 图片group选择
        # if self.dir == '':
        #     return
        print(self.dir)
        self.hbox1count = QtWidgets.QWidget(self)
        self.hbox1count.setGeometry(QtCore.QRect(0, 27, 600, 300))
        self.idvbox1count = QtWidgets.QWidget(self)
        # self.idvbox1count.setGeometry(QtCore.QRect(0, 0, 250, 273))
        self.cpbutboxcount = QtWidgets.QWidget(self)
        # self.cpbutboxcount.setGeometry(QtCore.QRect(250, 0, 350, 273))
        self.idvbox2count = QtWidgets.QWidget(self)
        # self.idvbox2count.setGeometry(QtCore.QRect(350, 0, 600, 273))

        self.hbox1 = QtWidgets.QHBoxLayout(self.hbox1count)
        self.idvbox1 = QtWidgets.QVBoxLayout(self.idvbox1count)
        self.cpbutbox = QtWidgets.QVBoxLayout(self.cpbutboxcount)
        self.idvbox2 = QtWidgets.QVBoxLayout(self.idvbox2count)

        self.idvbox1.addWidget(QtWidgets.QPushButton(str(1)))
        self.idvbox1.addWidget(QtWidgets.QPushButton(str(1)))
        self.cpbutbox.addWidget(QtWidgets.QPushButton(str(2)))
        self.cpbutbox.addWidget(QtWidgets.QPushButton(str(2)))
        self.idvbox2.addWidget(QtWidgets.QPushButton(str(3)))
        self.idvbox2.addWidget(QtWidgets.QPushButton(str(3)))

        self.hbox1.addWidget(self.idvbox1count)
        self.hbox1.addWidget(self.cpbutboxcount)
        self.hbox1.addWidget(self.idvbox2count)

        self.idvbox1count.setLayout(self.idvbox1)
        self.cpbutboxcount.setLayout(self.cpbutbox)
        self.idvbox2count.setLayout(self.idvbox2)
        self.hbox1count.setLayout(self.hbox1)

        self.idvbox1count.setStyleSheet('''background-color:blue;''')
        self.cpbutboxcount.setStyleSheet('''background-color:red;''')
        self.idvbox2count.setStyleSheet('''background-color:yellow;''')
        self.hbox1count.setStyleSheet('''background-color:black;''')



    def opendir(self):
        self.dir = QtWidgets.QFileDialog.getExistingDirectory(self, "选取文件夹")  # 起始路径
        # print(self.dir)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    am = AppMain()
    am.show()
    sys.exit(app.exec_())
