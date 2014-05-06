Ne jamais jeter l'eponge
==========================
{% python %}
attempts = 0
maxAttempts = random.randint(5,42)
\#
enonce = """
<span class="exoSummary">Le code python suivant utilise la structure de block try/except. Pouvez-vous expliquer ce qui se passe en detail lors de l'execution?</span><p>

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
</p>"""
\#
solution = """<p><br/><br/><span class="solutionButton">solution</span> <div class="solutionArea">

+	<span class="exoSolution">La fonction essaie d'etablir une connexion avec un serveur. Tant que le nombre d'essais ne depasse pas **""" + str(maxAttempts) + """**, la fonction **EtablishAConnection** est appelee recursivement dans le block **except**.</span>

</p></div>"""
\#
result = enonce + solution
return result
{% endpython %}