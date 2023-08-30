# QComboBox - Editable

"""
QComboBox(parent) --> Accts like a select tag in HTML

Here you can add new elements in case the value is not present inside the list
You can set the maximum number of text in the list

Methods -

    setEditable(bool), isEditable()
    lineEdit(), setLineEdit()       --> To edit the combo box text
    clearEditText(), setEditText(txt)

Signals -
    editTexChanged(txt)

"""

import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

class DlgMain(QDialog):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")
        self.resize(500,500)

        self.ecb = QComboBox(self)
        self.ecb.move(20, 30)
        self.ecb.resize(200, 80)
        self.ecb.setEditable(True)
        self.ecb.setDuplicatesEnabled(False)
        self.ecb.addItem("Navi Mumbai", "NM")
        self.ecb.addItem("Mumbai", "MU")
        self.ecb.addItem("Banglore", "BG")
        self.ecb.addItem("Delhi", "DL")
        self.ecb.currentTextChanged.connect(self.textOnly)
        self.ecb.currentIndexChanged.connect(self.txtVal)

    def textOnly(self, txt):
        print("text change : "+txt)
        return
    
    def txtVal(self, idx):

        # Below if loop takes care of giving a code to new value
        if not self.ecb.itemData(idx):
            txt , code = QInputDialog.getText(self, "Add code dialog",
                                             "Please enter code for newly added value : {}"
                                             .format(self.ecb.itemText(idx)))
            if code:
                self.ecb.setItemData(idx, txt)
        # QMessageBox.information(self,"New Value","Index change : " + self.ecb.itemData(idx))
        QMessageBox.information(self,"New Value","Index change : {}".format(self.ecb.itemData(idx)))
        return

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec())