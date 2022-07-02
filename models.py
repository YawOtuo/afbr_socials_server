import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json
import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# database_path = 'mysql+mysqlconnector//ks8pa75ol3h0skzv:el5w7f3rjcbisebg@z3iruaadbwo0iyfp.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/jwjgkj993t2yf6sa'
database_path='mysql+mysqlconnector://{user}:{password}@{server}/{database}'.format(user='ks8pa75ol3h0skzv',
 password='el5w7f3rjcbisebg', server='z3iruaadbwo0iyfp.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306', database='jwjgkj993t2yf6sa')

db = SQLAlchemy()


"""
setup_db(app)
    binds a flask application and a SQLAlchemy service
"""
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()
    migrate = Migrate(app, db)


"""
Post

"""


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.Text)
    comments = db.relationship('Comment', backref='post')

    def __repr__(self):
        return f'<Post "{self.title}">'

    
    def __init__(self, title, content, comments):
        self.title = title
        self.content = content
        self.comments = comments


    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'comments': [comment.format() for comment in self.comments],
           
            }


class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))

    def __repr__(self):
        return f'<Comment "{self.content[:20]}...">'


       
    def __init__(self, content, post_id):
        self.content = content
        self.post_id = post_id

    def format(self):
        return {
            'id': self.id,
            'content': self.content,
            'post_id': self.post_id,
           
            }