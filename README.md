# API для социальной сети Yatube

## Описание
REST API для социальной сети Yatube. Проект позволяет пользователям создавать посты, оставлять комментарии и подписываться на других авторов. Взаимодействие с API происходит через JWT-аутентификацию.

## Технологии
- Python 3.10
- Django 3.2
- Django REST Framework
- Djoser / SimpleJWT (аутентификация)
- drf-spectacular (документация Redoc)
- SQLite (база данных)

## Установка и запуск

1. Клонируйте репозиторий и перейдите в его папку:
   ```bash
   git clone <ссылка_на_ваш_репозиторий>
   cd api-final-yatube-ad
2. Создайте и активируйте виртуальное окружение:
    python -m venv venv
    source venv/bin/activate  # Для Linux/macOS
    venv\Scripts\activate     # Для Windows
3. Установите зависимости:
    pip install -r requirements.txt
4. Выполните миграции:
    python manage.py migrate
5. Запустите сервер:
    python manage.py runserver