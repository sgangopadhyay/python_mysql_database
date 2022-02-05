# Program to create a INSERT data into a table
import pymysql
db = db = pymysql.connect(
            host="localhost",
            user="root",
            password="suman",
            db="guvi"
        )
c = db.cursor();
sql = """INSERT INTO FOOD_NAME(ID, ITEM, COUNTRY) VALUES(5, 'Spegitti', 'Spain')"""
try:
    print("Database Connection Successfull");
    c.execute(sql);
    db.commit();
    print("Data Inserted into Table Successfully !");
    db.close();
except DatabaseError:
    print("Error in database connection");
