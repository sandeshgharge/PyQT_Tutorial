# Spin Box

"""
QAbstractSpinbox()

Methods -

    setReadOnly(bool) 
    isReadOnly()
    setAlignment(Qt.Alignment)
    setWrapping(bool)
    text(), clear(), selectAll()
    stepUp(), stepDown()

Signals -
    editingFinished()

For Entering number we have 2 types of Spin Box

QSpinBox        --> Allows to enter integer
QDoubleSpinBox  --> Allows to enter double

Methods -

    setMinimum(int), setMaximum(int), setRange(min, max)
    setSingleStep(int)
    setPrefix(str), setSuffix(str)
    setValue(), value()
    setDecimal(int) -- only for QDoubleSpinBox()

Signals -

    texChange(str)
    valueChange(int)

"""

import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

class DlgMain(QDialog):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")
        self.resize(200,200)

        self.sp = QSpinBox(self)
        self.sp.move(50,50)
        self.sp.setWrapping(True)
        self.sp.setRange(0, 1000)
        self.sp.setSingleStep(2)
        self.sp.setValue(55)
        # To add a condition e.g. the number is divisible by x then we can use below method
        self.sp.valueChanged.connect(self.spinBoxCondition)
        #editingFinished event is triggered when we click outside the box
        self.sp.editingFinished.connect(self.onBlur)

        self.spd = QDoubleSpinBox(self)
        self.spd.move(50,70)
        self.spd.setDecimals(5)
        self.spd.setWrapping(True)
        self.spd.setRange(-90, 90)
        self.spd.setSingleStep(0.01)
        self.spd.setPrefix("Latitude : ")
        # Check the ascii value for the suffix character. 176 is a degrees symbol used
        self.spd.setSuffix(chr(176))
        self.spd.setValue(55)
        self.spd.valueChanged.connect(self.doubleSpinBox)

    def spinBoxCondition(self, val):

        # Add the condition as required
        print(val)
        if (val % 4):
            self.sp.setStyleSheet("color:red")
        else:
            self.sp.setStyleSheet("color:white")
        return
    
    def doubleSpinBox(self, val):
        print(self.spd.text()) # Prints all the data
        print(self.spd.value())# Prints just the value
    
    # This method shows the message box when the value is invalid.
    # Other line takes care to re focus on the same field to enter a valid number
    def onBlur(self):
        if (self.sp.value() % 4):
            QMessageBox.critical(self, "Invalid value", "Description of the error")
            self.sp.setFocus()
        return

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec())