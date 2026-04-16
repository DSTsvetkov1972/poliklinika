import pyperclip
import os
from colorama import Fore

path = None
try:
    clipboard = pyperclip.paste()
    clipboard_parts = clipboard.replace('\r\n', '').split('\t')
    folder = clipboard_parts[0]

    file = clipboard_parts[1]

    if '_Скачано' in folder:
        path = os.path.join(os.getcwd(), 'Исходники', folder, file)
        print(Fore.GREEN, path, Fore.RESET)
        if os.path.exists(path):
            os.startfile(path)
    else:
        print(Fore.RED + f'Что-то не то в буфере обмена:\n{clipboard[:150]}...' + Fore.RESET)
except Exception as e:
    print(Fore.RED + f'{e}\nЧто-то не то в буфере обмена:\n{clipboard[:150]}...' + Fore.RESET)