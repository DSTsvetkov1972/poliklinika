import pandas as pd
import os, shutil
from datetime import datetime
# from config import folders_rules_dict
from colorama import Fore


def email_base(folder, file, folders_rules_dict):
    try:
        file_path = os.path.join(os.getcwd(), 'Исходники', folder, file)
        # print(folders_rules_dict[folder]['file_actions'])
        
        for sign, new_folder in folders_rules_dict[folder]['file_actions'].items():
            if sign in file:
                if new_folder == 'удалён':
                    # Удаляем файл
                    return (True, new_folder)
                elif new_folder :
                    new_file_path = os.path.join(os.getcwd(), 'Исходники', new_folder, file)
                    shutil.move(file_path, new_file_path)
                    return (True, new_folder)
        return (True, 'Не установлены правила обработки файла')
            
    except Exception as e:
        return(False, e)




separators_dict = {
    'email_base': email_base
    }


if __name__ == '__main__':
    folder = 'Альфа_Скачано'
    file = '1007_00346407_31-03-2026-20-15-21_all.xlsx'
    folders_rules_dict=folders_rules_dict
    print(email_base(folder, file, folders_rules_dict))