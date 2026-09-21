CREATE DATABASE test;
USE test;

CREATE TABLE users (
                       id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
                       firstname VARCHAR(30) NOT NULL,
                       lastname VARCHAR(30) NOT NULL,
                       email VARCHAR(50) NOT NULL,
                       age INT,
                       location VARCHAR(50),
                       date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
