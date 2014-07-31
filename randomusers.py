# coding: utf-8
from flask import Blueprint, jsonify
import random
import os

randomusers = Blueprint('randomusers', __name__, static_folder='static')


names = [
    'Чоткий',
    'Ровный',
    'Мутный',
]
surnames = [
    'Честный',
    'Сложный',
    'Дерзкий'
]

directory = os.path.join('static', 'img', 'avatars')
avatars = list(os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('jpg'))

@randomusers.route('/get')
def get():
    return jsonify(data={
        'name': '{name} {surname} '.format(
            name=random.choice(names),
            surname=random.choice(surnames)
        ),
        'avatar': random.choice(avatars).replace('\\', '/')
    })