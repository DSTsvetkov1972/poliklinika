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
    "Альфа_Открепление": {
        "processor_name": "base",
        "sheet_name": "",
        "header_row": 7,
        "filter_not_empty": "ФИО",
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
             "source_type": "column",
             "source_column_name": "Дата открепления с (с данной даты не обслуживается)"
             },
            {"target_column": "Дата рождения",
             "source_type": "column",
             "source_column_name": "Дата рождения"
             },
            {"target_column": "Фамилия",
             "source_type": "surname_from_column",
             "source_column_name": "ФИО"
             }, 
            {"target_column": "Имя",
             "source_type": "name_from_column",
             "source_column_name": "ФИО"
             },
            {"target_column": "Отчество",
             "source_type": "patronymic_from_column",
             "source_column_name": "ФИО"}                                                          
        ]
    },
    "Альфа_Прикрепление": {
    },
    "Альфа_Скачано": {
        "email_folder": "Альфа\xa0Страхование",
        "separator_name": "email_by_file_name",
        "file_rules": [
            {"pattern": "_snyat(_copy)*\.xlsx$", "target_folder": "Альфа_Открепление"},
            {"pattern": "_prikr(_copy)*\.xlsx$", "target_folder": "Альфа_Прикрепление"},
            {"pattern": "_all(_copy)*\.xlsx$", "target_folder": "удалён"},
            {"pattern": "^(_copy)*\.xlsx$", "target_folder": "удалён"},
            {"pattern": "^null(_copy)*\.xlsx$", "target_folder": "удалён"}
        ]
    },

    "ВСК_Открепление": {
        "processor_name": "base",
        "sheet_name": "",
        "header_row": 6,
        "filter_not_empty": "NAME1",
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
             "source_type": "column",
             "source_column_name": "END"
            },
            {"target_column": "Дата рождения",
             "source_type": "column",
             "source_column_name": "DATE"
            },
            {"target_column": "Фамилия",
             "source_type": "column",
             "source_column_name": "NAME1"
            }, 
            {"target_column": "Имя",
             "source_type": "column",
             "source_column_name": "NAME2"
            },    
            {"target_column": "Отчество",
            "source_type": "column",
            "source_column_name": "NAME3"
            }                                                         
        ]
    },
    "ВСК_Прикрепление": {
    },
    "ВСК_Скачано": {
        "email_folder": "ВСК",
        "separator_name": "email_by_file_name",
        "file_rules": [
            {"pattern": "^открепление(_copy)*\.xlsx$", "target_folder": "ВСК_Открепление"},
            {"pattern": "^прикрепление(_copy)*\.xlsx$", "target_folder":  "ВСК_Прикрепление"}
        ]
    },
        
    "ЗЕТТА_Открепление": {
        "processor_name": "base",
        "sheet_name": "Письмо",
        "header_row": 17,
        "filter_not_empty": "Фамилия имя  отчество",
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
             "source_type": "column",
             "source_column_name": "Дата открепления                              (последний день обслуживания)"
            },
            {"target_column": "Дата рождения",
             "source_type": "column",
             "source_column_name": "Дата рождения"
            },
            {"target_column": "Фамилия",
             "source_type": "surname_from_column",
             "source_column_name": "Фамилия имя  отчество"
            }, 
            {"target_column": "Имя",
             "source_type": "name_from_column",
             "source_column_name": "Фамилия имя  отчество"
            },    
            {"target_column": "Отчество",
             "source_type": "patronymic_from_column",
             "source_column_name": "Фамилия имя  отчество"
            }                                                         
        ]
    },
    "ЗЕТТА_Прикрепление": {
    },
    "ЗЕТТА_Скачано": {
        "email_folder": "Альянс",
        "separator_name": "email_by_cell_value",
        "file_rules": [
            {"sheet_name": "Письмо", "cell": "B12", "pattern": ".*мы просим Вас принять на медицинское обслуживание следующих застрахованных клиентов:$", "target_folder": "ЗЕТТА_Прикрепление"},
            {"sheet_name": "Письмо", "cell": "B11", "pattern": "просит Вас снять с медицинского обслуживания  застрахованных клиентов:", "target_folder": "ЗЕТТА_Открепление"}
        ]
    },
             
    "Лучи_Открепление": {
        "processor_name": "base",
        "sheet_name": "",
        "header_row": 18,
        "filter_not_empty": "Фамилия",
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
             "source_type": "column",
             "source_column_name": "Последний день обслуживания"
             },
            {"target_column": "Дата рождения",
             "source_type": "column",
             "source_column_name": "Дата рождения"
             },
            {"target_column": "Фамилия",
             "source_type": "column",
             "source_column_name": "Фамилия"
             }, 
            {"target_column": "Имя",
             "source_type": "column",
             "source_column_name": "Имя"
             },    
            {"target_column": "Отчество",
             "source_type": "column",
             "source_column_name": "Отчество"
             }                                                         
        ]
    },
    "Лучи_Прикрепление": {
    },
    "Лучи_Скачано": {
        "email_folder": "Лучи(Бестдоктор)",
        "separator_name": "email_by_file_name",
        "file_rules": {
            "Открепление пациентов": "ЛУЧИ_Открепление",
            "Прикрепление пациентов": "Лучи_Прикрепление"
        }
    },
        
    "Ренессанс_Открепление": {
        "processor_name": "renessans_otkrep",
        "sheet_name": "О1"                                
    },
    "Ренессанс_Прикрепление": {
    },
    "Ренессанс_Скачано": {
        "email_folder": "Ренессанс",
        "separator_name": "email_by_file_name",
        "file_rules": [
            {"pattern": "^П.*_прикр_.*\.xls$", "target_folder": "Ренессанс_Прикрепление"},
            {"pattern": "^П.*_откр_.*\.xls$", "target_folder": "Ренессанс_Открепление"}
        ]
    },
        
    "РЕСО_Открепление": {
        "processor_name": "base",
        "sheet_name": "Список",
        "header_row": 9,
        "filter_not_empty": "Открепление с",
        "source_header": [
            "", "№\nп/п", "ФИО", "Дата рождения", "Пол", "Адрес", "№ полиса", "Начало обслуживания", "Открепление с", "Программа мед.  обслуживания", "Страхователь"
        ],
        "result_columns": [
            {"target_column": "Номер полиса",
             "source_type": "column",
             "source_column_name": "№ полиса"
             },
            {"target_column": "Дата открепления",
             "source_type": "column",
             "source_column_name": "Открепление с"
             },
            {"target_column": "Дата рождения",
             "source_type": "column",
             "source_column_name": "Дата рождения"
             },
            {"target_column": "Фамилия",
             "source_type": "surname_from_column",
             "source_column_name": "ФИО"
             }, 
            {"target_column": "Имя",
             "source_type": "name_from_column",
             "source_column_name": "ФИО"
             },    
            {"target_column": "Отчество",
             "source_type": "patronymic_from_column",
             "source_column_name": "ФИО"
             }                                                         
        ]
    },
    "РЕСО_Прикрепление": {
    },
    "РЕСО_Скачано": {
        "email_folder": "Ресо-Гарантия",
        "separator_name": "email_by_file_name",
        "file_rules": [
            {"pattern":"^o418\d{5}(_copy)*\.xlsx$", "target_folder":"РЕСО_Открепление"},
            {"pattern":"^p418\d{5}(_copy)*\.xlsx$", "target_folder":"РЕСО_Прикрепление"}
        ]
    },
        
    "СОГАЗ_Открепление": {
        "processor_name": "base",
        "sheet_name": "Список",
        "header_row": 22,
        "filter_not_empty": "Фамилия",
        "source_header": [
            "№ п/п", "Фамилия", "Имя", "Отчество", "Дата рождения", "№ полиса", "Окончание обслуживания", "Программа мед.обслуживания", "Место работы (Страхователь)"
        ],
        "result_columns": [
            {"target_column": "Номер полиса",
             "source_type": "column",
             "source_column_name": "№ полиса"
            },
            {"target_column": "Дата открепления",
             "source_type": "column",
             "source_column_name": "Окончание обслуживания"
             },
            {"target_column": "Дата рождения",
             "source_type": "column",
             "source_column_name": "Дата рождения"
             },
            {"target_column": "Фамилия",
             "source_type": "column",
             "source_column_name": "Фамилия"
             }, 
            {"target_column": "Имя",
             "source_type": "column",
             "source_column_name": "Имя"
             },    
            {"target_column": "Отчество",
             "source_type": "column",
             "source_column_name": "Отчество"
             }                                                         
        ]
    },
    "СОГАЗ_Прикрепление": {
    },
    "СОГАЗ_Скачано": {
        "email_folder": "СОГАЗ",
        "separator_name": "email_by_file_name",
        "file_rules": [
            {"pattern": "_прикр_.*\.xls$", "target_folder": "Ренессанс_Прикрепление"},
            {"pattern": "_откр_.*\.xls$", "target_folder": "Ренессанс_Открепление"}
        ]
    },
        
    "СОГЛАСИЕ_Открепление": {
        "processor_name": "soglasie_otkrep",
        "sheet_name": "TDSheet"                                
    },
    "СОГЛАСИЕ_Прикрепление": {
    },
    "СОГЛАСИЕ_Скачано": {
        "email_folder": "Согласие",
        "separator_name": "email_by_cell_value",
        "file_rules": [
            {"sheet_name": "Лист1", "cell": "J7", "pattern": "POLICSER", "target_folder": "СОГЛАСИЕ_Прикрепление"},
            {"sheet_name": "TDSheet", "cell": "B7", "pattern": "просит Вас снять с медицинского обслуживания застрахованных", "target_folder": "СОГЛАСИЕ_Открепление"}
        ]
    },
        
    "Югория_Открепление": {
        "processor_name": "base",
        "sheet_name": "",
        "header_row": 7,
        "filter_not_empty": "Фамилия",
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
             "source_type": "column",
             "source_column_name": "Дата открепления (последний день обслуживания)"
            },
            {"target_column": "Дата рождения",
             "source_type": "column",
             "source_column_name": "Дата рождения"
            },
            {"target_column": "Фамилия",
             "source_type": "column",
             "source_column_name": "Фамилия"
            }, 
            {"target_column": "Имя",
             "source_type": "column",
             "source_column_name": "Имя"
            },    
            {"target_column": "Отчество",
             "source_type": "column",
             "source_column_name": "Отчество"
            }                                                         
        ]
    },
    "Югория_Прикрепление": {
    },
    "Югория_Скачано": {
        "email_folder": "Ф-1|Югория",
        "separator_name": "email_base",
        "file_rules": {
            "АО_ГСК_Югория_списки_прикрепление_ГБУЗ_ГП_№_220_ДЗМ_(Филиал_№1)_": "Югория_Прикрепление",
            "АО_ГСК_Югория_списки_открепление_ГБУЗ_ГП_№_220_ДЗМ_(Филиал_№1)_": "Югория_Открепление"
        }
    },
    
}

