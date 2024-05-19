"""Module for Task class"""

from web_flask import db
from datetime import datetime
from tzlocal import get_localzone
# Association table for many-to-many relationship
# task_members = db.Table('task_members',
#                         db.Column('task.id', db.Integer, db.ForeignKey('task.id'), primary_key=True),
#                         db.Column('user.id', db.Integer, db.ForeignKey('user.id'), primary_key=True))

task_members = db.Table('task_members',
                        db.Column('task_id', db.Integer, db.ForeignKey('task.id'), primary_key=True),
                        db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True)
                        )

class Task(db.Model):
    '''Task class'''
    __tablename__ = 'task'
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    todo_id = db.Column(db.Integer,db.ForeignKey("todo_list.id"), nullable=False)
    title = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text, nullable=True)
    members = db.relationship('User', secondary='task_members', backref=db.backref('tasks_assigned', lazy=True) , lazy='subquery')
    duedate = db.Column(db.DateTime, nullable=True)
    label = db.Column(db.String(64), nullable=True)
    history = db.relationship('TaskHistory', backref='task', lazy=True)
    percentage_executed = db.Column(db.Float, default=0.0)

    def __init__(self, owner_id, title, todo_id, description=None, members=None, duedate=None, label=None) -> None:
        self.owner_id = owner_id
        self.title = title
        self.todo_id = todo_id
        self.description = description
        self.members = []
        self.duedate = duedate
        self.label = label

class TaskHistory(db.Model):
    '''record the task history'''
    __tablename__ = 'task_history'
    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'), nullable=False)
    time_of_execution = db.Column(db.DateTime, default=datetime.now(get_localzone()))
    modification_executed = db.Column(db.Text, nullable=False)

    def __init__(self, task_id, modification_executed) -> None:
        self.task_id = task_id
        self.modification_executed = modification_executed

