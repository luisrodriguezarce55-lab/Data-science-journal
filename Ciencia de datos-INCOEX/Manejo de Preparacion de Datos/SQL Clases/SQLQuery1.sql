-- 1. Create the Teacher table first
CREATE TABLE Teacher (
    Teacher_ID VARCHAR(20) PRIMARY KEY,
    Subjects_Taught VARCHAR(255)
);

-- 2. Create the Subjects table
CREATE TABLE Subjects (
    Subject_ID VARCHAR(20) PRIMARY KEY,
    Subject_Code VARCHAR(50) NOT NULL,
    Subject_Name CHAR(75) NOT NULL,
    Teacher_ID VARCHAR(20),
    FOREIGN KEY (Teacher_ID) REFERENCES Teacher(Teacher_ID)
);

-- 3. Create the Students table
CREATE TABLE Students (
    Student_ID VARCHAR(20) PRIMARY KEY,
    DNI VARCHAR(20) NOT NULL UNIQUE,
    First_Name CHAR(50) NOT NULL,
    Last_Name CHAR(50) NOT NULL,
    Address VARCHAR(255)
);

-- 4. Create the Grades table
CREATE TABLE Grades (
    Student_ID VARCHAR(30),
    Subject_ID VARCHAR(20),
    Grade DECIMAL(5,2) NOT NULL, 
    Academic_Period DATE,
    Activity_Status VARCHAR(30) 
);

