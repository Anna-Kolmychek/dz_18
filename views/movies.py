from flask import request
from flask_restx import Resource, Namespace

from dao.model.movie import MovieSchema
from implemented import movie_service

movies_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


# Предсталение для фильмов: получить все записи, получить отфильтрованные записи, добавить новую запись
@movies_ns.route('/')
class Movies(Resource):
    def get(self):
        req = request.args
        if 'director_id' in req:
            movies = movie_service.get_by_director(req.get('director_id'))
            return movies_schema.dump(movies), 200
        elif 'genre_id' in req:
            movies = movie_service.get_by_genre(req.get('genre_id'))
            return movies_schema.dump(movies), 200
        elif 'year' in req:
            movies = movie_service.get_by_year(req.get('year'))
            return movies_schema.dump(movies), 200
        else:
            all_movies = movie_service.get_all()
            return movies_schema.dump(all_movies), 200

    def post(self):
        req_json = request.json
        movie_service.create(req_json)

        return '', 201


# Предсталение для фильмов по id: получить, изменить, изменить частично, удалить запись
@movies_ns.route('/<int:mid>')
class FilmViews(Resource):
    def get(self, mid):
        try:
            movie = movie_service.get_one(mid)
            return movie_schema.dump(movie), '200'
        except Exception:
            return '', 404

    def put(self, mid):
        req_json = request.json
        req_json['id'] = mid

        movie_service.update(req_json)

        return '', 204

    def patch(self, mid):
        req_json = request.json
        req_json['id'] = mid

        movie_service.update_partial(req_json)

        return '', 204

    def delete(self, mid):
        movie_service.delete(mid)

        return '', 204
