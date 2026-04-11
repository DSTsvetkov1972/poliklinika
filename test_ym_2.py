import imaplib
import email
from email.header import decode_header

# Данные для входа
# EMAIL = 'DSTsvetkovPRO@yandex.ru'  # Ваш полный адрес
# APP_PASSWORD = "dtpfgxyymoacfvbi" # Сгенерированный пароль

EMAIL = 'spiski220@yandex.ru'  # Ваш полный адрес
APP_PASSWORD = "scmvylbvzywljjou" # Сгенерированный пароль

# Настройки сервера Yandex
IMAP_SERVER = 'imap.yandex.ru'
IMAP_PORT = 993

try:
    # 1. Подключаемся и шифруем соединение
    mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
    
    # 2. Входим в ящик
    mail.login(EMAIL, APP_PASSWORD)
    print("Успешное подключение!")

    # 3. Выбираем папку для работы (INBOX - входящие)
    mail.select('Альфа Страхование')
    
    # --- Дальше будет код для получения писем ---

except imaplib.IMAP4.error as e:
    print(f"Ошибка подключения или входа: {e}")
    print("Проверьте, что вы используете пароль приложения, а не обычный.")


# ... (продолжение кода из Шага 2)

# Выбираем папку (INBOX, "Отправленные", "Спам" и т.д.)
mail.select('INBOX')

# 4. Ищем письма. 'ALL' - все письма.
#    Другие примеры: 'UNSEEN' (непрочитанные), 'FROM "someone@mail.ru"'
status, messages_ids = mail.search(None, 'UNSEEN')

if status != 'OK':
    print("Не удалось найти письма.")
    exit()

# messages_ids - это строка с ID через пробел, например: b'1 2 3 4'
# Превращаем её в список
email_ids = messages_ids[0].split()

print(f"Найдено писем: {len(email_ids)}")

# Получим последние 5 писем для примера
# Важно: ID сортируются от старых к новым, поэтому берем срез в конце списка
latest_ids = [] # email_ids[-5:]

for e_id in latest_ids:
    # 5. Получаем данные конкретного письма по его ID
    #    RFC822 - стандартный формат для получения всего письма
    status, msg_data = mail.fetch(e_id, '(RFC822)')
    
    if status != 'OK':
        print(f"Не удалось получить письмо с ID {e_id}")
        continue
        
    # 6. Преобразуем сырые байты в читаемое письмо
    #    msg_data[0][1] - это само письмо в байтах
    raw_email = msg_data[0][1]
    msg = email.message_from_bytes(raw_email)
    
    # 7. Извлекаем и декодируем тему письма
    subject = msg['Subject']
    if subject:
        # Декодируем тему на случай, если она в кодировке
        decoded_parts = decode_header(subject)
        subject = ''.join(
            part.decode(encoding if encoding else 'utf-8', errors='ignore') 
            if isinstance(part, bytes) else part 
            for part, encoding in decoded_parts
        )
    else:
        subject = '(Без темы)'
    
    # 8. Извлекаем отправителя
    from_ = msg['From']
    
    print(f"ID: {e_id.decode()}, От: {from_}, Тема: {subject}")
    
    # Дальше можно получить тело письма, это чуть сложнее.
    # Обычно письмо состоит из частей (текст, HTML, вложения).
    if msg.is_multipart():
        for part in msg.walk():
            content_type = part.get_content_type()
            content_disposition = str(part.get('Content-Disposition'))
            
            # Ищем текстовую часть
            if content_type == 'text/plain' and 'attachment' not in content_disposition:
                body = part.get_payload(decode=True).decode('utf-8', errors='ignore')
                print(f"Тело письма (первые 100 символов): {body[:100]}...")
                break
    else:
        # Если письмо не состоит из частей
        body = msg.get_payload(decode=True).decode('utf-8', errors='ignore')
        print(f"Тело письма: {body[:100]}...")

# 9. Закрываем соединение
mail.close()
mail.logout()    