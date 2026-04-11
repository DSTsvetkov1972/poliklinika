from imapclient import IMAPClient


EMAIL = 'spiski220@yandex.ru'  # Ваш полный адрес
APP_PASSWORD = "scmvylbvzywljjou" # Сгенерированный пароль
FOLDER_NAME= 'Альфа Страхование'

# Подключаемся и логинимся
with IMAPClient('imap.yandex.ru', port=993, use_uid=True, ssl=True) as server:
    server.login(EMAIL, APP_PASSWORD)
    
    # Получаем список всех папок
    # Метод list_folders() возвращает список кортежей (flags, delimiter, name)
    folders = server.list_folders()
    
    print("Список всех папок:")
    for flags, delimiter, name in folders:
        # Фильтруем служебные папки, которые не могут содержать письма
        if not flags or r'\Noselect' not in flags:
            print(f"  - {name}")


            with IMAPClient('imap.yandex.ru', port=993, use_uid=True, ssl=True) as server:
                server.login(EMAIL, APP_PASSWORD)
                
                # Выбираем папку — можно передать строку на русском!
                server.select_folder(name)
                
                # Получаем UID всех писем в папке
                messages = server.search(['UNSEEN'])
                print(f"Найдено писем: {len(messages)}")            