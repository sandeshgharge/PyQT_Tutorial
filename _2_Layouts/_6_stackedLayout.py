# Compund Layouts

"""
When multiple layouts are integrated into one window and can switched using -
    QComboBox
    QListBox
    QRadioButtons

Methods -
    addWidget()
    setCurrentIndex(idx)

"""

import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

class DlgMain(QDialog):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")

        ### Create Widget to control the stacked layouts
        self.cb = QComboBox()
        self.cb.addItems(["General","Education","Address"])
        self.cb.currentIndexChanged.connect(self.changeLayout)
        self.wgGeneral = QWidget()
        self.wgEdu = QWidget()
        self.wgAdd = QWidget()

        # General widgets
        self.fn = QLineEdit("", self)
        self.bd = QDateEdit()
        self.bd.setCalendarPopup(True)
        self.em = QLineEdit("", self)

        #  Education widgets
        self.b = QRadioButton("Bachelor", self)
        self.m = QRadioButton("Masters", self)
        self.um = QLineEdit("", self)

        # Address Widgets
        self.city = QComboBox(self)
        self.city.addItems(["Mumbai", "Delhi", "Kolkata", "Chennai"])

        self.setUpLayout()
    
    def setUpLayout(self):

        # Main Layout
        self.ml = QHBoxLayout()

        # Selector and Stacked layouts
        self.ll = QVBoxLayout()
        self.rl = QStackedLayout()

        self.ml.addLayout(self.ll)
        self.ml.addLayout(self.rl)

        ## Setting the selector widget on left side of the window
        self.ll.addWidget(self.cb)

        ## Setting the different widgets on stacked layout.
        self.rl.addWidget(self.wgGeneral)
        self.rl.addWidget(self.wgEdu)
        self.rl.addWidget(self.wgAdd)

        self.general = QFormLayout()
        self.general.addRow("Full Name", self.fn)
        self.general.addRow("Birth Date", self.bd)
        self.general.addRow("Email", self.em)
        self.wgGeneral.setLayout(self.general)

        self.eduL = QGridLayout()
        self.eduL.addWidget(self.m, 0, 0 , 1, 2)
        self.eduL.addWidget(self.b, 1, 0 , 1, 2)
        self.eduL.addWidget(QLabel("University Name : "), 2, 1)
        self.eduL.addWidget(self.um, 2, 2)
        self.wgEdu.setLayout(self.eduL)

        self.address = QVBoxLayout()
        self.address.addWidget(self.city)
        self.wgAdd.setLayout(self.address)

        self.setLayout(self.ml)

    def changeLayout(self, idx):
        self.rl.setCurrentIndex(idx)
        return

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec())