# -*- coding: utf8 -*-
"""This is the default application which launch the web app"""

import os, sys
# --------------------------------------
from packages.converter import converter
from jinja2 import Template, Environment
from packages.python_extension.python_extension import PythonExtension
# --------------------------------------
from flask import Flask, request, render_template
# --------------------------------------

from flask import request

# root folder of exercices
# ----------------------------
root = "exercices/"
# ----------------------------


# -------------------/
# --- ~ APP ~ ------/
# -----------------/
app = Flask(__name__, template_folder='')
app.jinja_env.add_extension(PythonExtension)


# Default values
@app.context_processor
def passer_titre():
	return dict(welcomeMessage = 'Visiteur')


# Filter to eval python code
@app.template_filter('eval')
def Evaluer_args(args):
    return eval(args)


# Index route
@app.route('/')
def index():
	return render_template('/templates/index.html')

#cours
@app.route('/cours')
def cours():
	return render_template('/templates/cours.html')

@app.route('/cours/info')
def coursInfo():
	return render_template('/templates/coursInfo.html')

@app.route('/cours/math')
def coursMath():
	return render_template('/templates/coursMath.html')


# Subjects
@app.route('/subject/')
def subjects():
	subjectsl = os.listdir(root)
	return render_template('/static/html/subject.html', subjects = subjectsl)




# Rédaction des exos
@app.route('/redaction', methods=['GET', 'POST'])
def redaction():
	if request.method == 'POST':
		return "vous avez rédigé un exercices"
	else:
		return render_template('/templates/redaction.html')


# Chapters list 
# -------------
@app.route('/subject/<science>/')
def chapters(science="informatique"):
	chosen=""					 # chosen subject
	subjectsl = os.listdir(root) # subjects list

	# find subject's index
	for subject in subjectsl:
		if science == subject:
			chosen = subject
			break;
	
	# chapters list
	chaptersl = os.listdir(root + chosen)
	return render_template('/static/html/chapter.html', chapters = chaptersl,
															 subject = chosen);


# Exercices list
# --------------
@app.route('/subject/<science>/chapter/<int:id>', methods=['GET', 'POST'])
def chapter(id=1, science="informatique"):
	if request.method == 'GET':
		id = id - 1 				 # start from 0
		# book = []					 # exercices' content
		memory = [] 				 # .html files' indexes to remove

		chosen=""					 # chosen subject
		subjectsl = os.listdir(root)
		chaptersl=[]
		exercicesl=[]

		# find subject's index
		for subject in subjectsl:
			if science == subject:
				chosen = subject
				break

		chaptersl = os.listdir(root + chosen)
		exercicesl = os.listdir(root + chosen + '/' + chaptersl[id])


		for index, ex in enumerate(exercicesl):
			
			if ".html" in ex:
				memory.append(index)
				# save .html indexes
				# continue # next exercice
			
			# path = root + subjectsl[0] + '/' + chaptersl[id] + '/'+ ex
			# with open(path, 'r') as work:
			# 			text = work.read()
			# 			book.append(text)	# ajoute l'exo dans le book

		
		# remove .html files from the list ------|
		cpt = 0
		deleted = 0
		while memory:
			del exercicesl[memory[cpt] - deleted]
			cpt += 1
			deleted += 1
			if deleted >= len(memory):
				break
		# ------------------------------------------|

		# return the html page
		return render_template('/static/html/exercice.html', id = id,
															 science = science,
															 exercices = exercicesl)


# Exercice show
# -------------
@app.route('/subject/<science>/chapter/<int:id>/<exercice>/')
def exercice(id=0, science="informatique", exercice="exercice1.html"):
	subjectsl = os.listdir(root) # subjects list
	chosen=""					 # subject chosen

	# find subject's index
	for subject in subjectsl:
		if science == subject:
			chosen = subject
			break;
	
	chaptersl = os.listdir(root + chosen)
	exercicesl = os.listdir(root + chosen + '/' + chaptersl[id])

	for index, ex in enumerate(exercicesl):
		if exercice in ex:
			path = root + chosen + '/' + chaptersl[id] + '/'+ ex
			break;

	# convert .md to .html
	converter.ConvertSingleFileToHTML(path)
	extension=".md"
	path = str.replace(path, extension, ".html")

	# return page
	return render_template('/static/html/work.html', id = id,
														 exercice = exercice,
														 path = path)
	
# debug mode if the 
# application.py is launched
# ----------------------
if __name__ == '__main__':
	app.run(debug=True)
# ----------------------
