# QColor used to create color object

"""
Methods to create Color object

QColor("#asfaft")        -- String as a parameter
QColor(210,123,158)     --
QColor(210,123,158, 58) -- With alpha value defining color transparency
QColor("salmon")        -- Using the name of the color
QColor()                -- Later set the values using setRed(100), setGreen(219) etc.
"""

import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

class DlgMain(QDialog):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")
        self.resize(200,200)

        self.btn = QPushButton("Click", self)
        self.btn.move(40,40)
        self.btn.clicked.connect(self.dialogDemo)
    
    def dialogDemo(self):
        clr = QColorDialog.getColor(QColor("red"), self, "Choose Color")
        print(clr)
        return

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec())