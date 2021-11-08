#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import datetime

data = pd.read_excel('TYLE.xlsx', sheet_name='ГРП')
dummy = pd.read_excel('TYLE.xlsx', sheet_name='МЭР')


# In[2]:


date_column_name = r'Дата ВНР после ГС \\ ГРП \\ЗБГС'
target = 'Скважина №'


# In[3]:


#составляю список скважин с историей большей или равной 6 месяцев
dummy1 = dummy.groupby(target).agg(
    {'Дата': lambda x: 
     x.tolist()}
)
dummy1['История'] = dummy1.apply(
    lambda x: 
    1 if len(x['Дата'])>=6
    else 0, axis=1)
dummy1 = dummy1.drop(dummy1[dummy1['История'] != 1].index)
dummy1.reset_index(inplace=True)
a=dummy1['Скважина №'].tolist()
a


# In[4]:


#удаляю те, которых нет в полученном списке
dummy=dummy[dummy['Скважина №'].isin(a)]
dummy


# In[5]:


step = data.groupby(target).agg(
    {date_column_name: lambda x: 
     x.tolist()[0] 
     if len(x.tolist()) == 1 else x.tolist()[1]}
)
step


# In[6]:


dums = dummy.merge(step, on=target)


# In[7]:


dums.head(10)


# In[8]:


dums[target] = dums.apply(
    lambda x: 
    str(x[target])
    + ('_ГРП' if x['Дата'] > x[date_column_name] else ''),
    axis=1
)
sheet_2 = dums.drop(date_column_name, axis=1)


# In[9]:


sheet_2.head(10)


# In[10]:


#удаляем стоки с нулевым дебитом нефти
sheet_2 = sheet_2.drop(sheet_2[sheet_2['Дебит нефти, т/сут'] == 0].index)
sheet_2


# In[18]:


#если нулевое пластовое давление, то беру предыдущее значение
sheet_2['Пластовое давление (ТР), атм'] = sheet_2.apply(
    lambda x: 
    sheet_2['Пластовое давление (ТР), атм'].shift() if x['Пластовое давление (ТР), атм']==0 else x['Пластовое давление (ТР), атм'],
    axis=1
)

sheet_2


# In[11]:


sheet_2.to_excel('tyle3333.xlsx')

