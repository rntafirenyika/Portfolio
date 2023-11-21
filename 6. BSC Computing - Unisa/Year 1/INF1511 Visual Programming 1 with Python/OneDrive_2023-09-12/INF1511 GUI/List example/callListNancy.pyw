import sys
from PyQt5.QtWidgets import QInputDialog, QLineEdit, QApplication, QMainWindow
from listNancy import Ui_Dialog

class addForm(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushAdd.clicked.connect(self.addlisting)
        self.ui.pushEdit.clicked.connect(self.editlisting)
        self.ui.pushDelete.clicked.connect(self.dellisting)
        self.ui.pushDeleteAll.clicked.connect(self.delallist)

    def addlisting(self):
        self.ui.listWidget.addItem(self.ui.lineEdit.text())
        self.ui.lineEdit.setText('')
        self.ui.lineEdit.setFocus()

    def editlisting(self):
        row = self.ui.listWidget.currentRow()
        self.ui.listWidget.takeItem(row)
        text, okPressed = QInputDialog.getText(self, "Get text", "New text:", QLineEdit.Normal, "")
        if okPressed and text != '':
            self.ui.listWidget.insertItem(row, str(text))

    def dellisting(self):
        self.ui.listWidget.takeItem(self.ui.listWidget.currentRow())

    def delallist(self):
        self.ui.listWidget.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    addApp = addForm()
    addApp.show()
    sys.exit(app.exec_())
