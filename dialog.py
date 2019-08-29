# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import database
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(430, 305)

        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(30, 60, 351, 171))
        self.groupBox.setObjectName("groupBox")
        self.Login = QtWidgets.QLineEdit(self.groupBox)
        self.Login.setGeometry(QtCore.QRect(110, 40, 113, 20))
        self.Login.setObjectName("Login")
        self.password = QtWidgets.QLineEdit(self.groupBox)
        self.password.setGeometry(QtCore.QRect(110, 90, 113, 20))
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.logujBtn = QtWidgets.QPushButton(self.groupBox)
        self.logujBtn.setGeometry(QtCore.QRect(250, 130, 75, 23))
        self.logujBtn.setObjectName("logujBtn")
        self.register_2 = QtWidgets.QPushButton(Dialog)
        self.register_2.setGeometry(QtCore.QRect(280, 30, 81, 23))
        self.register_2.setObjectName("register_2")




        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "Zalopguj się"))
        self.logujBtn.setText(_translate("Dialog", "Zaloguj!"))
        self.register_2.setText(_translate("Dialog", "Zarejestruj się"))





