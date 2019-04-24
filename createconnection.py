import sqlite3

conn = sqlite3.connect('rqpmain.db')
print("Opened database successfully")

conn.execute('CREATE TABLE questions (unum TEXT, ques TEXT, ans TEXT)')
print("Table created successfully")
conn.close()