# QComboBox - simple

"""
QComboBox(parent) --> Accts like a select tag in HTML

Methods -

    --> Icon is optional.
    addItem(QIcon, txt, obj)            --> Adds an item into combo box
    insertItem(index, QIcon, txt, obj)  --> Insert an item into a combo box
    insertSeperator(index)              --> Seperates the items using the seperator
    addItems(list)                      --> Can add multiple items at a time
    insertItems(index, lst)             --> Can insert list of items corresponding to list of index provided
    removeItem(index)                   --> Used to remove the item
    clear()                             --> Will clear all the items from the Combo Box
    count()                             --> Number of Items present inside the CB
    setPlaceHoldertext(text)            --> Set the text of place holder
    setCurrentIndex(index)              --> Set index of current item
    setCurrentText(text)                --> Set text of current item

    --> Returns current index / data / text of the item
    currentIndex(), currentData(), curentText()

    --> Returns data / text / icon at specified index
    itemText(index),itemData(index), itemIcon(index)

    --> Set text / data / icon of specified index
    setItemText(idx, txt), setItemData(index, obj), setItemIcon(index, QIcon)

    --> Set maximum limit of items in Combobox
    setMaxCount(int), setMaxVisibleItem(int)(default value : 10)
    
Signals -
    currentIndexChanged(index), currentTextChanged(text)    --> triggered whrn values changes
    activated(index), textActivated(text)                   --> triggered when user changes the data
    highlighted(index), textHighlighted(text)               --> triggered when user moves up and down using arrow keys
"""

import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

class DlgMain(QDialog):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")
        self.resize(500,500)

        self.cb = QComboBox(self)
        self.cb.move(20, 10)

        self.cb.addItems(["AL","AR","SG","VD"])
        self.cb.currentTextChanged.connect(self.textOnly)

        # There is only  1 value taking care of the combo box
        # Incase we need 2 values in key pair, below is the method to do it

        self.cb2 = QComboBox(self)
        self.cb2.move(20,40)

        self.cb2.addItem("Navi Mumbai", "NM")
        self.cb2.addItem("Mumbai", "MU")
        self.cb2.addItem("Banglore", "BG")
        self.cb2.addItem("Delhi", "DL")
        self.cb2.currentIndexChanged.connect(self.txtVal)

        self.cb3 = QComboBox(self)
        self.cb3.move(20,70)

        self.cb3.addItem("Pune", {"key" : "PN", "pop" : 14324})
        self.cb3.addItem("Ahmedabad", {"key" : "AH", "pop" : 57474})
        self.cb3.addItem("Hyderabad", {"key" : "HB", "pop" : 457634})
        self.cb3.addItem("Vizag", {"key" : "KI", "pop" : 24523})
        self.cb3.currentIndexChanged.connect(self.txtObj)
        self.cb3.highlighted.connect(self.highlightEG)

        self.lbl = QLabel("Population : 40000", self)
        self.lbl.move(200,70)

    def textOnly(self, txt):
        print(txt)
        return
    
    def txtVal(self, idx):
        print(self.cb2.itemData(idx))
        return

    def txtObj(self, idx):
        print(self.cb3.itemData(idx)["key"])
        print(self.cb3.itemData(idx)["pop"])
        return
    
    def highlightEG(self, idx):
        self.lbl.setText("Population : {}".format(self.cb3.itemData(idx)["pop"]))
        return

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec())