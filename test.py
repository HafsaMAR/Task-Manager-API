from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Replace 'your_username', 'your_password', 'your_host', and 'your_database_name' with your MySQL database details
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/task_db'

db = SQLAlchemy(app)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
