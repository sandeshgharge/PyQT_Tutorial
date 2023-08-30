#  QDateTimeEdit


"""
Inherits from QAbstractSpinBox, QDateEdit, QTimeEdit

Constructor
QDateTimeEdit(QTime, parent)
QDateTimeEdit(QDate, parent)
QDateTimeEdit(QDateTime, parent)
QDateTimeEdit(parent)

Methods -
    setCalenderPopup(bool), setcalenderWidget(QCalenderWidget)
    date(), time(), dateTime() --> returns the value currently set
    setDate(), setTime(), setDateTime() --> used to set the values as requried
    setMinimumDate(QDate), setMaximumDate(QDate), setDateRange(QDate, QDate) --> same as QSpinBox
    setDisplayFormat(str) --> 

Signals -
    dateChanged(Qdate), dateTimeChange(QDatetime), timeChanged(QTime)

"""

import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

class DlgMain(QDialog):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")
        self.resize(200,200)

        self.d = QDateTimeEdit(QDate().currentDate(), self)
        self.d.setCalendarPopup(True) # Once made true arrows are removed, try once
        self.d.move(50,20)

        self.dt = QDateTimeEdit(QTime().currentTime(), self)
        self.dt.move(50,50)

        self.dt = QDateTimeEdit(QDateTime(QDate().currentDate(),QTime().currentTime()), self)
        self.dt.move(50,80)

        self.btn = QPushButton("Elapsed Time", self)
        self.btn.clicked.connect(self.checkElapsedTime)

    def checkElapsedTime(self):
        seconds = QDateTime.currentDateTime().secsTo(self.dt.dateTime())
        # QMessageBox.information(self, "Elapsed Time : ", str(seconds))
        QMessageBox.information(self, "Elapsed Time : ", "{} seconds have elapsed since {}".format(seconds, self.dt.dateTime().toString()))
        return

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec())