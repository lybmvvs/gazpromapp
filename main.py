import sys
import datetime
import pandas as pd
import numpy as np
import copy
from PyQt5 import QtWidgets
from window1 import Ui_firstwindow
from window2_upd import Ui_secondwindow


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
        date_column_name = 'Дата ВНР после'
        target = 'Скважина №'
        data['Скважина №'] = data.apply(
            lambda x:
            str(x['Скважина №']), axis=1)
        dummy['Скважина №'] = dummy.apply(
            lambda x:
            str(x['Скважина №']), axis=1)
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
            data_L = copy.deepcopy(data)
            data_L['удалю'] = data_L.apply(
                lambda x:
                'нет' if 'Л' in str(x['Скважина №'])
                else 'да', axis=1)
            data_L = data_L.drop(data_L[data_L['удалю'] == 'да'].index).reset_index(drop=True)
            data_L = data_L.drop(['удалю'], axis=1)
            data_L['для_грп'] = data_L.apply(
                lambda x:
                x['Скважина №'].partition('_')[0] if '_' in str(x['Скважина №'])
                else x['Скважина №'], axis=1)
            data_L = data_L.groupby('для_грп').agg(
                {date_column_name: lambda x:
                x.tolist()[-1]})
            data_L.reset_index(inplace=True)
            wells_L = data_L['для_грп'].tolist()
            data_L['Скважина №'] = wells_L
            data_L = data_L.drop(['для_грп'], axis=1)
            data_L['Скважина №'] = data_L.apply(
                lambda x:
                str(x['Скважина №']).replace('Л', ''),
                axis=1
            )
            dummy = dummy.merge(data_L, on=target, how='left')
            if dummy.shape[0] != 0:
                dummy[target] = dummy.apply(
                    lambda x:
                    str(x[target])
                    + ('Л' if x['Дата'] <= x[date_column_name] else ''),
                    axis=1
                )
            dummy = dummy.drop(date_column_name, axis=1)


            data['для_грп'] = data.apply(
                lambda x:
                x['Скважина №'].partition('_')[0] if '_' in str(x['Скважина №'])
                else x['Скважина №'], axis=1)
            # важно: убираем скважины с фраками/ннс оставляем только грп
            data['fix'] = data.apply(
                lambda x:
                1 if 'ГРП' in str(x['Скважина №'])
                else 0, axis=1)
            data = data.drop(data[data['fix'] == 0].index)
            # важно
            no_grp = data.groupby('для_грп').agg(
                {'ГС/ННС': lambda x:
                x.tolist()}
            )
            no_grp.reset_index(inplace=True)
            no_grp['ГРП?'] = no_grp.apply(
                lambda x:
                0 if 'ГРП' not in str(x['ГС/ННС'])
                else 1, axis=1)
            no_grp = no_grp.drop(no_grp[no_grp['ГРП?'] == 1].index)
            spisok = no_grp['для_грп'].tolist()
            step = data.groupby('для_грп').agg(
                {date_column_name: lambda x:
                x.tolist()[0]
                }
            )
            step.reset_index(inplace=True)
            step = step[~step['для_грп'].isin(spisok)].reset_index(drop=True)
            vvv = step['для_грп'].tolist()

            step['Скважина №'] = vvv
            step = step.drop(['для_грп'], axis=1)
            dummy = dummy.merge(step, on=target, how='left')
            if dummy.shape[0] != 0:
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

            dummy2 = dummy[dummy['Забойное давление (ТР), атм'].isna()]
            dummy2 = dummy2.groupby('Скважина №').agg(
                {'Index': lambda x:
                x.tolist()})
            dummy2['забойки'] = dummy2.apply(lambda x: len(x['Index']), axis=1)
            dummy2 = dummy2.drop(dummy2[dummy2['забойки'] < 3].index)
            # wells_del_both=dummy1['Index'].tolist()
            delete_wellbore = []
            for i in dummy2['Index']:
                delete_wellbore += i
            dummy = dummy[~dummy['Index'].isin(delete_wellbore)].reset_index(drop=True)

            dummy = dummy.drop(dummy[dummy['Дебит нефти, т/сут'] == 0].index)
            #n = 1
            #z = dummy['Пласт'].value_counts()[:n].index.tolist()
            #plast = str(z[0])
            plast = ui.lineEdit.text()
            dummy = dummy.drop(dummy[dummy['Пласт'] != plast].index).reset_index(
                drop=True)
            dummy_res_zero = dummy.drop(dummy[dummy['Пластовое давление (ТР), атм'] != 0].index)
            dummy_res_zero = dummy_res_zero.groupby('Скважина №').agg(
                {'Index': lambda x:
                x.tolist()})
            dummy_res_zero['нули_пласт'] = dummy_res_zero.apply(lambda x: len(x['Index']), axis=1)
            dummy_res_zero = dummy_res_zero.drop(dummy_res_zero[dummy_res_zero['нули_пласт'] < 3].index)
            # wells_del_both=dummy1['Index'].tolist()
            delete_reservoir = []
            for i in dummy_res_zero['Index']:
                delete_reservoir += i
            dummy = dummy[~dummy['Index'].isin(delete_reservoir)].reset_index(drop=True)

            dummy_bore_zero = dummy.drop(dummy[dummy['Забойное давление (ТР), атм'] != 0].index)
            dummy_bore_zero = dummy_bore_zero.groupby('Скважина №').agg(
                {'Index': lambda x:
                x.tolist()})
            dummy_bore_zero['нули_заб'] = dummy_bore_zero.apply(lambda x: len(x['Index']), axis=1)
            dummy_bore_zero = dummy_bore_zero.drop(dummy_bore_zero[dummy_bore_zero['нули_заб'] < 3].index)
            # wells_del_both=dummy1['Index'].tolist()
            delete_bore = []
            for i in dummy_bore_zero['Index']:
                delete_bore += i
            dummy = dummy[~dummy['Index'].isin(delete_bore)].reset_index(drop=True)

            dummy_40 = dummy[dummy['Пластовое давление (ТР), атм'].isna()]
            dummy_40 = dummy_40.groupby('Скважина №').agg(
                {'Index': lambda x:
                x.tolist()})
            dummy_40['na_пласт'] = dummy_40.apply(lambda x: len(x['Index']), axis=1)
            dummy_40 = dummy_40.drop(dummy_40[dummy_40['na_пласт'] < 3].index)
            # wells_del_both=dummy1['Index'].tolist()
            del_plast = []
            for i in dummy_40['Index']:
                del_plast += i
            dummy = dummy[~dummy['Index'].isin(del_plast)].reset_index(drop=True)

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
            dummy["Забойное давление (ТР), атм"] = dummy["Забойное давление (ТР), атм"].replace(0, np.nan).bfill()
            dummy['депрессия'] = dummy.apply(
                lambda x:
                x['Пластовое давление (ТР), атм'] - x['Забойное давление (ТР), атм'], axis=1)
            dummy = dummy.drop(dummy[dummy['депрессия'] <= 0].index)
            dummy = dummy.drop('депрессия', axis=1)

        ui.pushButton_4.clicked.connect(sub_zero_pressure)

    def export_final():
        global dummy
        dummy = dummy.drop(['Index'], axis=1)
        dummy.to_excel('MER_new.xlsx')
        print('yep')

    ui.pushButton_5.clicked.connect(export_final)


ui.pushButton.clicked.connect(open_second_window)


sys.exit(app.exec_())
