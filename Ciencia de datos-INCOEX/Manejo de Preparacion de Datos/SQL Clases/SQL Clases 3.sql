-- 1. Select the database to be used
USE class_2;
GO

-- 2. Create the 'products' table with its respective columns and constraints
CREATE TABLE products (
    id INT NOT NULL,              -- Unique product identifier (cannot be null)
    name VARCHAR(10) NOT NULL,    -- Product name (maximum 10 characters, cannot be null)
    category VARCHAR(5) NOT NULL, -- Category or class (maximum 5 characters, cannot be null)
    CONSTRAINT PK_products PRIMARY KEY (id) -- Definition of 'id' as the primary key
);
GO

-- 3. Insert test data into the 'products' table
INSERT INTO products (id, name, category)
VALUES 
(1, 'Laptop', 'TECH'),   -- Product 1: Technology
(2, 'Keyboard', 'TECH'), -- Product 2: Technology
(3, 'Chair', 'OFFIC'),   -- Product 3: Office
(4, 'Table', 'OFFIC'),   -- Product 4: Office
(5, 'Mouse', 'TECH');    -- Product 5: Technology
GO

-- 4. Verification: Query the data to confirm it was saved correctly
SELECT * FROM products;