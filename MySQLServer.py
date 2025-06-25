
#!/usr/bin/env python3

import mysql.connector

# Database connection details
# IMPORTANT: For a production environment, avoid hardcoding sensitive info.
# For local root user on Linux Mint, sometimes an empty password works
# if 'auth_socket' plugin is configured for your system user.
# If connection fails, you might need to set a password for MySQL root user
# or create a dedicated user for your application.
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'MyNewPassword123!',  # Try empty string first. If it fails, you'll need to update this.
    # We are not specifying a database here because we want to create one.
}

DATABASE_NAME = "alx_book_store"

def create_database():
    """
    Connects to MySQL server and attempts to create the alx_book_store database.
    Handles connection errors and ensures the database is created if it doesn't exist.
    """
    cnx = None  # Initialize connection variable to None
    try:
        # Establish the connection to the MySQL server
        # We don't specify a database here because we want to create it.
        print(f"Attempting to connect to MySQL server as user '{DB_CONFIG['user']}'...")
        cnx = mysql.connector.connect(**DB_CONFIG)
        cursor = cnx.cursor()

        # SQL statement to create the database if it does not exist
        # Using uppercase for SQL keywords as per requirements
        create_db_query = f"CREATE DATABASE IF NOT EXISTS {DATABASE_NAME}"

        print(f"Executing: {create_db_query}")
        cursor.execute(create_db_query)

        print(f"Database '{DATABASE_NAME}' created successfully!")

    except mysql.connector.Error as err:
        # Handle different types of MySQL errors
        if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Access denied. Check your username and password.")
            print("Hint: For root user on Linux, sometimes no password works, or you might need to set one.")
            print("       Alternatively, create a dedicated MySQL user with a password for scripts.")
        elif err.errno == mysql.connector.errorcode.CR_CONN_HOST_ERROR:
            print(f"Error: Could not connect to MySQL host '{DB_CONFIG['host']}'. Is the MySQL server running?")
        else:
            print(f"An unexpected MySQL error occurred: {err}")
    except Exception as e:
        # Handle other potential Python errors
        print(f"An unexpected error occurred: {e}")
    finally:
        # Ensure the connection is closed even if an error occurs
        if cnx:
            print("Closing database connection.")
            cnx.close()

if __name__ == "__main__":
    create_database()

