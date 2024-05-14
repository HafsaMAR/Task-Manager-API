-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS task_db;
CREATE USER IF NOT EXISTS 'taks'@'localhost' IDENTIFIED BY 'taks_pwd';
GRANT ALL PRIVILEGES ON `task_db`.* TO 'taks'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'taks'@'localhost';
FLUSH PRIVILEGES;
