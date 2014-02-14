# -*-coding:Latin-1 -*

import os, sys

# chemin du dossier d'exercices
exercices_folder = """exercices/"""
dirs = os.listdir(exercices_folder)
# print dirs

# récupère chaque exercice au format .md
# et affiche son contenu dans le terminal
for course in dirs:
	print ("\n\n" + course)
	files = os.listdir(exercices_folder + course)
	for file in files:
		print("\n" + file)
		full_path = exercices_folder + course + "/" + file
		# print full_path
		with open(full_path, 'r') as exercice_file:
			text = exercice_file.read()
			print(text)

os.system('pause')