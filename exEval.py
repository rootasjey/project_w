#!/usr/bin/env python
from math import *
import os, sys
def call_Eval(block):
	print open(block).read()


	#make a list of safe functions
safe_list = ['math','acos', 'asin', 'atan', 'atan2', 'ceil', 'cos', 'cosh', 'degrees', 'e', 'exp', 'fabs', 'floor', 'fmod', 'frexp', 'hypot', 'ldexp', 'log', 
'log10', 'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh']
# utiliser la liste pour filtrer le namespace local
safe_dict = dict([ (k, locals().get(k, None)) for k in safe_list ])
# ajouter des builtins nécessaires
safe_dict['abs'] = abs

user_function = raw_input("type a function: y = ")

for x in range(1,10):
	# ajouter x
	safe_dict['x']=x
	print "x = ", x , ", y = ", eval(user_function,{"__builtins__":None},safe_dict)
os.system('pause')

