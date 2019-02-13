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
        self.textEdit.setHtml(_translate("childFrom", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">aa+bb</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))

