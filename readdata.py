# Program to create a INSERT data into a table
import pymysql
db = pymysql.connect("localhost", "root", "suman", "food");
c = db.cursor();
sql = """SELECT * FROM food_name"""
try:
    print("Database Connection Successfull");
    c.execute(sql);
    res = c.fetchall();
    for rows in res:
        a = rows[0];
        b = rows[1];
        c = rows[2];
        print("id : ", a);
        print("Food Name : ", b);
        print("Country of Origin : ", c);
    db.close();
except DatabaseError:
    print("Error in database connection");
