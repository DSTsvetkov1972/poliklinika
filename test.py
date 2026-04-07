import pandas as pd

header_row = 17

df = pd.read_excel('aaa.xlsx', header=None)
df = df.fillna('')

col_names = df.iloc[header_row-1].tolist()

df = df.iloc[header_row:]



df.columns = col_names

df = df[(df['Фамилия имя  отчество']!='')&(df['Фамилия имя  отчество']!='Фамилия имя  отчество')]
print(df)