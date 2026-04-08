import os, sys
import pandas as pd

sys.path.append(os.getcwd())

from package.config import folders_rules_dict
from package.processors import processors_dict
from openpyxl import load_workbook
from openpyxl.styles import Alignment, Font
from tqdm import tqdm
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





def prepared_maker():
    try:
        if os.path.exists(os.path.join(os.getcwd(), 'Сводка по подготовке файлов к загрузке.xlsx')):
            with open(os.path.join(os.getcwd(), 'Сводка по подготовке файлов к загрузке.xlsx'), 'r+b'):
                pass

        processor_log = []

        folders = list(os.walk('Исходники'))[0][1]

        max_folder_len = max([len(f) for f in folders])

        print(Fore.BLACK)
        for folder in folders:
            # print(Fore.MAGENTA, folder, Fore.RESET)
            files = list(os.walk(os.path.join('Исходники', folder)))[0][2]

            res_dfs = []
            
            if files:
                    
                bar = FillingSquaresBar(
                    f'{folder:>{max_folder_len}}',
                    max=len(files),
                    suffix = '%(index)d/%(max)d',
                    fill='█', empty_fill='░',
                    width = 50)    

                # for file in tqdm(files, desc=folder, unit='Файл', leave=True):
                for file in files:     
                    processor_starter_res = processor_starter(folder, file)
                    # print(file, processor_starter_res)
                    if processor_starter_res[0]:
                        res_dfs.append(processor_starter_res[1])
                        processor_log.append([folder, file, len(processor_starter_res[1])])
                    else:
                        processor_log.append([folder, file, processor_starter_res[1]])

                    if res_dfs:
                        res_df = pd.concat(res_dfs)
                        res_df.to_excel(os.path.join(os.getcwd(), 'Подготовленные', f'{ folder }.xlsx'), index=False)
                    bar.next()
                
                bar.finish()

        print(Fore.RESET)                

        log_df = pd.DataFrame(processor_log, columns=['Папка', 'Файл', 'Результат обработки'])
        log_df.to_excel('Сводка по подготовке файлов к загрузке.xlsx', index=None)
            
        wb = load_workbook('Сводка по подготовке файлов к загрузке.xlsx')

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

        wb.save('Сводка по подготовке файлов к загрузке.xlsx')
        return (True,)

    except Exception as e:
        return (False, str(e))


    

if __name__ == '__main__':
    folder = 'Согаз_изменение объёма'
    file = 'Согаз изменение объема пример.xls'
    err_list = []
    res_file_creator(folder, file, err_list)