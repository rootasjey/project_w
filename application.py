# -*- coding: utf8 -*-
"""This is the default application which launch the web app"""

import os, sys

from packages.converter import converter
from jinja2 import Template
from flask import Flask, request, render_template

# dossier racine des exercices
root = "exercices/"

# -------------------/
# --- ~ APP ~ ------/
# -----------------/
app = Flask(__name__, template_folder='')

# Valeurs par défault
@app.context_processor
def passer_titre():
	return dict(welcomeMessage = 'Visiteur')

# index route
@app.route('/')
def index():
	return render_template('/templates/index.html')

# matières
@app.route('/domaine/')
def domains():
	domainsl = os.listdir(root)
	return render_template('/static/html/domaine.html', domains = domainsl)

# liste des chapitres informatique
@app.route('/domaine/informatique/')
def informatique():
	domainsl = os.listdir(root)
	chaptersl = os.listdir(root + domainsl[0])
	return render_template('/static/html/informatique.html', chapitres = chaptersl);

# liste des chapitres maths
@app.route('/domaine/maths/')
def maths():
	domainsl = os.listdir(root)
	chaptersl = os.listdir(root + domainsl[1])
	return render_template('/static/html/maths.html', chapitres = chaptersl);

# liste des exos
@app.route('/domaine/informatique/chapitre/<int:id>', methods=['GET', 'POST'])
def chapter(id=1):
	if request.method == 'GET':
		id = id - 1 # commence à 0
		# book = []	# contiendra le contenu des exos
		memory = [] # contiendra les index des fichiers .md a retirer
		domainsl = os.listdir(root)
		chaptersl = os.listdir(root + domainsl[0])
		exercicesl = os.listdir(root + domainsl[0] + '/' + chaptersl[id])

		for index, ex in enumerate(exercicesl):
			
			if ".md" in ex:
				memory.append(index)
				# sauvegarde l'index des .md
				# continue # on passe à l'exo suivant
			
			# path = root + domainsl[0] + '/' + chaptersl[id] + '/'+ ex
			# with open(path, 'r') as work:
			# 			text = work.read()
			# 			book.append(text)	# ajoute l'exo dans le book

		
		# retire les fichiers .md de la liste ------|
		cpt = 0
		deleted = 0
		while memory:
			del exercicesl[memory[cpt] - deleted]
			cpt += 1
			deleted += 1
			if deleted >= len(memory):
				break
		# ------------------------------------------|

		# affichage de la page
		return render_template('/static/html/chapitre.html', id = id,
															 exercices = exercicesl)


@app.route('/domaine/informatique/chapitre/<int:id>/<exercice>/')
def exercice(id, exercice):
	domainsl = os.listdir(root)
	chaptersl = os.listdir(root + domainsl[0])
	exercicesl = os.listdir(root + domainsl[0] + '/' + chaptersl[id])

	for index, ex in enumerate(exercicesl):
		if exercice in ex:
			path = root + domainsl[0] + '/' + chaptersl[id] + '/'+ ex
			break;

	# affichage de la page
	return render_template('/static/html/exercice.html', id = id,
														 exercice = exercice,
														 path = path)
	
# run en debug si l'user
# exec application.py
if __name__ == '__main__':
	app.run(debug=True)