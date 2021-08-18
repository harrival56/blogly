from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

db = SQLAlchemy()
def connect_db(app):
    db.app = app
    db.init_app(app)


class User(db.Model):
    __tablename__ = 'users'



    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String)
    position = db.Column(db.String, nullable=False)
    c_of_origin = db.Column(db.String, nullable=False)
    image_url = db.Column(db.String, nullable=False)
    post = db.relationship('Post')

    def greet(self):
        return f"Hi welcome to my profile page, I'm {self.first_name} {self.last_name}" 
    


    def __repr__(self):
        return f"<User = id={self.first_name}, first_name={self.last_name}, position={self.position}, c_of_origin={self.c_of_origin}, imgage_url={self.image_url}"


class Post(db.Model):
    __tablename__ = "posts"


    id  = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user = db.relationship('User')

    def __repr__(self):
        return f"id={self.id}, title={self.title}, content={self.content}, user_id={self.user_id}"