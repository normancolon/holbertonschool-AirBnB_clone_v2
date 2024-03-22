-- Initialize MySQL for HBNB Clone Project Testing Environment
-- Ensures a test database named `hbnb_test_db`.
-- Creates a user `hbnb_test` with a specified password for accessing the test database.
-- Grants `hbnb_test` full privileges over the `hbnb_test_db` database for testing.
-- Grants `hbnb_test` SELECT privileges on `performance_schema` for database performance insights.

-- Step 1: Create the test database if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Step 2: Create the test user with a specific password for localhost access
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Step 3: Grant full privileges to the test user on the test database
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';

-- Step 4: Grant the test user permission to access `performance_schema`
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost';

-- Step 5: Apply all the privilege changes
FLUSH PRIVILEGES;
