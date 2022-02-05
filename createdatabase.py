# Program to create a new database
import pymysql
try:
    db = db = pymysql.connect(
            host="localhost",
            user="root",
            password="suman",
            db="guvi"
        )
    c = db.cursor();
    print("Database Connection Successfull");
    sql = """CREATE DATABASE food"""
    c.execute(sql);
    print("Database Created !");
    db.close();
except DatabaseError:
    print("Error in database connection");
