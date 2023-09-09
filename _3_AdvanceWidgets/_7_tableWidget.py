# QTableWidget

"""
QWidget
    QFrame
        QAbstractScollArea
            QAbstractItemView
                QTableView
                    QTableWidget
                        Methods -
                            QTableWidget(rows, columns, parent)
                            currentRow(), currentColumn(), columnCount(), rowCount()
                            insertColumn(col), insertRow(row), removeColumn(col), removeRow(row)
                            setColumnCount(int), setRowCount(int), setCellWidget(row, col, QWidget)
                            setHorizontalHeaderLabels([str])
                        Signals -
                            cellChanged(row, col), cellClicked(row, col), itemSelectionChanged()

Table Widget will help implement MVC structure

QTableWidgetItem
    QTableWidgetItem(type)
    QTableWidgetItem(str, type)
    QTableWidgetItem(icon. str, type)

    Methods -
        setText(str), setIcon(QIcon), setData(var), setSelected(bool)
        setTextAlignment, setToolTip(), setCheckState()
        setBackground(QBrush), setForeground(QBrush)
        
To Use QTableWidgetItems in QTablleWidget
    item(row, col) - returns QTableWidgetItem
    selectedItem() - returns list of QTWI's
    setCurrentItem(QTWI), setItem(row, col, QTWI)
    itemChanged(QTWI) itemClicked(QTWI)
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

    
    def dialogDemo(self):
        return

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec())