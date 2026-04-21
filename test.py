from dateutil import parser

def convert_date(date_string):
    date_obj = parser.parse(date_string, dayfirst=True)
    return date_obj.strftime('%d-%m-%Y')


# Примеры использования
if __name__ == "__main__":
    # Тестовые примеры
    test_dates = [
        "2024-12-25 00:00:00",      # ГГГГ-ММ-ДД
        "2024-12-25",      # ГГГГ-ММ-ДД
        "25-12-2024",      # ДД-ММ-ГГГГ
        "25/12/2024",      # ДД/ММ/ГГГГ с другим разделителем
        "25.12.2024",      # ДД.ММ.ГГГГ
        "25.12.2024 00:00:00",      # ДД.ММ.ГГГГ        
        "15-03-2023",      # ДД-ММ-ГГГГ
        "2023-03-15",      # ГГГГ-ММ-ДД
        "05-12-22",        # ДД-ММ-ГГ
        "2024/05/15",      # ГГГГ/ММ/ДД
    ]
    
    print("Преобразование дат в формат ДД-ММ-ГГГГ:")
    print("-" * 40)
    
    for date_str in test_dates:
        result = convert_date(date_str)
        print(result, type(result))