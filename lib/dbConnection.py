

import mysql.connector

host = "localhost"
user = "root"
password = "27511112086/2019"
database="cars_db"

mydb = mysql.connector.connect(host=host, user=user, password=password, database=database)

print(mydb)

cursor = mydb.cursor()

cursor.execute("show databases")

for item in cursor:
    print(item)
