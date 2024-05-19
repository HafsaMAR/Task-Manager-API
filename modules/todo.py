"""module for the todolist class"""

from web_flask import db
from datetime import datetime
from tzlocal import get_localzone

todo_members = db.Table('todo_members',
                        db.Column('todo_id', db.Integer, db.ForeignKey('todo_list.id', primary_key=True)),
                        db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True)
                        )


class TodoList(db.Model):
    """todo list class and its relation with user and tasks class"""

    __tablename__ = 'todo_list'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    members = db.relationship('User', secondary='todo_members', lazy='subquery', backref=db.backref('todos', lazy=True))
    tasks = db.relationship('Task', backref='todo_list', lazy=True)
    percentage_of_tasks_executed = db.Column(db.Float, default=0.0)
    label = db.Column(db.String(100), nullable=True)
    history=db.relationship('TodoHistory', backref='todo_list', lazy=True)

    def __init__(self, title, owner_id, label=None, members=None) -> None:
        self.title = title
        self.owner_id = owner_id
        self.label = label
        self.members = []

class TodoHistory(db.Model):
    """history of modification and creation of todo list"""
    __tablename__ = 'todo_history'
    id = db.Column(db.Integer, primary_key=True)
    todo_id = db.Column(db.Integer, db.ForeignKey('todo_list.id'), nullable=False)
    time_of_execution = db.Column(db.DateTime, default=datetime.now(get_localzone()))
    modification_executed = db.Column(db.Text, nullable=False)

    def __init__(self, todo_id,modification_executed) -> None:
        self.todo_id = todo_id
        self.modification_executed = modification_executed

