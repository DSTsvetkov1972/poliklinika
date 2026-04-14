import zipfile
import os



def extract_encrypted_zip(zip_path, extract_path, password_file_path):
    """
    Извлекает защищенный паролем ZIP-архив.
    
    Args:
        zip_path (str): Путь к ZIP-файлу.
        extract_path (str): Папка для извлечения файлов.
        password (str): Пароль от архива.
    """
    try:
        with open(password_file_path) as password_file:
            password =  password_file.readline()

    
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            # Пароль нужно передать в байтовом формате
            zip_ref.extractall(path=extract_path, pwd=password.encode('utf-8'))
        return(True, f"✅ Архив успешно извлечен в {extract_path}")
    
    except RuntimeError as e:
        return (False, f"❌ Ошибка: Неверный пароль или архив поврежден. {e}")
    except zipfile.BadZipFile:
        return(False, "❌ Ошибка: Файл не является ZIP-архивом или поврежден.")



password_file_path = os.path.join(os.getcwd(), "Исходники", "ЗЕТТА_Скачано", "password.txt")
extract_path =  os.path.join(os.getcwd(), "Исходники", "ЗЕТТА_Скачано")
zip_file_path = os.path.join(os.getcwd(),"Исходники", "ЗЕТТА_Скачано","Зетта 220 прикрепление на 13.04.2026.zip")
# Пример использования
extract_encrypted_zip(
    zip_path=zip_file_path,
    extract_path=extract_path,
    password_file_path=password_file_path#"a@:m1AV;_("
)