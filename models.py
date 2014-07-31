# coding: utf-8
from peewee import *

db = SqliteDatabase('database.db')

class BaseModel(Model):
	"""
	Base class for models.
	"""
	class Meta:
		database = db


class User(BaseModel):
	"""
	User model for minimalists.
	"""
	username = CharField()
	hashsum = CharField()


class GameSession(BaseModel):
	"""
	Game session model.
	"""
	is_active = BooleanField(default=False)
	gid = IntegerField() # на самом деле, айдишник уже есть в модели по умолчанию
	owner = ForeignKeyField(User, null=True)
	
	def get_users(self):
		"""
		Returns users who are involved in this game session.
		"""
		return (
			User.select()
			.join(SessionUsers)
			.join(GameSession)
			.where(SessionUsers.session == self)
		)

	
class SessionUsers(BaseModel):
	"""
	Implementation for any-to-many relation of GameSession and User models.
	"""
	session = ForeignKeyField(GameSession, null=True)
	user = ForeignKeyField(User, null=True)
	correct_answers = IntegerField()


class Question(BaseModel):
	"""Model for questions"""
	id = IntegerField(primary_key=True) # айдишник уже есть в модели по умолчанию
	type = CharField()
	description = CharField()
	question = CharField()
	correct_answer = CharField()
	
	def check_answer(self, user_answer):
		"""Returns True if user answer is correct, otherwise False"""
		return user_answer == self.correct_answer
	
	def serialize_to_dict(self, with_answer=False):
		"""Serializes this model into dict"""
		result = {
			'id': self.id,
			'type': self.type,
			'description': self.description,
			'question': self.question,
		}
		if with_answer:
			result['correct_answer'] = self.correct_answer
		return result
	
	@classmethod
	def serialize_all(cls, with_answers=False):
		"""Serializes all questions into list of dicts"""
		result = []
		for question in Question.select():
			result.append(question.serialize_to_dict(with_answer=with_answers))
		return result

if __name__ == '__main__':
	'''
	небольшие проверочки
	'''
	u = User.create(username='yoba', hashsum='123')
	u2 = User.create(username='yobayoba', hashsum='456')
	gs = GameSession.create(gid=30)
	su = SessionUsers.create(session=gs, user=u)
	su2 = SessionUsers.create(session=gs, user=u2)
	for user in gs.get_users():
		print(user.username)
