import os, sys
import pandas as pd
from progress.bar import FillingSquaresBar

sys.path.append(os.getcwd())

from openpyxl import load_workbook
from openpyxl.styles import Alignment, Font

from imap_tools import MailBox, AND
from package.config import IMAP_SERVER, IMAP_PORT, EMAIL, APP_PASSWORD, MARK_SEEN
from package.config import folders_rules_dict


def get_unread_messages(email_folder):
    #"""Получает количество непрочитанных писем в папке"""
    #try:
        with MailBox(IMAP_SERVER, port=IMAP_PORT).login(EMAIL, APP_PASSWORD, initial_folder='INBOX') as mailbox:

                mailbox.folder.set(email_folder)
                
                # Ищем непрочитанные письма (критерий seen=False)
                unread_messages = list(mailbox.fetch(AND(seen=False), mark_seen=False))
                
                return (True, len(unread_messages))
            
    #except socket.gaierror as e:
    #    return (True, f"get_unread_messages_from_all_folders: { e }.\nВозможно отсутствует подключение к интернет.")
    #except Exception as e:
    #    return (False, f"get_unread_messages_from_all_folders: { e }")


def email_summary():
    
    email_folders = {}
    
    for folder, folder_rules  in folders_rules_dict.items():

        email_folder = folder_rules.get('email_folder')
        if email_folder:
            email_folders[folder.split('_')[0]] = email_folder

       
    bar = FillingSquaresBar(
        'Просматриваем папки в электронной почте:',
        max=len(email_folders),
        suffix = '%(index)d/%(max)d',
        fill='█', empty_fill='░',
        width = 50) 
    
    for ensurence_company, email_folder in email_folders.items():
        #if ensurence_company!='Югория':
        #    continue
        email_folders[ensurence_company] = get_unread_messages(email_folder)[1]
        bar.next()
        
    bar.finish()
    return email_folders            

        

        



def folders_summary():
    """Получаем датафрейм
    с количеством файлов в исходных папках
    """

    downloaded_folders_info = []
    start_folders_info = []
    finish_folders_info = []

    for folder in folders_rules_dict.keys():
        folder_parts = folder.split('_')
        ensurence_company = folder_parts[0]
        file_type = folder_parts[1]

        files = list(os.walk(os.path.join(os.getcwd(), 'Исходники', folder)))[0][2]
        folder_dict = {'ensurence_company': ensurence_company, file_type: len(files)}

        if file_type == 'скачано' in folder:
            downloaded_folders_info.append(folder_dict)
        elif file_type == 'прикрепление' in folder:
            start_folders_info.append(folder_dict)
        elif file_type == 'открепление' in folder:
            finish_folders_info.append(folder_dict)

    downloaded_df = pd.DataFrame(downloaded_folders_info)
    start_df = pd.DataFrame(start_folders_info)
    finish_df = pd.DataFrame(finish_folders_info)

    res_df = pd.merge(downloaded_df, start_df, on='ensurence_company')
    res_df  = pd.merge(res_df, finish_df, on='ensurence_company')

    return res_df 

    

def prepared_summary():
    """Получаем датафрейм
    с количеством файлов собранных в файл
    подготвленных к загрузке и количество строк в этих файлах
    """

    prepared_files = list(os.walk(os.path.join(os.getcwd(), 'Подготовленные')))[0][2]
    prepared_files_info = []

    for file in prepared_files:
        df = pd.read_excel(os.path.join(os.getcwd(), 'Подготовленные', file))
        df = df[['Папка', 'Файл']]
        df = df.groupby('Папка').agg({
            'Файл': 'nunique',
            'Папка': 'count'
            }).rename(columns={
               'Файл': 'Файлов в подготовленном файле',
               'Папка': 'Строк в подготовленном файле'
               })
        # print(df)
        prepared_files_info.append(df)

    if prepared_files_info:
        total_df = pd.concat(prepared_files_info)
        total_df = total_df.reset_index('Папка')
    else:
        total_df = pd.DataFrame(columns=['Папка'])
    #total_df_grouped.columns = ['Папка', 'Подготовленных файлов']
    return total_df


def summary():
    
    if os.path.exists(os.path.join(os.getcwd(),'~$Исходники и подготовленные.xlsx')):
        return False
    else:
        email_summary_df = email_summary()
        folders_summary_df = folders_summary()
        prepared_summary_df = prepared_summary()

        res_df = pd.merge(folders_summary_df, prepared_summary_df, on='Папка', how='outer')
        res_df.to_excel('Исходники и подготовленные.xlsx', index=None)

        wb = load_workbook('Исходники и подготовленные.xlsx')

        ws = wb['Sheet1']

        ws.freeze_panes = 'A2'

        # Устанавливаем ширину для конкретной колонки
        ws.column_dimensions['A'].width = 36
        ws.column_dimensions['B'].width = 20
        ws.column_dimensions['C'].width = 20
        ws.column_dimensions['D'].width = 20

        for col in range(1, 5):
            cell = ws.cell(column=col, row=1)
            cell.font = Font(bold=True)  # Жирный шрифт
            cell.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)  # Выравнивание по центру

        for row in range(2, ws.max_row+1):
            ws.cell(column=2, row=row).alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
            ws.cell(column=3, row=row).alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
            ws.cell(column=4, row=row).alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)

        wb.save('Исходники и подготовленные.xlsx')
        return True



if __name__ == '__main__':
    print(email_summary())

    #print(folders_summary())
    # sources_and_prepared_summary()