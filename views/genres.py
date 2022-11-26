from flask import request
from flask_restx import Resource, Namespace

from dao.model.genre import GenreSchema
from decorators import auth_required, admin_required
from implemented import genre_service

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresViews(Resource):
    @auth_required
    def get(self):
        genres = genre_service.get_all()
        schema = GenreSchema(many=True)
        result = schema.dump(genres)
        return result, 200

    @admin_required
    def post(self):
        request_json = request.json
        genre = genre_service.create(request_json)
        return "", 201, {"location": f"/genres/{genre.id}"}


@genre_ns.route('/<int:uid>')
class GenreView(Resource):
    @auth_required
    def get(self, uid):
        genre = genre_service.get_one(uid)
        schema = GenreSchema()
        result = schema.dump(genre)
        return result, 200

    @admin_required
    def put(self, uid):
        request_json = request.json
        if "id" not in request_json:
            request_json["id"] = uid

        genre_service.update(request_json)
        return "", 204

    @admin_required
    def delete(self, uid):
        genre_service.delete(uid)
        return "", 204
