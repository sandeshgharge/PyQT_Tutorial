# QPlainTextEdit

"""
Qwidget
    QFrame - setFrameShadow,setFrameShape, setLineWidth
        QAbstractScrollArea - setVerticalScrollBarPolicy
            QPlainTextEdit(str)
                Methods -
                    setPlainText(str), insertPlainText(str), appendPlainText(str)
                    setReadOnly(bool), setPlaceHolderText(txt)
                
                Signals -
                    cursorPositionChanged(), selectorChanged(), textChanged()
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
        
        self.pt = QPlainTextEdit("Example of plain text Edit")
        self.ml = QVBoxLayout()
        self.ml.addWidget(self.pt)
        self.setLayout(self.ml)

    
    def dialogDemo(self):
        return

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec())