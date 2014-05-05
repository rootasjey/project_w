# -*- coding: utf8 -*-
"""This is the default application which launch the web app"""

import os, sys
# ------------
from packages.converter import converter
from jinja2 import Template, Environment
from packages.python_extension.python_extension import PythonExtension
# -----------------------------------------------
from flask import Flask, request, render_template


# dossier racine des exercices
# ----------------------------
root = "exercices/"
# ----------------------------


# -------------------/
# --- ~ APP ~ ------/
# -----------------/
app = Flask(__name__, template_folder='')
app.jinja_env.add_extension(PythonExtension)


# Valeurs par défault
@app.context_processor
def passer_titre():
	return dict(welcomeMessage = 'Visiteur')


# Filtre évaluant du code python
@app.template_filter('eval')
def Evaluer_args(args):
    return eval(args)


# Index route
@app.route('/')
def index():
	return render_template('/templates/index.html')


# Matières
@app.route('/subject/')
def subjects():
	subjectsl = os.listdir(root)
	return render_template('/static/html/subject.html', subjects = subjectsl)


# Rédaction des exos
@app.route('/redaction/')
def redaction():
	return render_template('/templates/redaction.html')


# Liste des chapitres 
@app.route('/subject/<science>/')
def chapters(science="informatique"):
	chosen=""	# matiere choisie
	subjectsl = os.listdir(root)

	if science == "informatique":
		chosen = subjectsl[0]
	elif science == "maths":
		chosen = subjectsl[1]

	chaptersl = os.listdir(root + chosen)
	return render_template('/static/html/'+ chosen +'.html', chapitres = chaptersl);


# Liste des exos
@app.route('/subject/<science>/chapitre/<int:id>', methods=['GET', 'POST'])
def chapter(id=1, science="informatique"):
	if request.method == 'GET':
		id = id - 1 # commence à 0
		# book = []	# contiendra le contenu des exos
		memory = [] # contiendra les index des fichiers .md a retirer
		subjectsl = os.listdir(root)
		chaptersl=[]
		exercicesl=[]
		if science == "informatique":
			chaptersl = os.listdir(root + subjectsl[0])
			exercicesl = os.listdir(root + subjectsl[0] + '/' + chaptersl[id])
		else:
			chaptersl = os.listdir(root + subjectsl[1])
			exercicesl = os.listdir(root + subjectsl[1] + '/' + chaptersl[id])
		

		for index, ex in enumerate(exercicesl):
			
			if ".html" in ex:
				memory.append(index)
				# sauvegarde l'index des .md
				# continue # on passe à l'exo suivant
			
			# path = root + subjectsl[0] + '/' + chaptersl[id] + '/'+ ex
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
															 science = science,
															 exercices = exercicesl)


# Présentation de l'exercice
@app.route('/subject/<science>/chapitre/<int:id>/<exercice>/')
def exercice(id=0, science="informatique", exercice="exercice1.html"):
	subjectsl = os.listdir(root) # liste des matières
	domain=""					 # matières choisie

	if science == "informatique":
		domain = subjectsl[0]

	elif science == "maths":
		domain = subjectsl[1]


	chaptersl = os.listdir(root + domain)
	exercicesl = os.listdir(root + domain + '/' + chaptersl[id])

	for index, ex in enumerate(exercicesl):
		if exercice in ex:
			path = root + domain + '/' + chaptersl[id] + '/'+ ex
			break;

	# conversion du document .md en .html
	converter.ConvertSingleFileToHTML(path)
	extension=".md"
	path = str.replace(path, extension, ".html")

	# affichage de la page
	return render_template('/static/html/exercice.html', id = id,
														 exercice = exercice,
														 path = path)
	
# run en debug si l'user
# exec application.py
if __name__ == '__main__':
	app.run(debug=True)