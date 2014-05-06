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
	# if(cleanFiles(False)):
	# 	deleteFiles(path)
	# os.system('pause')


# -------------------------------------------------------------
# Delete specifics files with the match extension (.md or .html)
# -------------------------------------------------------------
# _attempts = 0
# _maxAttempts = 2
def deleteFiles(path="exercices/", extensions = ".html", attempts = 0):
	"""Function which look for files ending with 'extentions' (parameter)
				at the 'path' specified, and delete them"""

	# if attempts < 2:
	# 	try:
	# 		dirs = os.listdir(path)
	# 	except:
	# 		if attempts == 0:
	# 			attempts += 1
	# 			newpath = "../../exercices/"
	# 			deleteFiles(newpath, attempts)
	# 		elif attempts == 1:
	# 			attempts += 1
	# 			newpath = "../exercices/"
	# 			deleteFiles(newpath, attempts)
	# 		else: return 'error'
	# else: 
	# 	return 'Cannot delete files'
	

	dirs = ""

	try:
		dirs = os.listdir(path)
	except WindowsError:
		print ">Recover the path to delete files..."
		try:
			print  ">Second attempt, recorvery..."
			path = "../../exercices/"
			dirs = os.listdir(path)
		except WindowsError:
			path = "../exercices/"
			dirs = os.listdir(path)
		

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
def cleanFiles(self):
	userinput = raw_input("Do you want to delete .html files? (Y/N) ")
	userinput = userinput.lower()
	if((userinput == 'y') | (userinput == 'yes') | (userinput== 'o') | (userinput == 'oui')):
		print "Deleteing .html file in progress... "
		if self == True:
			deleteFiles()
		else: return True
	else:
		print ".html files was not deleted"
		return False


# ----------------------
# TEST ----------------->
# ----------------------
# Run this code if this file 
# is the main app
if __name__ == '__main__':
	print("TEST PACKAGE")
	# convertMDtoHTML()
	cleanFiles(True)
	os.system('pause')