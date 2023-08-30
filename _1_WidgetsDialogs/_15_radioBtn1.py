# Radio Button

"""
QCheckBox(str, parent)
QCheckBox inherits from QAbstractButton

By default Radio buttons are autoexclusive
i.e. In a given parent, only one radio button can be checked.

This is a right behaviour but what if a parent dialog has 2 groups of radio buttons
e.g. One group is Yes / No, other is Male / Female
Here selecting out of all is not feasible

To solve we need to keep a group of radio buttons in a parent widget

QButtonGroup --> can be used to group a set of buttons

Methods --> 
    sender()            --> Can be used to check which button has been clicked incase of group of radio buttons
    addButton(QAbstractButton, id)
    checkedButton()     --> Returns the button that has been checked
    checkedId()         --> Returns the button id that has been checked
    setExclusive(bool)  --> can be used to define the group of buttons to be exclusive or non exclusive

Signals
    clicked(bool) --> returns status if it is checked, true or false

To check which radio button was clicked we can use the a method sender
    
"""

import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

class DlgMain(QDialog):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")
        self.resize(400,200)

        # Color button Group

        self.rr = QRadioButton("Red", self)
        self.rr.move(40,20)
        self.rr.clicked.connect(self.radioDemo)

        self.rb = QRadioButton("Blue", self)
        self.rb.move(40,40)
        self.rb.clicked.connect(self.radioDemo)

        self.rg = QRadioButton("Green", self)
        self.rg.move(40,60)
        self.rg.clicked.connect(self.radioDemo)

        self.lbl = QLabel("Hello World", self)
        self.lbl.move(40, 110)
        self.lbl.resize(100, 100)
        fnt = QFont("Times New Roman", 20, 75, True)
        self.lbl.setFont(fnt)

    def radioDemo(self):

        color = self.sender()
        print(color)
        self.lbl.setStyleSheet("color:"+color.text())
        return

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec())