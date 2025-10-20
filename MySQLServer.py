#!/usr/bin/python3
"""
Python script to create the 'alx_book_store' database if it does not already exist.
"""

import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (no specific database selected)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password"  # 🔒 replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
            print("Database 'alx_book_store' created or already exists.")

    except Error as e:
        print(f"Error: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()
