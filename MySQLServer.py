import mysql.connector
from mysql.connector import Error

def create_alx_book_store_database():
    """
    Connects to a MySQL server and attempts to create the 'alx_book_store' database.
    If the database already exists, the script will not fail due to 'IF NOT EXISTS'.
    Handles connection errors and ensures the database connection is properly closed.
    """
    # IMPORTANT: Database configuration details.
    # For production environments, it is highly recommended to retrieve these
    # credentials from secure environment variables, a secrets management service,
    # or a dedicated configuration file, rather than hardcoding them directly
    # in the script for security reasons.
    DB_CONFIG = {
        'host': 'localhost', # The hostname or IP address of your MySQL server
        'user': 'root',      # Your MySQL username
        'password': 'MyNewPassword123!' # Your MySQL password
    }

    connection = None
    cursor = None
    try:
        # Establish a connection to the MySQL server.
        # We connect without specifying a database initially, as we are creating one.
        print(f"Attempting to connect to MySQL server at {DB_CONFIG['host']} with user '{DB_CONFIG['user']}'...")
        connection = mysql.connector.connect(
            host=DB_CONFIG['host'],
            user=DB_CONFIG['root'],
            password=DB_CONFIG['MyNewPassword123!']
        )
        print("Successfully connected to MySQL server.")

        cursor = connection.cursor()

        # Define the SQL query to create the database.
        # The 'IF NOT EXISTS' clause is crucial as it prevents an error if
        # a database with the same name already exists, fulfilling the requirement.
     # CREATE DATABASE
        create_db_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"
        print(f"Executing query: '{create_db_query}'")
        cursor.execute(create_db_query)
        print("Database 'alx_book_store' created successfully!")

        # SHOW DATABASES
        print("Showing all databases:")
        cursor.execute("SHOW DATABASES")
        for db in cursor.fetchall():
            print(f" - {db[0]}")

        # Connect to the newly created database
        connection.database = "alx_book_store"

        # CREATE TABLE
        create_table_query = """
        CREATE TABLE IF NOT EXISTS books (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            author VARCHAR(255) NOT NULL
        )
        """
        cursor.execute(create_table_query)
        print("Table 'books' ensured.")

        # INSERT SAMPLE DATA
        insert_query = "INSERT INTO books (title, author) VALUES (%s, %s)"
        sample_data = [
            ("The Alchemist", "Paulo Coelho"),
            ("1984", "George Orwell"),
            ("To Kill a Mockingbird", "Harper Lee")
        ]
        connection = None
    cursor = None
    try:
        # Establish a connection to the MySQL server.
        # We connect without specifying a database initially, as we are creating one.
        print(f"Attempting to connect to MySQL server at {DB_CONFIG['host']} with user '{DB_CONFIG['user']}'...")
        connection = mysql.connector.connect(
            host=DB_CONFIG['host'],
            user=DB_CONFIG['user'],
            password=DB_CONFIG['password']
        )
        print("Successfully connected to MySQL server.")

        cursor = connection.cursor()

        # Define the SQL query to create the database.
        # The 'IF NOT EXISTS' clause is crucial as it prevents an error if
        # a database with the same name already exists, fulfilling the requirement.
        create_db_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"

        print(f"Executing query: '{create_db_query}'")
        cursor.execute(create_db_query)

        # Commit the transaction to apply the changes to the database.
        connection.commit()

        print("Database 'alx_book_store' created successfully!")

    except Error as e:
        # Catch and handle any errors that occur during connection or query execution.
        # This includes issues like incorrect credentials, host unreachable, etc.
        print(f"Error: Failed to connect to the database or create 'alx_book_store'.")
        print(f"Details: {e}")
    finally:
        # Ensure that the cursor and connection are closed to release resources,
        # regardless of whether an error occurred or not.
        if cursor:
            print("Closing database cursor.")
            cursor.close()
        if connection and connection.is_connected():
            print("Closing database connection.")
            connection.close()
        print("Database operation concluded.")

if __name__ == "__main__":
    # This block ensures that create_alx_book_store_database() is called
    # only when the script is executed directly (not when imported as a module).
    create_alx_book_store_database()