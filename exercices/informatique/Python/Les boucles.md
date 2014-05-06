Les Boucles
===========


{% python %}
a = random.randint(0,200)
b = random.randint(0,200)
if(a\>b):
	a,b=b,a
\#
enonce = """ Combien d'elements seront affiches par ce code?"""
code = """

    for(i in range( """ + str(a) + """,""" + str(b) + """)) {
    print i
    }
"""
\#
solution = """<p><br/><br/><span class="solutionButton">solution</span> <div class="solutionArea">

+	<span class="exoSolution">Il y aura **""" + str(b - a) + """** elements affiches</span>

</p></div>"""
return enonce + code + solution
{% endpython %}
