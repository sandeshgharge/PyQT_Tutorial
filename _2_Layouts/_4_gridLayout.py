# Grid Layout

"""

"""

import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

class DlgMain(QDialog):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")
        self.gL = QGridLayout()

        k = 0
        for i in range(3):
            for j in range(3):
                self.gL.addWidget(QPushButton("" + str((k+1))), i , j)
                k = k + 1
            # Need to check the logic for 7, to resemble the calculator layout
        self.gL.addWidget(QPushButton("0"), 4 , 1)

        # 1 and 3 are used for spanning hte cells ( merging )
        # 1 is 1 row and 3 stands for merging 3 columns

        self.gL.addWidget(QPushButton("Calculate"), 5 , 0 , 1, 3 )

        self.setLayout(self.gL)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec())