# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test01_pyqt5_ui02.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_childFrom(object):
    def setupUi(self, childFrom):
        childFrom.setObjectName("childFrom")
        childFrom.resize(274, 210)
        self.verticalLayout = QtWidgets.QVBoxLayout(childFrom)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = QtWidgets.QTextEdit(childFrom)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)

        self.retranslateUi(childFrom)
        QtCore.QMetaObject.connectSlotsByName(childFrom)

    def retranslateUi(self, childFrom):
        _translate = QtCore.QCoreApplication.translate
        childFrom.setWindowTitle(_translate("childFrom", "Form"))

