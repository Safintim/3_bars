# bars

## Описание

bars - простой скрипт, который находит самый большой, самый маленький и ближайший бар Москвы.

Данные взяты с [портала открытых данных правительства Москвы](https://data.mos.ru/)

## Требования

1. *Python3*
2. Формат передаваемого файла должен быть json, ввида:

```json
{
    "features": [
        {
            "geometry": {
                "coordinates": [37.621587946152012, 55.765366956608361],
                "type": "Point"
            },
            "properties": {
                "DatasetId": 1796,
                "VersionNumber": 2,
                "ReleaseNumber": 2,
                "RowId": "20a0b7c9-dad3-4af8-a2a2-08170f74379b",
                "Attributes": {
                    "global_id": 20660594,
                    "Name": "Юнион Джек",
                    "IsNetObject": "нет",
                    "OperatingCompany": null,
                    "AdmArea": "Центральный административный округ",
                    "District": "Мещанский район",
                    "Address": "Нижний Кисельный переулок, дом 3, строение 1",
                    "PublicPhone": [
                            {
                                "PublicPhone": "(495) 621-19-63"
                            }
                        ],
                        "SeatsCount": 30,
                        "SocialPrivileges": "нет"
                    }
                },
                "type": "Feature"
            },
            {
                ...
            }
```

## Как запустить

```sh
git clone https://github.com/Safintim/d-bars.git
cd d-bars
python3 bars.py <path_to_json>
```

Скрипт предложит ввести координаты.

## Пример работы скрипта

```sh
python3 bars.py
usage: bars.py [-h] file
bars.py: error: the following arguments are required: file
```

```sh
python3 bars.py bars.json
Самый большой бар: Спорт бар «Красная машина»
Самый маленький бар: БАР. СОКИ
Введите долготу: 1a
Координаты состоят только из чисел
```

Если не правильно ввести координаты, то увидите сообщение "Координаты состоят только из чисел"

```sh
python bars.py bars.json
Самый большой бар: Спорт бар «Красная машина»
Самый маленький бар: БАР. СОКИ
Введите долготу: 37.8999
Введите широту: 55.3333
Ближайший бар: Таверна
```

Если правильно ввести координаты, то увидите сообщение "Ближайший бар:<name_bar>

## Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
