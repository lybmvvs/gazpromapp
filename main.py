
from PyQt5 import QtCore, QtGui, QtWidgets
from window1 import Ui_firstwindow
from window2 import Ui_secondwindow
import pandas as pd
import datetime
import sys
app = QtWidgets.QApplication(sys.argv)
firstwindow = QtWidgets.QWidget()
ui = Ui_firstwindow()
ui.setupUi(firstwindow)
firstwindow.show()
def OpenSecondWindow():
    global secondwindow
    secondwindow = QtWidgets.QWidget()
    ui = Ui_secondwindow()
    ui.setupUi(secondwindow)
    firstwindow.close()
    secondwindow.show()
def im_file():
    file_name = ui.lineEdit.text()

    print(file_name)
ui.pushButton.clicked.connect(im_file)
ui.pushButton.clicked.connect(OpenSecondWindow)
sys.exit(app.exec_())