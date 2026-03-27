import os, sys
import pandas as pd

sys.path.append(os.getcwd())

from package.config import folders_rules_dict
from package.processors import processors_dict

def check_file(folder, file):
    file_path = os.path.join(os.getcwd(), 'Исходники', folder, file)
    print(file, os.path.exists(file_path))


def file_processor(folder, file):
    """
    """

    folder_rules = folders_rules_dict.get(folder)
    if not folder_rules:
        return (False, f'Не созданы правила обработки для { folder }')
    
    fns_name_in_config = folder_rules.get('fns_name')
    if not fns_name_in_config:
        return (False, f'В правилах обработки не задана функция обработки для { folder }')

    fns_name = processors_dict.get(fns_name_in_config)
    if not fns_name:
        return (False, f'Функция обработки файла { fns_name_in_config } не создана')
    
    return fns_name(folder, file, folders_rules_dict)


def sources_summary():

    folders_info = []
    folders = list(os.walk(os.path.join(os.getcwd(), 'Исходники')))[0][1]
    
    for folder in folders:
        files = list(os.walk(os.path.join(os.getcwd(), 'Исходники', folder)))[0][2]
        folders_info.append([folder, len(files)])

    df = pd.DataFrame(folders_info, columns=['Папка', 'Файлов в папке'])
    return df

    

def prepared_summary():

    prepared_files = list(os.walk(os.path.join(os.getcwd(), 'Подготовленные')))[0][2]
    prepared_files_info = []

    for file in prepared_files:
        df = pd.read_excel(os.path.join(os.getcwd(), 'Подготовленные', file))
        df = df[['Папка', 'Файл']]
        df = df.drop_duplicates()
        prepared_files_info.append(df)

    total_df = pd.concat(prepared_files_info)
    total_df_grouped = pd.DataFrame(total_df.value_counts(['Папка']))
    total_df_grouped = total_df_grouped.reset_index('Папка')
    total_df_grouped.columns = ['Папка', 'Подготовленных файлов']
    return total_df_grouped

if __name__ == '__main__':
    s = sources_summary()
    p = prepared_summary()
    r = pd.merge(s, p, on='Папка', how='outer')
    r.to_excel('aaa.xlsx')
    print(r)