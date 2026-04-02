
from colorama import Fore, init
import pandas as pd
import os
from package.config import folders_rules_dict, folders_maker
from package.logo import logo_colored
from package.sources_and_files import sources_and_prepared_summary
from package.download_to_pickomed import prepared_maker
from package.confirm_download import get_files_to_confirm, check_opened_files_to_confirm, confirm_files


from colorama import Fore, Style, init

init()
print(Style.BRIGHT)
print(logo_colored)

folders_maker(folders_rules_dict)
    
while True:
    try:
        print()
        print(Fore.BLUE, '1 - получить сводку по исходниками и подготовленным к загрузке', Fore.RESET)
        print(Fore.BLUE, '2 - подготовить файлы для загрузки в Пикомед', Fore.RESET)
        print(Fore.BLUE, '3 - подтвердить загрузку файлов в Пикомед', Fore.RESET)
        choise = input("Ваш выбор: ")

        if choise == '1':

            if sources_and_prepared_summary():
                print(Fore.GREEN, 'Файл "Исходники и подготовленные.xlsx" сформирован и открыт на рабочем столе.', Fore.RESET)
            else:
                print(Fore.RED, 'Файл "Исходники и подготовленные.xlsx" уже открыт на рабочем столе. Закройте его и повторите попытку.', Fore.RESET)                
            os.startfile('Исходники и подготовленные.xlsx')

        elif choise == '2':
            prepared_maker_res = prepared_maker()
            if prepared_maker_res[0]:
                print(Fore.GREEN, 'Файл "Сводка по подготовке файлов к загрузке.xlsx" сформирован и открыт на рабочем столе.', Fore.RESET)
                os.startfile('Сводка по подготовке файлов к загрузке.xlsx')    
            else:
                if '[Errno 13] Permission denied:' in prepared_maker_res[1]:
                    print(Fore.RED, 'Файл "Сводка по подготовке файлов к загрузке.xlsx" уже открыт на рабочем столе. Закройте его и повторите попытку.', Fore.RESET)
                                     
                else:
                    print(Fore.RED, prepared_maker_res[1], Fore.RESET) 
                      
            
        elif choise == '3':
            files_to_confirm = get_files_to_confirm()
            check_opened_files_to_confirm_res = check_opened_files_to_confirm()
            if check_opened_files_to_confirm_res:
                print(Fore.RED, f'Закройте файлы:\n{check_opened_files_to_confirm_res}\n и повторите попытку', Fore.RESET)
                continue

            files_to_confirm = get_files_to_confirm()
            print(files_to_confirm)
            confirm_files(files_to_confirm) 


    except Exception as e:
        print(Fore.RED, str(e), Fore.RESET)






















# print(folders_rules_dict['Согаз_изменение объёма'])

   

  


#
##if __name__ == '__main__':
#    folder = 'Согаз_изменение объёма'
#    file = 'Согаз изменение объема пример.xls'
#    file_processor_res = file_processor(folder, file)
#    print(file_processor_res)

