# Tree Widget

"""
Used for nested lists or data trees

This can be used where there are heirarchies e.g. Folder structure, Command Strutures, Biological families/Kingdoms

QTreeWidgetItem(parent, list[str], type)
Parent can be QTreeWidget (Top level Items) / QTreeWidgetItem(child items)

Methods -
    addChild(QTreeWidgetItem), addChildren([QTreeWidgetItem])
    insertChild(col, QTreeWidgetItem), insertChildren(col, [QTreeWidgetItem])
    setText(col, str), setIcon(col, QIcon), setData(col, QVariant), setExpanded(bool)
    setCheckState(col, bool), setBackground(col, QBrush), setForground(col, QBrush)
    childCount(), child(idx), text(col), data(col), icon(col)

Top Level - QTreeWidget
Methods -
    addTopLevelItem(QTWI), addTopLevelItems([QTWI])
    insertTopLevelItem(idx, QTWI), insertTopLevelItems(idx, [QTWI])
    findItems(str, Qt.MatchFlags, col), sortItems(col, Qt.SortOrder)
    topLevelItemCount(), topLevelItem(idx), selectedItems()
    setColumnCount(int), setHeaderLabels([lbls])
    collapseItem(QTWI), expandItem(QTWI), scrollToItem(QTWI)

Signals -
    itemChanged(QTWI, col), itemClicked(QTWI, col), itemDoubleClicked(QTWI, col)
    itemCollapsed(QTWI), itemExpanded(QTWI), itemSelectionChanged()

"""
import sys, random
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

class DlgMain(QDialog):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")
        self.resize(500,200)

        self.tw = QTreeWidget()
        self.tw.setColumnCount(3)
        self.tw.setHeaderLabels(["QT Class", "Methods", "Signals"])
        self.populateTree()

        # Here 0 defines the sorting coloumn
        # 0 -> QT Class
        # 1 -> Methods
        # 2 -> Signals
        self.tw.sortItems(0, Qt.SortOrder.AscendingOrder)

        # Column width incase needed
        self.tw.setColumnWidth(0, 200)

        # We can keep few trees expanded using below method
        # self.tw.expandItem(self.tw.twiQWidget)

        # Double click event example
        self.tw.itemDoubleClicked.connect(self.doubleClick)
        
        self.ml = QVBoxLayout()
        self.ml.addWidget(self.tw)

        self.setLayout(self.ml)
    
    def populateTree(self):

        self.twiQWidget = QTreeWidgetItem(self.tw, ["QWidget Module"])
        self.twiGUI = QTreeWidgetItem(self.tw, ["QGui Module"])
        self.twiQCore = QTreeWidgetItem(self.tw, ["QCore Module"])

        # We will add child items using below section

        lstQTWidgets = ["QDialog", "QLabel", "QLineEdit", "QTextEdit"]
        for item in lstQTWidgets:
            self.twiQWidget.addChild(QTreeWidgetItem([item, str(random.randrange(25)), str(random.randrange(8))]))

        lstQTWidgets = ["QBitmap", "QColor", "QFont", "QImage"]
        for item in lstQTWidgets:
            self.twiGUI.addChild(QTreeWidgetItem([item, str(random.randrange(25)), str(random.randrange(8))]))

        lstQTWidgets = ["QPixelMap", "QThread", "QDateTime", "QFile"]
        for item in lstQTWidgets:
            self.twiQCore.addChild(QTreeWidgetItem([item, str(random.randrange(25)), str(random.randrange(8))]))

        # Below code will add subitems to QDialog
        # Below method can return mutiple items and we will take only the first item in the list
        twi = self.tw.findItems("QDialog", Qt.MatchFlag.MatchRecursive)[0]
        lstQTWidgets = ["QFileDialog", "QColorDialog", "QFontDialog", "QMessageDialog"]
        for item in lstQTWidgets:
            twi.addChild(QTreeWidgetItem([item, str(random.randrange(25)), str(random.randrange(8))]))
        return
    
    def doubleClick(self, item, col):
        QMessageBox.information(self, "QT Class", "You just double clicked {}".format(item.text(col)))


        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec())