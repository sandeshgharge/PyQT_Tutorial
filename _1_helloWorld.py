# First QT application

#Import Section
import sys
from PyQt6.QtWidgets import *

# Create application
app = QApplication(sys.argv)

# Create Main GUI canvas
"""
 This statement can also used instead of below statements, in some cases
    dlgMain = QDialog() --> have additional features and methods that QWidget do not have
    dlgMain = QMainWindow() --> A bit small, but has ability to handle menu bars, toolbars, status bars i.e. creating a full featured application
"""
dlgMain = QWidget()

# Design the window
dlgMain.setWindowTitle("My GUI")

# Show the GUI
dlgMain.show()

# And finally for everything to work, execute the application
"""
exec() method returns exit code : 
0       --> Application exited successfully
error   --> in few  other cases

When it comes to Best Practice Methods we can write the same code as below ( it uses the standard Python methods for terminating )-
sys.exit(app.exec())
"""
app.exec()