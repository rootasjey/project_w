La Somme En Mille
=================
{% python %}
somme1 = random.randint(1,8)
somme2 = random.randint(8,32)
somme3 = random.randint(32,64)
somme4 = random.randint(64,2048)
\#
solution1 = (somme1 * (somme1 + 1))/2
solution2 = (somme2 * (somme2 + 1))/2
solution3 = (somme3 * (somme3 + 1))/2
solution4 = (somme4 * (somme4 + 1))/2
\#
enonce = """<span class="exoSummary">Calculez les sommes suivantes. Explicitez la methode si vous en utilisez une.</span>

+	\\(\sum\limits_{n=1}^{""" + str(somme1) + """} n\\)

+	\\(\sum\limits_{n=1}^{""" + str(somme2) + """} n\\)

+	\\(\sum\limits_{n=1}^{""" + str(somme3) + """} n\\)

+	\\(\sum\limits_{n=1}^{""" + str(somme4) + """} n\\)

"""
\#
solution = """<p><br/><br/><span class="solutionButton">solution</span> <div class="solutionArea">

+	<span class="exoSolution">Les valeurs des sommes sont : **""" + str(solution1) + """**, **""" + str(solution2) + """**, **""" + str(solution3) + """**, **""" + str(solution4) + """**</span>
"""
\#
result = enonce + solution
return result
{% endpython %}