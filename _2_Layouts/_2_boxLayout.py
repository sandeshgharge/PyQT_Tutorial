# Box Layout

"""
This program will cover Horizontal and Vertical layout

"""
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

class DlgMain(QDialog):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")
        self.resize(500,50)

        # Create widgets
        self.lbl = QLabel("Select City")
        self.btn = QPushButton("Button 1")
        self.lbl2  = QLabel("Line Edit")
        self.ledit = QLineEdit("Line Edit 1")
        self.ledit.resize(100,80)
        self.cb2 = QComboBox(self)
        self.cb2.addItem("Navi Mumbai", "NM")
        self.cb2.addItem("Mumbai", "MU")
        self.cb2.addItem("Banglore", "BG")
        self.cb2.addItem("Delhi", "DL")

        # Try any of the layout commenting the other one and you will see the difference
        self.mainL = QHBoxLayout()
        # self.mainL = QVBoxLayout()

        # Try commenting below line and stretch the window
        # addStretch can be added any where in the code
        # It allows the stretch the area, wherever the addStretch is defined
        # It can cannot be explained rather try adding the method then stretching it
        # Direction works with type of box layout selected i.e. Vertical / Horizontal

        self.mainL.addStretch()

        # You can add the optional parameter to specify how much percentage will the widget will occupy
        # In case you don't want to specify percentage, you can give interger value with total value of 12
        self.mainL.addWidget(self.lbl, 10)
        self.mainL.addWidget(self.cb2, 20)
        self.mainL.addWidget(self.lbl2, 10)
        self.mainL.addWidget(self.ledit, 20)
        self.mainL.addWidget(self.btn, 20)

        self.mainL.addStretch(20)

        self.setLayout(self.mainL)
    
    def dialogDemo(self):
        return

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec())