# -*- coding: utf8 -*-
"""This is the default application which launch the web app"""

import os, sys, codecs
# --------------------------------------
from packages.converter import converter
from packages.markdown import Markdown
from jinja2 import Template, Environment
from packages.python_extension.python_extension import PythonExtension
# --------------------------------------
from flask import Flask, request, render_template
# --------------------------------------


markdowner = Markdown()

# root folder of exercices
# ----------------------------
root_exercices = "exercices/"
root_lessons =  "lessons/"
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

# Filter to execute python code
@app.template_filter('exec')
def Exec_python(args):
    exec(args)


# Index route
@app.route('/')
def index():
	return render_template('/templates/index.html')


# About Page
@app.route('/about')
def about():
	path = ''
	path_about = 'static/md'
	files = os.listdir(path_about)
	for file in files:
		if 'About' in file:
			path = path_about + '/' + file
			break

	# open file with codecs for the markdown converter
	input_file = codecs.open(path, mode="r", encoding="utf-8")
	text = input_file.read()		# read
	input_file.close()				# clode

	html = markdowner.convert(text)	# conversion
	
	# page render
	return render_template('/static/html/other.html', htmlfile = html)


# Write Exercices
@app.route('/redaction', methods=['GET', 'POST'])
def redaction():
	if request.method == 'POST':
		return "vous avez rédigé un exercices"
	else:
		return render_template('/templates/redaction.html')


# Subjects
# --------
@app.route('/<practice>/')
def subjects(practice="exercices"):
	subjectsl = ""
	root_path = ""

	if practice == "exercices":
		root_path = root_exercices
	elif practice == "lessons":
		root_path = root_lessons

	subjectsl = os.listdir(root_path)
	return render_template('/static/html/subject.html', subjects = subjectsl,
														practice = practice)


# Chapters list 
# -------------
@app.route('/<practice>/<science>/')
def chapters(practice="exercices", science="informatique"):

	chosen_subject=""					 # chosen subject
	subjectsl = "" # subjects list
	root_path=""

	# check the practice type
	if practice=="exercices":
		root_path = root_exercices
	elif practice=="lessons":
		root_path = root_lessons

	subjectsl = os.listdir(root_path)


	# find subject's index
	for subject in subjectsl:
		if science == subject:
			chosen_subject = subject
			break
	
	# chapters list
	chaptersl = os.listdir(root_path + chosen_subject)
	return render_template('/static/html/chapter.html', practice = practice,
														chapters = chaptersl,
														subject = chosen_subject);




# Exercices/Lessons list
# --------------
@app.route('/<practice>/<science>/chapter/<int:id>', methods=['GET', 'POST'])
def chapter(practice="exercices", science="informatique", id=1):
	if request.method == 'GET':
		id = id - 1 				# start from 0
		memory = [] 				# .html files' indexes to remove

		chosen_subject=""			# chosen subject
		chaptersl=[]
		exoslessonsl=[]

		root_path = ""
		# subjectsl = os.listdir(root)
		if practice == "exercices":
			root_path = root_exercices
		elif practice == "lessons":
			root_path = root_lessons

		subjectsl = os.listdir(root_path)

		# find subject's index
		for subject in subjectsl:
			if science == subject:
				chosen_subject = subject
				break

		chaptersl = os.listdir(root_path + chosen_subject)
		exoslessonsl = os.listdir(root_path + chosen_subject + '/' + chaptersl[id])


		for index, exolesson in enumerate(exoslessonsl):
			
			if ".html" in exolesson:
				memory.append(index)
				# save .html indexes

		
		# remove .html files from the list ---------|
		cpt = 0
		deleted = 0
		while memory:
			del exoslessonsl[memory[cpt] - deleted]
			cpt += 1
			deleted += 1
			if deleted >= len(memory):
				break
		# ------------------------------------------|

		# return the html page
		return render_template('/static/html/chapterlist.html', practice = practice,
																science = science,
																id = id,
																exoslessons = exoslessonsl)


# Exercice/Lesson show
# -------------
@app.route('/<practice>/<science>/chapter/<int:id>/<work>/')
def work(practice="exercices", science="informatique", id=0, work=""):

	root_path=""
	if practice == "exercices":
		root_path = root_exercices
	elif practice == "lessons":
		root_path = root_lessons

	subjectsl = os.listdir(root_path) 	# subjects list
	chosen_subject=""					# subject chosen

	# find subject's index
	for subject in subjectsl:
		if science == subject:
			chosen_subject = subject
			break
	

	chaptersl = os.listdir(root_path + chosen_subject)
	exoslessonsl = os.listdir(root_path + chosen_subject + '/' + chaptersl[id])

	for index, ex in enumerate(exoslessonsl):
		if work in ex:
			path = root_path + chosen_subject + '/' + chaptersl[id] + '/'+ ex
			break

	# apply jinja2 parser
	page = render_template('/static/html/void.html', path = path)
	# apply markdown parser
	page = markdowner.convert(page)

	# render the page
	return render_template('/static/html/work.html',practice = practice,
													id = id,
													work = work,
													page = page)

# debug mode if the 
# application.py is launched
# ----------------------
if __name__ == '__main__':
	app.run(debug=True)