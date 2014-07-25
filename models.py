# coding: utf-8
from peewee import * # да, я знаю, что это плохо

db = SqliteDatabase('database.db')

class _Session(object):
	"""Абстрактная модель для сессий"""
	_active = False
	def __init__(self, users):
		self._users = users

class Session(Model):
	is_active = BooleanField(default=False)
	
	class Meta:
		database = db	


class _User(object):
	"""Модель юзера"""
	def __init__(self, name, surname, hashsum):
		self._name = name
		self._surname = surname
		self._blah = blah # абстрактный код

class User(Model):
	current_session = ForeignKeyField(Session, null=True)
	# текущая игровая сессия, может быть пустой
	username = CharField()
	hashsum = CharField()
	
	class Meta:
		database = db
	
class Question(Model):
	"""Класс для вопросов"""
	_id = IntegerField()
	
