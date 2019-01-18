import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from test01_pyqt5_ui import Ui_MainWindow

class App(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(App,self).__init__(parent)
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myapp = App()
    myapp.show()
    sys.exit(app.exec_())