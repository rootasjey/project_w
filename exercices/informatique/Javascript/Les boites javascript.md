Les Boites JavaScript
=======================

{% python %}

width = random.randint(0,100)


enonce1 = """<span class="exoQuestion"> Le code Javascript suivant effectue des modifications sur une page HTML existante. Lesquels?</span>"""



code="""<pre><code>
	function lambda() {
	var elements = querySelectorAll('.box');
	for(int i = 0; i< elements.length; i++) {
	elements[i].style.width = """ + str(width) + """px;
	}
	}
</code></pre>"""



solution = """<br/><br/>
<span class="solutionButton">solution</span>
<div class="solutionArea">
<span class="exoSolution">
La fonction recupere tous les elements ayant la classe **box** et leur donne une largeur de **""" + str(width) + """px**
</span></div>"""


result = enonce1 + code + solution
return result


{% endpython %}