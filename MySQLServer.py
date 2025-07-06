import mysql.connector

try:
    # Connect to MySQL Server (not to any specific database)
    connection = mysql.connector.connect(
        host='localhost',
        user='root',             # ✅ your actual MySQL username
        password='yourpassword'  # ✅ your actual MySQL password
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
        cursor.close()

except mysql.connector.Error as e:
    print(f"Error connecting to MySQL: {e}")

finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
