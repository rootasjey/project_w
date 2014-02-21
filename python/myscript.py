# -*-coding:Latin-1 -*

import os, sys
from py_packages.markdown import Markdown
from jinja2 import Template

markdowner = Markdown()
print markdowner.convert("*boo!*")

template = Template('Hello {{name}}!')
print template.render(name='John Doe')
# chemin du dossier d'exercices
# exercices_folder = """exercices/"""
# dirs = os.listdir(exercices_folder)
# print dirs

# récupère chaque exercice au format .md
# # et affiche son contenu dans le terminal
# for course in dirs:
# 	# print ("\n\n" + course)
# 	files = os.listdir(exercices_folder + course)
# 	for file in files:
# 		# print("\n" + file)
# 		chars = file[-3:]
# 		# print chars
# 		if ".md" in chars:
# 			full_path = exercices_folder + course + "/" + file
# 			# print full_path
# 			with open(full_path, 'r') as exercice_file:
# 				text = exercice_file.read()
# 				# print markdowner.convert(text)
# 				new_path = str.replace(full_path, file, file[:-2] + "html")
# 				# print new_path

# 				with open(new_path, 'w') as html_file:
# 					html_file.write(markdowner.convert(text))
# 					print("\nConversion : " + file)

os.system('pause')