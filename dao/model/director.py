from marshmallow import Schema, fields

from setup_db import db

# Модель для таблицы Режиссеров
class Director(db.Model):
    __tablename__ = 'director'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


# Схема для таблицы Режиссеров
class DirectorSchema(Schema):
    id = fields.Int()
    name = fields.Str()
