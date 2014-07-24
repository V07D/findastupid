#!/usr/bin/python3
# coding: utf-8
# таки на питончике третьем все работает
from flask import Flask
from flask import render_template
from flask import json
from flask import session, redirect, url_for, escape, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')    

@app.route("/game/<gid>")
def game(gid):
	pass
	
def getGameSession(gid):
	return Session()

if __name__ == "__main__":
	app.run(debug=True)
