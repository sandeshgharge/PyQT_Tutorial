# Widgets in QT

"""
*Example not implemented

QWidget

Current state
    isEnabled()
    isWindow()
    isVisible()
    isModal()
To check the current status

Positioning
    move(x,y)
    pos()
    resize(w,h)
    size()
    setGeometry(x,y,w,h)

Tips
    setStatusTip(string)
    setToolTip(string)

Styling
    setFont(QFont)
    setStyleSheet(str)

Visibility
    show()
    hide()
    setEnabled(bool)
"""

import sys
from PyQt6.QtWidgets import *

class DlgMain(QDialog):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")
        self.resize(200,200)

        self.btn = QPushButton("Click", self)
        self.btn.move(40,40)
        self.btn.clicked.connect(self.dialogDemo)
    
    def dialogDemo(self):
        return

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec())