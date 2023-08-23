#QLineEdit

"""
QLineEdit(parent)
QLineEdit(parent, self)

Methods -->
    test(), setText(), clear()  
    setPlaceHolder(Text)            --> Act as a message inside a text box
    setReadOnly(bool)               --> Value in this field cannot be edited but only viewed
    setEchoMode(QLineEdit.Password) --> Used in case of password where value entered should not be visible
    setAlignment(QT.Alignment)      --> Used to align the text i.e. right / left 7 center
    setMaxLength(int)               --> Defines max lenth of the value that can be entered

Signals -->

    textChanged(str) --> returns the current value when signal is edited++
    textEdit(str)    --> Similar to textChanged but textEdit(), works only case of user input 

"""
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

class DlgMain(QDialog):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")
        self.resize(200,200)

        self.lbl = QLabel("Hello World", self)
        self.lbl.move(40, 110)
        self.lbl.resize(100, 100)
        fnt = QFont("Times New Roman", 20, 75, True)
        self.lbl.setFont(fnt)

        self.lineEditText = QLineEdit("Enter you message", self)
        self.lineEditText.setPlaceholderText("Message")
        # self.lineEditText.setReadOnly(True)

        # Try all modes to check how it works
        # self.lineEditText.setEchoMode(QLineEdit.EchoMode.NoEcho)
        # self.lineEditText.setEchoMode(QLineEdit.EchoMode.Normal)
        # self.lineEditText.setEchoMode(QLineEdit.EchoMode.Password)
        # self.lineEditText.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)
        
        self.lineEditText.move(50,50)
        self.lineEditText.textChanged.connect(self.handletxt)

    def handletxt(self):
        self.lbl.setText(self.lineEditText.text())
        return

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec())