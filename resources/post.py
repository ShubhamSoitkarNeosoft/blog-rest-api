
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint,abort
from sqlalchemy.exc import SQLAlchemyError
from flask_jwt_extended import jwt_required
from db import db
import uuid
from models import PostModel, post
from cache import cache
from schemas import PostSchema, PostUpdateSchema
from pagination import pagination
from flask import current_app as app

blp = Blueprint("posts",__name__, description = "Operations on posts")


@blp.route("/post")
class PostList(MethodView):

  
    @jwt_required()
    @cache.cached(timeout=200, query_string=True)
    @blp.response(200,PostSchema(many=True))
    def get(self):
        # return pagination.paginate(PostModel.query.all(),PostSchema)
        return PostModel.query.all()

    @jwt_required()
    @blp.arguments(PostSchema)
    @blp.response(201,PostSchema)
    def post(self,post_data):
        post = PostModel(**post_data)
        try:
            db.session.add(post)
            db.session.commit()
            print(db)
        except SQLAlchemyError:
            abort(500, message="An error occured while inserting the item")
        return post


@blp.route("/post/<int:post_id>")
class Post(MethodView):

    @jwt_required()
    @blp.response(200,PostSchema) 
    def get(self,post_id):
        app.logger.info('Info level log')
        app.logger.warning('Warning level log')
        post = PostModel.query.get_or_404(post_id)
        return post

    @jwt_required()
    def delete(self,post_id):
        post = PostModel.query.get_or_404(post_id)
        db.session.delete(post)
        db.session.commit()
        return {"message":"Post deleted."}


    @jwt_required()
    @blp.arguments(PostUpdateSchema)
    @blp.response(200,PostSchema)
    def put(self,post_data,post_id):
        post =  PostModel.query.get(post_id)
        if post:
            post.title = post_data["title"]
            post.body = post_data["body"]
        # else:
        #     post =PostModel(id = post_id,**post_data)
        db.session.add(post)
        db.session.commit()
        return post

