-- task_2.sql

-- Select the database to work with
USE ALX_BOOK_STORE;

-- Create the 'Authors' table
-- This table stores information about authors.
CREATE TABLE AUTHORS (
    AUTHOR_ID INT PRIMARY KEY AUTO_INCREMENT, -- Primary Key: Unique identifier for each author, auto-increments.
    AUTHOR_NAME VARCHAR(215) NOT NULL         -- Author's full name, cannot be empty.
);

-- Create the 'Books' table
-- This table stores information about books available in the bookstore.
CREATE TABLE BOOKS (
    BOOK_ID INT PRIMARY KEY AUTO_INCREMENT,  -- Primary Key: Unique identifier for each book, auto-increments.
    TITLE VARCHAR(130) NOT NULL,             -- The title of the book, cannot be empty.
    AUTHOR_ID INT NOT NULL,                  -- Foreign Key: Links to the AUTHOR_ID in the Authors table.
    PRICE DOUBLE NOT NULL,                   -- The price of the book, cannot be empty.
    PUBLICATION_DATE DATE NOT NULL,          -- The publication date of the book, cannot be empty.
    -- Define the foreign key constraint:
    -- Ensures that every AUTHOR_ID in this table must exist in the AUTHORS table.
    -- ON DELETE CASCADE means if an author is deleted, all their books are also deleted.
    FOREIGN KEY (AUTHOR_ID) REFERENCES AUTHORS(AUTHOR_ID) ON DELETE CASCADE
);

-- Create the 'Customers' table
-- This table stores information about customers.
CREATE TABLE CUSTOMERS (
    CUSTOMER_ID INT PRIMARY KEY AUTO_INCREMENT, -- Primary Key: Unique identifier for each customer, auto-increments.
    CUSTOMER_NAME VARCHAR(215) NOT NULL,        -- Customer's full name, cannot be empty.
    EMAIL VARCHAR(215) NOT NULL UNIQUE,         -- Customer's email address, must be unique for each customer.
    ADDRESS TEXT                                -- Customer's physical address.
);

-- Create the 'Orders' table
-- This table stores information about orders placed by customers.
CREATE TABLE ORDERS (
    ORDER_ID INT PRIMARY KEY AUTO_INCREMENT,   -- Primary Key: Unique identifier for each order, auto-increments.
    CUSTOMER_ID INT NOT NULL,                  -- Foreign Key: Links to the CUSTOMER_ID in the Customers table.
    ORDER_DATE DATE NOT NULL,                  -- The date the order was placed, cannot be empty.
    -- Define the foreign key constraint:
    -- Ensures that every CUSTOMER_ID in this table must exist in the CUSTOMERS table.
    -- ON DELETE CASCADE means if a customer is deleted, all their orders are also deleted.
    FOREIGN KEY (CUSTOMER_ID) REFERENCES CUSTOMERS(CUSTOMER_ID) ON DELETE CASCADE
);

-- Create the 'Order_Details' table
-- This table stores information about the books included in each order.
-- This is a junction table for a many-to-many relationship between Orders and Books.
CREATE TABLE ORDER_DETAILS (
    ORDERDETAILID INT PRIMARY KEY AUTO_INCREMENT, -- Primary Key: Unique identifier for each order detail entry, auto-increments.
    ORDER_ID INT NOT NULL,                        -- Foreign Key: Links to the ORDER_ID in the Orders table.
    BOOK_ID INT NOT NULL,                         -- Foreign Key: Links to the BOOK_ID in the Books table.
    QUANTITY DOUBLE NOT NULL,                     -- The quantity of the specific book in this order detail, cannot be empty.
    -- Define foreign key constraint for ORDER_ID:
    -- Ensures that every ORDER_ID in this table must exist in the ORDERS table.
    -- ON DELETE CASCADE means if an order is deleted, its details are also deleted.
    FOREIGN KEY (ORDER_ID) REFERENCES ORDERS(ORDER_ID) ON DELETE CASCADE,
    -- Define foreign key constraint for BOOK_ID:
    -- Ensures that every BOOK_ID in this table must exist in the BOOKS table.
    -- ON DELETE CASCADE means if a book is deleted, its details in orders are also deleted.
    FOREIGN KEY (BOOK_ID) REFERENCES BOOKS(BOOK_ID) ON DELETE CASCADE
);

