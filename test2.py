from imap_tools import MailBox
from colorama import Fore 

def get_folders_imap_tools(username: str, password: str):
    """Подключается к Яндекс.Почте и выводит список папок, используя imap-tools."""

    with MailBox('imap.yandex.ru').login(username, password) as mailbox:
        print(f"Успешный вход для {username}")
        print("\nСписок папок в ящике:")
        print("-" * 30)
        
        # Метод folder.list() возвращает список объектов Folder
        # Каждый объект имеет атрибуты name, flags, delim
        for folder in mailbox.folder.list():
            if 'югория' in folder.name.lower() or 'зетта' in folder.name.lower():
                print(Fore.GREEN, folder.name, Fore.RESET)  # Имя папки уже корректно декодировано
            else:
                 # print(Fore.WHITE, folder.name, Fore.RESET)
                 pass

# --- Пример использования ---
# my_username = "your_email@yandex.ru"
# my_app_password = "your_app_specific_password"
# get_folders_imap_tools(my_username, my_app_password)

if __name__ == '__main__':
    get_folders_imap_tools('spiski220@yandex.ru', 'scmvylbvzywljjou')

    # print('югория' in 'Ф-1|Югория'.lower())