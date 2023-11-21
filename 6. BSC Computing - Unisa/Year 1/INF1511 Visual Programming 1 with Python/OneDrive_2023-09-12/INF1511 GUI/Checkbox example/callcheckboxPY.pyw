import sys
from PyQt5.QtWidgets import QApplication, QDialog
from checkbox import Ui_Dialog  # Import the generated UI class

class MyDialog(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Initialize the UI from the generated class
   
        # Connect the checkbox to a slot
        self.checkBox.stateChanged.connect(self.updateLineEdit)

    def updateLineEdit(self):
        if self.checkBox.isChecked():
            self.lineEdit.setText("selected")
        else:
            self.lineEdit.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = MyDialog()
    dialog.exec_()
    sys.exit(app.exec_())
