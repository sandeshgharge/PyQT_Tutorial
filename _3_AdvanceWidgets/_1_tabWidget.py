# QTabWidget(parent)

"""
This can used as a substitute for Stacked layout

Methods -
    addTab(QWidget)
    addTab(QWidget, QIcon, label)
    insert(idx, QWidget, label), removeTab(idx)
    count()                 --> Number of tabs
    currentIndex()          --> Returns index of the current tab

    setMoveable(bool)       --> This will allow the user to move the tab i.e. change the index / sequence of the tab
    setTabsCloseable(bool)  --> When enabled user can close the tab when required
    setTabText(idx, label)  --> We can change the text of the tab using this method

    setTabPosition(QTabWidget.TabPosition)  --> Bydefault North, can be changed to East West South
    setTabShape(QTabWidget.TabShape)        --> Used for changing the appearance of the tab

    setTabVisible(idx, bool)    --> Used to alter the visibilty of the tab
    setTabEnabled(idx, bool)    --> A tab cab be enabled and disabled using this method
    setCurrentIndex()           --> It change the current index of the tab to specified value

Signals -
    currentChanged(idx)     --> Signal emitted on tab changed
    tabBarClicked(idx)      --> Signal emitted on tab clicked
    tabBarDoubleClicked(idx)--> Signal emitted on double click of the tab

"""

import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

class DlgMain(QDialog):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")

        """
        Same code as Tab Widget, here we added a Tab Widget
        """
        # Create tab widget
        self.tabW = QTabWidget()

        ## Try out different position for the layout
        # self.tabW.setTabPosition(QTabWidget.TabPosition.West)
        # self.tabW.setTabPosition(QTabWidget.TabPosition.South)
        self.tabW.setTabPosition(QTabWidget.TabPosition.East)

        # Setting moveable and closeable
        self.tabW.setMovable(True)

        self.tabW.setTabsClosable(True)
        self.tabW.tabCloseRequested.connect(self.closeTab)

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

        # For tab layout we will comment below .... *
        # self.rl = QStackedLayout()

        self.ml.addLayout(self.ll)

        # * ... change below line to .... *
        # self.ml.addLayout(self.rl)
        self.ml.addWidget(self.tabW)

        ## Setting the selector widget on left side of the window
        self.ll.addWidget(self.cb)

        ## * ... also below line of code will be replaced by ....*
        ## Setting the different widgets on stacked layout.
        # self.rl.addWidget(self.wgGeneral)
        # self.rl.addWidget(self.wgEdu)
        # self.rl.addWidget(self.wgAdd)

        self.tabW.addTab(self.wgGeneral, "Genaral")
        self.tabW.addTab(self.wgEdu, "Education")
        self.tabW.addTab(self.wgAdd, "Address")

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
    
    def closeTab(self, idx):
        q = QMessageBox.question(self, "Close", "Are you want to close '{}' tab ?".format(self.tabW.tabText(idx)))
        if q == QMessageBox.StandardButton.Yes:
            self.tabW.removeTab(idx)
        return

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec())