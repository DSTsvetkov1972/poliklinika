import io
import pandas as pd
import msoffcrypto
import os

file_path = os.path.join(
    os.getcwd(),
    "Исходники",
    "Росгосстрах ТЭК_Скачано",
    '25.02.21 1 Ю761(010-1).xlsx')

password = 'rgs2023'

# 1. Открываем encrypted-файл и дешифруем его в объект BytesIO
decrypted = io.BytesIO()
with open(file_path, 'rb') as f:
    office_file = msoffcrypto.OfficeFile(f)
    office_file.load_key(password=password)  # Применяем пароль
    office_file.decrypt(decrypted)           # Расшифровываем в память

# 2. Переводим "курсор" в начало потока и читаем файл через pandas
decrypted.seek(0)
df = pd.read_excel(decrypted, header=None) # engine указывать необязательно

# 3. Готово!
print(df)

print(df.iloc[5].loc[0])