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
                "source": "column", "value": "policy_number"
            },
            "Дата открепления": {
                "source": "column", "value": "date_cancel"
            },
            "Дата рождения": {
                "source": "column", "value": "birth_date"
            },
            "Фамилия": {
                "source": "column", "value": "per_last_name"
            }, 
            "Имя": {
                "source": "column", "value": "per_first_name"
            },    
            "Отчество": {
                "source": "column", "value": "per_middle_name"
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
                "source": "column", "value": "POLIC SER"
            },
            "Дата открепления": {
                "source": "column", "value": "END"
            },
            "Дата рождения": {
                "source": "column", "value": "DATE"
            },
            "Фамилия": {
                "source": "column", "value": "NAME1"
            }, 
            "Имя": {
                "source": "column", "value": "NAME2"
            },    
            "Отчество": {
                "source": "column", "value": "NAME3"
            }                                                         
        }
    }
}

