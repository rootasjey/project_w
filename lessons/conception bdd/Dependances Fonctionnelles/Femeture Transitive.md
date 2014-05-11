Fermeture d'un ensemble
=======================

Soit X un ensemble d'attributs et F un ensemble de Dépendances Fonctionnelles (DF).
On appelle **fermeture de X** par rapport à F, l'ensemble de tous les attributs qu'on peut déduire de X par des DF.
On le note \\(X^+ \\)


###Algorithme
1. Initialiser \\( X^+ \\) à X
2. Trouver une DF de F dont la partie gauche contient des éléments de \\( X^+ \\)
3. Ajouter dans \\( X^+ \\) les attributs placés en partie droite de la DF
4. Répéter les étapes à partir de 2 jusqu'à ce que \\( X^+ \\) n'évolue plus


###Exemple
\\( F = \\{ A \rightarrow C, A  \rightarrow E, B  \rightarrow D, C  \rightarrow D, BE  \rightarrow G, DE  \rightarrow C \\} \\)

Chercher la fermeture de AD

1. \\( \\{AD^+\\} = \\{AD\\} \\)
2. \\( A \rightarrow C \ et \  A \rightarrow E \implies  \bbox[5px, border:2px solid black]{\\{AD^+\\} = \\{ACDE\\}} \\)