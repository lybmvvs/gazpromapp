import sys
import datetime
import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets
from window1 import Ui_firstwindow
from window2 import Ui_secondwindow


app = QtWidgets.QApplication(sys.argv)
first_window = QtWidgets.QWidget()
ui = Ui_firstwindow()
ui.setupUi(first_window)
first_window.show()


def open_second_window():
    global second_window
    second_window = QtWidgets.QWidget()
    ui = Ui_secondwindow()
    ui.setupUi(second_window)
    first_window.close()
    second_window.show()


def im_file():
    file_name = ui.lineEdit.text()

    print(file_name)


ui.pushButton.clicked.connect(im_file)
ui.pushButton.clicked.connect(open_second_window)
sys.exit(app.exec_())
