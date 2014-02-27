# -*- coding: utf8 -*-
"""This is the default application which launch the web app"""

import os, sys
from packages.jinja2 import Template
from packages.flask import Flask
from packages.converter import converter

app = Flask(__name__)

@app.route('/')
def index():
	return "BIENVENU(E) !"

@app.route('/contact/')
def contact():
	# mail = "jeremiecorpinot@outlook.com"
	tel = "01 23 45 67 89"
	return "Mail: {} --- Tel: {}".format(mail, tel)

if __name__ == '__main__':
	app.run(debug=True)