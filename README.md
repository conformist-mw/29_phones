# Microservice for Search Index of Phone Numbers

Данный проект позволяет сделать дамп базы данных и нормализовать телефонные номера в ней. 

# Установка и запуск
Установить все необходимые зависимости:
```
pip3 install -r requirements.txt
```
Далее необоходимо выполнить несколько действий:
- заполнить `config.py` своими данными
- заполнить поле `sqlalchemy.url` в `alembic.ini`
- сделать дамп БД:
```
python3 dump.py
```
- выполнить upgrade базы данных для добавления новой колонки с форматированными номерами
```
alembic upgrade head
```
После этого все подготовительные процессы закончены и можно запускать:
```
python3 phones.py
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
