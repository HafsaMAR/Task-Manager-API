from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/task_db'

db = SQLAlchemy(app)
from modules.user import User
from modules.todo import TodoList
from modules.todo import TodoHistory
from modules.task import Task

from web_flask.routes.hello import *
