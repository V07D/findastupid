# coding: utf-8
from flask import (
	Flask, render_template, json, session, redirect, url_for, escape, request, send_from_directory, jsonify
)
from flask.ext.login import LoginManager
import logging
import hashlib
import os
from functools import reduce, wraps
import logic
import models
from helpers import makehash, login_required

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)

from jayson import jayson
app.register_blueprint(jayson, url_prefix='/json')

from randomusers import randomusers
app.register_blueprint(randomusers, url_prefix='/randomusers')

m = hashlib.md5() # не знаю, что ты этим имел в виду, но это неправильно в корне

user = {'login': 'test', 'password': 'test'}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
	email = request.form['email']
	password = request.form['password']
	if email == user['login'] and password == user['password']:
		app.logger.info('Email: %s' % email)
		m.update((email + password).encode('utf-8')	)
		sid = m.digest()
		session['logged'] = True
		app.logger.info('sid: %s' % sid)
	else:
		app.logger.info('login incorrect')
		session['logged'] = 0
	return redirect(url_for('index'))

@app.route('/login/status')
def login_status():
	'''Returns JSON with status of user login: logged (True) or not logged (False).'''
	logged = session.get('logged') or False
	return jsonify(logged=logged)

@app.route('/logout')
def logout():
	session.pop('logged', None)
	return redirect(url_for('index'))

@app.route('/question/check_answer/')
def check_answer():
	answer = request.args.get('answer')
	id = request.args.get('id')
	question = models.Question.get(id=int(id))
	return jsonify(result=question.check_answer(answer))


@app.route('/game/<gid>')
def game(gid):
	action = request.form['action']
	#action_route выпилил, потому что пришлось бы трахаться с функциями-обертками
	if action == 'next':
		logic.next_question(gid)

	
@app.route('/register', methods=['GET', 'POST'])
def register():
	if request.method == 'POST':
		email = request.form['email']
		username = request.form['username']
		password = request.form['password']
		#TODO: validate
		hashsum = makehash(username, email, password)
		user = Models.User.create(username=username, hashsum=hashsum)
		session['logged'] = True
		session['sid'] = makehash(username) #TODO: реализовать это на нормальном механизме сессий. Сейчас семи-секьюрно, потому что, все-таки, sid шифруется второй раз в куках.
		# нахуя хранить sid в куках? нихуя не понял, например
		
		
	return redirect(url_for('index'))


def get_user(name):
	user = models.User.get(name=name)


if __name__ == '__main__':
	app.secret_key = '9sabdf9(B&F(B9fa0bdb(&D(S&(0dbfas[f9'
	# ключ надо генерировать, это очевидно, но можно и забыть
	app.debug = True
	app.run()
