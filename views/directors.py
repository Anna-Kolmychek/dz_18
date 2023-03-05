from flask import request
from flask_restx import Resource, Namespace

from dao.model.director import DirectorSchema
from implemented import director_service

directors_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


# Предсталение для режиссеров: получить все записи
@directors_ns.route('/')
class Directors(Resource):
    def get(self):
        all_directors = director_service.get_all()
        return directors_schema.dump(all_directors), 200


# Предсталение для режиссеров: получить запись по id
@directors_ns.route('/<int:did>')
class DirectorViews(Resource):
    def get(self, did):
        try:
            director = director_service.get_one(did)
            return director_schema.dump(director), '200'
        except Exception:
            return '', 404

