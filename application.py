# -*- coding: utf8 -*-
"""This is the default application which launch the web app"""

import os, sys
from packages.jinja2 import Template
from packages.flask import Flask, request, render_template
from packages.converter import converter

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html', welcomeMessage="visiteur")

@app.route('/contact/')
def contact():
	mail = "jeremiecorpinot@outlook.com"
	tel = "01 23 45 67 89"
	return "Mail: {} --- Tel: {}".format(mail, tel)

if __name__ == '__main__':
	app.run(debug=True)