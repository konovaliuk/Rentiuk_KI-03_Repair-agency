-- Create database
create DATABASE repair_agency;

-- Use database
USE repair_agency;
-- Create roles table

CREATE TABLE roles (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(50) NOT NULL
);

-- Create users table
CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  login VARCHAR(50) UNIQUE NOT NULL,
  password VARCHAR(255) NOT NULL,
  role_id INT NOT NULL,
  FOREIGN KEY (role_id) REFERENCES roles(id)
);

-- Create requests table
CREATE TABLE requests (
  id INT AUTO_INCREMENT PRIMARY KEY,
  product_name VARCHAR(50) NOT NULL,
  product_model VARCHAR(50) NOT NULL,
  problem_description TEXT NOT NULL,
  price INT,
  status ENUM('pending', 'accepted', 'rejected', 'in-work', 'completed') NOT NULL DEFAULT 'pending',
  user_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users(id)
);


-- Create feedback table
CREATE TABLE feedbacks (
  id INT AUTO_INCREMENT PRIMARY KEY,
  text TEXT,
  request_id INT NOT NULL,
  master_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (request_id) REFERENCES requests(id),
  FOREIGN KEY (master_id) REFERENCES users(id)
);