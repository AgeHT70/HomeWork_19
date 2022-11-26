from flask import request
from flask_restx import Resource, Namespace

from dao.model.director import DirectorSchema
from decorators import auth_required, admin_required
from implemented import director_service

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    @auth_required
    def get(self):
        directors = director_service.get_all()
        schema = DirectorSchema(many=True)
        result = schema.dump(directors)
        return result, 200

    @admin_required
    def post(self):
        request_json = request.json
        director = director_service.create(request_json)
        return "", 201, {"location": f"/directors/{director.id}"}


@director_ns.route('/<int:uid>')
class DirectorView(Resource):
    @auth_required
    def get(self, uid):
        director = director_service.get_one(uid)
        schema = DirectorSchema()
        result = schema.dump(director)
        return result, 200

    @admin_required
    def put(self, uid):
        request_json = request.json
        if "id" not in request_json:
            request_json["id"] = uid

        director_service.update(request_json)
        return "", 204

    @admin_required
    def delete(self, uid):
        director_service.delete(uid)
        return "", 204
