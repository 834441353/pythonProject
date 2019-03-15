from PyQt5.QtCore import QObject, pyqtSignal


class QTypeSignal(QObject):
    sengmsg = pyqtSignal(str, str)

    def __init__(self):
        super(QTypeSignal, self).__init__()

    def get(self):
        self.sengmsg.emit('first', 'second')


class QTypeSlot(QObject):
    def __init__(self):
        super(QTypeSlot, self).__init__()

    def run(self, msg1, msg2):
        print(msg1, ' + ', msg2)


if __name__ == '__main__':
    sendmsg = QTypeSignal()
    slotmsg = QTypeSlot()

    sendmsg.sengmsg.connect(slotmsg.run)
    sendmsg.get()

    sendmsg.sengmsg.disconnect(slotmsg.run)
    sendmsg.get()
