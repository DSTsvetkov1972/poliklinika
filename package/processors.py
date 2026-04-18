import pandas as pd
import os, sys, shutil
import pandas as pd
from datetime import datetime
from pprint import pprint

sys.path.append(os.getcwd())
from package.config import folders_rules_dict
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

    fio = fio.strip()
    whitespace_qty = fio.count(' ')

    fio_parts = fio.split(' ')

    if whitespace_qty == 3 and fio[-4:].lower() in ['кызы', 'оглы'] :
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
        
        source_header = folders_rules_dict[folder]['source_header']

        df = pd.read_excel(os.path.join('Исходники',folder, file), header=None, index_col=None)
        if df.empty:
            return(False, 'Пустой исходный файл') 
        
        df = df.fillna('')
        df_columns = df.iloc[header_row-1].tolist()



        if source_header == df_columns:
            df = df.iloc[header_row:]
            df.columns = df_columns
        

            filter_not_in_column = folders_rules_dict[folder]['filter_not_in']['column']
            if filter_not_in_column not in df_columns:
                return(False, f'Нет колонки "{ filter_not_in_column }" по которой задана фильтрация')             

            #
            for condition in folders_rules_dict[folder]['filter_not_in']['conditions']:
                df = df[df[filter_not_in_column]!=condition]                                                # Колонка не должна быть пустой и
                                                                                                            # не содержать значение равное
                                                                                                            # имени колонки. 
                                                                                                            # Так сделано на случай, если на листе
                                                                                                            # несколько таблиц с одинаковыми заголовками    

            if df.empty:
                return(False, 'Пустая таблица') 
            else:
                #pprint(folders_rules_dict[folder]['result_columns'])
                res_df = pd.DataFrame()                                                                                                

                for result_column_dict in folders_rules_dict[folder]['result_columns']:
                    #print(result_column_dict)
                    target_column  = result_column_dict['target_column']
                    source_column_name = result_column_dict['source_column_name']

                    if result_column_dict['source_type'] == 'column':
                        res_df[target_column] = df[source_column_name]
                    elif result_column_dict['source_type'] == 'surname_from_column':
                        res_df[target_column] = df[source_column_name].apply(lambda fio: fio_splitter(fio)['surname'])
                    elif result_column_dict['source_type'] == 'name_from_column':
                        res_df[target_column] = df[source_column_name].apply(lambda fio: fio_splitter(fio)['name'])
                    elif result_column_dict['source_type'] == 'patronymic_from_column':                                                
                        res_df[target_column] = df[source_column_name].apply(lambda fio: fio_splitter(fio)['patronymic'])
                    elif result_column_dict['source_type'] == 'dict':                                                
                        res_df[target_column] = df[source_column_name].apply(lambda k: result_column_dict['dict'][k])                            

                res_df['Папка'] = folder
                res_df['Файл'] = file        
                return (True, res_df)

                    
        else:
            return (False,
                    f"В файле заголовок:\n"
                    f"{ df_columns }\n"
                    f"Ожидалось:\n"
                    f"{ source_header }")

    except Exception as e:
        return(False, repr(e))
    

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
        return(False, e)


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
        return(False, e)


def zetta_prikrep_conditions(shifted_1, shifted_3):

    if shifted_1 == 'npp' and 'Программа' in shifted_3:
        return(shifted_3)
    elif shifted_1 == 'npp' and 'Программа' not in shifted_3:
        raise KeyError('Неожиданная структура файла. Не возможно считать программу страхования')
    else:
        None
        


def zetta_prikrep(folder, file, folders_rules_dict):

    file_path = os.path.join(os.getcwd(), "Исходники", folder, file)
    header_row = 17
    source_header = [
        "", "№ ", "Фамилия", "Имя", "Отчество", "№ ИБ", "Дата рождения", "Пол \n(муж,\nжен)", "№ Полиса",
        "Серия полиса", "Домашний адрес", "Телефон", "Категория", "Место работы", "Дата прикр.", "Дата откр."
        ]
    codes_dict = folders_rules_dict[folder]['dict']
    
    # if True:
    try:
        df = pd.read_excel(file_path, header=None)
        df = df.fillna('')
        df_columns = list(df.iloc[header_row])
        
        if df_columns != source_header:
            return (False,
                    f"В файле заголовок:\n"
                    f"{ df_columns }\n"
                    f"Ожидалось:\n"
                    f"{ source_header }")
        
        df.columns = df_columns

        df['shifted_1'] = df['№ '].shift(1)
        df['shifted_3'] = df['№ '].shift(3)
        
        df = df[(df['Дата прикр.'] != "")&(df['Дата прикр.'] != "Дата прикр.") & (df['Дата прикр.'] != "BEGIN")]

        df['по программе'] = df.apply(lambda x: zetta_prikrep_conditions(x['shifted_1'], x['shifted_3']), axis=1)
        df['по программе'] = df['по программе'].ffill()

        df=df[["Дата прикр.", "Дата откр.", "Дата рождения", "Фамилия", "Имя", "Отчество", "по программе"]]
        df=df.rename(
            columns={
                "Дата прикр.": "Период обслуживания c",
                "Дата откр.": "Период обслуживания по",
                "DATE": "Дата рождения",
                "Фамилия": "Фамилия",
                "Имя": "Имя",
                "Отчество": "Отчество",
                "по программе": "Вид медицинского обслуживания" 
                })
        df['Код ПИКОМЕД'] = df['Вид медицинского обслуживания'].apply(lambda k: codes_dict[k])
        df['Папка'] = folder
        df['Файл'] = file

        return (True, df)

    except Exception as e:
        return (False, repr(e))
    




