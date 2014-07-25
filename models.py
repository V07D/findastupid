# coding: utf-8
from peewee import * # да, я знаю, что это плохо

db = SqliteDatabase('database.db')

class _Session(object):
	"""Абстрактная модель для сессий"""
	_active = False
	def __init__(self, owner):
		self._active = True
		self._owner = owner

class GameSession(Model):
	is_active = BooleanField(default=False)
	gid = IntegerField()
	owner = ForeignKeyField(User, null=True)
	
	class Meta:
		database = db

class _User(object):
	"""Модель юзера"""
	def __init__(self, name, surname, hashsum):
		self._name = name
		self._surname = surname
		self._blah = blah # абстрактный код

class User(Model):
	current_session = ForeignKeyField(GameSession, null=True)
	# текущая игровая сессия, может быть пустой
	username = CharField()
	hashsum = CharField()
	
	class Meta:
		database = db

		
class SessionUsers(Model):
	session = ForeignKeyField(GameSession, null=True)
	user = ForeignKeyField(User, null=True)
	
	#SELECT u.username FROM User u, GameSession s, SessionUsers set WHERE u.id = set.user AND set.session = :PARAMETER:;


class Question(Model):
	"""Класс для вопросов"""
	id = IntegerField(primary_key=True)
	type = CharField()
	description = CharField()
	question = CharField()
	correct_answer = CharField()
	
	def check_answer(self, user_answer):
		"""Возвращает булево значение в зависимости от правильности ответа."""
		return user_answer == self.correct_answer
	
	def serialize_to_dict(self, with_answer=False):
		"""Сериализует экземпляр модели в словарь"""
		result = {
			'id': self.id,
			'type': self.type,
			'description': self.description,
			'question': self.question,
		}
		if with_answer:
			result['correct_answer'] = self.correct_answer
		return result
	
	class Meta:
		database = db
