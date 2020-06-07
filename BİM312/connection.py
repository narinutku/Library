import mysql.connector
import _sqlite3


connection=mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    database="library"
)

#("INSERT INTO book (Name,Author,Genre,Publishing House,Publication Date,Language,Number of Copies) VALUES (%s,%s,%s,%s,%s,%s,%s)"