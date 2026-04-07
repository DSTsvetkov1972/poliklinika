import pandas as pd






df = pd.DataFrame([{'fio': 'Цвектков Дмитрий Сергеевич'}, {'fio': 'Буль оглы кизы Мухамед Ибрагимович'}, {'fio': 'Петрос Иванович Кузьмин'}])

df['name'] = df['fio'].apply(lambda x: ' '.join(x.split(' ')[:-2]))
print(df)