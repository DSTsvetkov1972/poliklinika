import os, sys
sys.path.append(os.getcwd())
from colorama import Fore
from imap_tools import MailBox, OR
from time import sleep

from package.config import IMAP_SERVER, IMAP_PORT, EMAIL, APP_PASSWORD, MARK_SEEN
from package.config import folders_rules_dict


def get_attached_file(email_folder, download_folder):

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
                        
                        file_path = os.path.join(os.getcwd(), 'Исходники', download_folder, att.filename)

                        while True:
                            file_path_parts = file_path.split('.')
                            file_path_short = '.'.join(file_path_parts[0:-1])
                            file_path_extension = file_path_parts[-1]

                            if os.path.exists(file_path):
                                file_path = f'{ file_path_short }_copy.{file_path_extension}'
                            else:
                                break

                            
                        

                        with open(file_path, 'wb') as f:
                            f.write(att.payload)

            print(f'получено писем: { msg_qty }, загружено файлов: { att_qty }', Fore.RESET)     
        return (True,)
    except Exception as e:
        return(False, e)


def attachments_downloader():
    try:

        folders = list(os.walk('Исходники'))[0][1]
        downloaded_folders = [folder for folder in folders if '_Скачано' in folder]

        for download_folder in downloaded_folders:
            email_folder = folders_rules_dict[download_folder]['email_folder']
            print(Fore.BLACK + f'Загружаем из { email_folder } в {download_folder}...')
            get_attached_file(email_folder, download_folder)

        return (True,)

    except Exception as e:
        return (False, e)

    

if __name__=='__main__':
    #email_folder = 'Альянс'
    #download_folder = 'ЗЕТТА_Скачано'
    #get_attached_file(email_folder, download_folder)
    attachments_downloader()
