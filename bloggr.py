# all the imports
#import sqlite3
import MySQLdb
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from contextlib import closing

#configuration
DEBUG = True
SECRET_KEY = '\xa2\xab\x9c\x02\xaf\x8d\xb2^\x11R\n8\xed\xbf\xe4\xe2\x9cM@\xca\xc0\x1d\x95\x92'
USERNAME = 'admin'
PASSWORD = 'default'

conn = MySQLdb.connect (host = "localhost",
                        user = "root",
                        passwd = "***REMOVED***",
                        db = "blog")
cur = conn.cursor()

# create our little application
app = Flask(__name__)
app.config.from_object(__name__)

def query_db(query):
	return curr.execute(query)


@app.before_request
def before_request():
	g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
	db = getattr(g, 'db', None)
	if db is not None:
		db.close()

@app.route('/')
def show_entries():
	cur = g.db.execute('select title, text from entries order by id desc')
	entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
	return render_template('show_entries.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
	if not session.get('logged_in'):
		abort(401)
	g.db.execute('insert into entries (title, text) values (?, ?)',[request.form['title'], request.form['text']])
	g.db.commit()
	flash('New entry was successfully posted')
	return redirect(url_for('show_entries'))

@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method =='POST':
		if request.form['username'] != app.config['USERNAME']:
			error = 'Invalid username'
		elif request.form['password'] != app.config['PASSWORD']:
			error = 'Invalid password'
		else:
			session['logged_in'] = True
			flash('You were logged in')
			return redirect(url_for('show_entries'))
	return render_template('login.html', error=error)

@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	flash('You were logged out')
	return redirect(url_for('show_entries'))


if __name__ == '__main__':
	app.run()

