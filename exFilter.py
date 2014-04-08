import re
from jinja2 import evalcontextfilter, Markup, escape
import os, sys
from jinja2.utils import Markup, escape, pformat, urlize, soft_unicode
from jinja2.exceptions import FilterArgumentError, SecurityError


# quelques filtres :)

@evalcontextfilter
def to_replace(eval_ctx, stingS, old, new, count = None):
	# retourner une copie de la valeur de toutes les occurences de la sous chaine remplacé pour une nouvelle
	# le premier arg est la sous chaine qui doit etre remplacé 
	# le second arg est la chaîne de remplacement.
	# si l'optionnel arg "count" est donné, juste les premiers "count" sont remplacés


	# exemple de ce que ma fonction doit faire {{ "Salut toi"|replace("toi", "Somia") }}
            # -> Salut somia 

    if count is None:
    	# si le paramètre "count" égale "None", nous imprimons à la place une valeur spéciale (-1). Cela évite la TypeError.
    	count = -1
    if not eval_ctx.autoescape:
    	# si l'autoscaping n'est pas activé:
    	return unicode(stringS).replace(unicode(old), unicode(new), count)

    if hasattr(old, '__html__') or hasattr(new, '__html__') and \
      not hasattr(stringS, '__html__'):
      	# pour échapper les caractères spéciaux dans stringS 
        stringS = escape(stringS)

    else:
    	# Faire un unicode chaîne si ce n'est pas déjà fait. De cette façon une chaîne de balisage n'est pas reconverti en unicode.
        stringS = soft_unicode(stringS) 
    return stringS.replace(soft_unicode(old), soft_unicode(new), count)

os.system('pause')

# def to_tronsforme(stringS):
# 	# transformer une chaine de caractère en une expression mathématique est evaluer avec eval
# 	for()
