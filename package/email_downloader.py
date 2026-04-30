import os, sys
sys.path.append(os.getcwd())
from colorama import Fore
from imap_tools import MailBox, OR
from package.fns import get_file_path

from package.config import IMAP_SERVER, IMAP_PORT, EMAIL, APP_PASSWORD
from package.config import folders_rules_dict


MARK_SEEN = os.getenv('MARK_SEEN')


def get_email_folders():
     with MailBox(IMAP_SERVER, port=IMAP_PORT).login(EMAIL, APP_PASSWORD, 'INBOX') as mailbox:
    
        for folder_info in mailbox.folder.list():
        
           print(f"Имя папки: {folder_info.name}")



def file_path_if_exists(file_path):
    while True:
        file_path_parts = file_path.split('.')
        file_path_short = '.'.join(file_path_parts[0:-1])
        file_path_extension = file_path_parts[-1]

        if os.path.exists(file_path):
            file_path = f'{ file_path_short }_copy.{file_path_extension}'
        else:
            return file_path



def attachments_downloader():
        folders = list(os.walk('Исходники'))[0][1]
        downloaded_folders = [folder for folder in folders if '_Скачано' in folder]

        folders_len = [len(download_folder + folders_rules_dict[download_folder]['email_folder']) for download_folder in downloaded_folders]
        max_folders_len = max(folders_len)

        for download_folder in downloaded_folders:
            email_folder = folders_rules_dict[download_folder]['email_folder']
            
            get_attached_file(email_folder, download_folder, max_folders_len)





def get_attached_file(email_folder, download_folder, max_folders_len):
    start_message = Fore.BLUE + f'Загружаем из { email_folder } в {download_folder}...'.ljust(max_folders_len+20)
    print(start_message)
    try:
        with MailBox(IMAP_SERVER, port=IMAP_PORT).login(EMAIL, APP_PASSWORD, 'INBOX') as mailbox:
            # print("Подключение успешно! Обработка писем...")

            mailbox.folder.set(email_folder)     
           
            msg_qty = 0
            att_qty = 0

            for msg in mailbox.fetch(OR(new=True, seen=False), mark_seen=MARK_SEEN):
                msg_qty += 1
                
                for att in msg.attachments:
                    # if att.content_disposition != 'inline':
                        att_qty += 1
                    
                        # Если всё же нужна подстраховка, можно принудительно закодировать/раскодировать
                        # safe_name = att.filename.encode('utf-8').decode('utf-8')
                        
                        file_name = att.filename

                        # если файл с таким названием существует,
                        # добавляем в конце суффикс _copy
                        # пока не получится уникальное имя файла
                        file_path = get_file_path(file_name, download_folder)

                        with open(file_path, 'wb') as f:
                            f.write(att.payload)
        summary = Fore.GREEN + f'получено писем: {msg_qty:3}, 2файлов: {att_qty:4}' + Fore.RESET
        finish_message = '\033[F\033[' + start_message + summary
        print(finish_message)
    except Exception as e:
        summary = Fore.RED+ f'получено писем: {msg_qty:3}, загружено файлов: {att_qty:4} ОШИБКА { repr(e) }' + Fore.RESET
        finish_message = '\033[F\033[' + start_message + summary
        print(finish_message)


if __name__=='__main__':
    get_email_folders()


