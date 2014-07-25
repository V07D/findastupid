	#!/usr/bin/python3
# coding: utf-8
# таки на питончике третьем все работает
from flask import Flask
from flask import render_template
from flask import json
from flask import session, redirect, url_for, escape, request
import logging
import hashlib

app = Flask(__name__)

m = hashlib.md5()

user = {"login":"test","password":"test"}

@app.route("/")
def index():
    return render_template('index.html',logged=int(bool(session.get('logged'))))

@app.route("/login",methods=['post'])
def login():
	email = request.form['email']
	password = request.form['password']
	if email == user['login'] and password == user['password']:
		app.logger.info('Email: %s' % (email,))
		m.update(email+password)
		sid = m.digest()
		session['logged'] = 1
		app.logger.info('sid: %s' % (sid,))
	else:
		app.logger.info('login incorrect')
		session['logged'] = 0
	return redirect(url_for('index'))

@app.route("/game/<gid>")
def game(gid):
	pass
	
@app.route("/json/questions")
def questions():
	if bool(session.get('logged')):	
		with open('static/json/questions.json') as json:
			return json.read()
	else:
		return 'You a not logged in, sorry!'
	
def getGameSession(gid):
	return Session()

if __name__ == "__main__":
	app.secret_key = '9sabdf9(B&F(B9fa0bdb(&D(S&(0dbfas[f9'
	app.run(debug=True)
