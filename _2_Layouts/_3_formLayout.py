# Form Layout

"""
This program will cover Horizontal and Vertical layout

"""
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

class DlgMain(QDialog):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")
        self.resize(300,50)

        # Create widgets here
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
        # self.mainL = QHBoxLayout()
        self.mainL = QFormLayout()
        self.mainL.addRow("Enter your full name : ", self.ledit)
        self.mainL.addRow("Select city : ", self.cb2)
        self.mainL.addRow("", self.btn)

        # Check for multiple alignment properties
        self.mainL.setLabelAlignment(Qt.AlignmentFlag.AlignLeft)

        # Check for multiple wrapping policy
        # self.mainL.setRowWrapPolicy(QFormLayout.RowWrapPolicy.WrapAllRows)
        self.mainL.setRowWrapPolicy(QFormLayout.RowWrapPolicy.WrapLongRows)

        self.setLayout(self.mainL)
    
    def dialogDemo(self):
        return

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec())