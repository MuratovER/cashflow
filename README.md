# Cash flow 
Приложение для учета личных финансов.Учета активов пасивов а также дельты в месяц.
## Технологический стэк
-Python
-Django
-Postgresql
-HTML,CSS,JS

### Установка зависимостей
```
pip install -r requirements.txt
```
### Сохранение зависимостей в requirements.txt
```
pip freeze > requirements.txt
```

##Contributing
[CONTRIBUTING.md](https://github.com/MuratovER/cashflow/blob/main/CONTRIBUTING.md)


## База данных

### Требования к базе данных
Возможно использование SQLite. Это не требует установки, однако если ты занимаешься backend разработкой, то рекомендуется установить PostgreSQL.

Для использования SQLite поменяй database backend ```settings.py```

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

### Установка PostgresSQL и pgadmin
- [How to install PostreSQL](https://www.postgresqltutorial.com/install-postgresql/)

Для работы с базой данных можно использовать встроенную консоль ```psql``` или установить [pgAdmin 4](https://www.pgadmin.org/download/pgadmin-4-windows/)

Пользователь, которого нужно создать:

login: ```eldar```

password: ```tkmlfhvehfnjd```

### Создание базы данных

Открыть консоль

Windows
```
(venv) C:\ts> psql
```

Linux
```
psql
```


Ввести команды для создания пользователя и содания базы данных
```
CREATE USER eldar;

ALTER USER eldar WITH PASSWORD 'tkmlfhvehfnjd';

CREATE DATABASE cashflow OWNER eldar;
```
