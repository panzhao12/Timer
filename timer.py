import sys
import timer_ui
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWindow(QMainWindow, timer_ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)

        self.lcdNumber.display("00:00:00")

        self.timer = QTimer(self)
        self.timer.setTimerType(Qt.PreciseTimer)
        self.timer.timeout.connect(self.refresh_time)

        self.initial_time = QTime(0, 0, 0)
        self.current_time = QTime(0, 0, 0)

        self.start_time_flag = 1
        self.current_time_flag = 1

        self.pushButton.clicked.connect(self.start_timer)
        self.pushButton_2.clicked.connect(self.stop_timer)
        self.pushButton_3.clicked.connect(self.reset_timer)

    # start timer
    def start_timer(self):
        if self.start_time_flag:
            self.timer.start(1000)

        self.start_time_flag = 0

    # add 1 sec and display
    def refresh_time(self):
        self.initial_time = self.initial_time.addSecs(1)
        self.current_time = self.initial_time
        self.lcdNumber.display(self.current_time.toString())

        # print(self.current_time.toString())

    # stop timer
    def stop_timer(self):
        self.start_time_flag = 1
        self.timer.stop()

    # reset timer
    def reset_timer(self):
        self.start_time_flag = 1
        self.timer.stop()
        self.initial_time = QTime(0, 0, 0)
        self.lcdNumber.display(self.initial_time.toString())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
