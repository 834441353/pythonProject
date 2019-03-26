import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from WeatherWin import Ui_Form
import requests


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

    def queryWeather(self):
        city = self.ui.weatherComboBox.currentText()
        key = '580c4cfd2d078baaf3b81e42bc76e582'
        # rep = requests.get('http://apis.juhe.cn/simpleWeather/query?city=' + city + '&key=' + key)
        rep = requests.get('http://apis.juhe.cn/simpleWeather/query?city=%s&key=%s' % (city, key))
        rep.encoding = 'utf-8'
        print('reason :%s' % rep.json()['reason'])
        if rep.json()['reason'] == '超过每日可允许请求次数!':
            return 0
        msg1 = '温度：%s\n' % rep.json()['result']['realtime']['temperature']
        msg2 = '湿度：%s\n' % rep.json()['result']['realtime']['humidity']
        msg3 = '天气情况：%s\n' % rep.json()['result']['realtime']['info']
        msg4 = '风向：%s\n' % rep.json()['result']['realtime']['direct']
        msg5 = '风力：%s\n' % rep.json()['result']['realtime']['power']
        msg6 = '空气质量指数：%s\n' % rep.json()['result']['realtime']['aqi']
        result = msg1 + msg2 + msg3 + msg4 + msg5 + msg6
        self.ui.resultText.setText(result)

    def clearWeather(self):
        self.ui.resultText.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
