# Push button

"""
QPushButton(str, parent)
QPushButton inherits from QAbstractButton

Methods in QAbstractButton

    setIcon(QIcon)
    setText(str)
    setAutoRepeat(bool)
    setAutoRepeatDelay(msec)
    .
    .
    .

Signals
    clicked
    .
    .
    .

Check document online
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

        # Customised icons for buttons
        # self.btn.setIcon(QPixmap(""))
        # 
        
        self.btn.setFlat(True)
        self.btn.move(40,40)
        self.btn.clicked.connect(self.dialogDemo)

        self.lbl = QLabel("Hello World", self)
        self.lbl.move(40, 100)
        self.lbl.resize(100, 100)
        fnt = QFont("Times New Roman", 20, 75, True)
        self.lbl.setFont(fnt)
    
    def dialogDemo(self):
        print(self.lbl.isEnabled())
        if self.lbl.isEnabled():
            self.lbl.setDisabled(True)
        else:
            self.lbl.setDisabled(False)
        return

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec())