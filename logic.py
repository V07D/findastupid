import models
import random

MAX_QUESTIONS = 5

def next(user,session):
	pass
	
def start(user):
	all_questions = Question.select()
	questions = random.sample(list(all_questions, MAX_QUESTIONS))
	game =  models.GameSession.create(owner=uid, is_active=True, questions=serialize(questions))
	
