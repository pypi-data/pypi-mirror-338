def get_parse_config(*, query: str, page: int = 1, captcha: str = ""):
    params = {
        "mode": "search-ul",
        "queryAll": "",  # Поиск по названию
        "queryUl": query,  # Поиск по организациям
        "okvedUl": "",  # Категория
        "regionUl": "",
        "statusUl": "",
        "isMspUl": "",
        "mspUl1": "1",
        "mspUl2": "1",
        "mspUl3": "1",
        "queryIp": "",  # Поиск по ИП
        "okvedIp": "",
        "regionIp": "",
        "statusIp": "",
        "isMspIp": "",
        "mspIp1": "1",
        "mspIp2": "1",
        "mspIp3": "1",
        "taxIp": "",
        "queryUpr": "",  # Поиск по "Участие в ЮЛ"
        "uprType1": "1",
        "uprType0": "1",
        "queryRdl": "",  # Поиск по "Дисквалификация"
        "dateRdl": "",
        "queryAddr": "",  # Поиск по адресу
        "regionAddr": "",
        "queryOgr": "",  # Поиск по "Ограничения участия в ЮЛ"
        "ogrFl": "1",
        "ogrUl": "1",
        "ogrnUlDoc": "",
        "ogrnIpDoc": "",
        "npTypeDoc": "1",
        "nameUlDoc": "",
        "nameIpDoc": "",
        "formUlDoc": "",
        "formIpDoc": "",
        "ifnsDoc": "",
        "dateFromDoc": "",
        "dateToDoc": "",
        "page": page,
        "pageSize": "100",
        "pbCaptchaToken": captcha,
        "token": ""
    }
    return params
