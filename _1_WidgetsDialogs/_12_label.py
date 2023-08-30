# Label

"""
QLabel(str, parent)

Methods - 
    setText(str)
    setNum(int / dbl)
    setPixmap(QPixmap)
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

        self.lbl = QLabel("Hello World", self)
        self.lbl.move(40, 100)
        self.lbl.resize(100, 100)
        fnt = QFont("Times New Roman", 20, 75, True)
        self.lbl.setFont(fnt)
    
    def dialogDemo(self):

        str = """
        <ul>
            <li>Red</li>
            <li>Blue</li>
        </ul>
        """
        self.lbl.setText(str)

        # In some scenarios setText do not work in 1 go
        # use self.lbl.repaint()

        # Label can also updated with image using Pixmap object
        # pm = QPixmap("./fileName.jpg")
        # pm2 = pm.scaled(100,100) # To show full image in small area
        # self.lbl.setPixmap(pm2)
        return

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec())