# CRUD для Yatube - API для сайта Yatube.
API реализовано на Django Rest Framework. Можно обращаться к API для получения информации постов, групп и комментариев, а так же их редактирование.

# Стек:
- Python
- Django
- Djangorestframework-simplejwt
- Django REST Framework

# Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git@github.com:nicros22/api_yatube.git
```

```
cd api_yatube
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```
