import pyperclip
import os, re
from colorama import Fore

def open_file():
    path = None
    try:
        clipboard = pyperclip.paste()
        #clipboard = 'РЕСО_Прикрепление_2	p41899714.xlsx'
        clipboard_parts = clipboard.replace('\r\n', '').split('\t')
        folder = clipboard_parts[0]
        folder_parts = folder.split('_')

        file = clipboard_parts[1]

        for folder_1 in ['Открепление', 'Прикрепление', 'Прикрепление_2', 'Скачано', 'Изменение']:
            supposed_folder = f'{folder_parts[0]}_{folder_1}'
            path = os.path.join(os.getcwd(), 'Исходники', supposed_folder, file)
            if os.path.exists(path):
                print(Fore.GREEN + f'Открыли:\n{file} из папки {supposed_folder}' + Fore.RESET)
                os.startfile(path)
                return
            else:
                continue
        print(Fore.RED + f'Что-то не то в буфере обмена:\n{clipboard[:150]}...' + Fore.RESET)
    except Exception as e:
        print(Fore.RED + f'Ошибка выполнения:\n{e}\nЧто-то не то в буфере обмена:\n{clipboard[:150]}...' + Fore.RESET)


def get_file_path(file_name, downloaded_folder):
    pattern_capture_1 = r'(.*)\[(\d+)\]\.(\w+)$'
    pattern_capture_2 = r'(.*)\.(\w+)$'

    
    company = downloaded_folder.split('_')[0]

    source_folders = list(os.walk(os.path.join(os.getcwd(), 'Исходники')))[0][1]
    
    company_files = []
    for folder in source_folders:
        if company in folder:
            files = list(os.walk(os.path.join(os.getcwd(), 'Исходники', folder)))[0][2]
            company_files += files

    new_file_name = file_name
    
    while True:
        if new_file_name in company_files:
            match_1 = re.match(pattern_capture_1, new_file_name)
            match_2 = re.match(pattern_capture_2, new_file_name)

            if match_1:
                path = match_1.group(1)
                number = match_1.group(2)
                extension = match_1.group(3)
                new_file_name = f"{path}[{ int(number)+1 }].{extension}"
 
            elif match_2:
                path = match_2.group(1)
                extension = match_2.group(2)
                new_file_name = f"{path}[0].{extension}"
            else:
                raise ValueError('имя файла не соответствует шаблону')
            continue
        else:
            new_file_path = os.path.join(os.getcwd(), 'Исходники', downloaded_folder, new_file_name)
            return new_file_path               

if __name__ == '__main__':
    open_file()