Petits Calculs
==============
{% python %}
a = random.randint(0,10)
b = random.randint(0,20)
c = random.randint(0,8)

enonce = """<span class="exoQuestion"> Quelles seront les valeurs affichees? </span>"""
code = """
<pre><code>int a = """ + str(a) + """
int b = """ + str(b) + """
int c = """ + str(c) + """
print(a/b);
print(b+c);
print(a*c);</code></pre>
"""

solution = """<br/><br/><span class="solutionButton">solution</span><div class="solutionArea">
<span class="exoSolution">Les valeurs affichees sont : **""" + str(a/b) + """**, **""" + str(b+c) + """** et **""" + str(a*c) + """**</span></div>"""

result = enonce + code + solution
return result
{% endpython %}
