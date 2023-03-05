from marshmallow import Schema, fields

from setup_db import db


# Модель для таблицы Жанров
class Genre(db.Model):
    __tablename__ = 'genre'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


# Схема для таблицы Жанров
class GenreSchema(Schema):
    id = fields.Int()
    name = fields.Str()
