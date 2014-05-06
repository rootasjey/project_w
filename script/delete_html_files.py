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
from packages.converter import converter		  #|
												  #|
# --------------------------------------------------

# Ask to delete .html files
converter.cleanFiles(True)
os.system('pause')