# coding: utf-8
from flask import Flask, Blueprint, json, url_for, jsonify
from helpers import login_required
import os.path
from models import Question

jayson = Blueprint('json', __name__, static_folder='static')

@jayson.route('/questions/')
@login_required
def questions():
    return jsonify(questions=Question.serialize_all())

@jayson.route('/question/<id>')
@login_required
def question(id):
    return jsonify(question=Question.get(id=id).serialize_to_dict())