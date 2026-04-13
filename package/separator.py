import os, sys
import pandas as pd

sys.path.append(os.getcwd())

from package.config import folders_rules_dict
from package.processors import processors_dict
from openpyxl import load_workbook
from openpyxl.styles import Alignment, Font
# from tqdm import tqdm
from progress.bar import FillingSquaresBar
from colorama import Fore



def processor_starter(folder, file):
    """
    """

    folder_rules = folders_rules_dict.get(folder)
    if not folder_rules:
        return (False, f'Не созданы правила обработки для { folder }')
    
    processor_name_in_config = folder_rules.get('processor_name')
    if not processor_name_in_config:
        return (False, f'В правилах обработки не задан обработчик для { folder }')

    processor = processors_dict.get(processor_name_in_config)
    if not processor:
        return (False, f'Обработчик файлов { processor_name_in_config } не создан')
    return processor(folder, file, folders_rules_dict)





def separator():
    try:
        processor_log = []

        folders = list(os.walk('Исходники'))[0][1]
        downloaded_folders = [folder for folder in folders if '_Скачано' in folder]
        
        max_folder_len = max([len(f) for f in downloaded_folders])

        print(Fore.BLACK)
        for folder in downloaded_folders:
            #print(Fore.MAGENTA, folder, Fore.RESET)
            files = list(os.walk(os.path.join('Исходники', folder)))[0][2]

                        
            if files:

                bar = FillingSquaresBar(
                    f'{folder:>{max_folder_len}}',
                    max=len(files),
                    suffix = '%(index)d/%(max)d',
                    fill='█', empty_fill='░',
                    width = 50)    


                for file in files:
                    processor_starter_res = processor_starter(folder, file)
                    processor_log.append([folder, file, processor_starter_res[1]])

                    bar.next()
                
                bar.finish()

        print(Fore.RESET)                

        log_df = pd.DataFrame(processor_log, columns=['Папка', 'Файл', 'Результат обработки'])
        log_df.to_excel('Сводка по распределению файлов.xlsx', index=None)
            
        wb = load_workbook('Сводка по распределению файлов.xlsx')

        ws = wb['Sheet1']

        ws.freeze_panes = 'A2'

        # Устанавливаем ширину для конкретной колонки
        ws.column_dimensions['A'].width = 36
        ws.column_dimensions['B'].width = 42
        ws.column_dimensions['C'].width = 64


        for col in range(1, 4):
            cell = ws.cell(column=col, row=1)
            cell.font = Font(bold=True)  # Жирный шрифт
            cell.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)  # Выравнивание по центру

        #for row in range(2, ws.max_row+1):
        #    ws.cell(column=2, row=row).alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
        #    ws.cell(column=3, row=row).alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
        #    ws.cell(column=4, row=row).alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)

        wb.save('Сводка по распределению файлов.xlsx')
        return (True,)

    except Exception as e:
        return (False, e)


    

if __name__ == '__main__':
    folder = 'Альфа_Скачано'
    file = '1007g_00346689_01-04-2026-20-16-51_1007gфв_prikr.xlsx'

    separator()