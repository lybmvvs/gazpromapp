# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window1.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_firstwindow(object):
    def setupUi(self, firstwindow):
        firstwindow.setObjectName("firstwindow")
        firstwindow.resize(301, 278)
        firstwindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        firstwindow.setStyleSheet("\n"
"QPushButton{\n"
"background-color: rgb(255, 255, 53);\n"
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
"\n"
"\n"
"")
        self.verticalLayoutWidget = QtWidgets.QWidget(firstwindow)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 261, 211))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("QLabel{\n"
"background-color:rgb(96, 255, 39);\n"
"width:100px;\n"
"length:200px;\n"
"font-size: 14px;\n"
"font-weight:bold;\n"
"border:none;\n"
"text-align:center;\n"
"}\n"
"")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.label_2 = QtWidgets.QLabel(firstwindow)
        self.label_2.setGeometry(QtCore.QRect(80, 250, 221, 20))
        self.label_2.setStyleSheet("QLabel{\n"
"\n"
"width:100px;\n"
"length:200px;\n"
"font-size: 12px;\n"
"font-weight:bold;\n"
"border:none;\n"
"text-align:center;\n"
"color: rgb(171, 171, 171)\n"
"}")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(firstwindow)
        QtCore.QMetaObject.connectSlotsByName(firstwindow)

    def retranslateUi(self, firstwindow):
        _translate = QtCore.QCoreApplication.translate
        firstwindow.setWindowTitle(_translate("firstwindow", "Form"))
        self.label.setText(_translate("firstwindow", "             Выберите Excel файл:"))
        self.pushButton.setText(_translate("firstwindow", "Импортировать"))
        self.label_2.setText(_translate("firstwindow", "Автор-разработчик: Любимов В.С."))
