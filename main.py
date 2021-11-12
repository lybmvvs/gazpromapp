import sys
import datetime
import pandas as pd
import numpy as np
from PyQt5 import QtWidgets
from window1 import Ui_firstwindow
from window2 import Ui_secondwindow



app = QtWidgets.QApplication(sys.argv)
first_window = QtWidgets.QWidget()
ui = Ui_firstwindow()
ui.setupUi(first_window)
first_window.show()




class File_functions():


    def im_file(self):
        global file_name, data, date_column_name, target, dummy
        file_name = ui.lineEdit.text()
        data = pd.read_excel(file_name, sheet_name='ГРП')
        dummy = pd.read_excel(file_name, sheet_name='МЭР')
        date_column_name = r'Дата ВНР после ГС \\ ГРП \\ЗБГС'
        target = 'Скважина №'
        print(data.shape, dummy.shape, file_name, date_column_name)


    ui.pushButton.clicked.connect(im_file)


def open_second_window():
    global second_window,ui
    second_window = QtWidgets.QWidget()
    ui = Ui_secondwindow()
    ui.setupUi(second_window)
    first_window.close()
    second_window.show()


    class Plus_grp(File_functions):
        def add_grp(self):
            global dummy
            step = data.groupby(target).agg(
                {date_column_name: lambda x:
                x.tolist()[0]
                if len(x.tolist()) == 1 else x.tolist()[1]}
            )
            dummy = dummy.merge(step, on=target)
            dummy[target] = dummy.apply(
                lambda x:
                str(x[target])
                + ('_ГРП' if x['Дата'] > x[date_column_name] else ''),
                axis=1
            )
            dummy = dummy.drop(date_column_name, axis=1)

        ui.pushButton.clicked.connect(add_grp)


    class Debit(File_functions):
        def delete_zero_debit(self):
            global dummy
            dummy = dummy.drop(dummy[dummy['Дебит нефти, т/сут'] == 0].index)

        ui.pushButton_2.clicked.connect(delete_zero_debit)


    class History(File_functions):
        def red_small_hist(self):
            global dummy
            dummy1 = dummy.groupby(target).agg(
                {'Дата': lambda x:
                x.tolist()}
            )
            dummy1['История'] = dummy1.apply(
                lambda x:
                1 if len(x['Дата']) >= 6
                else 0, axis=1)
            dummy1 = dummy1.drop(dummy1[dummy1['История'] != 1].index)
            dummy1.reset_index(inplace=True)
            a = dummy1['Скважина №'].tolist()
            dummy = dummy[dummy['Скважина №'].isin(a)]

        ui.pushButton_3.clicked.connect(red_small_hist)


    class Pressure(File_functions):
        def sub_zero_pressure(self):
            global dummy
            dummy['Предыдущее пластовое давление'] = dummy['Пластовое давление (ТР), атм'].shift(-1)

            dummy['Пластовое давление (ТР), атм'], dummy['Предыдущее пластовое давление'] = np.where(
                dummy['Пластовое давление (ТР), атм'] == 0,
                (dummy['Предыдущее пластовое давление'], dummy['Пластовое давление (ТР), атм']),
                (dummy['Пластовое давление (ТР), атм'], dummy['Предыдущее пластовое давление']))
            dummy = dummy.drop('Предыдущее пластовое давление', axis=1)

        ui.pushButton_4.clicked.connect(sub_zero_pressure)



    def export_final():
        global dummy
        dummy.to_excel('MER_new.xlsx')

    ui.pushButton_5.clicked.connect(export_final)

ui.pushButton.clicked.connect(open_second_window)


sys.exit(app.exec_())
