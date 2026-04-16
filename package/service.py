import pyperclip
import os
from colorama import Fore

def open_file():
    path = None
    try:
        clipboard = pyperclip.paste()
        clipboard_parts = clipboard.replace('\r\n', '').split('\t')
        folder = clipboard_parts[0]
        folder_parts = folder.split('_')

        file = clipboard_parts[1]

        for folder_1 in ['Открепление', 'Прикрепление', 'Скачано', 'Изменение']:
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