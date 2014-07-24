#!/usr/bin/python3
# coding: utf-8
# таки на питончике третьем все работает
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == "__main__":
	app.run(debug=True)
