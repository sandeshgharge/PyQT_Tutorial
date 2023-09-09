# QTextEdit

"""
Allows you to change font, make bold/italic ...

Rich Text Format
    HTML
    MarkDown

QTextCursors
    position()  --> Gives the position of the cursor in the text
    anchor()    --> In case any text is not selected, it gives the same information as position,
                    else it gives the position from where the selection started

    setPosition(pos, QTextCursor.MoveAnchor) --> You can set the position of the cursor as you need
                                                 In case you pass the anchor value, a part of text will bbe selected
                        
    setPosition(pos, QTextCursor.KeepAnchor) --> You can set the position of the cursor as you need
                                                 In case you pass the anchor value, a part of text will bbe selected

QTextEdit

To be continued ...
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