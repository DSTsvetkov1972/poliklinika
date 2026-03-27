import pandas as pd
import os


def base(folder, file, folders_rules_dict):
    """Предположительно самый распространенный вариант парсинга,
    когда заголовок всегда в одной и той же строке,
    заголовок всегда соответсвует шаблону,
    таблица содержит все строки с непустым значением в
    заданной колонке    
    """
    try:
        skiprows=folders_rules_dict[folder]['skiprows']
        filter_not_empty_column = folders_rules_dict[folder]['filter_not_empty']
        source_header = folders_rules_dict[folder]['source_header']

        df = pd.read_excel(os.path.join('Исходники',folder, file), skiprows=skiprows)
        
        df_columns = list(df.columns)
        if source_header==df_columns:
            df = df .fillna('')
            df = df[df[filter_not_empty_column]!='']
            df['Папка'] = folder
            df['Файл'] = file

            if df.empty:
                return(False, 'Пустая таблица') 
            else:    
                return (True, df)
        else:
            return (False,
                    f"В файле заголовок:\n"
                    f"{ df_columns }\n"
                    f"Ожидалось:\n"
                    f"{ source_header }")
    except Exception as e:
        return(False, str(e))
    

processors_dict = {'base': base}