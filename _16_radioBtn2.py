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


        # Size button group
        self.rs = QRadioButton("Small", self)
        self.rs.move(40,80)
        self.rs.clicked.connect(self.radioDemo)

        self.rm = QRadioButton("Medium", self)
        self.rm.move(40,100)
        self.rm.clicked.connect(self.radioDemo)

        self.rb = QRadioButton("Big", self)
        self.rb.move(40,120)
        self.rb.clicked.connect(self.radioDemo)

        # Now we need to create 2 groups for color and size
        # Comment the group creation part to know the significance

        self.cg = QButtonGroup(self)
        self.cg.addButton(self.rr)
        self.cg.addButton(self.rb)
        self.cg.addButton(self.rg)

        self.cs = QButtonGroup(self)
        self.cs.addButton(self.rs, 10)
        self.cs.addButton(self.rm, 15)
        self.cs.addButton(self.rb, 20)


        self.lbl = QLabel("Hello World", self)
        self.lbl.move(40, 120)
        self.lbl.resize(100, 100)
        fnt = QFont("Times New Roman", 20, 75, True)
        self.lbl.setFont(fnt)

    def radioDemo(self):

        # To detect which radio button is clicked we will use the sender() method
        if self.cg.checkedButton() and self.cs.checkedButton():
            color = self.cg.checkedButton()
            size = self.cs.checkedId()
            self.lbl.setStyleSheet("color:"+color.text()+";font-size:"+str(size)+"px")
        return

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec())