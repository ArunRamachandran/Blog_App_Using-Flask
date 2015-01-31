import sqlite3

con = sqlite3.connect('comments.db')
con.execute("DROP TABLE IF EXISTS comments")
con.execute("CREATE TABLE comments(id INT NOT NULL, name TEXT NOT NULL, comment TEXT NOT NULL)")
