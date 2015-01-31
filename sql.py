import sqlite3 as lite
import sys

con = lite.connect('posts.db')

with con:
	cur = con.cursor()
	cur.execute("DROP TABLE IF EXISTS posts")
	cur.execute("CREATE TABLE posts (id INT PRIMARY KEY, name TEXT, post TEXT)")
	cur.execute("INSERT INTO posts (id, name, post) values(1, 'Arun', 'The avangers movie was a nice one !')")


