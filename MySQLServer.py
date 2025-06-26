import mysql.connector
from mysql.connector import Error

def create_database():
    """
    Creates the 'alx_book_store' database in MySQL server.
    Handles connection errors and ensures clean resource management.
    """

    DB_CONFIG = {
        'host': 'localhost',
        'user': 'root',
        'password': 'MyNewPassword123!'  # Change this to your actual MySQL password
    }

    connection = None
    cursor = None

    try:
        # Connect to MySQL server (without specifying a database)
        print(f"Connecting to MySQL server at {DB_CONFIG['host']}...")
        connection = mysql.connector.connect(
            host=DB_CONFIG['host'],
            user=DB_CONFIG['user'],
            password=DB_CONFIG['password']
        )
        print("Connection successful.")

        cursor = connection.cursor()

        # Create database if it doesn't exist
        create_db_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"
        cursor.execute(create_db_query)
        print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print("Error: Failed to connect to the database or create 'alx_book_store'.")
        print(f"Details: {e}")

    finally:
        # Ensure cursor and connection are closed
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()
        print("Database connection closed.")

if __name__ == "__main__":
    create_database()
