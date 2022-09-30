from db import db
from datetime import datetime

class PostModel(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    body = db.Column(db.String(80), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"),unique=False, nullable=False)
    user = db.relationship("UserModel",back_populates="posts")
    comments = db.relationship("CommentModel", back_populates = "post",lazy = "dynamic")
