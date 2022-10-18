
import celery
from flask import Flask
from db import db
from flask_smorest import Api
from flask_jwt_extended import JWTManager
from resources.user import blp as UserBluePrint
from resources.post import blp as PostBluePrint
from resources.comment import blp as CommentBluePrint
from flask_migrate import Migrate
from flask_celery import make_celery
from celery import Celery
from cache import cache
from pagination import pagination
import logging



# def create_app(db_url=None):
#     app = Flask(__name__)
#     app.config["PROPOGATE_EXCEPTIONS"] = True

#     app.config["API_TITLE"] = "Blog REST API"
#     app.config["API_VERSION"] = "v1"

#     #openapi documentation version
#     app.config["OPENAPI_VERSION"] = "3.0.3"

#     #Root url of openapi
#     app.config["OPENAPI_URL_PREFIX"] = "/"

#     #Below code tells flask smorest to use swagger for api documentation
#     app.config["OPENAPI_SWAGGER_UI_PATH"] = "swagger-ui"
#     app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

#     app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blogdata.db"
#     app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

#     db.init_app(app)
#     app.config["JWT_SECRET_KEY"] = "shubham"
#     jwt = JWTManager(app)

#     migrate = Migrate(app, db)

#     #Cache config
#     # app.config.from_object('cache_config.BaseConfig')
#     cache.init_app(app)


#     #Celery Config
#     app.config.update(
#     CELERY_BROKER_URL='redis://localhost:6379',
#     CELERY_RESULT_BACKEND='redis://localhost:6379'
#     )
#     celery = make_celery(app)
   


#     @app.before_first_request
#     def create_tables():
#         db.create_all()
    
#     api = Api(app)

#     api.register_blueprint(UserBluePrint)
#     api.register_blueprint(PostBluePrint)
#     api.register_blueprint(CommentBluePrint)

#     logging.basicConfig(level=logging.DEBUG, 
#     format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

#     return app



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

migrate = Migrate(app, db)

    #Cache config
    # app.config.from_object('cache_config.BaseConfig')
cache.init_app(app)



    #  Celery Config
#Configure the redis server
# app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
# app.config['RESULT_BACKEND'] = 'redis://localhost:6379/0'

    #creates a Celery object
app.config.update(CELERY_CONFIG={
    'broker_url': 'redis://localhost:6379',
    'result_backend': 'redis://localhost:6379',
})
celery = make_celery(app)

#pagination config
app.config['PAGINATE_PAGE_SIZE'] = 5
# app.config['PAGINATE_PAGE_PARAM'] = "pagenumber"
# app.config['PAGINATE_SIZE_PARAM'] = "pagesize"
# app.config['PAGINATE_RESOURCE_LINKS_ENABLED'] = False
# app.config['PAGINATE_PAGINATION_OBJECT_KEY'] = "pagination"
# app.config['PAGINATE_DATA_OBJECT_KEY'] = "data"
pagination.init_app(app,db)


@app.before_first_request
def create_tables():
    db.create_all()

  
api = Api(app)

api.register_blueprint(UserBluePrint)
api.register_blueprint(PostBluePrint)
api.register_blueprint(CommentBluePrint)

logging.basicConfig(level=logging.DEBUG, 
format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')


# return app


# @celery.task()
# def async_function(arg1, arg2):
#     #Async task
#     return arg1+arg2

# async_function(10, 30)

@celery.task()
def add_together(a, b):
    print("inside celery task")
    return a + b

result = add_together.delay(23, 42)


# if "__name__"=="__main__":
#     app.run(debug=True)
#     db.drop_all()





