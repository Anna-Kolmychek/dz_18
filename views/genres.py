from flask import request
from flask_restx import Resource, Namespace

from dao.model.genre import GenreSchema
from implemented import genre_service

genres_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


# Предсталение для жанров: получить все записи
@genres_ns.route('/')
class Genres(Resource):
    def get(self):
        all_genres = genre_service.get_all()
        return genres_schema.dump(all_genres), 200


# Предсталение для жанров: получить запись по id
@genres_ns.route('/<int:gid>')
class GenreViews(Resource):
    def get(self, gid):
        try:
            genre = genre_service.get_one(gid)
            return genre_schema.dump(genre), '200'
        except Exception:
            return '', 404

