La Somme En Mille
=================
{% python %}
_somme1 = random.randint(1,8)
_somme2 = random.randint(8,32)
_somme3 = random.randint(32,64)
_somme4 = random.randint(64,2048)

_solution1 = (_somme1 * (_somme1 + 1))/2
_solution2 = (_somme2 * (_somme2 + 1))/2
_solution3 = (_somme3 * (_somme3 + 1))/2
_solution4 = (_somme4 * (_somme4 + 1))/2

_enonce = """<span class="exoSummary">
Calculez les sommes suivantes. Explicitez la methode si vous en utilisez une </span>"""

_exo = """<ul>
<li> \\\(\\sum\\limits_{n=1}^{""" + str(_somme1) + """} n\\\)</li><br/>""" + """
<li> \\\(\\sum\\limits_{n=1}^{""" + str(_somme2) + """} n\\\)</li><br/>""" + """
<li> \\\(\\sum\\limits_{n=1}^{""" + str(_somme3) + """} n\\\)</li><br/>""" + """
<li> \\\(\\sum\\limits_{n=1}^{""" + str(_somme3) + """} n\\\)</li><br/>
</ul>"""

solution = """<span class="solutionButton">solution</span>
<div class="solutionArea">
<ul>
<li>{0}</li>
<li>{1}</li>
<li>{2}</li>
<li>{3}</li>
</ul></div>""".format(_solution1,_solution2,_solution3, _solution4)

_result = _enonce + _exo + solution
return _result
{% endpython %}