from flask import Flask
from flask_restx import Api

from config import Config
from setup_db import db

from app.views.genres import genre_ns
from app.views.movies import movie_ns
from app.views.directors import director_ns


def create_app(config_obj):
    application = Flask(__name__)
    application.config.from_object(config_obj)
    register_extensions(application)
    return application


def register_extensions(appl):
    api = Api(appl)
    db.init_app(appl)
    api.add_namespace(genre_ns)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)


application = create_app(Config())
application.debug = True

if __name__ == '__main__':
    application.run(host="127.0.0.1", port=10001, debug=True)
