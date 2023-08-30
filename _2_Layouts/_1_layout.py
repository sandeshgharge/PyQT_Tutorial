"""
Layouts

Previous all the examples had absolute positioning
Here we will arrange the dialogs and widgets using layouts

Absolute Layout
    - Lots of work
    - Not Elastic

QLayout - Abstract Class
    addWidget()
    removeWidget(),
    count(),
    setAlignment(),
    setEnabled(bool)    --> Enable / Disable entire layout

    QBoxLayout()
        QVBoxLayout()
        QHBoxLayout()
        
        addLayout(lyt, int)
        addStretch(int)     --> Pushing the layouts to left or right
        setDirection()      --> Setting the direction from 
                                left or right ( in case of Vertical Layout) /
                                top or bottom ( in case of Horizontal Layout)
    
    QFormLayout() -->   In case we want to design a form, no need to create label and widget seperately
                        We can pass both together and this layout will take care of rest of the things

        addRow(label, QWidget) 
        insertRow(idx, label, QWidget)
        removeRow(idx)
        setLabelAlignment(Qt.QAlignment)

    QGridLayut()
        addWidget(QWidget, x, y, xspan?, yspan?)
            --> xspan and yspan are optional, they work for merging of cells of grid
            --> in case we need the a widget to take 2 cells in a row / column span parameters will help

    QStackedLayout()
        Here layout are stacked and can be activated using QComboBox / QListBox /QRadioButtons to select a layout
        Achieve similar functionality to a tabbed layout
"""


import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

class DlgMain(QDialog):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")
        self.resize(200,200)

        """
        Check for next file for practical implementation
        """
    
    def dialogDemo(self):
        return

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec())