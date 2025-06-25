-- task_5.sql

-- This script inserts a single row into the 'CUSTOMERS' table
-- in the database specified as an argument to the mysql command.

-- The database is assumed to be 'alx_book_store'.

INSERT INTO CUSTOMERS (CUSTOMER_ID, CUSTOMER_NAME, EMAIL, ADDRESS) VALUES
(1, 'Cole Baidoo', 'cbaidoo@sandtech.com', '123 Happiness Ave.');

