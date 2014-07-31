# coding: utf-8
import hashlib
from flask import session, redirect, url_for
from functools import wraps
import re

def makehash(*args):
	"""
	Returns string (hashsum) created from args:
	sha1(sha1(arg1) + sha1(arg2) + ... + sha1(argn))

	Usage:
	>>> makehash('John Doe', 'SuPaRsEcretpwd1337')
	'84d2814d87e6259dc8f4f0553e820f1a0aadbbee'
	"""
	algoritm = hashlib.sha1
	sequence = [algoritm(n.encode('utf-8')).hexdigest() for n in args]
	return algoritm(''.join(sequence).encode('utf-8')).hexdigest()

def login_required(f):
	"""
	Decorator for flask.
	"""
	@wraps(f)
	def decorated_function(*args, **kwargs):
		if not session.get('logged'):
			return redirect(url_for('login'))
		return f(*args, **kwargs)
	return decorated_function

def register_validate(data): # TODO: сделать красиво
							 # делается красиво через flask-wtf
	"""
	Checks if data is valid.
	data is a dict:
	{
		'email': str,
		'username' str
	}
	Returns boolean value.
	"""
	if data['email']:
		if not '@' in data['email']:
			return False
		else:
			pass #Проверки на спецсимволы
	else:
		return False #Если нет email, фейл
	if data['username'] and len(data['username'] > 3):
		pass #Проверки на спецсимволы
	else:
		return False
	
	
