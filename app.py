from flask import Flask
from flask_restx import Api
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from auth.auth import auth_ns
from models.db import db
from flask import json
from werkzeug.exceptions import InternalServerError


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)

    migrate = Migrate(app, db)
    JWTManager(app)

    api = Api(app, doc="/docs")

    api.add_namespace(auth_ns)

    @app.route("/")
    def index():
        return 'hello world'

    return app