# Program to connect to a MySQL database
import pymysql
try:
    db = db = pymysql.connect(
            host="localhost",
            user="root",
            password="suman",
            db="guvi"
        )
    cursor = db.cursor();
    print("Database Connection Successfull");
    db.close();
except DatabaseError:
    print("Error in database connection");
