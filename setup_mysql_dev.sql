-- Create the database if it does not already exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create the user if it does not already exist, with the specified password
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all privileges on the database `hbnb_dev_db` to the user `hbnb_dev`
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';

-- Ensure `hbnb_dev` has SELECT privileges on `performance_schema`
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';

-- Apply changes
FLUSH PRIVILEGES;

