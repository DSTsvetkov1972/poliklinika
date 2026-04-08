from datetime import datetime
import pandas as pd
from package.processors import fio_splitter, is_date

df = pd.read_excel('aaa.xls', header=None, sheet_name='О1')


df[6] = df[0].apply(lambda x: x[-88:-78] if 'просит Вас снять с' in str(x) and is_date(x[-88:-78]) else None)
df[6] = df[6].ffill()

df[7] = df[4].apply(lambda x: is_date(x))
df = df[df[7]]

print(list([type(col) for col in df.columns]))

df.rename(columns={1:'Фамилия', 2:'Имя', 3:'Отчество', 4:'Дата рождения', 5:'Номер полиса', 6:'Дата открепления'}, inplace=True)
df = df[["Номер полиса", "Дата открепления", "Дата рождения", "Фамилия", "Имя", "Отчество"]]
df.to_excel('bbb.xlsx')