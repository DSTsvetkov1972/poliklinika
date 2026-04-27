import os, sys, shutil
import pandas as pd
from datetime import datetime 
sys.path.append(os.getcwd())

from package.config import folders_rules_dict
from package.processors import processors_dict
from openpyxl import load_workbook
from openpyxl.styles import Alignment, Font

from colorama import Fore

from progress.bar import FillingSquaresBar

def is_excel_file_open(filepath):
    try:
        # Попытка открыть файл для записи (режим 'rb' тоже сработает)
        # Важно: мы не используем with, чтобы закрыть файл сразу после проверки
        with open(filepath, 'r+b'):
            # Если получилось открыть — файл не заблокирован
            return False
    except (IOError, PermissionError):
        # Если вылетела ошибка доступа — файл, скорее всего, открыт в Excel
        return True
    

def get_files_to_confirm():

    files_to_confirm = {}
    files = list(os.walk(os.path.join(os.getcwd(), 'Подготовленные')))[0][2]
    
    print(Fore.BLACK)
    bar = FillingSquaresBar(
        'Читаем подготовленные файлы:',
        max=len(files),
        suffix = '%(index)d/%(max)d',
        fill='█', empty_fill='░',
        width = 50)  
    
    bar.start()
    
    for file in files:
        df = pd.read_excel(os.path.join(os.getcwd(), 'Подготовленные', file))

        files_in_file = list(df['Файл'].drop_duplicates())

        df = df.groupby('Папка').agg({
            'Файл': 'nunique',
            'Папка': 'count'
            }).rename(columns={
               'Файл': 'Файлов в подготовленном файле',
               'Папка': 'Строк в подготовленном файле'
               })
        files_qty = df['Файлов в подготовленном файле'].iloc[0]
        rows_qty = df['Строк в подготовленном файле'].iloc[0]
        backup_file_name = f"{ file[:-5]}_{ datetime.now().strftime("%Y-%m-%d %H-%M-%S")}_файлов { files_qty }_строк { rows_qty}.xlsx"

        files_to_confirm[file] = {'files_in_file': files_in_file,
                                  'backup_file_name': backup_file_name}
        
        bar.next()
    
    print(Fore.RESET)    
    bar.finish()
    return files_to_confirm


def check_opened_files_to_confirm():


    prepared_files = list(os.walk(os.path.join(os.getcwd(), 'Подготовленные')))[0][2]
    prepared_opened_files = [f"Подготовленные\\{ prepared_file[2:] }" for prepared_file in prepared_files if prepared_file[:2] == '~$']

    source_folders = list(os.walk(os.path.join(os.getcwd(), 'Исходники')))[0][1]
    source_opened_files = []
    for source_folder in source_folders:
        # print(source_folder)
        source_folder_path = os.path.join(os.getcwd(), 'Исходники', source_folder)
        source_files = list(os.walk(source_folder_path))[0][2]
        # print(source_files)
        source_opened_files_in_folder = []
        
        for source_file in source_files:
            if source_file[:2] == '~$':
                continue

            sorce_file_path = os.path.join(source_folder_path, source_file)
            if is_excel_file_open(sorce_file_path):
                source_opened_files_in_folder.append(f"Исходники\\{ source_folder }\\{ source_file }")
        # print(source_opened_files_in_folder)

        source_opened_files += source_opened_files_in_folder

    #print(Fore.YELLOW, source_opened_files, Fore.RESET)
        
    opened_files = prepared_opened_files+source_opened_files    
    #print(Fore.RED, opened_files, Fore.RESET)
    opened_files_str = "\n".join(opened_files)

    
    return opened_files_str


def confirm_files(files_to_confirm):
    
    confirm_files_qty = 0
  

    for downloaded_file, downloaded_file_data in files_to_confirm.items():
        downloaded_folder = downloaded_file[:-5]
        for source_file in downloaded_file_data['files_in_file']:
            source_file_path = os.path.join(os.getcwd(), 'Исходники', downloaded_folder, source_file)
            os.remove(source_file_path)

        downloaded_file_path = os.path.join(os.getcwd(), 'Подготовленные', downloaded_file)
        backup_file_path = os.path.join(os.getcwd(), 'Загруженные', downloaded_file_data['backup_file_name'])
        shutil.move(downloaded_file_path, backup_file_path)
        confirm_files_qty += len(downloaded_file_data['files_in_file'])
          
    return confirm_files_qty
        
        

if __name__ == '__main__':
    print(check_opened_files_to_confirm())
    files_to_confirm = get_files_to_confirm()
    print(files_to_confirm)
    confirm_files(files_to_confirm)

