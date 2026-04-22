from datetime import datetime
from colorama import Fore


def convert_date(date_str):
        patterns = ['%d-%m-%Y %H:%M:%S',
                    '%d-%m-%Y %H:%M',
                    '%d-%m-%Y',
                    '%d.%m.%Y %H:%M:%S',
                    '%d.%m.%Y %H:%M',
                    '%d.%m.%Y %H:%M:%S',
                    '%d.%m.%Y %H:%M',
                    '%d.%m.%Y',
                    '%d/%m/%Y',
                    '%Y-%m-%d %H:%M:%S.%f',                    
                    '%Y-%m-%d %H:%M:%S',
                    '%Y-%m-%d %H:%M',
                    '%Y-%m-%d',
                    '%Y.%m.%d %H:%M:%S',                    
                    '%Y.%m.%d'               
                    ]
                    
        for pattern in patterns:
            # print(date_str, pattern)
            try:
                dt = datetime.strptime(date_str, pattern)
                print(Fore.GREEN, dt, Fore.RESET)
                # result = f"{dt.tm_year}-{str(dt.tm_mon).zfill(2)}-{str(dt.tm_mday).zfill(2)} {str(dt.tm_hour).zfill(2)}:{str(dt.tm_min).zfill(2)}:{str(dt.tm_sec).zfill(2)}"
                return dt
            except:
                pass
        raise ValueError (f"Значение {date_str} не соответствует ни одному паттерну даты функции convert_date!")
    

# Тесты
dates = [
    "2026-03-12",
    "2026-03-12 00:00:00",    
    "12/03/2026",
    "12.03.2026",
    "25.04.2026",
    "12.03.2026 00:00",
    "2026-04-25 00:00:00"
]

for date_str in dates:
    print(Fore.MAGENTA, date_str, Fore.RESET)
    convert_date(date_str)
