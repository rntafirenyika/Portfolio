import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi

class MyDialog(QDialog):
    def __init__(self):
        super().__init__()
        # the .ui file is loaded at runtime using the loadUi function
        self.ui = loadUi("checkbox.ui", self)  # Load the .ui file

        # Connect the checkbox to a slot
        self.ui.checkBox.stateChanged.connect(self.updateLineEdit)

    def updateLineEdit(self):
        if self.ui.checkBox.isChecked():
            self.ui.lineEdit.setText("selected")
        else:
            self.ui.lineEdit.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = MyDialog()
    dialog.exec_()
    sys.exit(app.exec_())

