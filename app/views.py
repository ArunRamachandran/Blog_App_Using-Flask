from flask import render_template, redirect, url_for, session, flash
from app import app
import sys
import sqlite3 as lite
import os
from flask import request

new_post = []
comments = []

@app.route('/')
@app.route('/blog', methods = ['POST'])
def blog():
	
#	con = lite.connect('posts.db')
#	with con:
#		cur = con.cursor()
#		name = []
#		rows = []
#		cursor = cur.execute("SELECT name,post FROM posts")
		
#		for row in cursor:
#			rows.append(row)
	user = { 'name' : 'Arun' }
	new  = { 'posted' : 'The Movie was a good one !!'}
	new_post.append(new)
	
	
	return render_template('blog.html', title="Blogger", user=user, new_post=new_post)


@app.route('/comment', methods=['POST', 'GET'])
def comment():
	user = { 'name':'Arun'}
	name = request.form['name'] 
	comment = request.form['comments']
#	new_post = new_post

	new_comment = { 'name' : name, 'comment' : comment }
	comments.append(new_comment)
		
	if name == '' or comment == '':
		return ''' 
		<html>
			<head>
			<title>Error !</title>
			</head>
			<body>	
				<center>
				<h3>Please Provide Valid Data</h3>
				</center>
			</body>
		</html>'''

	return render_template('comment.html', title='Home', user=user, name=name,comments=comments,new_post=new_post)

@app.route('/login')
def login():
	return render_template('login.html', title="LogIn") 

@app.route('/new_user', methods = ['GET', 'POST'])
def new_user():
	userid = request.form['userid']
	password = request.form['password']

	if userid == '' or password =='':
		return render_template('invalid.html', title='Error !')
	return render_template('post.html', title='Home-Blogger')

@app.route('/process', methods=['POST','GET'])
def process():
	title = request.form['title']
	post  = request.form['text']

	user  = {'name' : 'Arun'}
	latest= {'posted' : post }

	new =[]
	new.append(latest)


	new_post.append(latest)
	return render_template('blog.html', title='Blogger', user=user, new_post=new)

@app.route('/myblogs', methods=['GET', 'POST'])
def myblogs():
	l = len(new_post)
	blogs = new_post
	user  = {'name' : 'Arun'}

	return render_template('view.html', title="My Blogs", user=user, blogs=blogs)

@app.route('/view', methods =['GET', 'POST'])
def view():
	return render_template('login.html', title="LogIn")

@app.route('/about', methods = ['GET', 'POST'])
def about():
	return '''
	<html>
		<head>
		<title>About Me</title>
		</head>
		<body>
		<h2>About me... </h2>
		</br>
		<h3>Contents will Update Sooon...</h3>
		</body>
	</html>'''
