# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window2.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_secondwindow(object):
    def setupUi(self, secondwindow):
        secondwindow.setObjectName("secondwindow")
        secondwindow.resize(529, 365)
        secondwindow.setStyleSheet("\n"
"QPushButton{\n"
"background-color:white ;\n"
"width:100px;\n"
"length:200px;\n"
"font-size: 14px;\n"
"font-weight:bold;\n"
"border:none;\n"
"text-align:center;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:silver;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(96, 255, 39);\n"
"}\n"
"QLabel{\n"
"background-color:rgb(121, 173, 255);\n"
"width:100px;\n"
"length:200px;\n"
"font-size: 11px;\n"
"font-weight:bold;\n"
"border:none;\n"
"text-align:center;\n"
"}")
        self.gridLayoutWidget = QtWidgets.QWidget(secondwindow)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 40, 478, 231))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 2, 1, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 3, 1, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(secondwindow)
        self.pushButton_5.setGeometry(QtCore.QRect(140, 300, 251, 28))
        self.pushButton_5.setStyleSheet("\n"
"QPushButton{\n"
"background-color: rgb(255, 255, 53);\n"
"width:100px;\n"
"length:200px;\n"
"font-size: 20px;\n"
"font-weight:bold;\n"
"border:none;\n"
"text-align:center;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:silver;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(96, 255, 39);\n"
"}\n"
"")
        self.pushButton_5.setObjectName("pushButton_5")

        self.retranslateUi(secondwindow)
        QtCore.QMetaObject.connectSlotsByName(secondwindow)

    def retranslateUi(self, secondwindow):
        _translate = QtCore.QCoreApplication.translate
        secondwindow.setWindowTitle(_translate("secondwindow", "Form"))
        self.label.setText(_translate("secondwindow", "Добавить \"_ГРП\" к номеру скважины:"))
        self.label_2.setText(_translate("secondwindow", "Удалить строки с нулевым дебитом:"))
        self.label_3.setText(_translate("secondwindow", "!НАЖИМАТЬ ПЕРВОЙ! Удалить скважины с короткой историей:"))
        self.label_4.setText(_translate("secondwindow", "Продлить пластовое значение, если оно нулевое:"))
        self.pushButton.setText(_translate("secondwindow", "Выполнить"))
        self.pushButton_2.setText(_translate("secondwindow", "Выполнить"))
        self.pushButton_3.setText(_translate("secondwindow", "Выполнить"))
        self.pushButton_4.setText(_translate("secondwindow", "Выполнить"))
        self.pushButton_5.setText(_translate("secondwindow", "Экспорт Excel файла"))
