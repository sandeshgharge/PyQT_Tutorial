# Image

"""
*Example not implemented

QPixmap(w, h) / QPixmap(File)
Method -
fill(QColor)    --> loads background with solid color
load(file)      --> Load image in the background
size()
height()
width()
scaled(w,h)
scaledToWidth(w)
scaledToHeight(h)
save(file)

QImage, QPicture, QBitmap, QPainter --> Dialogs you can work on

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