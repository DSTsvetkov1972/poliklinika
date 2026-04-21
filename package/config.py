IMAP_SERVER = 'imap.yandex.ru'
IMAP_PORT = 993

# EMAIL = 'dstsvetkovpro@yandex.ru'  # Ваш полный адрес
#APP_PASSWORD = "dtpfgxyymoacfvbi" # Сгенерированный пароль

EMAIL = 'spiski220@yandex.ru'  # Ваш полный адрес
APP_PASSWORD = "scmvylbvzywljjou" # Сгенерированный пароль

MARK_SEEN = False # Для разработки. Если False,
                  # письма просмотренные программой
                  # не будут помечаться как прочитанные  




folders_rules_dict = {
    "Альфа_Изменение": {
    },
    "Альфа_Открепление": {
        "processor_name": "base",
        "sheet_name": "",
        "header_row": 7,
        "filter_not_in": {
            "column": "ФИО",
            "conditions": ["", "ФИО"]
            },
        "source_header": [
            "№ п/п", "№ полиса", "ФИО", "Дата рождения", "Группа, № договора, организация",
            "Дата открепления с (с данной даты не обслуживается)"
            ],
        "result_columns": [
            {"target_column": "Номер полиса",
             "source_type": "column",
             "source_column_name": "№ полиса"
             },
            {"target_column": "Дата открепления",
             "source_type": "date_column",
             "source_column_name": "Дата открепления с (с данной даты не обслуживается)"
             },
            {"target_column": "Дата рождения",
             "source_type": "date_column",
             "source_column_name": "Дата рождения"
             },
            {"target_column": "ФИО",
             "source_type": "column",
             "source_column_name": "ФИО"}                                                       
        ]
    },
    "Альфа_Прикрепление": {
        "processor_name": "base",
        "sheet_name": "",
        "header_row": 7,
        "filter_not_in": {
            "column": "ФИО",
            "conditions": ["","ФИО"]
            },
        "source_header": [
            "№ п/п", "№ полиса", "ФИО", "Дата рождения", "Адрес фактического проживания, телефон",
            "Группа, № договора, организация", "Период обслуживания", "", "Вид медицинского обслуживания"
            ],
        "result_columns": [
            {"target_column": "Серия полиса",
             "source_type": "const",
             "const": ""
             },
            {"target_column": "Номер полиса",
             "source_type": "column",
             "source_column_name": "№ полиса"
             },
            {"target_column": "Период обслуживания c",
             "source_type": "date_column",
             "source_column_name": "Период обслуживания"
             },
            {"target_column": "Период обслуживания по",
             "source_type": "date_column",
             "source_column_name": ""
             },
            {"target_column": "Дата рождения",
             "source_type": "date_column",
             "source_column_name": "Дата рождения"
             },
            {"target_column": "ФИО",
             "source_type": "column",
             "source_column_name": "ФИО"
             },
            {"target_column": "Вид медицинского обслуживания",
             "source_type": "column",
             "source_column_name": "Вид медицинского обслуживания"
             },
            {"target_column": "Код ПИКОМЕД",
             "source_type": "dict",
             "source_column_name": "Вид медицинского обслуживания",
             "dict": {
                 "Программа \"ЭКОНОМ\", стоматология, без вызова врача на дом, без скорой помощи": "028.19",
                 "Программа \"ЭКОНОМ\", без вызова врача на дом, без скорой помощи, без стоматологии": "025.19",
                 "Программа \"ЭКОНОМ\", вызов врача на дом, без скорой помощи, без стоматологии (Вызов врача на дом в пределах МКАД)": "026.19",
                 "Программа \"ЭКОНОМ\", вызов врача на дом, стоматология, без скорой помощи (Вызов врача на дом в пределах МКАД)": "027.19"
                 }
            }                                                       
        ]
    },
    "Альфа_Скачано": {
        "email_folder": "Альфа\xa0Страхование",
        "separator_name": "email_by_file_name",
        "file_rules": [
            {"pattern": ".doc$", "target_folder": "Альфа_Изменение"},            
            {"pattern": "_snyat(_copy)*\.xlsx$", "target_folder": "Альфа_Открепление"},
            {"pattern": "в_prikr(_copy)*\.xlsx$", "target_folder": "Альфа_Прикрепление"},
            {"pattern": "_all(_copy)*\.xlsx$", "target_folder": "удалён"},
            {"pattern": "^(_copy)*\.xlsx$", "target_folder": "удалён"},
            {"pattern": "^null(_copy)*\.xlsx$", "target_folder": "удалён"}
        ]
    },

    "ВСК_Изменение": {
    },
    "ВСК_Открепление": {
        "processor_name": "base",
        "sheet_name": "Открепление",
        "header_row": 6,
        "filter_not_in": {
            "column": "NAME1",
            "conditions": ["", "NAME1"]
            },
        "source_header": [
            "npp", "NAME1", "NAME2", "NAME3", "NIB", "DATE", "SEX", "POLIC", "POLIC SER", "ADDRESS P",
            "TEL1", "KATEGORY", "PLACE", "Holding", "BEGIN", "END"
        ],
        "result_columns": [
            {"target_column": "Номер полиса",
             "source_type": "column",
             "source_column_name": "POLIC SER"
            },
            {"target_column": "Дата открепления",
             "source_type": "date_column",
             "source_column_name": "END"
            },
            {"target_column": "Дата рождения",
             "source_type": "date_column",
             "source_column_name": "DATE"
            },
            {"target_column": "ФИО",
             "source_type": "concat_by_whitespace",
             "source_columns": ["NAME1", "NAME2", "NAME3"]
             }                                    
        ]
    },
    "ВСК_Прикрепление": {
        "processor_name": "base",
        "sheet_name": "Прикрепление",
        "header_row": 8,
        "filter_not_in": {
            "column": "DATE",
            "conditions": ["", "DATE"]
            },
        "source_header": [
            "npp", "NAME1", "NAME2", "NAME3", "NIB", "DATE", "SEX", "POLIC", "POLIC SER",
            "ADDRESS", "TEL1", "PLACE", "Holding", "BEGIN", "KATEGORY", "END"
            ],
        "result_columns": [
            {"target_column": "Серия полиса",
             "source_type": "column",
             "source_column_name": "POLIC SER"
             },            
            {"target_column": "Номер полиса",
             "source_type": "column",
             "source_column_name": "POLIC"
             },
            {"target_column": "Период обслуживания c",
             "source_type": "date_column",
             "source_column_name": "BEGIN"
             },
            {"target_column": "Период обслуживания по",
             "source_type": "date_column",
             "source_column_name": "END"
             },
            {"target_column": "Дата рождения",
             "source_type": "date_column",
             "source_column_name": "DATE"
             },
            {"target_column": "ФИО",
             "source_type": "concat_by_whitespace",
             "source_columns": ["NAME1", "NAME2", "NAME3"]
             },
            {"target_column": "Вид медицинского обслуживания",
             "source_type": "column",
             "source_column_name": "Holding"
             },
            {"target_column": "Код ПИКОМЕД",
             "source_type": "dict",
             "source_column_name": "KATEGORY",
             "dict": {
                 "АПП ПНД(в пред.МКАД) Стом. (без протез.) ": "012.58",
                 "АПП Стом. (без протез.) ": "013.58",
                 "АПП ПНД(в пред.МКАД) ": "011.58"
                 }
            }
        ]
    },
    "ВСК_Скачано": {
        "email_folder": "ВСК",
        "separator_name": "email_by_file_name",
        "file_rules": [
            {"pattern": "^открепление(_copy)*\.xlsx$", "target_folder": "ВСК_Открепление"},
            {"pattern": "^прикрепление(_copy)*\.xlsx$", "target_folder":  "ВСК_Прикрепление"}
        ]
    },
        
    "ЗЕТТА_Изменение": {
    },
    "ЗЕТТА_Открепление": {
        "processor_name": "base",
        "sheet_name": "Письмо",
        "header_row": 17,
        "filter_not_in": {
            "column": "Фамилия имя  отчество",
            "conditions": ["", "Фамилия имя  отчество"]
            },
        "source_header": [
            "", "№", "Номер полиса", "", "Фамилия имя  отчество", "", "Дата рождения",
            "Дата открепления                              (последний день обслуживания)"
        ],
        "result_columns": [
            {"target_column": "Номер полиса",
             "source_type": "column",
             "source_column_name": "Номер полиса"
            },
            {"target_column": "Дата открепления",
             "source_type": "date_column",
             "source_column_name": "Дата открепления                              (последний день обслуживания)"
            },
            {"target_column": "Дата рождения",
             "source_type": "date_column",
             "source_column_name": "Дата рождения"
            },
            {"target_column": "ФИО",
             "source_type": "column",
             "source_column_name": "Фамилия имя  отчество"
            }                                                         
        ]
    },
    "ЗЕТТА_Прикрепление": {
        "processor_name": "zetta_prikrep",
        "dict": {
            "Программа \"Стандарт\". Поликлиническое обслуживание без стоматологии, с вызовом врача на дом в пределах административной границы г.Москвы, за исключением г. Зеленограда и территорий, присоединенных  к  Москве с  01.07.2012 г.": "002.3",
            "Программа \"Стандарт\". Поликлиническое обслуживание со стоматологией, вызовом врача на дом в пределах административной границы г.Москвы, за исключением г. Зеленограда и территорий, присоединенных  к  Москве с  01.07.2012 г.": "003.3",
            "Программа \"Стандарт\". Поликлиническое обслуживание со стоматологией и вызовом врача на дом в пределах административной границы г.Москвы, за исключением г. Зеленограда и территорий,  присоединенных  к  Москве с  01.07.2012 г.": "003.3",
            "Программа \"Стандарт\". Поликлиническое обслуживание без стоматологии, без вызова врача на дом.": "005.3"
        }
    },
    "ЗЕТТА_Скачано": {
        "email_folder": "Альянс",
        "separator_name": "email_by_cell_value",
        "file_rules": [
            {"sheet_name": "Письмо", "cell": "C11", "pattern": "^Уведомляем Вас об изменении программы обслуживания с:$", "target_folder": "ЗЕТТА_Изменение"},            
            {"sheet_name": "Письмо", "cell": "C14", "pattern": "^Уведомляем Вас об изменении персональных данных застрахованных с:$", "target_folder": "ЗЕТТА_Изменение"},
            {"sheet_name": "Письмо", "cell": "B12", "pattern": ".*мы просим Вас принять на медицинское обслуживание следующих застрахованных клиентов:$", "target_folder": "ЗЕТТА_Прикрепление"},
            {"sheet_name": "Письмо", "cell": "B11", "pattern": "просит Вас снять с медицинского обслуживания  застрахованных клиентов:", "target_folder": "ЗЕТТА_Открепление"}
        ]
    },

    "Лучи_Изменение": {

    },         
    "Лучи_Открепление": {
        "processor_name": "base",
        "sheet_name": "Лист1",
        "header_row": 18,
        "filter_not_in": {
            "column": "Фамилия",
            "conditions": ["", "Фамилия"]
            },
        "source_header": [
            "№п/п", "№ полиса", "Фамилия", "Имя", "Отчество", "Пол", "Дата рождения",
            "Последний день обслуживания", "Место работы", "Программа", "Тип оплаты", "Клиники сети"
        ],
        "result_columns": [
            {"target_column": "Номер полиса",
             "source_type": "column",
             "source_column_name": "№ полиса"
            },
            {"target_column": "Дата открепления",
             "source_type": "date_column",
             "source_column_name": "Последний день обслуживания"
             },
            {"target_column": "Дата рождения",
             "source_type": "date_column",
             "source_column_name": "Дата рождения"
             },
            {"target_column": "ФИО",
             "source_type": "concat_by_whitespace",
             "source_columns": ["Фамилия", "Имя", "Отчество"]
             }                                                            
        ]
    },
    "Лучи_Прикрепление": {
        "processor_name": "base",
        "sheet_name": "Лист1",
        "header_row": 18,
        "filter_not_in": {
            "column": "Фамилия",
            "conditions": ["", "Фамилия"]
            },
        "source_header": [
            "№п/п", "№ полиса", "Фамилия", "Имя", "Отчество", "Пол", "Дата рождения", "Адрес фактический", "Телефон домашний",
            "Дата начала обслуживания", "Последний день обслуживания", "Место работы", "Программа", "Тип оплаты", "Клиники сети"
            ],
        "result_columns": [
            {"target_column": "Серия полиса",
             "source_type": "const",
             "const": ""
             },         
            {"target_column": "Номер полиса",
             "source_type": "column",
             "source_column_name": "№ полиса"
             },
            {"target_column": "Период обслуживания c",
             "source_type": "date_column",
             "source_column_name": "Дата начала обслуживания"
             },
            {"target_column": "Период обслуживания по",
             "source_type": "date_column",
             "source_column_name": "Последний день обслуживания"
             },
            {"target_column": "Дата рождения",
             "source_type": "date_column",
             "source_column_name": "Дата рождения"
             },
            {"target_column": "ФИО",
             "source_type": "concat_by_whitespace",
             "source_columns": ["Фамилия", "Имя", "Отчество"]
             },                   
            {"target_column": "Вид медицинского обслуживания",
             "source_type": "column",
             "source_column_name": "Программа"
             },
            {"target_column": "Код ПИКОМЕД",
             "source_type": "dict",
             "source_column_name": "Программа",
             "dict": {
                 "АПП+ПНД": "031.136",
                 "АПП": "030.136",
                 "АПП+Стомат": "033.136",
                 "Стомат": "033.136",
                 }
            }
        ]
    },
    "Лучи_Скачано": {
        "email_folder": "Лучи(Бестдоктор)",
        "separator_name": "email_by_file_name",
        "file_rules": [
            {"pattern": "Изменения данных пациентов", "target_folder":  "Лучи_Изменение"},
            {"pattern": "Открепление пациентов", "target_folder": "ЛУЧИ_Открепление"},
            {"pattern": "Прикрепление пациентов", "target_folder":  "Лучи_Прикрепление"}
        ]
    },

    "Ренессанс_Изменение":{        
    },
    "Ренессанс_Открепление": {
        "processor_name": "renessans_otkrep",
        "sheet_name": "О1"                                
    },
    "Ренессанс_Прикрепление": {
        "processor_name": "renessans_prikrep",
        "dict": {
            "Полное поликлиническое обслуживание без стоматологии и помощи на дому": "045.56",
            "Поликлиническое обслуживание с вызовом врача на дом , стоматологическое обслуживание без протезирования": "047.56",
            "Полное поликлиническое обслуживание без стоматологии, с вызовов врача на дом, без СМП": "046.56",
            "Поликлиническое обслуживание со стоматологией(без протезирования) без вызова врача на дом, без СМП поликлиники": "048.56"
            }
    },
    "Ренессанс_Скачано": {
        "email_folder": "Ренессанс",
        "separator_name": "email_by_file_name",
        "file_rules": [
            {"pattern": "^П.*_прикр_.*\.xls$", "target_folder": "Ренессанс_Прикрепление"},
            {"pattern": "^П.*_откр_.*\.xls$", "target_folder": "Ренессанс_Открепление"},
            {"pattern": "^П.*_мемо_.*\.xls$", "target_folder": "Ренессанс_Изменение"}
        ]
    },

    "РЕСО_Изменение": {
    },       
    "РЕСО_Открепление": {
        "processor_name": "base",
        "sheet_name": "Список",
        "header_row": 9,
        "filter_not_in": {
            "column": "Открепление с",
            "conditions": ["", "Открепление с"]
            },
        "source_header": [
            "", "№\nп/п", "ФИО", "Дата рождения", "Пол", "Адрес", "№ полиса", "Начало обслуживания", "Открепление с", "Программа мед.  обслуживания", "Страхователь"
        ],
        "result_columns": [
            {"target_column": "Номер полиса",
             "source_type": "column",
             "source_column_name": "№ полиса"
             },
            {"target_column": "Дата открепления",
             "source_type": "date_column",
             "source_column_name": "Открепление с"
             },
            {"target_column": "Дата рождения",
             "source_type": "date_column",
             "source_column_name": "Дата рождения"
             },
            {"target_column": "ФИО",
             "source_type": "column",
             "source_column_name": "ФИО"
             }                                                         
        ]
    },
    "РЕСО_Прикрепление": {
        "processor_name": "base",
        "sheet_name": "Список",
        "header_row": 9,
        "filter_not_in": {
            "column": "Адрес",
            "conditions": ["", "Адрес"]
            },
        "source_header": [
            "", "№\nп/п", "ФИО", "Дата рождения", "Пол", "Адрес", "№ полиса", "Начало обслуживания", "Окончание обслуживания", "Программа мед.  обслуживания", "Страхователь"
        ],
        "result_columns": [
            {"target_column": "Серия полиса",
             "source_type": "const",
             "const": ""
             },        
            {"target_column": "Номер полиса",
             "source_type": "column",
             "source_column_name": "№ полиса"
             },
            {"target_column": "Период обслуживания c",
             "source_type": "date_column",
             "source_column_name": "Начало обслуживания"
             },
            {"target_column": "Период обслуживания по",
             "source_type": "date_column",
             "source_column_name": "Окончание обслуживания"
             },
            {"target_column": "Дата рождения",
             "source_type": "date_column",
             "source_column_name": "Дата рождения"
             },
            {"target_column": "ФИО",
             "source_type": "column",
             "source_column_name": "ФИО"
             },
            {"target_column": "Вид медицинского обслуживания",
             "source_type": "column",
             "source_column_name": "Программа мед.  обслуживания"
             },
            {"target_column": "Код ПИКОМЕД",
             "source_type": "dict",
             "source_column_name": "Программа мед.  обслуживания",
             "dict": {
                 "СТОМАТОЛОГИЧЕСКАЯ ПОМОЩЬ (уровень стом. услуг 2)": "067.17",
                 "АМБУЛАТОРНАЯ ПОМОЩЬ, ПОМОЩЬ НА ДОМУ": "065.17",
                 "АМБУЛАТОРНАЯ ПОМОЩЬ, ПОМОЩЬ НА ДОМУ, СТОМАТОЛОГИЧЕСКАЯ ПОМОЩЬ (уровень стом. услуг 2)": "066.17",
                 "АМБУЛАТОРНАЯ ПОМОЩЬ": "068.17",
                 "АМБУЛАТОРНАЯ ПОМОЩЬ, СТОМАТОЛОГИЧЕСКАЯ ПОМОЩЬ (уровень стом. услуг 2)": "067.17"
                 }
            }
        ]
    },
    "РЕСО_Прикрепление_2": {
        "processor_name": "reso_prikrep_2",
        "dict": {
            "СТОМАТОЛОГИЧЕСКАЯ ПОМОЩЬ (уровень стом. услуг 2)": "067.17",
            "АМБУЛАТОРНАЯ ПОМОЩЬ, ПОМОЩЬ НА ДОМУ": "065.17",
            "АМБУЛАТОРНАЯ ПОМОЩЬ, ПОМОЩЬ НА ДОМУ, СТОМАТОЛОГИЧЕСКАЯ ПОМОЩЬ (уровень стом. услуг 2)": "066.17",
            "АМБУЛАТОРНАЯ ПОМОЩЬ": "068.17",
            "АМБУЛАТОРНАЯ ПОМОЩЬ, СТОМАТОЛОГИЧЕСКАЯ ПОМОЩЬ (уровень стом. услуг 2)": "067.17"
            }
    },
    "РЕСО_Скачано": {
        "email_folder": "Ресо-Гарантия",
        "separator_name": "email_by_cell_value",
        "file_rules": [
            {"sheet_name": "Список", "cell": "B8", "pattern": "принять на медицинское обслуживание застрахованных", "target_folder":"РЕСО_Прикрепление"},
            {"sheet_name": "Лист1", "cell": "A6", "pattern": "принять на медицинское обслуживание", "target_folder":"РЕСО_Прикрепление_2"},
            {"sheet_name": "Список", "cell": "B8", "pattern": "просит Вас  снять с обслуживания", "target_folder":"РЕСО_Открепление"},
            {"sheet_name": "Список", "cell": "A12", "pattern": "просит Вас внести изменения", "target_folder":"РЕСО_Изменение"},
            {"sheet_name": "Список", "cell": "B8", "pattern": "изменить программу обслуживания", "target_folder":"РЕСО_Изменение"},                      
        ]
    },

    "СОГАЗ_Изменение": {
    },    
    "СОГАЗ_Открепление": {
        "processor_name": "base",
        "sheet_name": "Список",
        "header_row": 22,
        "filter_not_in": {
            "column": "Фамилия",
            "conditions": ["", "Фамилия"]
            },
        "source_header": [
            "№ п/п", "Фамилия", "Имя", "Отчество", "Дата рождения", "№ полиса", "Окончание обслуживания", "Программа мед.обслуживания", "Место работы (Страхователь)"
        ],
        "result_columns": [
            {"target_column": "Номер полиса",
             "source_type": "column",
             "source_column_name": "№ полиса"
            },
            {"target_column": "Дата открепления",
             "source_type": "date_column",
             "source_column_name": "Окончание обслуживания"
             },
            {"target_column": "Дата рождения",
             "source_type": "date_column",
             "source_column_name": "Дата рождения"
             },
            {"target_column": "ФИО",
             "source_type": "concat_by_whitespace",
             "source_columns": ["Фамилия", "Имя", "Отчество"]
             }                                                               
        ]
    },
    "СОГАЗ_Прикрепление": {
        "processor_name": "base",
        "sheet_name": "Лист_1",
        "header_row": 22,
        "filter_not_in": {
            "column": "Дата рождения",
            "conditions": ["", "Дата рождения"]
            },
        "source_header": [
            "№ п/п", "Фамилия", "Имя", "Отчество", "Дата рождения", "Пол", "Адрес проживания", "Телефон домашний", "Телефон служебный", "Телефон мобильный",
            "№ полиса", "Начало обслуживания", "Окончание обслуживания", "Программа мед. обслуживания", "Место работы (Страхователь)", "Должность"
            ],
        "result_columns": [
            {"target_column": "Серия полиса",
             "source_type": "const",
             "const": ""
             },            
            {"target_column": "Номер полиса",
             "source_type": "column",
             "source_column_name": "№ полиса"
             },
            {"target_column": "Период обслуживания c",
             "source_type": "date_column",
             "source_column_name": "Начало обслуживания"
             },
            {"target_column": "Период обслуживания по",
             "source_type": "date_column",
             "source_column_name": "Окончание обслуживания"
             },
            {"target_column": "Дата рождения",
             "source_type": "date_column",
             "source_column_name": "Дата рождения"
             },
            {"target_column": "ФИО",
             "source_type": "concat_by_whitespace",
             "source_columns": ["Фамилия", "Имя", "Отчество"]
             },
            {"target_column": "Вид медицинского обслуживания",
             "source_type": "column",
             "source_column_name": "Программа мед. обслуживания"
             },
            {"target_column": "Код ПИКОМЕД",
             "source_type": "dict",
             "source_column_name": "Программа мед. обслуживания",
             "dict": {
                 "Амб. взрослые; ПНД в пределах МКАД; Стоматология в ЛПУ": "072.16 ",
                 "Амб. взрослые": "071.16",
                 "Амб. взрослые; Стоматология в ЛПУ": "073.16",
                 "Амб. взрослые; ПНД в пределах административной границы города; Стоматология в ЛПУ": "072.16",
                 "Амб. взрослые; ПНД в пределах МКАД": "070.16",
                 "ПНД в пределах МКАД": "070.16"
                 }
            }
        ]
                           
    },
    "СОГАЗ_Скачано": {
        "email_folder": "СОГАЗ",
        "separator_name": "email_by_file_name",
        "file_rules": [
            {"pattern": "_Прикрепление_.*\.xls$", "target_folder": "СОГАЗ_Прикрепление"}
        ]
    },
        
    "СОГЛАСИЕ_Изменение": {                              
    },
    "СОГЛАСИЕ_Открепление": {
        "processor_name": "soglasie_otkrep",
        "sheet_name": "TDSheet"                                
    },
    "СОГЛАСИЕ_Прикрепление": {
        "processor_name": "base",
        "sheet_name": "Лист1",
        "header_row": 7,
        "filter_not_in": {
            "column": "Фамилия",
            "conditions": ["", "Фамилия"]
            },
        "source_header": [
            "", "№\nп/п", "Фамилия", "Имя", "Отчество", "", "Дата рождения", "Пол", "Полис", "POLICSER",
            "Адрес ", "Телефон", "Программа", "Организация", "Начало ", "Конец "
            ],
        "result_columns": [
            {"target_column": "Серия полиса",
             "source_type": "column",
             "source_column_name": "POLICSER"
             },
            {"target_column": "Номер полиса",
             "source_type": "column",
             "source_column_name": "Полис"
             },
            {"target_column": "Период обслуживания c",
             "source_type": "date_column",
             "source_column_name": "Начало "
             },
            {"target_column": "Период обслуживания по",
             "source_type": "date_column",
             "source_column_name": "Конец "
             },
            {"target_column": "Дата рождения",
             "source_type": "date_column",
             "source_column_name": "Дата рождения"
             },
            {"target_column": "ФИО",
             "source_type": "concat_by_whitespace",
             "source_columns": ["Фамилия", "Имя", "Отчество"]
             },                 
            {"target_column": "Вид медицинского обслуживания",
             "source_type": "column",
             "source_column_name": "Программа"
             },
            {"target_column": "Код ПИКОМЕД",
             "source_type": "dict",
             "source_column_name": "Программа",
             "dict": {
                 "Амбулаторно-поликлиническая помощь. Стоматологическая помощь. Помощь на дому в пределах МКАД.": "059.49",
                 "Амбулаторно-поликлиническая помощь. Стоматологическая помощь.": "060.49",
                 "Амбулаторно-поликлиническая помощь. Помощь на дому в пределах МКАД.": "058.49",
                 "Амбулаторно-поликлиническая помощь.": "057.49"
                 }
            }
        ]
    },
    "СОГЛАСИЕ_Скачано": {
        "email_folder": "Согласие",
        "separator_name": "email_by_cell_value",
        "file_rules": [
            {"sheet_name": "TDSheet", "cell": "D3", "pattern": "извещает Вас об изменении данных у застрахованных:", "target_folder": "СОГЛАСИЕ_Изменение"},            
            {"sheet_name": "Лист1", "cell": "J7", "pattern": "POLICSER", "target_folder": "СОГЛАСИЕ_Прикрепление"},
            {"sheet_name": "TDSheet", "cell": "B7", "pattern": "просит Вас снять с медицинского обслуживания застрахованных", "target_folder": "СОГЛАСИЕ_Открепление"}
        ]
    },
        
    "Югория_Изменение": {
    },    
    "Югория_Открепление": {
        "processor_name": "base",
        "sheet_name": "",
        "header_row": 7,
        "filter_not_in": {
            "column": "Фамилия",
            "conditions": ["", "Фамилия"]
        },
        "source_header": [
            "№ п/п", "Полис", "Фамилия", "Имя", "Отчество", "Пол", "Дата рождения", "Адрес", "Телефон",
            "Дата открепления (последний день обслуживания)", "Наименование Страхователя", "Название страховой компании"
        ],
        "result_columns": [
            {"target_column": "Номер полиса",
            "source_type": "column",
            "source_column_name": "Полис"
            },
            {"target_column": "Дата открепления",
             "source_type": "date_column",
             "source_column_name": "Дата открепления (последний день обслуживания)"
            },
            {"target_column": "Дата рождения",
             "source_type": "date_column",
             "source_column_name": "Дата рождения"
            },
            {"target_column": "ФИО",
             "source_type": "concat_by_whitespace",
             "source_columns": ["Фамилия", "Имя", "Отчество"]
             }                                                               
        ]
    },
    "Югория_Прикрепление": {
        "processor_name": "base",
        "sheet_name": "Лист_1",
        "header_row": 7,
        "filter_not_in": {
            "column": "Фамилия",
            "conditions": ["", "Фамилия"]
        },
        "source_header": [
            "№ п/п", "№ полиса", "Фамилия", "Имя", "Отчество", "Пол", "Дата рождения", "Адрес", "Телефон",
            "Дата прикрепления", "Дата открепления", "№ программы обслуживания", "Наименование Страхователя", "Название страховой компании"
        ],
        "result_columns": [
            {"target_column": "Серия полиса",
             "source_type": "const",
             "const": ""
             },
            {"target_column": "Номер полиса",
             "source_type": "column",
             "source_column_name": "№ полиса"
             },
            {"target_column": "Период обслуживания c",
             "source_type": "date_column",
             "source_column_name": "Дата прикрепления"
             },
            {"target_column": "Период обслуживания по",
             "source_type": "date_column",
             "source_column_name": "Дата открепления"
             },
            {"target_column": "Дата рождения",
             "source_type": "date_column",
             "source_column_name": "Дата рождения"
             },
            {"target_column": "ФИО",
             "source_type": "concat_by_whitespace",
             "source_columns": ["Фамилия", "Имя", "Отчество"]
             },                 
            {"target_column": "Вид медицинского обслуживания",
             "source_type": "column",
             "source_column_name": "№ программы обслуживания"
             },
            {"target_column": "Код ПИКОМЕД",
             "source_type": "dict",
             "source_column_name": "№ программы обслуживания",
             "dict": {
                 "АПП": "009.23-06"
                 }
            }
        ]
    },
    "Югория_Скачано": {
        "email_folder": "Ф-1|Югория",
        "separator_name": "email_by_file_name",
        "file_rules": [
            {"pattern": "АО_ГСК_Югория_списки_прикрепление_ГБУЗ_ГП_№_220_ДЗМ_\(Филиал_№1\)_", "target_folder": "Югория_Прикрепление"},
            {"pattern": "АО_ГСК_Югория_списки_открепление_ГБУЗ_ГП_№_220_ДЗМ_\(Филиал_№1\)_", "target_folder": "Югория_Открепление"}
        ]
    }
}

