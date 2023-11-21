# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addlist.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(721, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 91, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(132, 20, 181, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.pushAdd = QtWidgets.QPushButton(Dialog)
        self.pushAdd.setGeometry(QtCore.QRect(200, 70, 93, 28))
        self.pushAdd.setObjectName("pushAdd")
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(380, 10, 256, 192))
        self.listWidget.setObjectName("listWidget")
        self.pushEdit = QtWidgets.QPushButton(Dialog)
        self.pushEdit.setGeometry(QtCore.QRect(200, 120, 93, 28))
        self.pushEdit.setObjectName("pushEdit")
        self.pushDelete = QtWidgets.QPushButton(Dialog)
        self.pushDelete.setGeometry(QtCore.QRect(200, 170, 93, 28))
        self.pushDelete.setObjectName("pushDelete")
        self.pushDeleteAll = QtWidgets.QPushButton(Dialog)
        self.pushDeleteAll.setGeometry(QtCore.QRect(200, 220, 93, 28))
        self.pushDeleteAll.setObjectName("pushDeleteAll")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Please enter: "))
        self.pushAdd.setText(_translate("Dialog", "Add"))
        self.pushEdit.setText(_translate("Dialog", "Edit"))
        self.pushDelete.setText(_translate("Dialog", "Delete"))
        self.pushDeleteAll.setText(_translate("Dialog", "Delete All"))

