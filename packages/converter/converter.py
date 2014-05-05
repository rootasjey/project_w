# -*- coding: utf8 -*-
"""The CONVERTER PACKAGE is used to
convert exercices from .md format to .html format.
A function checks if new files has been added or updated."""

import os, sys
# Add 'webbapp' module in the PYTHONPATH
# Allow the import of Markdown module,
# even if we are in a sub-folder (so we climb the arborescence)
folder = os.path.dirname(os.path.abspath(__file__))
while not folder.endswith('webbapp'):
	folder = os.path.dirname(folder)

if folder not in sys.path:
	sys.path.append(folder)
#  -------------------------------------------------
from packages.markdown import Markdown 			  #|
markdowner = Markdown()							  #|
# --------------------------------------------------


# ------------------------------------------------
# FUNCTIONS --------------------------------------->
# ------------------------------------------------


# ---------------------------------
# Convert one file from .md to .html
# ---------------------------------
def ConvertSingleFileToHTML(path=""):
	if path == "":
		return

	extension = ".md"
	if path.endswith(extension):
		# open file
		with open(path, 'r') as exercice:
			text = exercice.read()
			# create a new absolute path (for the new file) > replacing the extension
			new_path = str.replace(path, extension, ".html")
			# create a new file
			with open(new_path, 'w') as html_file:
				# conversion + write in the new file
				html_file.write(markdowner.convert(text)) 


# ----------------------------------------------------------------
# Convert multiple files from .md -> .html
# Take one parameter : root folder
# root folder must contains subjects, then chapters, and finally exercices
# It won't work properly if the arborescence changes (must adapt)
# ----------------------------------------------------------------
def convertMDtoHTML(path = "exercices/"):
	"""Look for .md files (exercices) in the path (parameter),
				and convert them in .html with markdown module"""

	# listdir folders list 
	try:
		dirs = os.listdir(path)
	except WindowsError as detail:
		print detail
		print ">Try to recorver the path..."
		path = "../../exercices/"
		dirs = os.listdir(path)

	extensions = ".md"
	file_path = ''
	
	for discipline in dirs:
		file_path = path + discipline + '/'
		courses = os.listdir(file_path)
		# for each chapter of a subject
		for course in courses:
			file_path = path + discipline + '/' + course + '/'
			files = os.listdir(file_path)
			# for each exercice in a chapter
			for file in files:
				# verify that our file get the right extension
				if file.endswith(extensions):
					file_path = path + discipline + '/' + course + '/' + file
					# open the file
					with open(file_path, 'r') as exercice:
						text = exercice.read()
						# create a new absolute path (for the new file) > replacing the extension
						new_path = str.replace(file_path, file, file[:-2] + "html")
						# create a new file
						with open(new_path, 'w') as html_file:
							# conversion + write in the new file
							html_file.write(markdowner.convert(text)) 
							print("Conversion : " + file + " > " + file[:-2] + "html")
	
	# ask the user if he wants to delete original files
	# if(cleanFiles()):
	# 	deleteFiles(path)
	# os.system('pause')


# -------------------------------------------------------------
# Delete specifics files with the match extension (.md or .html)
# -------------------------------------------------------------
def deleteFiles(path="exercices/", extensions = ".html"):
	"""Fonction qui recherche les fichiers de type 'extentions' (passé en paramètre)
				au chemin 'path' spécifié, et les supprime"""

	try:
		dirs = os.listdir(path)
	except WindowsError:
		print ">Recover the path to delete files..."
		path = "../../exercices/"

	file_path = ''
	
	for discipline in dirs:
		file_path = path + discipline + '/'
		courses = os.listdir(file_path)
		# for each chapter of a subject
		for course in courses:
			file_path = path + discipline + '/' + course + '/'
			files = os.listdir(file_path)
			# for each exercice in a chapter
			for file in files:
				# verify that our file get the right extension
				if file.endswith(extensions):
					file_path = path + discipline + '/' + course + '/' + file
					print("Suppression de {}".format(file_path))
					os.remove(file_path)


# ---------------------------------------
# Ask for the deletions of files 
# ---------------------------------------
def cleanFiles():
	userinput = raw_input("Voulez-vous supprimer les fichiers .html? (Y/N) ")
	userinput = userinput.lower()
	if((userinput == 'y') | (userinput == 'yes') | (userinput== 'o') | (userinput == 'oui')):
		print "Suppression des fichiers .html en cours... "
		return True
	else:
		print "Les fichiers .html ont ete conserves"
		return False


# ----------------------
# TEST ----------------->
# ----------------------
# Run this code if this file 
# is the main app
if __name__ == '__main__':
	print("TEST PACKAGE")
	convertMDtoHTML()
	# deleteFiles()
	os.system('pause')