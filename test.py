import unittest
from web_flask import app, db
from modules.task import Task, TaskHistory
from modules.todo import TodoList, TodoHistory
from modules.user import User

class BestTestCase(unittest.TestCase):
    def setUp(self) -> None:
        """setUp the unitest env"""
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        with app.app_context():
            db.create_all()
        
    def tearDown(self) -> None:
        """end the session and clear memory"""
        with app.app_context():
            db.session.remove()
            db.drop_all()

class UserTestCase(BestTestCase):
    def test_create_user(self):
        with app.app_context():
            user = User(username="John Doe", email="john@example.com", password="1234567890")
            db.session.add(user)
            db.session.commit()

            self.assertEqual(User.query.count(), 1)
            queried_user = User.query.first()
            self.assertEqual(queried_user.username, "John Doe")
            self.assertEqual(queried_user.email, "john@example.com")
    
    def test_user_tasks_relationship(self):
        """Task class and User class relationships"""
        with app.app_context():
            user = User(username="Jane Doe", email="jane@example.com", password="password123")
            db.session.add(user)
            db.session.commit()

            # define the todolist of the user
            todo_list = TodoList(title="jane's Todo List", owner_id=user.id)
            db.session.add(todo_list)
            db.session.commit()

            task = Task(owner_id=user.id, title="Test the Task", todo_id=todo_list.id)
            db.session.add(task)
            db.session.commit()

            self.assertEqual(user.tasks[0].title, "Test the Task")


class TaskTestCase(BestTestCase):
    def test_create_task(self):
        with app.app_context():
            user = User(username="John Doe", email="john@example.com", password="1234567890")
            db.session.add(user)
            db.session.commit()

            # define the todolist of the user
            todo_list = TodoList(title="jane's Todo List", owner_id=user.id)
            db.session.add(todo_list)
            db.session.commit()

            task = Task(owner_id=user.id, todo_id=todo_list.id, title="Test the Task")
            db.session.add(task)
            db.session.commit()

            self.assertEqual(Task.query.count(), 1)
            queried_task = Task.query.first()
            self.assertEqual(queried_task.title, "Test the Task")
            self.assertEqual(queried_task.owner.id, user.id)
            self.assertEqual(queried_task.todo_list.id, todo_list.id)
    

    def test_task_history(self):
        with app.app_context():
            user = User(username="John Doe", email="john@example.com", password="1234567890")
            db.session.add(user)
            db.session.commit()

            # define the todolist of the user
            todo_list = TodoList(title="jane's Todo List", owner_id=user.id)
            db.session.add(todo_list)
            db.session.commit()

            task = Task(owner_id=user.id, todo_id=todo_list.id, title="Test the Task")
            db.session.add(task)
            db.session.commit()

            history_entry = TaskHistory(task_id=task.id, modification_executed='Created task')
            db.session.add(history_entry)
            db.session.commit()

            self.assertEqual(TaskHistory.query.count(), 1)
            queried_history = TaskHistory.query.first()
            self.assertEqual(queried_history.modification_executed, 'Created task')


class TodoListTestCase(BestTestCase):
    def test_create_todo_list(self):
        with app.app_context():
            user = User(username="John Doe", email="john@example.com", password="1234567890")
            db.session.add(user)
            db.session.commit()

            todo_list = TodoList(title='Test Todo List', owner_id= user.id)
            db.session.add(todo_list)
            db.session.commit()

            self.assertEqual(TodoList.query.count(), 1)
            queried_todo_list = TodoList.query.first()
            self.assertEqual(queried_todo_list.title, 'Test Todo List')
            self.assertEqual(queried_todo_list.owner.id, user.id)
            