def reso_prikrep_2_conditions(npp_shifted_1, npp_shifted_2, NAME2_shifted_2):

    if npp_shifted_1 == 'npp' and npp_shifted_2 == 'по программе' and NAME2_shifted_2 != '':
        return(NAME2_shifted_2)
    elif npp_shifted_1 == 'npp' and (npp_shifted_2 != 'по программе' or NAME2_shifted_2 == ''):
        raise KeyError('не возможно считать программу страхования')
    else:
        None


def reso_prikrep_2(folder, file, folders_rules_dict):
    codes_dict = folders_rules_dict[folder]['dict']
        
    try:
    
        expected_columns = ['npp', 'NAME1', 'NAME2', 'NAME3', 'NIB', 'DATE', 'SEX', 'POLIC', 'POLIC SER', 'ADDRESS P', 'TEL1', 'KATEGORY ', 'PLACE', 'BEGIN', 'END']
        file_path = os.path.join(os.getcwd(), "Исходники", "РЕСО_Прикрепление_2", file)

        df = pd.read_excel(file_path, header=None)
        df =df.fillna('')
        df_columns = list(df.iloc[7])
        
        if df_columns != expected_columns:
            return (False,
                    f"В файле заголовок:\n"
                    f"{ df_columns }\n"
                    f"Ожидалось:\n"
                    f"{ expected_columns }")
        
        df.columns = df_columns

        df['npp_shifted_1'] = df['npp'].shift(1)
        df['npp_shifted_2'] = df['npp'].shift(2)        
        df['NAME2_shifted_2']  =df['NAME2'].shift(2)
        df = df[(df['NAME1']!='')&(df['NAME1']!='NAME1')]
        df['по программе'] = df.apply(lambda x: reso_prikrep_2_conditions(x['npp_shifted_1'], x['npp_shifted_2'], x['NAME2_shifted_2']), axis=1)
        df['по программе'] = df['по программе'].ffill()
        df =df.fillna('')
        df=df[['BEGIN', 'END', 'DATE', 'NAME1', 'NAME2', 'NAME3', 'по программе']]
        df=df.rename(
            columns={
                'BEGIN': 'Период обслуживания c',
                'END': 'Период обслуживания по',
                'DATE': 'Дата рождения',
                'NAME1': 'Фамилия',
                'NAME2': 'Имя',
                'NAME3': 'Отчество',
                'по программе': 'Вид медицинского обслуживания' 
                })
        df['Код ПИКОМЕД'] = df['Вид медицинского обслуживания'].apply(lambda k: codes_dict[k])
        df['Папка'] = folder
        df['Файл'] = file

        return (True, df)

    except Exception as e:
        return (False, repr(e))
    


processors_dict = {
    'base': base,
    'renessans_otkrep': renessans_otkrep,
    'soglasie_otkrep': soglasie_otkrep,
    'zetta_prikrep': zetta_prikrep,
    'reso_prikrep_2': reso_prikrep_2
    }
   
if __name__ == '__main__':
    #folder, file = 'РЕСО_Прикрепление', 'p41894408.xlsx'
    folder, file = 'ЗЕТТА_Прикрепление', '220_ММВП-210022737_(66004-66004)(1)(4770135).xlsx'
    print(Fore.MAGENTA)
    (zetta_prikrep(folder, file , folders_rules_dict))


    print(Fore.CYAN)
    folder, file = 'ЗЕТТА_Прикрепление', '220_ММВП-210022737_(74677-74754)(2)(4795856).xlsx'

    (zetta_prikrep(folder, file , folders_rules_dict))

    print(Fore.RESET)









     