# Checkbox

"""
QCheckBox(str, parent)
QCheckBox inherits from QAbstractButton

Methods --> QAbstractButton
    isChecked()
    setChecked(bool)

Signals
    clicked(bool) --> returns status if it is checked, true or false
    toggled(bool) --> Can used from code without involvement of User

Methods --> QCheckBox
    isTristate, setTristate(bool)
    checkstate(), setCheckstate(Qt.CheckState)

Signals
    stateChanged(int)
    
"""
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

class DlgMain(QDialog):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")
        self.resize(240,200)

        self.lbl = QLabel("Hello World", self)
        self.lbl.move(40, 100)
        self.lbl.resize(100, 100)
        fnt = QFont("Times New Roman", 20, 75, True)
        self.lbl.setFont(fnt)

        self.cb = QCheckBox("Disable", self)
        self.cb.move(40,40)
        self.cb.clicked.connect(self.dialogDemo)

        self.cb3 = QCheckBox("Three State Checkbox", self)
        self.cb3.setTristate(True)
        self.cb3.clicked.connect(self.threeCheckDemo)
        #self.cb3.stateChanged.connect(self.threeCheckDemo)
        self.cb3.move(40, 60)


    def dialogDemo(self):

        if self.cb.isChecked():
            self.lbl.setDisabled(True)
        else:
            self.lbl.setDisabled(False)
        return
    
    def threeCheckDemo(self):
        #self.lbl.setText(self.cb3.checkState())
        print(self.cb3.checkState())

    def threeCheckDemo1(self, state):
        #self.lbl.setText(self.cb3.checkState())
        print(state)

"""
Noted Behaviour : ???

When above 2 methods are overloaded method without parameter gives True or False output
When not is gives output as Checked, Unchecked or PartiallyChecked

"""

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec())