import pandas as pd
import os, sys, shutil
sys.path.append(os.getcwd())
import re
from datetime import datetime
from package.config import folders_rules_dict
from colorama import Fore
from openpyxl import load_workbook


def email_by_file_name(folder, file, folders_rules_dict):
    try:
        file_path = os.path.join(os.getcwd(), 'Исходники', folder, file)
        # print(folders_rules_dict[folder]['file_actions'])
        
        for file_rule in folders_rules_dict[folder]['file_rules']:
            if re.search(file_rule['pattern'], file):
                if file_rule['target_folder'] == 'удалён':
                    # Удаляем файл
                    return (True, file_rule['target_folder'])
                elif file_rule['target_folder'] :
                    new_file_path = os.path.join(os.getcwd(), 'Исходники', file_rule['target_folder'], file)
                    shutil.move(file_path, new_file_path)
                    return (True, file_rule['target_folder'])
        return (True, 'Не установлены правила обработки файла')
            
    except Exception as e:
        return(False, e)


def email_by_cell_value(folder, file, folders_rules_dict):
    if file[-4:] not in ['.xls', 'xlsx']:
        return (True, 'Не установлены правила обработки файла')
    
    try:
        file_path = os.path.join(os.getcwd(), 'Исходники', folder, file)
        wb = load_workbook(file_path, data_only=True)
        
        for file_rule in folders_rules_dict[folder]['file_rules']:
            if file_rule['sheet_name'] not in wb.sheetnames:
                continue
            
            else:
                ws = wb[file_rule['sheet_name']]
                if ws[file_rule['cell']].value == file_rule['value']:
                    new_file_path = os.path.join(os.getcwd(), 'Исходники', file_rule['target_folder'], file)
                    shutil.move(file_path, new_file_path)
                    return (True, file_rule['target_folder'])
        
        return (True, 'Не установлены правила обработки файла')    

    except Exception as e:
        return(False, e)



separators_dict = {
    'email_by_file_name': email_by_file_name,
    'email_by_cell_value': email_by_cell_value
    }


if __name__ == '__main__':
    folder = 'СОГЛАСИЕ_Скачано'
    file = '2501343.xlsx'
    folders_rules_dict=folders_rules_dict
    print(email_by_cell_value(folder, file, folders_rules_dict))