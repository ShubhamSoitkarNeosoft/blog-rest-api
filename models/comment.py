from enum import unique
from db import db
from datetime import datetime


class CommentModel(db.Model):
    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(80), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"),unique=False, nullable=False)
    user = db.relationship("UserModel",back_populates="comments")
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"), unique = False)
    post = db.relationship("PostModel", back_populates= "comments")
