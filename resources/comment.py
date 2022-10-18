from async_timeout import timeout
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError
from db import db
from models import CommentModel, comment
from flask_jwt_extended import jwt_required
from schemas import CommentSchema, CommentUpdateSchema
from cache import cache


blp = Blueprint("comments", __name__, description="Operations on comments")


@blp.route("/comment")
class CommentList(MethodView):

    # @jwt_required()
    @cache.cached(timeout=30, query_string=True)
    @blp.arguments(CommentSchema)
    @blp.response(201, CommentSchema)
    def post(self, comment_data):
        comment = CommentModel(**comment_data)
        try:
            db.session.add(comment)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occured while adding the comment")
        return comment

    @cache.cached(timeout=30, query_string=True)
    @blp.response(200, CommentSchema(many=True))
    def get(self):
        obj = CommentModel.query.all()
        return obj


@blp.route("/comment/<int:comment_id>")
class Comment(MethodView):

    @jwt_required()
    @blp.response(200, CommentSchema)
    def get(self, comment_id):
        comment = CommentModel.query.get_or_404(comment_id)
        return comment

    @jwt_required()
    def delete(self, comment_id):
        comment = CommentModel.query.get_or_404(comment_id)
        db.session.delete(comment)
        db.session.commit()
        return {"message": "Comment deleted."}

    @jwt_required()
    @blp.arguments(CommentUpdateSchema)
    @blp.response(200, CommentUpdateSchema)
    def put(self, comment_data, comment_id):
        comment = CommentModel.query.get(comment_id)
        if comment:
            comment.body = comment_data["body"]
        # else:
        #     comment =commentModel(id = comment_id,**comment_data)
        db.session.add(comment)
        db.session.commit()
        return comment
