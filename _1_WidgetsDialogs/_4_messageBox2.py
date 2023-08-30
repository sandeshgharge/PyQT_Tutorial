# Method 2 to use Message Box

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
        msg = QMessageBox()
        msg.setText("Heading")
        msg.setDetailedText("Description")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setWindowTitle("Title")
        msg.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        res = msg.exec()
        print(res)

        msg2 = QMessageBox()
        msg2.setText("Message box without detailed text")
        # msg.setDetailedText("Description")
        msg2.setIcon(QMessageBox.Icon.Critical)
        msg2.setWindowTitle("Title")
        msg2.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        print(msg2.exec())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec())