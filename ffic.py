
from colorama import Fore, init
import pandas as pd
import os
from package.project_starter import folders_maker
from package.config import folders_rules_dict
from package.logo import logo_colored
from package.summary import summary
from package.separator import separator
from package.prepare import prepared_maker
from package.confirm import get_files_to_confirm, check_opened_files_to_confirm, confirm_files


from colorama import Fore, Style, init

init()
print(Style.BRIGHT)
print(logo_colored)

folders_maker()
    
while True:
    try:
        print()
        print(Fore.WHITE + '0' + Fore.BLUE + ' - получить сводку по исходникам и подготовленным к загрузке' + Fore.RESET)
        # print(Fore.WHITE + '1' + Fore.BLUE + ' - скачать вложения из писем электронной почты' + Fore.RESET)
        print(Fore.WHITE + '2' + Fore.BLUE + ' - разобрать скаченные вложения по папкам' + Fore.RESET)                
        print(Fore.WHITE + '3' + Fore.BLUE + ' - подготовить файлы для загрузки в Пикомед' + Fore.RESET)
        print(Fore.WHITE + '4' + Fore.BLUE + ' - подтвердить загрузку файлов в Пикомед' + Fore.RESET)
        
        choise = input("Ваш выбор: ")


        if choise == '0':
            if summary():
                print(Fore.GREEN + 'Файл "Исходники и подготовленные.xlsx" сформирован и открыт на рабочем столе.' + Fore.RESET)
            else:
                print(Fore.RED + 'Файл "Исходники и подготовленные.xlsx" уже открыт на рабочем столе. Закройте его и повторите попытку.' + Fore.RESET)                
            os.startfile('Исходники и подготовленные.xlsx')
        elif choise == '2':

            if os.path.exists(os.path.join(os.getcwd(), "~$Сводка по распределению файлов.xlsx")):
                print(Fore.RED + 'Файл "Сводка по распределению файлов.xlsx" уже открыт на рабочем столе. Закройте его и повторите попытку.' + Fore.RESET)                
                os.startfile('Сводка по распределению файлов.xlsx')
                continue

            separator()
            print(Fore.GREEN + 'Файл "Сводка по распределению файлов.xlsx" сформирован и открыт на рабочем столе.' + Fore.RESET)
            os.startfile('Сводка по распределению файлов.xlsx')
        
        elif choise == '3':
            prepared_maker_res = prepared_maker()
            if prepared_maker_res[0]:
                print(Fore.GREEN + 'Файл "Сводка по подготовке файлов к загрузке.xlsx" сформирован и открыт на рабочем столе.' + Fore.RESET)
                os.startfile('Сводка по подготовке файлов к загрузке.xlsx')    
            else:
                if '[Errno 13] Permission denied:' in prepared_maker_res[1]:
                    print(Fore.RED + 'Файл "Сводка по подготовке файлов к загрузке.xlsx" уже открыт на рабочем столе. Закройте его и повторите попытку.' + Fore.RESET)
                                     
                else:
                    print(Fore.RED + prepared_maker_res[1], Fore.RESET) 
                      
            
        elif choise == '4':
            check_opened_files_to_confirm_res = check_opened_files_to_confirm()
            if check_opened_files_to_confirm_res:
                print(Fore.RED + f'Закройте файлы:\n{check_opened_files_to_confirm_res}\n и повторите попытку' + Fore.RESET)
                continue

            files_to_confirm = get_files_to_confirm()
            confirmed_files_qty = confirm_files(files_to_confirm)
            print(Fore.GREEN + f'Подтверждена загрузка файлов: { confirmed_files_qty }' + Fore.RESET)
             


    except Exception as e:
        print(Fore.RED, str(e), Fore.RESET)






















# print(folders_rules_dict['Согаз_изменение объёма'])

   

  


#
##if __name__ == '__main__':
#    folder = 'Согаз_изменение объёма'
#    file = 'Согаз изменение объема пример.xls'
#    file_processor_res = file_processor(folder, file)
#    print(file_processor_res)

