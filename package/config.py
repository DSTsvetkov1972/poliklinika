folders_rules_dict = {
    "Согаз_изменение объёма": {
        "fns_name": "base",
        "skiprows": 21,
        "filter_not_empty": "Фамилия",
        "source_header": [
            "№ п/п", "Фамилия", "Имя", "Отчество", "Дата рождения", "№ полиса", "Пол", "Прежний объем обслуживания", "Новый объем обслуживания",
            "Дата начала обслуживания","Дата окончания обслуживания","Место работы (Страхователь)"
        ],
        "result_columns": {
            "aaa": {
                "source": "column", "value": "aaaaaaaa"
            },
            "adfsdfsdafasdaa": {
                "source": "default_value", "value": "45.7"
            }            
        }
    }
}