# YamDB

### Описание

YamDB - REST API для обмена мнениями пользователей о фильмах, книгах и музыке

### Технологии

Python 3.7
Django 2.2.19
Django REST framework 3.12.4

### Запуск проекта в dev-режиме

- Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/AndrewYatskevich/api_yamdb.git
```

```
cd api_yamdb
```

- Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

- Активировать вирутальное окружение:

```
source venv/bin/activate
```
- Далее выполните команды:

```
python3 -m pip install --upgrade pip
```

- Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

- Выполнить миграции:

```
python3 manage.py migrate
```

- Запустить проект:

```
python3 manage.py runserver
```

Автор: Андрей Яцкевич https://github.com/AndrewYatskevich