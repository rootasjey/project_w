# -*- coding: utf8 -*-
"""This file contains a set of test functions to check if
everything works well"""

import os, sys
from packages.jinja2 import Template
from packages.flask import Flask
from packages.converter import converter

try:
	converter.convertMDtoHTML()
except NameError as detail:
	print detail
	os.system('pause')

template = Template('Hello {{name}}!')
print template.render(name='John Doe')

os.system('pause')
