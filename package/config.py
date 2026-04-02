import os
from colorama import Fore

def folders_maker(folders_rules_dict): 

    print(Fore.BLUE, f'Проверяем папки в папке "Исходники"...', Fore.RESET)  
    sources_folder = os.path.join(os.getcwd(), 'Исходники') 
    folders = list(os.walk(sources_folder))[0][1]

    
    for k in folders_rules_dict.keys():
        if k not in folders:
            print(Fore.GREEN, f'Создали папку "{k}"', Fore.RESET)
            os.mkdir(os.path.join(sources_folder, k))




folders_rules_dict = {
    "Тест": {
        "processor_name": "base",
        "skiprows": 21,
        "filter_not_empty": "Фамилия",
        "source_header": [
            "№ п/п", "Фамилия", "Имя", "Отчество", "Дата рождения", "№ полиса", "Пол", "Прежний объем обслуживания", "Новый объем обслуживания",
            "Дата начала обслуживания","Дата окончания обслуживания","Место работы (Страхователь)"
        ],
        "result_columns": {
            "aaa": {
                "source": "column", "value": "aaaaaaaa"
            },
            "adfsdfsdafasdaa": {
                "source": "default_value", "value": "45.7"
            }            
        }
    }
}