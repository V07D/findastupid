# coding: utf-8
import models
import random
from helpers import makehash

MAX_QUESTIONS = 5

def next_question(user, session):
	pass
	
def start(user):
	all_questions = Question.select()
	questions = random.sample(list(all_questions, MAX_QUESTIONS))
	game = models.GameSession.create(owner=uid, is_active=True, questions=serialize(questions))

def getQuestion(gid):
    pass

def login(username, password):
    """
    Returns True if there is user with this username and password,
    otherwise returns false
    """
    hashsum = makehash(username, password)
    try:
        models.User.get(username=username, hashsum=hashsum)
        return True
    except:
        return False

class Game(object):
    """
    Было бы пиздец как удобно с помощью такого объекта делать всё, например, сериализуя его.
    """