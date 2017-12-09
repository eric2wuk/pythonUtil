import mysql.connector

conn = mysql.connector.connect(user='root', password='root', database='test')
cursor = conn.cursor()

cursor.execute('create table user (id varchar(20) PRIMARY KEY, NAME VARCHAR (20))')

cursor.rowcount


