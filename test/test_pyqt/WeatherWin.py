# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WeatherWin.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(401, 300)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 381, 241))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 30, 71, 31))
        self.label.setObjectName("label")
        self.weatherComboBox = QtWidgets.QComboBox(self.groupBox)
        self.weatherComboBox.setGeometry(QtCore.QRect(100, 30, 87, 22))
        self.weatherComboBox.setObjectName("weatherComboBox")
        self.weatherComboBox.addItem("")
        self.weatherComboBox.addItem("")
        self.weatherComboBox.addItem("")
        self.resultText = QtWidgets.QTextEdit(self.groupBox)
        self.resultText.setGeometry(QtCore.QRect(10, 80, 351, 151))
        self.resultText.setObjectName("resultText")
        self.queryBut = QtWidgets.QPushButton(Form)
        self.queryBut.setGeometry(QtCore.QRect(50, 260, 93, 28))
        self.queryBut.setObjectName("queryBut")
        self.clearBut = QtWidgets.QPushButton(Form)
        self.clearBut.setGeometry(QtCore.QRect(250, 260, 93, 28))
        self.clearBut.setObjectName("clearBut")

        self.retranslateUi(Form)
        self.queryBut.clicked.connect(Form.queryWeather)
        self.clearBut.clicked.connect(Form.clearWeather)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "查询城市天气"))
        self.label.setText(_translate("Form", "城市"))
        self.weatherComboBox.setItemText(0, _translate("Form", "北京"))
        self.weatherComboBox.setItemText(1, _translate("Form", "天津"))
        self.weatherComboBox.setItemText(2, _translate("Form", "上海"))
        self.queryBut.setText(_translate("Form", "查询"))
        self.clearBut.setText(_translate("Form", "清空"))

