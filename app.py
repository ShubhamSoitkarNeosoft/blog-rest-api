from flask import Flask
from db import db
from flask_smorest import Api
from flask_jwt_extended import JWTManager
from resources.user import blp as UserBluePrint
from resources.post import blp as PostBluePrint
from resources.comment import blp as CommentBluePrint


def create_app(db_url=None):
    app = Flask(__name__)
    app.config["PROPOGATE_EXCEPTIONS"] = True

    app.config["API_TITLE"] = "Blog REST API"
    app.config["API_VERSION"] = "v1"

    #openapi documentation version
    app.config["OPENAPI_VERSION"] = "3.0.3"

    #Root url of openapi
    app.config["OPENAPI_URL_PREFIX"] = "/"

    #Below code tells flask smorest to use swagger for api documentation
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blogdata.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    app.config["JWT_SECRET_KEY"] = "shubham"
    jwt = JWTManager(app)


    @app.before_first_request
    def create_tables():
        db.create_all()
    
    api = Api(app)

    api.register_blueprint(UserBluePrint)
    api.register_blueprint(PostBluePrint)
    api.register_blueprint(CommentBluePrint)
    return app






