# -*- coding: utf8 -*-
"""The CONVERTER PACKAGE is used to
convert exercices from .md format to .html format.
A function checks if new files has been added or updated."""

import os, sys
# Ajoute le module racine 'webbapp' dans le PYTHONPATH
# Permet d'importer le module Markdown, même si on se
# trouve dans un sous-doosier (>remonte l'arborescence des fichiers)
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
# Convertit un fichier .md en .html
# ---------------------------------
def ConvertSingleFileToHTML(path=""):
	if path == "":
		return

	extension = ".md"
	if path.endswith(extension):
		# ouverture du fichier
		with open(path, 'r') as exercice:
			text = exercice.read()
			# création du nouveau chemin absolu (du nouveau fichier) > en replaçant l'extension
			new_path = str.replace(path, extension, ".html")
			# création du nouveau fichier
			with open(new_path, 'w') as html_file:
				# conversion + écriture dans le nouveau fichier
				html_file.write(markdowner.convert(text)) 


# ----------------------------------------------------------------
# Convertit un ensemble de fichiers .md -> .html
# Prend en paramètre un répertoire racine  qui doit contenir
# des répertoires matières, puis des chapitres, et enfin des exos
# ----------------------------------------------------------------
def convertMDtoHTML(path = "exercices/"):
	"""Fonction qui cherche des fichiers .md (exercices) contenus
				à l'adresse du chemin passé en paramètre,
				et les convertit en .html grâce au module markdown"""

	# listdir liste les dossiers 
	# et fichiers au chemin 
	# absolu passé en paramètre
	try:
		dirs = os.listdir(path)
	except WindowsError as detail:
		print detail
		print ">Récupération du chemin du dossier d'exercice..."
		path = "../../exercices/"
		dirs = os.listdir(path)

	extensions = ".md"
	file_path = ''
	
	for discipline in dirs:
		file_path = path + discipline + '/'
		courses = os.listdir(file_path)
		# pour chaque cours d'une discipline
		for course in courses:
			file_path = path + discipline + '/' + course + '/'
			files = os.listdir(file_path)
			# pour chaque exercice d'un cours
			for file in files:
				# vérifie que notre fichier a la bonne extension
				if file.endswith(extensions):
					file_path = path + discipline + '/' + course + '/' + file
					# ouverture du fichier
					with open(file_path, 'r') as exercice:
						text = exercice.read()
						# création du nouveau chemin absolu (du nouveau fichier) > en replaçant l'extension
						new_path = str.replace(file_path, file, file[:-2] + "html")
						# création du nouveau fichier
						with open(new_path, 'w') as html_file:
							# conversion + écriture dans le nouveau fichier
							html_file.write(markdowner.convert(text)) 
							print("Conversion : " + file + " > " + file[:-2] + "html")
	
	# demande à l'utilisateur s'il veut suprimmer les fichiers de génération
	# if(cleanFiles()):
	# 	deleteFiles(path)
	# os.system('pause')


# -------------------------------------------------------------
# Supprime les fichiers d'une certaine extension (.md ou .html)
# -------------------------------------------------------------
def deleteFiles(path="exercices/", extensions = ".html"):
	"""Fonction qui recherche les fichiers de type 'extentions' (passé en paramètre)
				au chemin 'path' spécifié, et les supprime"""

	try:
		dirs = os.listdir(path)
	except WindowsError:
		print ">Récupération du chemin du dossier de fichiers a supprimer..."
		path = "../../exercices/"

	file_path = ''
	
	for discipline in dirs:
		file_path = path + discipline + '/'
		courses = os.listdir(file_path)
		# pour chaque cours d'une discipline
		for course in courses:
			file_path = path + discipline + '/' + course + '/'
			files = os.listdir(file_path)
			# pour chaque exercice d'un cours
			for file in files:
				# vérifie que notre fichier a la bonne extension
				if file.endswith(extensions):
					file_path = path + discipline + '/' + course + '/' + file
					print("Suppression de {}".format(file_path))
					os.remove(file_path)


# ---------------------------------------
# Demande pour la suppression de fichiers 
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

# TEST ----------------->
# s'exécute si ce fichier 
# est lancé en standalone
if __name__ == '__main__':
	print("TEST PACKAGE")
	convertMDtoHTML()
	# deleteFiles()
	os.system('pause')