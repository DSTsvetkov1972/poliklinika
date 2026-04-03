
import os
import sys
from colorama import Fore
sys.path.append(os.getcwd())

from package.config import folders_rules_dict

def folders_maker(): 
    folders_created = False


    print(Fore.BLUE + f'Проверяем наличие нужных папок в проекте...' + Fore.RESET, end='')  
    sources_folder = os.path.join(os.getcwd(), 'Исходники') 
    folders = list(os.walk(sources_folder))[0][1]

    for folder in ['Исходники', 'Подготовленные', 'Загруженные']:
        if not os.path.exists(folder):
            os.mkdir(folder)
            folders_created = True
            print(Fore.GREEN + '\nСоздали папку ' + Fore.WHITE + fr'"\{folder}"' + Fore.RESET, end='')            

    
    for k in folders_rules_dict.keys():
        if k not in folders:
            os.mkdir(os.path.join(sources_folder, k))
            folders_created = True
            print(Fore.GREEN + '\nСоздали папку ' + Fore.WHITE + fr'"\Исходники\{k}"' + Fore.RESET, end = '')

    if not folders_created:
        print(Fore.GREEN + f'Ok' + Fore.RESET, end='')  

    print() 
    
if __name__ == '__main__':
    folders_maker()