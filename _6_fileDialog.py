# File dialog to accept file from the user

"""
Users OS file dialogs to open / save a filename

QFileDialog.getOpenFileName(parent, "Title", directory, type)   --> Single file
QFileDialog.getOpenFileNames(parent, "Title", directory, type)  --> Multiple files, return value is array of file names
QFileDialog.getSaveFileDialog(parent, "Title", directory, type) --> Used to save the file

directory   --> a string defines the default path of the directory
type        --> allowed type of the file. Multiple values can be passed using 2 semicolons - ;;
                e.g. JPF File (*.jpg);;PNG Files (*.png)

Empty string is returned in case nothing is selected
"""

import sys
from PyQt6.QtWidgets import *

class DlgMain(QDialog):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")
        self.resize(200,200)

        self.btn = QPushButton("Open Dialog", self)
        self.btn.move(40,40)
        self.btn.clicked.connect(self.openDialog)
    
    def openDialog(self):
        file = QFileDialog.getOpenFileName(self, "Open File", "/home/", "JPF File (*.jpg);;PNG Files (*.png)")
        print(file)

        file = QFileDialog.getOpenFileNames(self, "Open File", "/home/", "JPF File (*.jpg);;PNG Files (*.png)")
        print(file)

        file = QFileDialog.getSaveFileName(self, "Open File", "/home/", "JPF File (*.jpg);;PNG Files (*.png)")
        print(file)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec())

