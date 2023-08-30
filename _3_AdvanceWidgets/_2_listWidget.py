# QListWidget

"""
Below is the heirarchy of the List Widget that we will be learning here

QWidget
    QFrame - setFrameShadow, setFrameShape, setLineWidth
        QAcstractScrollArea - setVerticalScrollBarPolicy
            QAbstractItemView
                -- setEditTriggers, setDragDropMode, setSelectionMode
                QListView
                    QListWidget
                        Methods -
                            addItem(txt), addItems(list), insertItem(idx, txt)
                            setCurrentRow(idx), sortItems(Qt.SortOrder)
                        Signals -
                            currentRowChanged(int)
                            currentTextChanged(txt)#
                            itemsSelectionChanged()

QListWidgetItem

type    -- ?
str     -- ?
QListWidgetItem (str, parent,type)
QListWidgetItem (QIcon, str, parent, type)
QListWidgetItem  (QListWidgetItem)          --> Creates a copy

Customization
    settext, setIcon, setFont, setData
    setToolTip  --> Text to be displayed when the cursor is hovering over
    setCheckedState, setSelected, setHidden

QListWidget methods and signals that utilise QListWidgetItem
    Methods -
        addItem(QLWI), insertItem(idx, QLWI)
        item(idx)               --> Get the item at specific index
        currentItem()           --> Get the index of the current item
        removeItemWidget(QLWI)  --> Remove the item
        row(QLWI)               --> Returns the index of item
        selectedItems([QLWIs])  --> Select the items by passing the items that has to be selected

    Slots
        currentItemChanged(currentQLWI, previousQLWI)
        itemClicked(QLWI)
        itemDoubleClicked(QLWI)
"""

import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

class DlgMain(QDialog):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")
        self.resize(200,200)

        self.lngLst1 = QListWidget()
        self.lngLst.addItems(["JAVA", "Python", "C++"])

        self.lngLst2 = QListWidget()

        self.lr = QPushButton("-->")
        self.rl = QPushButton("<--")

        self.btn = QPushButton("Confirm")

        self.setUpLayout()

    def setUpLayout(self):

        self.ml = QVBoxLayout()
        self.ws = QHBoxLayout()
        self.l1 = QVBoxLayout()
        self.l2 = QVBoxLayout()
        self.action = QVBoxLayout()

        self.ws.addWidget(self.l1)
        self.ws.addLayout(self.action)
        self.ws.addWidget(self.l2)

        self.ml.addLayout(self.ws)
        self.ml.addWidget(self.action)

        self.action.addStretch()
        self.action.addWidget(self.lr)
        self.action.addWidget(self.rl)
        self.action.addStretch()

        #self.setLayout(slef.)
        return

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec())

