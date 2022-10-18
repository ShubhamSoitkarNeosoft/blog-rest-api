from marshmallow import Schema,fields


class PlainPostSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    body = fields.Str(required=True)
    created_at = fields.Str(dump_only=True)
    updated_at = fields.Str(dump_only=True)
   

class PlainCommentSchema(Schema):
    id = fields.Int(dump_only = True)
    body = fields.Str(required=True)
    created_at = fields.Str(dump_only=True)
    updated_at = fields.Str(dump_only=True)


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)


class PostSchema(PlainPostSchema):
    user_id = fields.Int(required=True, load_only = True)
    user = fields.Nested(UserSchema(),dump_only=True)


class PostUpdateSchema(Schema):
    title = fields.Str(required=True)
    body = fields.Str(required=True)

class CommentSchema(PlainCommentSchema):
    user_id = fields.Int(required=True, load_only = True)
    user = fields.Nested(UserSchema(),dump_only=True)
    post_id = fields.Int(required=True, load_only = True)
    post = fields.Nested(PostSchema(), dump_only = True)

class CommentUpdateSchema(Schema):
    body = fields.Str(required=True)






