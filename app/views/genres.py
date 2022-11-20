from flask_restx import Resource, Namespace

from app.dao.model.genre import GenreSchema
from implemented import genre_service

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresViews(Resource):
    def get(self):
        genres = genre_service.get_all()
        schema = GenreSchema(many=True)
        result = schema.dump(genres)
        return result, 200


@genre_ns.route('/<int:uid>')
class GenreView(Resource):
    def get(self, uid):
        genre = genre_service.get_one(uid)
        schema = GenreSchema()
        result = schema.dump(genre)
        return result, 200
