# -*- coding: utf8 -*-
"""This is the default application which launch the web app"""

import os, sys
import flask, jinja2
from packages.jinja2 import Template
from packages.flask import Flask, request, render_template
from packages.converter import converter


app = Flask(__name__, template_folder='')

@app.context_processor
def passer_titre():
	return dict(welcomeMessage= 'Visiteur')

@app.route('/')
def index():
	return render_template('/templates/index.html')



@app.route('/domains/')
def domains():
	domainsl = os.listdir('exercices/')
	return render_template('/static/html/domains.html', domains = domainsl)

@app.route('/domains/informatique')
def informatique():
	domainsl = os.listdir('exercices/')
	chaptersl = os.listdir('exercices/' + domainsl[0])
	for chap in chaptersl:
		exerc = os.listdir('exercices/' + domainsl[0] + '/' + chap)
		print exerc
	return render_template('/static/html/domains_informatique.html', chapitres = chaptersl);

@app.route('/domains/maths')
def maths():
	domainsl = os.listdir('exercices/')
	chaptersl = os.listdir('exercices/' + domainsl[1])
	return render_template('/static/html/domains_maths.html', chapitres = chaptersl);

# @app.route('/domains/informatique/<chapitre>')
# def exercices():
# 	domainsl = os.listdir('exercices/')
# 	chaptersl = os.listdir('exercices/' + domainsl[0])

if __name__ == '__main__':
	app.run(debug=True)