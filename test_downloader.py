import os
import email
from imap_tools import MailBox, AND

# НАСТРОЙКИ ДЛЯ ЯНДЕКСА
IMAP_SERVER = 'imap.yandex.ru'   # IMAP-сервер Яндекса
IMAP_PORT = 993                  # Порт для защищенного подключения
EMAIL = 'dstsvetkovpro@yandex.ru'   # Ваш полный email-адрес
PASSWORD = 'dtpfgxyymoacfvbi'   # СЮДА ВСТАВИТЬ ПАРОЛЬ ПРИЛОЖЕНИЯ!
DOWNLOAD_DIR = 'yandex_attachments'  # Папка для сохранения

# Создаем папку, если её не существует
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# Подключаемся к почте
with MailBox(IMAP_SERVER, port=IMAP_PORT).login(EMAIL, PASSWORD, 'INBOX') as mailbox:
    print("Подключение успешно! Обработка писем...")

    mailbox.folder.set('Файлы 220')
    
    # Перебираем все письма в папке INBOX
    for msg in mailbox.fetch(AND(seen=False)):
        print(f"\nПисьмо: {msg.subject} {msg.__dict__}")
        
        for att in msg.attachments:
            # filename уже корректно раскодирован библиотекой [citation:1][citation:8]

            if att.content_disposition != 'inline':
            
                # Если всё же нужна подстраховка, можно принудительно закодировать/раскодировать
                # safe_name = att.filename.encode('utf-8').decode('utf-8')
                
                file_path = os.path.join(DOWNLOAD_DIR, att.filename)
                
                # Сохраняем файл
                with open(file_path, 'wb') as f:
                    f.write(att.payload)
                
                print(f'  → Сохранено: {att.filename} ({att.size} байт) {att.content_disposition}')