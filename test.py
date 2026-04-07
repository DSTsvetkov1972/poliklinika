from datetime import datetime
import pandas as pd
from package.processors import fio_splitter, is_date

df = pd.read_excel('aaa.xlsx', header=None, sheet_name='TDSheet')

ef = pd.ExcelFile('aaa.xlsx')
print(ef.sheet_names)

df[4] = df[3].apply(lambda x: is_date(x))


df[5] = df[2].apply(lambda x: x if is_date(x) else None)
df[5] = df[5].ffill()

df = df[df[4]]


df['Фамилия'] = df[2].apply(lambda x: fio_splitter(x)['surname'])
df['Имя'] = df[2].apply(lambda x: fio_splitter(x)['name'])
df['Отчество'] = df[2].apply(lambda x: fio_splitter(x)['patronymic'])


df.columns= [0, "Номер полиса", 2, "Дата рождения", 4, "Дата открепления", "Фамилия", "Имя", "Отчество"]
df = df[["Номер полиса", "Дата открепления", "Дата рождения", "Фамилия", "Имя", "Отчество"]]
df.to_excel('bbb.xlsx')