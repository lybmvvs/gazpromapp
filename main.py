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
            global dummy,data
            no_grp = data.groupby('Скважина №').agg(
                {'ГС/ННС': lambda x:
                x.tolist()}
            )
            no_grp.reset_index(inplace=True)
            no_grp['ГРП?'] = no_grp.apply(
                lambda x:
                0 if 'ГРП' not in str(x['ГС/ННС'])
                else 1, axis=1)
            no_grp = no_grp.drop(no_grp[no_grp['ГРП?'] == 1].index)
            spisok = no_grp['Скважина №'].tolist()
            step = data.groupby(target).agg(
                {date_column_name: lambda x:
                x.tolist()[0]
                if len(x.tolist()) == 1 else x.tolist()[1]}
            )
            step.reset_index(inplace=True)
            step = step[~step['Скважина №'].isin(spisok)].reset_index(drop=True)
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
            global dummy,data
            dummy['Index'] = dummy.index
            dummy1 = dummy.drop(dummy[dummy['Пластовое давление (ТР), атм'] != 0].index)
            dummy1 = dummy1.drop(dummy1[dummy1['Забойное давление (ТР), атм'] != 0].index)
            dummy1 = dummy1.groupby('Скважина №').agg(
                {'Index': lambda x:
                x.tolist()})
            dummy1['кол'] = dummy1.apply(lambda x: len(x['Index']), axis=1)
            dummy1 = dummy1.drop(dummy1[dummy1['кол'] < 3].index)

            delete = []
            for i in dummy1['Index']:
                delete += i
            dummy = dummy[~dummy['Index'].isin(delete)].reset_index(drop=True)

            dummy = dummy.drop(dummy[dummy['Дебит нефти, т/сут'] == 0].index)
            n = 1
            z = dummy['Пласт'].value_counts()[:n].index.tolist()
            plast = str(z[0])
            dummy = dummy.drop(dummy[dummy['Пласт'] != plast].index).reset_index(
                drop=True)

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
            dummy["Пластовое давление (ТР), атм"] = dummy["Пластовое давление (ТР), атм"].replace(0, np.nan).bfill()

        ui.pushButton_4.clicked.connect(sub_zero_pressure)



    def export_final():
        global dummy
        dummy = dummy.drop(['Index'], axis=1)
        dummy.to_excel('MER_new.xlsx')

    ui.pushButton_5.clicked.connect(export_final)

ui.pushButton.clicked.connect(open_second_window)


sys.exit(app.exec_())
