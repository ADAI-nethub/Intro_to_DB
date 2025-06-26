import mysql.connector
from mysql.connector import Error # Keep this import for general use if desired, but explicitly use mysql.connector.Error below

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
        'password': 'password' # Your MySQL password
    }

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

    except mysql.connector.Error as e: # Changed to explicitly use mysql.connector.Error
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
