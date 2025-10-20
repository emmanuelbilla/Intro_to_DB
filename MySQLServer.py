"""
Script to create the 'alx_book_store' database if it does not already exist.
"""

import MySQLdb
import sys

def create_database():
    try:
        # Connect to MySQL server (no database selected yet)
        db = MySQLdb.connect(
            host="localhost",
            user="root",
            passwd="your_password"  # replace with your MySQL root password
        )
        cursor = db.cursor()

        # Create database if it doesn’t exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
        print("Database 'alx_book_store' created or already exists.")

    except MySQLdb.Error as e:
        print(f"Error: {e}")

    finally:
        if db:
            db.close()

if __name__ == "__main__":
    create_database()
