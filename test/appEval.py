
import os, sys


from packages.converter import converter
from jinja2 import Template
from flask import Flask, request, render_template

app = Flask(__name__, template_folder='')

@app.route('/testEval')
def testEval():
	return render_template('/Tests/testEval.html')
@app.template_filter('eval_filtre')
def Evaluer_args(var1):
    return eval(var1)
@app.template_filter('exec_filtre')
def Executer_args(code):
	exec code



if __name__ == '__main__':
	app.run(debug=True)