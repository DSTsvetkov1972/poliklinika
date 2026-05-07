
import os
import sys
import sqlite3

from colorama import Fore
sys.path.append(os.getcwd())

from package.config import folders_rules_dict

def folders_maker(): 

    print(Fore.BLACK + f'Проверяем наличие нужных папок в проекте...' + Fore.RESET, end='')  
    folders_created = False

    for folder in ['Исходники', 'Подготовленные', 'Загруженные']:
        if not os.path.exists(folder):
            os.mkdir(folder)
            folders_created = True
            print(Fore.GREEN + '\nСоздали папку ' + Fore.WHITE + fr'"\{folder}"' + Fore.RESET, end='')            

    sources_folder = os.path.join(os.getcwd(), 'Исходники') 
    folders = list(os.walk(sources_folder))[0][1]

    for k in folders_rules_dict.keys():
        if k not in folders:
            os.mkdir(os.path.join(sources_folder, k))
            folders_created = True
            print(Fore.GREEN + '\nСоздали папку ' + Fore.WHITE + fr'"\Исходники\{k}"' + Fore.RESET, end = '')

    if not folders_created:
        print(Fore.GREEN + f'Ok' + Fore.RESET, end='')  

    print() 


def db_starter():
    with sqlite3.connect(os.path.join(os.getcwd(), 'project.db')) as conn:
        sql = """CREATE TABLE IF NOT EXISTS folder_category_code (
    folder TEXT,
    category TEXT,
    code TEXT,
    UNIQUE(folder, category)
);"""
        
        cur = conn.cursor()
        cur.execute(sql)

    print(Fore.BLACK + 'База соответствия кодов ПИКОМЕД...' + Fore.GREEN + 'Ok' + Fore.RESET)          

if __name__ == '__main__':
    folders_maker()