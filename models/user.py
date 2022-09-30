from db import db
from datetime import datetime

class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    posts = db.relationship("PostModel",back_populates="user",lazy = "dynamic")
    comments = db.relationship("CommentModel", back_populates = "user",lazy = "dynamic")
