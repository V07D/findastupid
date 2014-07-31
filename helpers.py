# coding: utf-8
import hashlib
from flask import session, redirect, url_for
from functools import wraps

def makehash(*args):
	"""sha1(sha1(arg1) + sha1(arg2) + ... + sha1(argn))"""
	# потому что я могу
	sha1 = hashlib.sha1
	sequence = [sha1(n.encode('utf-8')).hexdigest() for n in args]
	return sha1(''.join(sequence).encode('utf-8')).hexdigest()

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('logged'):
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function
