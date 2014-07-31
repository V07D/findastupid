# coding: utf-8
"""
Типа, генерируем вопросы и суём их в бд, чтобы тестить!
"""
from models import Question
import random

blank = {
    'id': 0, # надо инкрементить
    'type': 'input'
}

for i in range(50):
    blank['id'] += 1
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    blank['description'] = '{a} + {b} = ?'.format(a=a, b=b)
    blank['question'] = '<input id={id}>'.format(id=blank['id'])
    blank['correct_answer'] = str(a + b)
    Question.create(**blank)