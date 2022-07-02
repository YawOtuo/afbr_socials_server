from models import db, Post, Comment, setup_db
import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random


# db.session.commit()

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)
    

    """
    @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
    """

    @app.after_request
    def after_request(response):
        response.headers.add(
            'Access-Control-Allow-Headers', 'Content-Type, Authorization, true'

        )
        response.headers.add(
            'Access-Control-Allow-Methods', 'GET,PATCH, POST, DELETE, OPTIONS'
            
        )
        return response

    @app.route('/')
    def save():
        posts = Post.query.all()

        return jsonify({
            'success':True,
            'posts': [post.format() for post in posts]
        })

   
    return app