# Program to create a TABLE
import pymysql
try:
    db = pymysql.connect("localhost", "root", "suman", "food");
    c = db.cursor();
    print("Database Connection Successfull");
    sql = """CREATE TABLE FOOD_NAME(ID INT(3), ITEM VARCHAR(20), COUNTRY VARCHAR(20))"""
    c.execute(sql);
    print("TABLE created successfully !");
    db.close();
except DatabaseError:
    print("Error in database connection");
