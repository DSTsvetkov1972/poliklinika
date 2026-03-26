import os
import pandas as pd
from config import folders_rules_dict
from fns.processors import fns_dict

def check_file(folder, file):
    file_path = os.path.join(os.getcwd(), 'files', folder, file)
    print(file, os.path.exists(file_path))


def file_processor(folder, file):

    folder_rules = folders_rules_dict.get(folder)
    if not folder_rules:
        return (False, f'Не созданы правила обработки для { folder }')
    
    fns_name_in_config = folder_rules.get('fns_name')
    if not fns_name_in_config:
        return (False, f'В правилах обработки не задана функция обработки для { folder }')

    fns_name = fns_dict.get(fns_name_in_config)
    if not fns_name:
        return (False, f'Функция обработки файла { fns_name_in_config } не создана')
    
    return fns_name(folder, file, folders_rules_dict)