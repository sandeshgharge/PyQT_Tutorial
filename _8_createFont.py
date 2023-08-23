# Create a font for the application

"""
QFont("Arial", 24)  --> Font family and size of the fonts
QFont("Arial", 24, 81, True) --> 81 defines the extra bold style and true is for Italic
QFont() --> now you can set the values using set methods

returns a tuple with font and status(true/false)
Other styles are defined and can be checked on QT website
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

        # We can also set default font
        f = QFont("Times New Roman", 28, 75,True)
        self.btn.setFont(f)
        self.btn.clicked.connect(self.dialogDemo)
    
    def dialogDemo(self):
        f = QFontDialog.getFont()
        print(f)

        # Set the font to the button to check the result instantly
        self.btn.setFont(f[0])
        return

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec())