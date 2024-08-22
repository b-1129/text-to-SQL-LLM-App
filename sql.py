import sqlite3

## Connect sqlite
connection=sqlite3.connect("student.db")

## create a cursor object to insert record, create table, retireve
cursor= connection.cursor()

## create a table
table_info= """
create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25), MARKS INT);
"""
cursor.execute(table_info)

## Insert some records

cursor.execute('''Insert into STUDENT values("John","Data Science", "A", 90)''')
cursor.execute('''Insert into STUDENT values("Johny","Data Science", "B", 80)''')
cursor.execute('''Insert into STUDENT values("Bobby","Web Dev", "C", 100)''')
cursor.execute('''Insert into STUDENT values("celina","Data Science", "D", 80)''')
cursor.execute('''Insert into STUDENT values("julia","Web Dev", "E", 90)''')
cursor.execute('''Insert into STUDENT values("james","Data Science", "F", 85)''')
cursor.execute('''Insert into STUDENT values("eliana","Web Dev", "E", 70)''')
cursor.execute('''Insert into STUDENT values("kristina","Data Science", "G", 45)''')

## Display all the records

print("The inserted records are")

data=cursor.execute('''select * from STUDENT''')

for row in data:
    print(row)

## close the connection

connection.commit()
connection.close()