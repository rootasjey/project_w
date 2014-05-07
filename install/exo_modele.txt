;; This buffer is for notes you don't want to save, and for Lisp evaluation.
;; If you want to create a file, visit that file with C-x C-f,
;; then enter the text in that file's own buffer.

## Échange de clef de Diffie-Hellman

<%
from random import randrange 
p = 17
g = 3
a = randrange(17)
b = randrange(17)
%>

Alice et Bob veulent convenir d'un secret en utilisant le
protocole d'échange de clef de Diffie-Hellman. Ils se mettent
d'accord pour le corps $$\mathbb{Z}/\sage{p}\mathbb{Z}$$ et pour
le générateur $$g = {{ g }}$$. Alice choisit la clef secrète
$$a = {{ a }}$$ et Bob $$b = {{ b }}$$.

1. Calculez les clefs publiques de Alice et Bob.

2. Calculez la clef partagée.

Utilisez l'algorithme d'exponentiation binaire pour répondre aux
deux questions. Ne donnez pas seulement les résultats finaux:
développez en détail les étapes du calcul. 

3. Calculez $${{ g }}^{ {{ 100 * (p-1) + randrange(1,4) }} } \mod {{ p }}$$.

4. Calculez le logarithme en base $$g$$ de $${{ pow(g, 3, p) }}$$.

