# ДЗ 18

В проекте рализовано REST API для работы с данными
из БД. Применен подходт разделения на Сервисы и ДАО

## Эндпоинты

Разделены по namespace-ам, лежат в папке views.

### views / movies.py
Содержит 2 CBV для namespace = "movies"
* /movies
    * GET - возвращает все фильмы из БД.
  Может содержать аргументы director_id, genre_id и year.
  В этом случае происходит фильтрация по соответствующим значениям полей. 
    * POST - добавляет новый фильм в базу
* /movies/int:id
  * GET - возвращает фильм с указанным id
  * PUT - меняет все поля фильма с указанным id
  * PATCH - меняет часть или все поля фильма с указанным id
  * DELETE - удаляет запись с указанным id
  

### views / directors.py
Содержит 2 CBV для namespace = "directors"
* /directors
    * GET - возвращает всех рижессеров из БД.
* /directors/int:id
  * GET - возвращает данные режиссера с указанным id

### apis / genres.py
Содержит 2 CBV для namespace = "genres"
* /genres
    * GET - возвращает все жанры из БД.
* /genres/int:id
  * GET - возвращает жанр с указанным id


## Используемые технологии
* flask
* flask-restx
* flask-sqlalchemy
* marshmallow