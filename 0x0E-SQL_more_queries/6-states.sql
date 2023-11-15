-- creates the database hbtn_0d_usa and table states (in the database hbtn_0d_usa) on your MySQL server
-- creates the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- uses a database
USE hbtn_0d_usa;
-- will creates a table
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE NOT NULL AUTO_INCREMENT, name VARCHAR(256) NOT NULL, PRIMARY KEY(id));

