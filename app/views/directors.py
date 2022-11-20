from flask_restx import Resource, Namespace

from app.dao.model.director import DirectorSchema
from implemented import director_service

director_ns = Namespace('directors')

@director_ns.route('/')
class DirectorsViews(Resource):
    def get(self):
        directors = director_service.get_all()
        schema = DirectorSchema(many=True)
        result = schema.dump(directors)
        return result, 200

@director_ns.route('/<int:uid>')
class DirectorView(Resource):
    def get(self, uid):
        director = director_service.get_one(uid)
        schema = DirectorSchema()
        result = schema.dump(director)
        return result, 200


