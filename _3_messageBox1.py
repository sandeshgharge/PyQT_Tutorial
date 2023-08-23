# Message box is used to give an output to user

"""
Method 1 - Static Method (prefererd)
    This file shows demo with Method 1
      parent = QWidget where the message box to be centered in
      result = QMessageBox.warning(parent, "Title of the box", "Message")
          warning can be replaced by - Information, critical, question
      
      We can add buttons as required where we can also set one of them as default
      result = QMessageBox.warning(parent, "Title of the box", "Message", button1 | button2 | button3.buttonDefault)


Check out list of message box on the official website

Method 2 - Lengthy and Customisable

    msg = QMessageBox()
    msg.setText("Heading")
    msg.setDetailedText("Description")
    msg.setIcon(QMessageBox.information)
    msg.setWindowTitle("Title")
    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    msg.exec()
"""

import sys
from PyQt6.QtWidgets import *

class DlgMain(QDialog):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")
        self.resize(200,200)

        self.btn = QPushButton("ShowMessage", self)
        self.btn.move(40,40)
        self.btn.clicked.connect(self.showMsg)
    
    def showMsg(self):

        # List of different Message box
        res = QMessageBox.information(self, "Well Done.!", "Check the console for the output of the buttons on Message Box")
        print(res)
        res = QMessageBox.warning(self, "Well Done.!", "Check the console for the output of the buttons on Message Box")
        print(res)
        res = QMessageBox.critical(self, "Well Done.!", "Check the console for the output of the buttons on Message Box")
        print(res)
        res = QMessageBox.question(self, "Well Done.!", "Check the console for the output of the buttons on Message Box")
        print(res)

        # Few values of pre defined buttons
        print(QMessageBox.StandardButton.Yes)
        print(QMessageBox.StandardButton.Abort)

        # These values can be used to define the process using conditional Statement

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec())
