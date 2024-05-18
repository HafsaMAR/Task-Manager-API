"""Module to define the user class"""

from web_flask import db


class User(db.Model):
    """user class"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(256), unique=True, nullable=False)
    # url of the photo uploaded
    photo = db.Column(db.String(256))
    # task the user implement (foreign key)
    tasks = db.relationship('Task', backref='owner', lazy=True)

    def __init__(self, username, email, password, photo=None):
        '''Initialize the user class'''
        self.username  = username
        self.email = email
        self.password = password
        self.photo = photo