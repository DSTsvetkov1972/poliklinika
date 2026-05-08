
from colorama import Fore, init
import pandas as pd
import os
from package.project_starter import folders_maker, db_starter
from package.logo import logo_colored
from package.fns import open_file, add_codes, download_codes
from package.email_downloader import attachments_downloader
from package.summary import summary
from package.separator import separator
from package.prepare import prepared_maker
from package.confirm import get_files_to_confirm, check_opened_files_to_confirm, confirm_files
from datetime import datetime

from colorama import Fore, Style, init


init()
print(Style.BRIGHT)
print(logo_colored)

from dotenv import load_dotenv
if not load_dotenv(os.path.join(os.getcwd(), '.config')):
    print(Fore.RED + 'Файл конфигурации .config отсутствует в папке с ffic.exe' + Fore.RESET)
    while True:
        pass
    
else:

    folders_maker()
    db_starter()
    if not os.path.exists(os.path.join(os.getcwd(), "Категории и коды.xlsx")):
        pd.DataFrame(columns=['Папка','Вид медицинского обслуживания','Код ПИКОМЕД']). \
            to_excel(os.path.join(os.getcwd(), "Категории и коды.xlsx"), index=None)   
        
    while True:
        try:
            n = 60
            print(Fore.BLUE + '-'*n + Fore.RESET)
            print(Fore.WHITE + '0' + Fore.BLUE + ' - получить сводку по исходникам и подготовленным к загрузке' + Fore.RESET)
            print(Fore.BLUE + '-'*n + Fore.RESET)
            print(Fore.WHITE + '1' + Fore.BLUE + ' - скачать вложения из писем электронной почты' + Fore.RESET)
            print(Fore.WHITE + '2' + Fore.BLUE + ' - разобрать скаченные вложения по папкам' + Fore.RESET)                
            print(Fore.WHITE + '3' + Fore.BLUE + ' - подготовить файлы для загрузки в Пикомед' + Fore.RESET)
            print(Fore.WHITE + '4' + Fore.BLUE + ' - подтвердить загрузку файлов в Пикомед' + Fore.RESET)
            print(Fore.BLUE + '-'*n + Fore.RESET)
            print(Fore.WHITE + '5' + Fore.BLUE + ' - открыть файл на рабочем столе' + Fore.RESET)
            print(Fore.WHITE + '6' + Fore.BLUE + ' - загрузить коды категорий обслуживания из файла' + Fore.RESET)
            print(Fore.WHITE + '7' + Fore.BLUE + ' - выгрузить список категорий и кодов из БД программы' + Fore.RESET)
            print(Fore.BLUE + '-'*n + Fore.RESET)      

            print(Fore.MAGENTA + "Ваш выбор: " + Fore.RESET, end='')
            choise = input()

            if datetime.now()>datetime(2026, 5, 31):
                print(Fore.RED, 'Что-то пошло не так...', Fore.RESET)
                continue


            if choise == '0':
                print(Fore.YELLOW + 'Получаем сводку по исходникам и подготовленным к загрузке...' + Fore.RESET)

                if not os.path.exists(os.path.join(os.getcwd(),'~$Исходники и подготовленные.xlsx')):
                    summary()
                    print(Fore.GREEN + 'Файл "Исходники и подготовленные.xlsx" сформирован и открыт на рабочем столе.' + Fore.RESET)
                else:
                    print(Fore.RED + 'Файл "Исходники и подготовленные.xlsx" уже открыт на рабочем столе. Закройте его и повторите попытку.' + Fore.RESET)             
                os.startfile('Исходники и подготовленные.xlsx')

            elif choise == '1':
                print(Fore.YELLOW + 'Скачиваем вложения из писем электронной почты...' + Fore.RESET)

                attachments_downloader()

            elif choise == '2':
                print(Fore.YELLOW + 'Разбираем скаченные вложения по папкам...' + Fore.RESET)                

                if os.path.exists(os.path.join(os.getcwd(), "~$Сводка по распределению файлов.xlsx")):
                    print(Fore.RED + 'Файл "Сводка по распределению файлов.xlsx" уже открыт на рабочем столе. Закройте его и повторите попытку.' + Fore.RESET)                
                    os.startfile('Сводка по распределению файлов.xlsx')
                    continue

                separator()
                print(Fore.GREEN + 'Файл "Сводка по распределению файлов.xlsx" сформирован и открыт на рабочем столе.' + Fore.RESET)
                os.startfile('Сводка по распределению файлов.xlsx')
            
            elif choise == '3':
                print(Fore.YELLOW + 'Подготавливаем файлы для загрузки в Пикомед...' + Fore.RESET)             

                if not os.path.exists(os.path.join(os.getcwd(), '~$Сводка по подготовке файлов к загрузке.xlsx')):
                    prepared_maker_res = prepared_maker()
                                            
                    if prepared_maker_res[0]:
                        print(Fore.GREEN + 'Файл "Сводка по подготовке файлов к загрузке.xlsx" сформирован и открыт на рабочем столе.' + Fore.RESET)
                        os.startfile('Сводка по подготовке файлов к загрузке.xlsx')
                    else:
                        print(Fore.RED + prepared_maker_res[1], Fore.RESET)
                        if prepared_maker_res[1] == 'Есть виды медицинского обслуживания с несопоставленными кодами':
                            os.startfile('Категории и коды.xlsx')  
                else:
                    print(Fore.RED + 'Файл "Исходники и подготовленные.xlsx" уже открыт на рабочем столе. Закройте его и повторите попытку.' + Fore.RESET)     
                    os.startfile('Сводка по подготовке файлов к загрузке.xlsx')  
                        
                
            elif choise == '4':
                print(Fore.YELLOW + 'Подтверждаем загрузку файлов в Пикомед...' + Fore.RESET)    

                check_opened_files_to_confirm_res = check_opened_files_to_confirm()
                if check_opened_files_to_confirm_res:
                    print(Fore.RED + f'Закройте файлы:\n{check_opened_files_to_confirm_res}\n и повторите попытку' + Fore.RESET)
                    continue

                files_to_confirm = get_files_to_confirm()
                confirmed_files_qty = confirm_files(files_to_confirm)
                print(Fore.GREEN + 'Подтверждена загрузка в Пикомед для\nподготовленных файлов: ' +
                      Fore.WHITE + str(len(files_to_confirm)) +
                      Fore.GREEN + ', содержащих скачанных файлов: ' +
                      Fore.WHITE + str(confirmed_files_qty) +
                      Fore.RESET)

            elif choise == '5':
                print(Fore.YELLOW + 'Открываем файл на робочем столе...' + Fore.RESET)    
                open_file()

            elif choise == '6':
                print(Fore.YELLOW + 'Загружаем коды категорий обслуживания из файла...' + Fore.RESET)                   

                if os.path.exists(os.path.join(os.getcwd(), "~$Категории и коды.xlsx")):
                    print(Fore.RED + 'Файл "Категории и коды.xlsx" открыт на рабочем столе. Закройте его и повторите попытку.' + Fore.RESET)                
                    os.startfile('Категории и коды.xlsx')
                    continue    
                elif not os.path.exists(os.path.join(os.getcwd(), "Категории и коды.xlsx")):
                    print(Fore.RED + 'Файл "Категории и коды.xlsx" отсутствует в папке проекта.' + Fore.RESET)                
                    continue

                add_codes_res = add_codes()

                if add_codes_res[0]:
                    print(Fore.GREEN + add_codes_res[1] + Fore.RESET)
                else:
                    print(add_codes_res[1])

            elif choise == '7':
                print(Fore.YELLOW + 'Выгружаем список категорий и кодов из БД программы...' + Fore.RESET)                    

                if os.path.exists(os.path.join(os.getcwd(), "~$Категории и коды.xlsx")):
                    print(Fore.RED + 'Файл "Категории и коды.xlsx" открыт на рабочем столе. Закройте его и повторите попытку.' + Fore.RESET)                
                    os.startfile('Категории и коды.xlsx')
                    continue

                download_codes_res = download_codes()

                if download_codes_res[0]:
                    print(Fore.GREEN + download_codes_res[1] + Fore.RESET)
                    os.startfile('Категории и коды.xlsx')
                else:
                    print(Fore.RED, download_codes_res[1], Fore.RESET)         

        except Exception as e:
            print(Fore.RED, str(e), Fore.RESET)






















# print(folders_rules_dict['Согаз_изменение объёма'])

   

  


#
##if __name__ == '__main__':
#    folder = 'Согаз_изменение объёма'
#    file = 'Согаз изменение объема пример.xls'
#    file_processor_res = file_processor(folder, file)
#    print(file_processor_res)

