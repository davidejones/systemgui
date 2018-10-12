import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
import platform
import psutil


class SystemInfo(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def addLabel(self, key, value, x, y):
        lbl1 = QLabel('{}:'.format(key), self)
        lbl1.move(x, y)
        lbl2 = QLabel(value, self)
        lbl2.move(x+90, y)

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('SystemInfo')

        self.addLabel('Machine', platform.machine(), 10, 10)
        self.addLabel('Version', platform.version(), 10, 30)
        self.addLabel('Platform', platform.platform(), 10, 50)
        self.addLabel('System', platform.system(), 10, 70)
        self.addLabel('Processor', platform.processor(), 10, 90)
        self.addLabel('CPU Cores', '{}'.format(psutil.cpu_count(logical=False)), 10, 130)
        self.addLabel('CPU Threads', '{}'.format(psutil.cpu_count()), 10, 110)

        self.setGeometry(300, 300, 400, 160)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SystemInfo()
    sys.exit(app.exec_())