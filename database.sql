DROP DATABASE IF EXISTS flaskdb;
CREATE DATABASE flaskdb;
USE flaskdb;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE
);

INSERT INTO users (name, email) VALUES
('Carlos Gómez', 'carlos@example.com'),
('María López', 'maria@example.com'),
('Juan Pérez', 'juan@example.com');
