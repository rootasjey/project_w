# -*- coding: utf8 -*-
"""This is the default application which launch the web app"""

import os, sys

from packages.converter import converter
from jinja2 import Template
from flask import Flask, request, render_template

# try:
	# from packages.jinja2 import Template
	# from packages.flask import Flask, request, render_template
# except Exception as e:
# 	print e
# 	os.system('pause')


app = Flask(__name__, template_folder='')

@app.context_processor
def passer_titre():
	return dict(welcomeMessage= 'Visiteur')

@app.route('/')
def index():
	return render_template('/templates/index.html')



@app.route('/domaine/')
def domains():
	domainsl = os.listdir('exercices/')
	return render_template('/static/html/domaine.html', domains = domainsl)

@app.route('/domaine/informatique/')
def informatique():
	domainsl = os.listdir('exercices/')
	chaptersl = os.listdir('exercices/' + domainsl[0])
	# for chap in chaptersl:
	# 	exerc = os.listdir('exercices/' + domainsl[0] + '/' + chap)
	return render_template('/static/html/informatique.html', chapitres = chaptersl);

@app.route('/domaine/maths/')
def maths():
	domainsl = os.listdir('exercices/')
	chaptersl = os.listdir('exercices/' + domainsl[1])
	return render_template('/static/html/maths.html', chapitres = chaptersl);

@app.route('/domaine/informatique/chapitre/<int:id>', methods=['GET', 'POST'])
def exercices(id=1):
	if request.method == 'GET':
		id = id - 1 #commencer à 0
		domainsl = os.listdir('exercices/')
		chaptersl = os.listdir('exercices/' + domainsl[0])
		exercicesl = os.listdir('exercices/' + domainsl[0] + '/' + chaptersl[id])
		print exercicesl
		return render_template('/static/html/chapitre.html', id = id, exercices = exercicesl)
		

if __name__ == '__main__':
	app.run(debug=True)