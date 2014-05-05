Echange de clef de Diffie-Hellman
=================================

{% python %}
	p = 17
	g = 3
	a = random.randint(1, 117)
	b = random.randint(1,17)
	\# 
	\# 
	\#
	enonce1 = """ <span class="exoSummary"> Alice et Bob veulent convenir d'un secret en utilisant le protocole d'echange de clef de Diffie-Hellman."""
	enonce1 += """ Ils se mettent d'accord pour le corps \\(Z/""" + str(p) +"Z\\)"""
	enonce1 += """ et pour le generateur \\(g = """ + str(g) + """\\)."""
	enonce1 += """ Alice choisit la clef secrete \\(a = """ + str(a) + """\\) et Bob \\(b = """ + str(b) + """\\). </span>"""
	\# 
	question1 = """<p class="exoQuestion"> 1. Calculez les clefs publiques de Alice et Bob. </p>"""
	\# 
	question2 = """<p class="exoQuestion"> 2. Calculez la clef partagee. </p>"""
	\# 
	\# 
	\# 
	enonce2 = """ <br/><span class="exoSummary"> Utilisez l'algorithme d'exponentiation binaire pour repondre aux
		deux questions. Ne donnez pas seulement les resultats finaux:
		developpez en detail les etapes du calcul. </span>"""
	\# 
	question3 = """<p class="exoQuestion"> 3. Calculez \\(""" + str(g) + """^{""" + str(100 * (p-1) + random.randint(1,4)) + """} \mod """ + str(p) + """\\). </p>"""
	\# 
	question4 = """<p class="exoQuestion"> 4. Calculez le logarithme en base """ +  str(g) + """ de \\(""" + str(pow(g, 3, p)) + """\\). </p>"""
	\# 
	\# 
	\# 
	\# --------valeur de retour----------
	exercice = enonce1 + question1 + question2 + enonce2 + question3 + question4
	\# ---------------------------------
	return exercice
	\# 
{% endpython %}

{% python %}
return ''
{% endpython %}