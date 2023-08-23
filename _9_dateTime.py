# Date and Time

"""
QDate(YYYY,MM,DD)
Methods - addDays(), addMonths(), toJulianDay(), dayOfWeek(), dayOfYear(), daysTo(QDate) etc.

QTime(HH,MM,ss,ms)
Methods - addSecond(), secsTo(QTime), toString()

QTimeZone(seconds)
seconds --> Offset from GMT

QDateTime(QDate, Qtime) --> used to combine date and time
QDateTime(QDate, Qtime, QTimeZone)
This object will have both the methods defined for date and time
"""
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

class DlgMain(QDialog):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")
        self.resize(200,200)

        self.btn = QPushButton("Click", self)
        self.btn.move(40,40)
        self.btn.clicked.connect(self.dialogDemo)
    
    def dialogDemo(self):
        dt = QDate().currentDate()
        print(dt.toString())
        print(dt.toJulianDay())
        print(dt.dayOfYear())

        t = QTime.currentTime()
        t2 = QTime(14, 33, 12)

        print("")
        print(t.toString())
        print(t2.toString())

        print(t.secsTo(t2))

        t3 = t2.addSecs(480)
        print(t3.toString())
        print(t3.secsTo(t2))
        return

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec())