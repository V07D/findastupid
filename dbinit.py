# coding: utf-8
from models import User, GameSession, Question

for model in (User, GameSession, Question):
	try:
		model.drop_table()
	except Exception as e:
		pass
	finally:
		model.create_table()
