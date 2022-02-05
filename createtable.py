# Program to create a TABLE
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
    sql = """CREATE TABLE FOOD_NAME(ID INT(3), ITEM VARCHAR(20), COUNTRY VARCHAR(20))"""
    c.execute(sql);
    print("TABLE created successfully !");
    db.close();
except DatabaseError:
    print("Error in database connection");
