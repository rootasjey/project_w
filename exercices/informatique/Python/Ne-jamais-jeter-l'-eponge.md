Ne jamais jeter l'eponge
==========================
{% python %}

attempts = 0
maxAttempts = random.randint(5,42)

enonce = """<span class="exoQuestion">
Le code python suivant utilise la structure de block try/except. Pouvez-vous expliquer ce qui se passe en détail lors de l'exécution?</span>"""

code = """<pre><code>
    attempts = """ + str(attempts) + """
    maxAttempts = """ + str(maxAttempts) + """
    def EtablishAConnection():
	    try :
	    	connect(server)
	    except :
	    	if attemps < maxAttempts:
	    		maxAttemp++
	    		EtablishAConnection()
	    	else: DropTheSponge()
</code></pre>"""



solution = """<br/><br/>
<span class="solutionButton">solution</span>
<div class="solutionArea">
<span class="exoSolution">
	La fonction essaie d'établir une connexion avec un serveur. Tant que le nombre d'essais ne depasse pas **""" + str(maxAttempts) + """**, la fonction **EtablishAConnection** est appelée récursivement dans le block **except**.
</span>
</div>"""

result = enonce + code + solution
return result
{% endpython %}