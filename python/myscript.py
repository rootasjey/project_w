# -*-coding:Latin-1 -*

import os, sys
# import py_packages.markdown
from py_packages.markdown import Markdown

# print py_packages.markdown.markdown("*boo!*")

markdowner = Markdown()
# print markdowner.convert("*boo!*")


# chemin du dossier d'exercices
exercices_folder = """exercices/"""
dirs = os.listdir(exercices_folder)
# print dirs

# récupère chaque exercice au format .md
# et affiche son contenu dans le terminal
for course in dirs:
	# print ("\n\n" + course)
	files = os.listdir(exercices_folder + course)
	for file in files:
		# print("\n" + file)
		chars = file[-3:]
		# print chars
		if ".md" in chars:
			full_path = exercices_folder + course + "/" + file
			# print full_path
			with open(full_path, 'r') as exercice_file:
				text = exercice_file.read()
				# print markdowner.convert(text)
				new_path = str.replace(full_path, file, file[:-2] + "html")
				# print new_path

				with open(new_path, 'w') as html_file:
					html_file.write(markdowner.convert(text))
					print("\nConversion : " + file)

os.system('pause')