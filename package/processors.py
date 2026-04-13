import pandas as pd
import os, shutil
from datetime import datetime
# from config import folders_rules_dict
from colorama import Fore


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

    if whitespace_qty == 3 and fio[-4:] in ['кызы', 'оглы'] :
        return {
            'surname': fio_parts[0],
            'name': fio_parts[1],
            'patronymic': ' '.join(fio_parts[2:])}

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
        raise ValueError(f'Строка с ФИО "{ fio }" должна содержать 1 или 2 пробела или 3 пробела и оканчиваться на "кызы" или "оглы". По факту: { whitespace_qty }')


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
    

def soglasie_otkrep(folder, file, folders_rules_dict):
    

    try:
        file_path = os.path.join(os.getcwd(), 'Исходники', folder, file)
        df = pd.read_excel(file_path, header=None, sheet_name=folders_rules_dict[folder]['sheet_name'])

        df[4] = df[3].apply(lambda x: is_date(x))


        df[5] = df[2].apply(lambda x: x if is_date(x) else None)
        df[5] = df[5].ffill()

        df = df[df[4]]


        df['Фамилия'] = df[2].apply(lambda x: fio_splitter(x)['surname'])
        df['Имя'] = df[2].apply(lambda x: fio_splitter(x)['name'])
        df['Отчество'] = df[2].apply(lambda x: fio_splitter(x)['patronymic'])


        df.columns= [0, "Номер полиса", 2, "Дата рождения", 4, "Дата открепления", "Фамилия", "Имя", "Отчество"]
        df = df[["Номер полиса", "Дата открепления", "Дата рождения", "Фамилия", "Имя", "Отчество"]]
        df['Папка'] = folder
        df['Файл'] = file
        return (True, df)
    except Exception as e:
        return(False, str(e))


def renessans_otkrep(folder, file, folders_rules_dict):
    

    try:
        file_path = os.path.join(os.getcwd(), 'Исходники', folder, file)
        df = pd.read_excel(file_path, header=None, sheet_name=folders_rules_dict[folder]['sheet_name'])

        df[6] = df[0].apply(lambda x: x[-88:-78] if 'просит Вас снять с' in str(x) and is_date(x[-88:-78]) else None)
        df[6] = df[6].ffill()

        df[7] = df[4].apply(lambda x: is_date(x))
        df = df[df[7]]

        df.rename(columns={1:'Фамилия', 2:'Имя', 3:'Отчество', 4:'Дата рождения', 5:'Номер полиса', 6:'Дата открепления'}, inplace=True)
        df = df[["Номер полиса", "Дата открепления", "Дата рождения", "Фамилия", "Имя", "Отчество"]]
        
        df['Папка'] = folder
        df['Файл'] = file
        return (True, df)
    
    except Exception as e:
        return(False, str(e))



def soglasie_otkrep(folder, file, folders_rules_dict):
    

    try:
        file_path = os.path.join(os.getcwd(), 'Исходники', folder, file)
        df = pd.read_excel(file_path, header=None, sheet_name=folders_rules_dict[folder]['sheet_name'])

        df[4] = df[3].apply(lambda x: is_date(x))


        df[5] = df[2].apply(lambda x: x if is_date(x) else None)
        df[5] = df[5].ffill()

        df = df[df[4]]


        df['Фамилия'] = df[2].apply(lambda x: fio_splitter(x)['surname'])
        df['Имя'] = df[2].apply(lambda x: fio_splitter(x)['name'])
        df['Отчество'] = df[2].apply(lambda x: fio_splitter(x)['patronymic'])


        df.columns= [0, "Номер полиса", 2, "Дата рождения", 4, "Дата открепления", "Фамилия", "Имя", "Отчество"]
        df = df[["Номер полиса", "Дата открепления", "Дата рождения", "Фамилия", "Имя", "Отчество"]]
        df['Папка'] = folder
        df['Файл'] = file
        return (True, df)
    except Exception as e:
        return(False, str(e))




def email_base(folder, file, folders_rules_dict):
    try:
        file_path = os.path.join(os.getcwd(), 'Исходники', folder, file)
        print(folders_rules_dict[folder]['file_actions'])
        
        for k, new_folder in folders_rules_dict[folder]['file_actions'].items():
            if k in file:
                if not new_folder:
                    continue
                elif new_folder == 'trash':
                    pass
                else:
                    new_file_path = os.path.join(os.getcwd(), 'Исходники', new_folder, file)
                    shutil.move(file_path, new_file_path)

        return (True, new_folder)
    except Exception as e:
        return(False, e)




processors_dict = {
    'base': base,
    'renessans_otkrep': renessans_otkrep,
    'soglasie_otkrep': soglasie_otkrep,
    'email_base': email_base
    }


if __name__ == '__main__':
    folder = 'Альфа_Скачано'
    file = '1007_00346407_31-03-2026-20-15-21_all.xlsx'
    folders_rules_dict=folders_rules_dict
    print(email_base(folder, file, folders_rules_dict))