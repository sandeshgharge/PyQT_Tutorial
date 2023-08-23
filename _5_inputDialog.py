# Input dialog to get inputs from user

import sys
from PyQt6.QtWidgets import *

class DlgMain(QDialog):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")
        self.resize(200,200)

        self.btn = QPushButton("ShowMessage", self)
        self.btn.move(40,40)
        self.btn.clicked.connect(self.openPromt)
    
    def openPromt(self):

        # All the examples have common first 3 Parameters i.e. self, Title, Description
        ip = QInputDialog().getText(self, "Title", "Prompt")
        print(ip)

        name, status = QInputDialog().getText(self, "Enter your name", "Your name")
        print(name)
        print(status)

        # While getting int/double value you can pass extra parameters as
        # getInt(self, "Enter your Age", "Your Age", defaultValue, min, max, step value)

        intVal = QInputDialog().getInt(self, "Enter your Age", "Your Age", 18, 18, 65, 1)
        print(intVal)

        price = QInputDialog().getDouble(self, "Enter total cost", "Total cost", 2.0, 0.10, 10.0, 1)
        print(price)

        # To select through the multiple option we can use getItem
        lstColor = ['Red', 'Blue', 'Green']
        item = QInputDialog.getItem(self, "Color Name","Select your fav color", lstColor, editable=False)
        print(item)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec())