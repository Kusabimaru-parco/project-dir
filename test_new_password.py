# test_mysql.py
import mysql.connector

try:
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='newpassword123',
        port=3306
    )
    print("✅ MySQL connection successful!")
    conn.close()
except Exception as e:
    print(f"❌ MySQL failed: {e}")