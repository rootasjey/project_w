Saisissez les chats
====================

{% python %}

chats = random.randint(1,50)

enonce = """<span class="exoSummary">
	Le code python ci-dessous affiche differentes informations selon une condition. Explicitez ce code?
</span>"""

code = """<pre><code>
	chats = input("Comien de chats avez-vous? : ")
	chats = int(chats)
	if(chats < """ + str(chats) + """) print("Cela ne fait pas beaucoup de chats")
	else print('Vous avez """ + str(chats) + """ chats ?!')
</code></pre>"""

solution = """<p><br/><br/><span class="solutionButton">solution</span> <div class="solutionArea">
<span class="exoSolution">
	Le programme demande a l'utilisateur combien de chats il possede. S'il a moins de **""" + str(chats) + """** chats, alors le programme lui dit qu'il n'a pas beaucoup de chats, sinon il affiche **'Vous avez """ + str(chats) + """ chats?!'**
</span>
</div>"""

result = enonce + code + solution
return result

{% endpython %}