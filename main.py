#!/usr/bin/python3
# coding: utf-8
# таки на питончике третьем все работает
from flask import (
	Flask, render_template, json, session, redirect, url_for, escape, request, send_from_directory
)
import logging
import hashlib
import os
from functools import reduce # бугага
from operator import add # бвзазваава

app = Flask(__name__)

m = hashlib.md5()

def makehash(*args):
	"""sha1(sha1(arg1) + sha1(arg2) + ... + sha1(argn))"""
	# потому что я могу
	sha1 = hashlib.sha1
	sequence = [sha1(n.encode('utf-8')).hexdigest() for n in args]
	return sha1(reduce(add, sequence, '').encode('utf-8')).hexdigest()


user = {'login': 'test', 'password': 'test'}

@app.route("/")
def index():
    return render_template('index.html',
		logged=int(bool(session.get('logged')))
	)

@app.route("/login", methods=['POST'])
def login():
	email = request.form['email']
	password = request.form['password']
	if email == user['login'] and password == user['password']:
		# '%s' % s <- валидно
		app.logger.info('Email: %s' % email)
		m.update((email + password).encode('utf-8'))
		sid = m.digest()
		# не совсем понял, зачем тебе sid
		session['logged'] = 1
		app.logger.info('sid: %s' % sid)
	else:
		app.logger.info('login incorrect')
		session['logged'] = 0
	return redirect(url_for('index'))

@app.route("/game/<gid>")
def game(gid):
	action = request.form['action']
	action_route = {'next':_next}
	
@app.route("/json/questions")
def questions():
	if session.get('logged'):	
		#with open('./static/json/questions.json') as json:
		#	return json.read()
		# депрекатед дуе то некрасиво
		# os.path.join, по хорошему, нужен
		filename = os.path.join('json', 'questions.json')
		# /static/json/questions.json
		return app.send_static_file(filename)
	else:
		return 'You are not logged in, sorry!'
		
@app.route("/json/question/<id>")
def getQuestion(qid):
	if session.get('logged'):	
		return 'We will get question from DB by qid here'
	else:
		return 'You a not logged in, sorry!'
		
	
def getGameSession(gid):
	return Session()

if __name__ == "__main__":
	app.secret_key = '9sabdf9(B&F(B9fa0bdb(&D(S&(0dbfas[f9'
	# ключ надо генерировать, это очевидно, но можно и забыть
	app.debug = True
	app.run()
