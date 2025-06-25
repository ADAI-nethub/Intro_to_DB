-- task_4.sql

-- This script prints the full description of the 'BOOKS' table
-- from the database specified as an argument to the mysql command.
-- It avoids using DESCRIBE or EXPLAIN statements as per the requirements.

SELECT
    COLUMN_NAME,
    COLUMN_TYPE,
    IS_NULLABLE,
    COLUMN_KEY,
    COLUMN_DEFAULT,
    EXTRA
FROM
    INFORMATION_SCHEMA.COLUMNS
WHERE
    TABLE_SCHEMA = DATABASE() -- DATABASE() function gets the current database name used by the connection
    AND TABLE_NAME = 'BOOKS'
ORDER BY
    ORDINAL_POSITION;

