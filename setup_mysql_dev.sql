-- Creates the MySQL server with specified configurations
-- Database: hbnb_dev_db
-- User: hbnb_dev with password hbnb_dev_pwd

-- Create database if not exists
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create user if not exists
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant privileges to database
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grant select privilege on performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

USE hbnb_dev_db;

-- Create tables
CREATE TABLE IF NOT EXISTS states (
    id VARCHAR(60) NOT NULL PRIMARY KEY,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    name VARCHAR(128) NOT NULL
);

CREATE TABLE IF NOT EXISTS cities (
    id VARCHAR(60) NOT NULL PRIMARY KEY,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    state_id VARCHAR(60) NOT NULL,
    name VARCHAR(128) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id) ON DELETE CASCADE
);

-- Ensure proper character set and collation
ALTER DATABASE hbnb_dev_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE states CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE cities CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Flush privileges to apply changes
FLUSH PRIVILEGES;