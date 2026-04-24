import os, sys
import pandas as pd
from datetime import datetime

sys.path.append(os.getcwd())

from package.config import folders_rules_dict
from package.processors import processors_dict
from openpyxl import load_workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter

from progress.bar import FillingSquaresBar
from colorama import Fore
import warnings

warnings.filterwarnings('ignore', category=UserWarning, module='openpyxl.styles.stylesheet')

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

        folders = [folder for folder in folders if '_Открепление' in folder or '_Прикрепление' in folder]

        max_folder_len = max([len(f) for f in folders])

        print(Fore.BLACK)
        for folder in folders:
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

                        prepared_file = os.path.join(os.getcwd(), 'Подготовленные', f'{ folder }.xlsx')
                        res_df.to_excel(prepared_file, index=False)

                        wb = load_workbook(prepared_file)
                        ws = wb.active
                        
                        ws.freeze_panes = 'A2'
                        ws.auto_filter.ref = ws.dimensions 

                        for col in range(1, ws.max_column+1):
                            header_cell = ws.cell(column=col, row=1)
                            ws.column_dimensions[get_column_letter(col)].width = 24
                            if header_cell.value in ['Дата рождения', 'Период обслуживания c', 'Период обслуживания по', 'Дата открепления']:
                                for row in range(2, ws.max_row+1):
                                    cell_to_format = ws.cell(row=row, column=col)
                                    cell_to_format.number_format = 'DD.MM.YYYY'
                                    cell_to_format.font = Font(bold=True)

                        wb.save(prepared_file)            



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

        ws.auto_filter.ref = ws.dimensions  
        #for row in range(2, ws.max_row+1):
        #    ws.cell(column=2, row=row).alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
        #    ws.cell(column=3, row=row).alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
        #    ws.cell(column=4, row=row).alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)

        wb.save('Сводка по подготовке файлов к загрузке.xlsx')
        return (True,)

    except Exception as e:
        return (False, e)


    

if __name__ == '__main__':
    folder = 'ВСК_Открепление'
    file = 'Согаз изменение объема пример.xls'
    processor_starter(folder, file)