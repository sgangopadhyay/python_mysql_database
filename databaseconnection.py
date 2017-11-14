# Program to connect to a MySQL database
import pymysql
try:
    db = pymysql.connect("localhost", "root", "suman", "food");
    cursor = db.cursor();
    print("Database Connection Successfull");
    db.close();
except DatabaseError:
    print("Error in database connection");
