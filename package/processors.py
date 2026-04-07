import pandas as pd
import os
from datetime import datetime



def is_date(string, date_format="%d.%m.%Y"):
    """Проверяет, можно ли преобразовать строку в дату"""
    try:
        datetime.strptime(str(string), date_format)
        return True
    except ValueError:
        return False


def fio_splitter(fio):
    """Функция возвращает словарь с фамилией, именем и отчеством из
    строки ФИО. Если строка содержит более двух пробелов, функция выкидывает
    исключение"""

    whitespace_qty = fio.count(' ')

    fio_parts = fio.split(' ')

    if whitespace_qty == 2:
        return {
            'surname': fio_parts[0],
            'name': fio_parts[1],
            'patronymic': fio_parts[2]}
    elif whitespace_qty == 1:
        return {
            'surname': fio_parts[0],
            'name': fio_parts[1],
            'patronymic': ''}
    else:
        raise ValueError(f'Строка с ФИО "{ fio }" должна содержать 1 или 2 пробела. По факту: { whitespace_qty }')


def base(folder, file, folders_rules_dict):
    """Предположительно самый распространенный вариант парсинга,
    когда заголовок всегда в одной и той же строке,
    заголовок всегда соответсвует шаблону,
    таблица содержит все строки с непустым значением в
    заданной колонке    
    """
    try:
        header_row = folders_rules_dict[folder]['header_row']
        filter_not_empty_column = folders_rules_dict[folder]['filter_not_empty']
        source_header = folders_rules_dict[folder]['source_header']

        df = pd.read_excel(os.path.join('Исходники',folder, file), header=None, index_col=None)
        if df.empty:
            return(False, 'Пустая исходный файл') 
        
        df = df.fillna('')
        df_columns = df.iloc[header_row-1].tolist()

        if filter_not_empty_column not in df_columns:
            return(False, f'Нет колонки "{ filter_not_empty_column }" по которой задана фильтрация') 

        if source_header == df_columns:

            df = df.iloc[header_row:]
            df.columns = df_columns

            df = df[(df[filter_not_empty_column]!='')&(df[filter_not_empty_column]!=filter_not_empty_column)] # Колонка не должна быть пустой и
                                                                                                            # не содержать значение равное
                                                                                                            # имени колонки. 
                                                                                                            # Так сделано на случай, если на листе
                                                                                                            # несколько таблиц с одинаковыми заголовками    

            if df.empty:
                return(False, 'Пустая таблица') 
            else:
                res_df = pd.DataFrame()                                                                                                

                try:
                    for k, v in folders_rules_dict[folder]['result_columns'].items():
                        if v['source_type'] == 'column':
                            res_df[k] = df[v['source_column_name']]
                        elif v['source_type'] == 'surname_from_column':
                            res_df[k] = df[v['source_column_name']].apply(lambda fio: fio_splitter(fio)['surname'])
                        elif v['source_type'] == 'name_from_column':
                            res_df[k] = df[v['source_column_name']].apply(lambda fio: fio_splitter(fio)['name'])
                        elif v['source_type'] == 'patronymic_from_column':                                                
                            res_df[k] = df[v['source_column_name']].apply(lambda fio: fio_splitter(fio)['patronymic'])

                    res_df['Папка'] = folder
                    res_df['Файл'] = file        
                    return (True, res_df)
                except Exception as e:
                    return(False, str(e))
        else:
            return (False,
                    f"В файле заголовок:\n"
                    f"{ df_columns }\n"
                    f"Ожидалось:\n"
                    f"{ source_header }")
    except Exception as e:
        return(False, str(e))
    

processors_dict = {'base': base}