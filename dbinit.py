# coding: utf-8
from models import *

for model in (User, GameSession, SessionUsers, Question):
	try:
		model.drop_table()
	except Exception as e:
		pass
	finally:
		model.create_table()
