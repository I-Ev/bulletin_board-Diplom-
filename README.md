# ДОСКА ОБЪЯВЛЕНИЙ
Данная работа представляет собой backend-часть для сайта объявлений под готовый frontend.

В Бэкенд-части проекта  реализован следующий функционал:

- Авторизация и аутентификация пользователей.
- Распределение ролей между пользователями (пользователь и админ).
- Восстановление пароля через электронную почту.
- CRUD для объявлений на сайте (админ может удалять или редактировать все объявления, а пользователи только свои).
- Под каждым объявлением пользователи могут оставлять отзывы.
- В заголовке сайта можно осуществлять поиск объявлений по названию.


---
Состав проекта
---
* Фронтенд проекта реализован на React (папка frontend_react) и предоставлен в готовом виде
* Бэкэен разработан под готовый фронт и написан на Python c использованием Django Rest_Framework и JWT
--- 
## Запуск проекта через docker-compose

### Бэкенд

Перейти в папку `backend_compose`:
```python
cd skymarket
```
Выполнить команду:
```python
 python manage.py runserver
```
Бэкенд-часть проекта будет доступна по адресу `localhost:8000`

### Фронтенд
Перейти в папку `frontend_react`:
```python
cd market_postgres
```
Выполнить команду:
```python
docker-compouse up
```

Фронтенд-часть проекта будет доступна по адресу `localhost:3000` и будет взаимодействовать с бэкенд-сервером.  
 


## Загрузка фикстур в базу данных

```python
python manage.py loaddata users.json
python manage.py loaddata ads.json
python manage.py loaddata comments.json
```
