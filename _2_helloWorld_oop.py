# Hello World using OOPs concept

# Import Section
import sys
from PyQt6.QtWidgets import *

# Create a class which extends the desired options (QDialog / QMainWindow / QWidgets)
class DlgMain(QDialog):

    # Constructor in Python is defined as below
    def __init__(self):

        # This line is know to people with understanding of OOPs concept
        # If not have a look on super keyword
        super().__init__()

        """
        Section where you can add widgets and set properties
        """
        # Setting the title
        self.setWindowTitle("My GUI")

        # resizing the window, sometime necessary in case the there are less no of widgets
        # It takes the size of the widgets, and looks it really small
        self.resize(200,200)

        # Checkout the widget where we can enter the data like a input text field in HTML
        self.lineEditText = QLineEdit("Enter you message", self)

        # Since the widget added seems to be at top-left corner we move it to look better
        self.lineEditText.move(50,50)

        # Button Widget - here we will update the Window title on click of a button
        # and the value will be fetched from the line edit text field
        self.btn = QPushButton("Update Window Title", self)
        self.btn.move(35, 88)
        # On click event pass the function name as argument
        self.btn.clicked.connect(self.updateWindowTitle)

    # Method defined to upate the window title on click of a button
    def updateWindowTitle(self):
        self.setWindowTitle(self.lineEditText.text())


if __name__ == "__main__":
    # Create application
    app = QApplication(sys.argv)

    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec())

