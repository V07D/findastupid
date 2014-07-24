# coding: utf-8

class User:
	__init__(self):
		self._name = ''
		self._surname = ''
	
class Session: 
	_state = 'INACTIVE'
	def __init__(self,users):
		self._users = users
	
	
