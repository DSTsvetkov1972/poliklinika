IMAP_SERVER = 'imap.yandex.ru'
IMAP_PORT = 993

# EMAIL = 'dstsvetkovpro@yandex.ru'  # Ваш полный адрес
#APP_PASSWORD = "dtpfgxyymoacfvbi" # Сгенерированный пароль

EMAIL = 'spiski220@yandex.ru'  # Ваш полный адрес
APP_PASSWORD = "scmvylbvzywljjou" # Сгенерированный пароль

MARK_SEEN = False # Для разработки. Чтобы письма просмотренные программой
                  # не помечались как прочитанные  




folders_rules_dict = {
    "Альфа_Открепление": {
        "processor_name": "base",
        "sheet_name": "",
        "header_row": 1,
        "filter_not_empty": "row_number",
        "source_header": [
            "row_number", "policy_number", "date_from", "date_to", "date_cancel", "prog_code", "fio", "prog_name",
            "add_phone", "address", "phone_home", "phone_office", "birth_date", "person_sex", "insurer", "ag_number",
            "our_subj", "hosp_extrim", "hospital", "ambulance", "per_title", "group_name", "company_of_work",
            "place_of_work", "history_num", "citizen", "new_policy", "policy_omc", "docum",
            "degree_of_relationship","per_mobile_phone", "servicing_office", "adr_country", "adr_post_code",
            "adr_city", "adr_region", "adr_street", "adr_house", "adr_building", "adr_appartment", "adr_entrance",
            "adr_access_code", "adr_floor", "undgr_station", "per_last_name", "per_first_name", "per_middle_name", 
            "pdoc_ser",	"pdoc_no", "pdoc_issue_date", "pdoc_issue_place", "lpu_number","risk_code",	"age_id",
            "pay_type", "med_prog_short"
        ],
        "result_columns": {
            "Номер полиса": {
                "source_type": "column", "source_column_name": "policy_number"
            },
            "Дата открепления": {
                "source_type": "column", "source_column_name": "date_cancel"
            },
            "Дата рождения": {
                "source_type": "column", "source_column_name": "birth_date"
            },
            "Фамилия": {
                "source_type": "column", "source_column_name": "per_last_name"
            }, 
            "Имя": {
                "source_type": "column", "source_column_name": "per_first_name"
            },    
            "Отчество": {
                "source_type": "column", "source_column_name": "per_middle_name"
            }                                                         
        }
    },
    "Альфа_Прикрепление": {
    },
    "Альфа_Скачано файлов": {
        "email_folder": "Альфа\xa0Страхование",
        "processor_name": "email_base",
        "file_actions": {
            "_snyat.xlsx": "Альфа_Открепление",
            "_prikr.xlsx": "Альфа_Прикрепление",
            "_all.xlsx": "trash"
        }
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
        "result_columns": {
            "Номер полиса": {
                "source_type": "column", "source_column_name": "POLIC SER"
            },
            "Дата открепления": {
                "source_type": "column", "source_column_name": "END"
            },
            "Дата рождения": {
                "source_type": "column", "source_column_name": "DATE"
            },
            "Фамилия": {
                "source_type": "column", "source_column_name": "NAME1"
            }, 
            "Имя": {
                "source_type": "column", "source_column_name": "NAME2"
            },    
            "Отчество": {
                "source_type": "column", "source_column_name": "NAME3"
            }                                                         
        }
    },
    "ВСК_Прикрепление": {
    },
    "ВСК_Скачано файлов": {
        "email_folder": "ВСК",
        "processor_name": "email_base",
        "file_actions": {
            "_snyat.xlsx": "ВСК_Открепление",
            "_prikr.xlsx": "прикрепление.xlsx"
        }
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
        "result_columns": {
            "Номер полиса": {
                "source_type": "column", "source_column_name": "Номер полиса"
            },
            "Дата открепления": {
                "source_type": "column", "source_column_name": "Дата открепления                              (последний день обслуживания)"
            },
            "Дата рождения": {
                "source_type": "column", "source_column_name": "Дата рождения"
            },
            "Фамилия": {
                "source_type": "surname_from_column", "source_column_name": "Фамилия имя  отчество"
            }, 
            "Имя": {
                "source_type": "name_from_column", "source_column_name": "Фамилия имя  отчество"
            },    
            "Отчество": {
                "source_type": "patronymic_from_column", "source_column_name": "Фамилия имя  отчество"
            }                                                         
        }
    },
    "ЗЕТТА_Прикрепление": {
    },
    "ЗЕТТА_Скачано файлов": {
        "email_folder": "Альянс",
        "processor_name": "email_zetta"
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
        "result_columns": {
            "Номер полиса": {
                "source_type": "column", "source_column_name": "№ полиса"
            },
            "Дата открепления": {
                "source_type": "column", "source_column_name": "Последний день обслуживания"
                },
            "Дата рождения": {
                "source_type": "column", "source_column_name": "Дата рождения"
                },
            "Фамилия": {
                "source_type": "column", "source_column_name": "Фамилия"
                }, 
            "Имя": {
                "source_type": "column", "source_column_name": "Имя"
                },    
            "Отчество": {
                "source_type": "column", "source_column_name": "Отчество"
                }                                                         
        }
    },
    "Лучи_Прикрепление": {
    },
    "Лучи_Скачано файлов": {
        "email_folder": "Лучи(Бестдоктор)",
        "processor_name": "email_base",
        "file_actions": {
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
    "Ренессанс_Скачано файлов": {
        "email_folder": "Ренессанс",
        "processor_name": "email_base",
        "file_actions": {
            "_откр_": "Ренессанс_Открепление",
            "_прикр_": "Ренессанс_Прикрепление"
        }
    },
        
    "РЕСО_Открепление": {
        "processor_name": "base",
        "sheet_name": "Список",
        "header_row": 9,
        "filter_not_empty": "Открепление с",
        "source_header": [
            "", "№\nп/п", "ФИО", "Дата рождения", "Пол", "Адрес", "№ полиса", "Начало обслуживания", "Открепление с", "Программа мед.  обслуживания", "Страхователь"
        ],
        "result_columns": {
            "Номер полиса": {
                "source_type": "column", "source_column_name": "№ полиса"
            },
            "Дата открепления": {
                "source_type": "column", "source_column_name": "Открепление с"
                },
            "Дата рождения": {
                "source_type": "column", "source_column_name": "Дата рождения"
                },
            "Фамилия": {
                "source_type": "surname_from_column", "source_column_name": "ФИО"
                }, 
            "Имя": {
                "source_type": "name_from_column", "source_column_name": "ФИО"
                },    
            "Отчество": {
                "source_type": "patronymic_from_column", "source_column_name": "ФИО"
                }                                                         
        }
    },
    "РЕСО_Прикрепление": {
    },
    "РЕСО_Скачано файлов": {
        "email_folder": "Ресо-Гарантия",
        "processor_name": "email_base",
        "file_actions": {
            "o": "РЕСО_Открепление",
            "p": "РЕСО_Прикрепление"
        }
    },
        
    "СОГАЗ_Открепление": {
        "processor_name": "base",
        "sheet_name": "Список",
        "header_row": 22,
        "filter_not_empty": "Фамилия",
        "source_header": [
            "№ п/п", "Фамилия", "Имя", "Отчество", "Дата рождения", "№ полиса", "Окончание обслуживания", "Программа мед.обслуживания", "Место работы (Страхователь)"
        ],
        "result_columns": {
            "Номер полиса": {
                "source_type": "column", "source_column_name": "№ полиса"
            },
            "Дата открепления": {
                "source_type": "column", "source_column_name": "Окончание обслуживания"
                },
            "Дата рождения": {
                "source_type": "column", "source_column_name": "Дата рождения"
                },
            "Фамилия": {
                "source_type": "column", "source_column_name": "Фамилия"
                }, 
            "Имя": {
                "source_type": "column", "source_column_name": "Имя"
                },    
            "Отчество": {
                "source_type": "column", "source_column_name": "Отчество"
                }                                                         
        }
    },
    "СОГАЗ_Прикрепление": {
    },
    "СОГАЗ_Скачано файлов": {
        "email_folder": "СОГАЗ",
        "processor_name": "email_sogaz",
        "file_actions": {
            "": "",
            "": ""
        }
    },
        
    "СОГЛАСИЕ_Открепление": {
        "processor_name": "soglasie_otkrep",
        "sheet_name": "TDSheet"                                
    },
    "СОГЛАСИЕ_Прикрепление": {
    },
    "СОГЛАСИЕ_Скачано файлов": {
        "email_folder": "Согласие",
        "processor_name": "email_soglasie",
        "": "",
        "": ""
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
        "result_columns": {
            "Номер полиса": {
                "source_type": "column", "source_column_name": "Полис"
            },
            "Дата открепления": {
                "source_type": "column", "source_column_name": "Дата открепления (последний день обслуживания)"
            },
            "Дата рождения": {
                "source_type": "column", "source_column_name": "Дата рождения"
            },
            "Фамилия": {
                "source_type": "column", "source_column_name": "Фамилия"
            }, 
            "Имя": {
                "source_type": "column", "source_column_name": "Имя"
            },    
            "Отчество": {
                "source_type": "column", "source_column_name": "Отчество"
            }                                                         
        }
    },
    "Югория_Прикрепление": {
    },
    "Югория_Скачано файлов": {
        "email_folder": "Ф-1|Югория",
        "processor_name": "email_base",
        "АО_ГСК_Югория_списки_Прикрепление_ЗХ_ГБУЗ_ГП_№_220_ДЗМ_(Филиал_№1)_": "Югория_Прикрепление",
        "АО_ГСК_Югория_списки_Открепление_ГБУЗ_ГП_№_220_ДЗМ_(Филиал_№1)_": "Югория_Прикрепление"
    },
    
}

