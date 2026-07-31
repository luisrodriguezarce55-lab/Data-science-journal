---Create database for the first portafolio---
Create database Portafolio_1

--Create table for the customers---
create table customers(
customer_id int primary Key,
gender char(20),
age INTEGER,
city char(20),
signup_date DATE,
loyalty_member binary);

--Create table for the customers---
create table customers(
customer_id int primary Key,
gender char(20),
age TINYINT,
city char(20),
signup_date DATE,
loyalty_member binary);

--- Alter Table for improvement---
    ALTER TABLE customers 
    ALTER COLUMN age INT NOT NULL;

ALTER TABLE customers 
    ALTER COLUMN city CHAR(20) NOT NULL;

ALTER TABLE customers 
    ALTER COLUMN signup_date DATE NOT NULL;

    EXEC sp_rename 'customers', 'customer';