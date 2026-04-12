from imap_tools import MailBox, AND
from datetime import datetime
from package.config import IMAP_SERVER, IMAP_PORT, EMAIL, APP_PASSWORD, MARK_SEEN
from colorama import Fore
import socket


def get_unread_messages_from_all_folders(folder_name):
    #"""Получает все непрочитанные письма из всех папок Яндекс Почты"""
    try:
        with MailBox(IMAP_SERVER, port=IMAP_PORT).login(EMAIL, APP_PASSWORD, initial_folder='INBOX') as mailbox:
                print(IMAP_SERVER, IMAP_PORT, EMAIL, APP_PASSWORD)
            
                mailbox.folder.set(folder_name)
                
                # Ищем непрочитанные письма (критерий seen=False)
                unread_messages = list(mailbox.fetch(AND(seen=False), mark_seen=False))
                
                return (True, len(unread_messages))
    except socket.gaierror as e:
        return (True, f"get_unread_messages_from_all_folders: { e }.\nВозможно отсутствует подключение к интернет.")
    except Exception as e:
        return (True, f"get_unread_messages_from_all_folders: { e }")
            
            
if __name__ == '__main__':
    folder_name = 'Файлы 220'
    print(get_unread_messages_from_all_folders(folder_name))