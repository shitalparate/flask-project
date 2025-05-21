
print("prograaming")

import mysql.connector


connection= mysql.connector.connect(host="localhost" ,username="root", password="123456",database="home_builder")

print(f"{connection}")

cursor=connection.cursor()

# cursor.execute("select * from labours_table")
insert_query = "select * from labours_table"
cursor.execute(insert_query)
cursor.fetchall()
# print("enter the new data")
connection.close()
cursor.close()

# result=cursor.fetchall()
# print(result)