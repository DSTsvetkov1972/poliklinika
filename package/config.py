folders_rules_dict = {
    "Альфа_открепление": {
        "processor_name": "base",
        "skiprows": 0,
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
    "ВСК_открепление": {
        "processor_name": "base",
        "skiprows": 5,
        "filter_not_empty": "NAME1",
        "source_header": [
            "npp", "NAME1", "NAME2", "NAME3", "NIB", "DATE", "SEX", "POLIC", "POLIC SER", "ADDRESS P",
            "TEL1", "KATEGORY", "PLACE", "Holding", "BEGIN", "END"
        ],
        "result_columns": {
            "Номер полиса": {
                "source": "column", "source_column_name": "POLIC SER"
            },
            "Дата открепления": {
                "source": "column", "source_column_name": "END"
            },
            "Дата рождения": {
                "source": "column", "source_column_name": "DATE"
            },
            "Фамилия": {
                "source": "column", "source_column_name": "NAME1"
            }, 
            "Имя": {
                "source": "column", "source_column_name": "NAME2"
            },    
            "Отчество": {
                "source": "column", "source_column_name": "NAME3"
            }                                                         
        }
    },
    "ЗЕТТА_открепление": {
        "processor_name": "base",
        "skiprows": 16,
        "filter_not_empty": "Фамилия имя  отчество",
        "source_header": [
            "Unnamed: 0", "№", "Номер полиса", "Unnamed: 3", "Фамилия имя  отчество", "Unnamed: 5", "Дата рождения",
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
    "ЛУЧИ_открепление": {
        "processor_name": "base",
        "skiprows": 17,
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
    }
}

