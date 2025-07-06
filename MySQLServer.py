import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL server (update user and password if needed)
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='MJMUSIC'
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except Error as e:
    print(f"Error while connecting to MySQL: {e}")

finally:
    # Always close the cursor and connection
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
