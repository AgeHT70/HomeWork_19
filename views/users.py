from flask import request
from flask_restx import Resource, Namespace

from dao.model.user import UserSchema
from implemented import user_service

user_ns = Namespace('users')


@user_ns.route('/')
class UsersView(Resource):
    def get(self):
        users = user_service.get_all()
        schema = UserSchema(many=True)
        result = schema.dump(users)
        return result, 200

    def post(self):
        request_json = request.json
        user = user_service.create(request_json)
        return "", 201, {"location": f"/users/{user.id}"}


@user_ns.route('/<int:uid>')
class UserView(Resource):
    def get(self, uid):
        user = user_service.get_one(uid)
        schema = UserSchema()
        result = schema.dump(user)
        return result, 200

    def put(self, uid):
        request_json = request.json
        if "id" not in request_json:
            request_json["id"] = uid

        user_service.update(request_json)
        return "", 204

    def delete(self, uid):
        user_service.delete(uid)
        return "", 204
