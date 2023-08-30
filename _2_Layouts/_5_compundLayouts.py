# Compund Layouts

"""
A layout is compound layouts when layouts are inside the layout
A Window consisting of combination of layouts
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