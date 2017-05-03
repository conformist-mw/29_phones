# Microservice for Search Index of Phone Numbers

Данный скрипт добавляет новую колонку `fmt_phone` в БД и сохраняет нормализованные номера в неё. 

# Установка и запуск

Установить все необходимые зависимости:

```
pip3 install -r requirements.txt
```

Для работы необоходимо выполнить upgrade базы данных для добавления новой колонки с форматированными номерами:

```
alembic upgrade head
```

После этого можно запускать:

```
python3 phones.py
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
