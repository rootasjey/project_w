<span id="title">
PROJET</span>
# Plateforme d'exercices en ligne de maths/info


<!-- Saut de ligne -->
<br/><br/><br/>
<!-- Saut de ligne -->

<!--Comment (Luca): Des <br> pour faire de la mise en page ? Beurk !
En plus je parie que vous n'avez pas été consistants sur le nombre de
<br> par rapport au niveau des entêtes. Modifiez plutôt le margin-top
des <hx> pour obtenir cette mise en page. Si vous avez besoin d'un
espacement spécial à un endroit particulier, faites-le avec une balise
occasionnelle munie d'une classe spécifique.  -->

<!--Comment (Luca): Attention, vous avez des apostrophes ASCII (') et
des apostrophes Windows (’) dans votre texte. -->


## Tables des matières
* <a href="#introduction">Introduction</a>
* <a href="#developpement">Développement</a>
* <a href="#methodologie">Méthodologie</a>
* <a href="#bugs">Les bugs rencontrés</a>
* <a href="#application">L'application</a>
* <a href="#futur">Perspectives futures</a>
* <a href="#conclusion">Conclusion</a>
* <a href="#contribution">Déclaration de contribution</a>
* <a href="#references">Références</a>

<!-- Saut de ligne -->
<br/><br/><br/>
<!-- Saut de ligne -->

<span id="introduction">
# Introduction
</span>

<!--Comment (Luca): Attention : code incorrect. Ceci génère

	<p><span id="introduction"></p>
	<h1>Introduction</h1>
	<p></span></p>

Utilisez <div> à la place de <span>, ou faites un <span id="..."> vide
avant `# Introduction`, ou utilisez l'extension pour la table des
matières. -->

<!--Comment (Luca): Il est considéré bonne pratique d'arrêter les
lignes de code/texte à la 79 colonne, comme ce commentaire. Ça aide la
lisibilité dans les éditeurs de texte, et du coup aussi dans les pages
Github (remarquez comment c'est illisible, par exemple, ici :
<https://github.com/rootasjey/webbapp/blob/master/application.py#L159-160>).
Beaucoup d'éditeurs de texte savent faire ce formatage automatiquement
sur des paragraphes de texte (Alt+Q avec Sublime, apparemment
<http://stackoverflow.com/questions/12466430>). -->

Les mathématiques et l’informatique sont devenus des outils indispensables dans le domaine scientifique. C’est pour cette raison que l’apprentissage de ces disciplines est un atout majeur pour surmonter de nouveaux challenges. Les étudiants peuvent acquérir des connaissances dans ces domaines en s'exerçant à travers des problèmes. Cet apprentissage peut se faire de diverses manières et plus la méthode choisie est dynamique et interactive, plus elle est efficace et appréciée par les étudiants.

Des plateformes web telles que [Code.org](http://code.org) et [Codecademy.com](http://codecademy.com) proposent exclusivement  des exercices en informatique qui permettent aux étudiants de s'entraîner. Une autre plateforme, [OpenClassrooms](http://openclassrooms.com) donne accès aussi bien à des cours théoriques qu'à des exercices en Informatique et en Mathématiques. Ces sites, mis en place récemment, ont pour objectif d’enseigner la programmation et les mathématiques au grand public et ainsi donner à chacun un accès facile aux connaissances. Il a été constaté que peu de plateformes web existent en français alliant ces deux disciplines pour le niveau universitaire.

Notre projet de Master 1 a pour but de fournir aux étudiants de l’Université de Versailles Sciences un accès à des connaissances scientifiques nécessaires dans leur cursus universitaire. Pour ce faire, des technologies modernes, notamment des outils de développement web, sont employés afin d’obtenir des résultats différents de ce qui existe déjà.


<!-- Saut de ligne -->
<br/><br/><br/>
<!-- Saut de ligne -->

<span id="developpement">
# Développement
</span>

## Description du projet

Dans ce projet, on est appelé à réaliser une application web qui permet de publier, faire ou corriger des exercices en ligne de Math/Info.

L’application se divise en deux parties :

* Le  serveur, générant les exercices à partir de leur description.
* Le  client, permettant de présenter les exercices à l’utilisateur, de vérifier l’exactitude de la réponse, et de présenter la solution.


La dite application doit fonctionner en se basant sur ces deux cotés afin de fournir un espace autonome, robuste et fiable sur le long terme.

Le projet vise à :

* Faciliter l’accès du rédacteur pour pouvoir rédiger et publier des exercices en ligne.
* Faciliter l’accès de l’utilisateur à l’application afin de consulter les exercices publiés en ligne ainsi que la solution de chaque exercice.
* Créer une interface simple, claire et facile à utiliser.

Une des sources d'inspiration a été [RStudio](https://www.rstudio.com/), un logiciel open-source capable d’exécuter du code R et accessoirement de créer des documents scientifiques. Le langage R est très répandu chez les statisticiens et les explorateurs de données.

Notre projet se différencie en plusieurs points :

* Il a pour but d’offrir un moyen à des enseignants de rédiger des exercices et de les proposer rapidement à un groupe d’étudiants au travers d’une plateforme en ligne. Celui de RStudio est de créer des documents portant sur des études de données, ce qui représente qu’une partie de notre application.

* Les langage utilisés pour la prédaction des exercices sont le Markdown, le HTML, et le Python.

* La plateforme est destinée à être en ligne et accessible par les utilisateurs.


<!-- Saut de ligne -->
<br/><br/>
<!-- Saut de ligne -->


## Langages et technologies utilisés

Afin de mener à terme le travail demandé, nous utilisons plusieurs langages de programmation et différents outils, ce qui offre une grande flexibilité et une puissance accrue dans le développement.

Le langage Python représente le cœur de l’application.



<!-- Saut de ligne -->
<br/>
<!-- Saut de ligne -->


### Langages

#### Python

Python est un langage de programmation de haut niveau utilisé dans divers domaines, dont les sciences. Sa syntaxe permet aux programmeurs  d'exprimer des concepts en moins de lignes de code par rapport à d’autres langages tels que le C. 

Python supporte plusieurs paradigmes de programmation, y compris l’orienté aux objets et la programmation fonctionnelle. Il dispose d'un typage dynamique fort et d’une gestion automatique de la mémoire. Une grande bibliothèque de modules spécialisés permet d’étendre les fonctionnalités de base du langage.

L’une des premières choses que nous avons apprises en codant en Python est l'importance de l’indentation, et l’absence d’accolades a été déroutante au début. Mais la simplicité et la modularité du langage nous a permis d’obtenir des résultats concluant très rapidement.

	# ---------------------------------
	# Convert one file from .md to .html
	# ---------------------------------
	def ConvertSingleFileToHTML(path=""):
		if path == "":
			return

		extension = ".md"
		if path.endswith(extension):
			# open file
			with open(path, 'r') as exercice:
				text = exercice.read()
				# create a new absolute path 
				# (for the new file) > replacing the extension
				new_path = str.replace(path, extension, ".html")
				# create a new file
				with open(new_path, 'w') as html_file:
					# conversion + write in the new file
					html_file.write(markdowner.convert(text)) 


<!-- Saut de ligne -->
<br/>
<!-- Saut de ligne -->


#### HTML

Le HTML (Hypertext Markup Language) est un langage de balisage
permettant d’écrire de l’hypertexte. Il est conçu pour structurer le
contenu d'une page web. C’est avec ce contenu que l'utilisateur final
interagit.

	<div id="footer">
	        <ul>
	            <li><a href="/">accueil</a></li>
	            <li><a href="/report">report</a></li>
	            <li><a href="/about">à propos</a></li>
	        </ul>

	    <a href="https://github.com/rootasjey/webbapp/keny">
	        <img class="keny_icon" alt="keny" src="dead_keny.png"/>
	    </a>
	</div>


<!-- Saut de ligne -->
<br/>
<!-- Saut de ligne -->


#### CSS

CSS (Cascading Style Sheets : feuilles de style en cascade) sert à décrire la mise en forme des documents HTML et XML. Introduit au milieu des années 1990, CSS devient couramment utilisé dans la conception de sites web et bien pris en charge par les navigateurs web dans les années 2000.
	
Le langage CSS donne un moyen de séparer le contenu de la mise en forme. Il agrémente les éléments HTML de styles tels que la couleur, la transparence, les bordures, la position, ainsi que les animations.
Notre platforme possède des feuilles de style distinctes des documents HTML pour une plus grande clarté et faciliter la maintenance du code. Ainsi, si pour une raison particulière on venait à modifier l’affichage, ce changement se ferait à un seul endroit du code. 

	/*HEADER*/
	.report_header{
		margin-left: 40px;
		font-family: great_vibesregular;
		font-size: 3em;
	}



<!-- Saut de ligne -->
<br/>
<!-- Saut de ligne -->


#### JavaScript

JavaScript est un langage de programmation de scripts principalement utilisé dans les pages web interactives. C'est un langage orienté aux objets à prototypes; c'est-à-dire que les bases du langage et ses principales interfaces sont fournies par des objets qui ne sont pas des instances de classes, mais qui sont chacun équipés de constructeurs permettant de générer leurs propriétés.

Le JavaScript offre à notre application des fonctionnalités que seuls le HTML et le CSS ne pourraient fournir. On a ainsi pu effectuer des actions spécifiques lors des évènements. Le clic sur un bouton solution permet, par exemple, d’afficher ou de masquer la solution d’un exercice.

Dans une prochaine version de cette application, le JavaScript pourrait permettre d’utiliser la technologie AJAX afin d'éviter le rechargement complet des différentes pages de l'application.

	var _clock = null;
	(function happyHour() {
	       _clock = setInterval(TicTac, 1000);
	})();


<!-- Saut de ligne -->
<br/>
<!-- Saut de ligne -->


#### Markdown

Markdown est un format qui permet d’écrire du HTML de manière simplifiée. Il peut cependant être utilisé tel quel, sans formatage particulier. La conversion de ce format vers le format HTML est rendue facile grâce à de nombreux outils existants.

Ce rapport est lui-même rédigé dans le format **Markdown**.
<!--Comment (Luca): pourquoi ne pas mettre ici un lien vers le code
source (raw) de cette page sur GitHub? -->

<!-- Saut de ligne -->
<br/><br/>
<!-- Saut de ligne -->


### Les modules

Les modules python sont les différentes parties qui sont venues s’intégrer à l’application de base afin d’étendre ses fonctionnalités. Ces modules nous évitent de tout coder et nous permettent de gagner du temps sur le développement.

<!--Comment (Luca): "Python" ou "python" ? Soyez cohérents. -->

<!-- Saut de ligne -->
<br/>
<!-- Saut de ligne -->


#### Markdown

Un module python permettant la conversion d’un fichier Markdown
(extension `.md`) à un fichier HTML (extension `.html`) est utilisé
par l’application.


<!-- Saut de ligne -->
<br/>
<!-- Saut de ligne -->

#### Flask

Flask est un  micro-Framework pour python permettant de créer des applications web comme un micro blog ou un clone Twitter. L’application, crée par Armin Ronacher, est en licence Free-BSD et tout le monde peut contribuer au projet sur [GitHub](https://github.com/mitsuhiko/flask).

L’avantage de Flask par rapport aux autres Framework web existant tels que Django ou Pyramid, qui sont plus répandus, est que la syntaxe est simple et le module est très basique. Il nous a donc fallu peu de temps pour comprendre le fonctionnement de ce module et nous n’avons pas rencontré de difficulté particulière lors de son utilisation. Cependant, l’aspect basique de Flask est voulu car il est possible d’étendre ses fonctionnalités.
Il serait intéressant par la suite d’implémenter un cache pour notre plateforme, ou le support de l’authentification OAuth.


	# Index route
	@app.route('/')
	def index():
		return render_template('/static/html/index.html')

<!--Comment (Luca): Expliquez un peu plus en détail ce que font ces
lignes de code (par exemple, dans le commentaire). -->

Pour fonctionner, Flask a besoin de Werkzeug et de Jinja2, deux extensions supplémentaires créées par le même auteur.

#### Werkzeug

Werkzeug est une librairie utilitaire python pour la WSGI (Web Server Gateway Interface). La WSGI est une spécification qui définit comment des serveurs web communiquent avec les applications web, et comment  les applications web peuvent être assemblées ensemble pour former une seule requête.

<!--Comment (Luca): J'enleverais les références à Wekzeug : ça n'a pas
vraiment d'importance pour votre projet. -->

<!-- Saut de ligne -->
<br/>
<!-- Saut de ligne -->


#### Jinja2

Jinja2 est un moteur de templates puisant et très utilisé pour Python. 
Un langage de templating permet de définir des squelettes pour les contenus d’une application. Dans notre cas, les squelettes seront destinés à harmoniser toutes les pages web de notre plateforme. La syntaxe  se rapproche de celle des langages de balisage.

Jinja 2, inspiré par Django, possède une syntaxe plus expressive et l’auto-échappement de caractères offre une bonne sécurité.
Allant de pair avec Flask, le choix de ce module de templating s’est fait naturellement.

L’application devient plus légère en évitant la redondance de code HTML, et est dotée d’une structure de programmation : il devient alors possible de créer des boucles, des conditions ou de parcourir des tableaux. Sans ce module, le nombre de pages HTML aurait été conséquent.

	{% block css %}
		{{super()}} <!--récupère le contenu du block parent-->
		<link type="text/css" href="url" rel="stylesheet" />

		<!-- highlight script -->
		<script type="text/javascript" src="url"></script>
	{% endblock %}

De nombreuses organisations utilisent Jinja, telles que Mozilla, SourceForge, Instagram, NPR.


<!-- Saut de ligne -->
<br/><br/>
<!-- Saut de ligne -->


### Outils

#### GitHub

GitHub est le service web que nous avons utilisé pour héberger le code source de l’application web. Très efficace pour le partage et le suivi de développement de logiciel, il a joué un rôle essentiel pour la production en collaboration. Nous avions un suivi détaillé de ce que nous faisions, des graphes de statistiques ainsi qu’un moyen facile de suivre les fonctionnalités que chacun apportait au projet.

Il est multiplateforme, facile à prendre en main, et utilise Git qui est un logiciel de version décentralisé.


<!-- Saut de ligne -->
<br/>
<!-- Saut de ligne -->


#### SublimeText

Comme dans tout projet informatique, nous avions besoin d’un bon éditeur de code, de préférence supportant plusieurs langages à la fois, et multiplateforme. SublimeText répondait parfaitement à nos attentes, léger et facile d’utilisation, le développement n’a été que plus agréable.


<!-- Saut de ligne -->
<br/><br/><br/>
<!-- Saut de ligne -->


<span id="methodologie" >
# Méthodologie
</span>

Un planning a été établi afin d’organiser les différentes tâches à effectuer. La majeure partie du temps, on a essayé de travailler conjointement sur une fonctionnalité dans le but de compléter rapidement le point en cours et d’atteindre le point suivant dans les meilleurs délais.


<!-- Saut de ligne -->
<br/><br/>
<!-- Saut de ligne -->


## Utilisation de Markdown Pour générer les exercices

Nous avons donc commencé l’apprentissage du langage Python en écrivant une extension capable de convertir un fichier au format Markdown (`.md`) vers le format HTML (`.html`). Cette tâche, étant la première du projet, nous a pris quelques semaines mais l’existence d’un module Python nous a grandement facilité la tâche. Il suffisait d’intégrer correctement ce module dans notre application.

Au départ, le code de ce module devait explorer le contenu d’un dossier passé en argument, trouver les fichiers possédant l’extension `.md` et créer de nouveaux fichiers avec l’extension `.html`, en formatant le contenu.


Par la suite, nous n’aurons besoin que de formater un bloc de texte Markdown en HTML avec les balises correspondantes. Il ne nous sera pas nécessaire de créer et de sauvegarder les fichiers HTML en sortie de la conversion. La conversion sera effectuée à chaque affichage.
	
Il a fallu, dès cette première partie, comprendre les fonctionnements de bases du langage Python, notamment la création et l’utilisation d’un module, l’ouverture et l’écriture dans un fichier, ainsi que l’utilisation du module `os` qui permet d’éditer des fichiers sur le système d’exploitation.


<!-- Saut de ligne -->
<br/><br/>
<!-- Saut de ligne -->


## Création d'un serveur web avec Flask

La création d’un serveur local afin d’avoir un début d’application fonctionnelle était l’étape suivante. Nous devions intégrer le module correspondant et maîtriser son utilisation. Cela s’est fait assez rapidement étant donné la simplicité de la syntaxe de Flask. En effet 7 lignes de code suffisent à créer une application web locale fonctionnelle. Il ne restait plus qu’à effectuer les tests nécessaires en se rendant à l’adresse : <http://localhost:5000>.

Flask possède un système de routes qui sont les URLs accessibles pour accéder à la plateforme côté utilisateur. Au début, nous avons réalisé des routes qui semblaient très similaires : une route pour le domaine mathématique, une autre route pour le domaine informatique. Cependant, en maîtrisant de plus en plus le framework, nous avons généralisé au maximum, et nous avons utilisé des routes dynamiques pour éviter des doublons.
Les routes dynamiques contiennent des variables dans l’URL ; on a une partie constante et répétitive, et une autre qui change en fonction de ce que demande l’utilisateur.

<!--Comment (Luca): "accessibles pour accéder", "semblaient
similaires". C'est pas du Français, ça ! Évitez les allitérations et
les répétitions. -->

Ainsi, la page d’affichage d’un exercice est définie par la route suivante :
[`/<practice>/<science>/chapter/<id>`](/exercices/informatique/chapter/2/Les-boucles.md/)

`<practice>` définissant le type de contenu, si l'utilisateur souhaite s'entraîner sur des exercices, ou apprendre de nouvelles connaissances. La variables `<science>` correspondant à la matière *(Maths, Informatique, Cryptographie)*, `<chapter>` a <!--Comment (Luca): oui ?--> et `<id>` est le numéro de l’exercice demandé. Un exemple pratique de route serait :
[`/exercices/maths/chapter/0/La-somme-en-mille.md/`](/exercices/maths/chapter/0/La-somme-en-mille.md/)

<!--Comment (Luca): Et où est `La-somme-en-mille.md` dans la route dynamique  ? -->

Pour cette route, on accédera à l’exercice ‘La somme en mille’ du chapitre 0 du domaine des mathématiques. L’exercice est au format Markdown, et traduit à la volé lors de son affichage.

L’utilisation de Python nous a donné un accès facile au système de fichiers du système d’exploitation. C’est grâce à cela que nous avons pu coder de manière souple les routes des pages de l’application. La création d’un nouveau dossier correspondant à un domaine suffit pour ajouter une matière à la plateforme, il n’est pas nécessaire de modifier le code source de l’application. La procédure est identique pour les chapitres et les exercices associés. L’application se chargera seule de parcourir tous les dossiers disponibles dans le répertoire, et lister les nouveaux contenus disponibles à l’utilisateur.


<!-- Saut de ligne -->
<br/><br/>
<!-- Saut de ligne -->


## Jinja2 et le Templating

On a réalisé l’écriture du HTML et l’utilisation du templating conjointement au développement du serveur de l’application. Ayant immédiatement saisi le potentiel de Jinja2, la première étape était de définir un modèle de base pour toutes les pages HTML de notre application. Puisque sur un site web dynamique, beaucoup d’éléments sont redondant tels que la barre de navigation, le pied de page, certaines images, nous n’avions besoin que de coder une fois pour toutes ces éléments redondants.

Pouvant maintenant utiliser des structures de programmation telles que les conditions et les variables, nous avons utilisé ces fonctionnalités pour créer les routes dynamiques. En effet il est possible de passer des variables au moteur de templates, et c’est ce que nous avons fait en passant en paramètre la liste des matières disponibles dans le dossier d’exercices, ou la liste des chapitres disponibles pour une matière par exemple.

Ce procédé montre toute la flexibilité de ces framework et les possibilités qu’apporte leur utilisation côte à côte.



<!-- Saut de ligne -->
<br/><br/>
<!-- Saut de ligne -->





##Affichage mathématique avec MathJax

Notre projet devant présenter des exercices de mathématiques, il était indispensable de trouver un moyen d’afficher de manière élégante les formules comme les équations, les limites, et les symboles spéciaux. Sous les conseils de notre Maître de projet, nous nous sommes penchés sur les bibliothèques JavaScript disponibles dans le domaine du web. Notre choix s’est porté sur MathJax, une bibliothèque JavaScript open source multiplateforme.

Notre application exécute ainsi le script MathJax, disponible à travers son Content Distribution Network (CDN), ce qui permet d’alléger la taille du projet. Le script MathJax pesant actuellement 32.9Mb, nous aurions eu une augmentation non négligeable de la taille de l’application.



<!-- Saut de ligne -->
<br/><br/><br/>
<!-- Saut de ligne -->

## Extension des capacités de Jinja2

Cette partie a été la plus laborieuse. Le but était de créer une extension Jinja2 capable d’exécuter du code Python à l’intérieur d’un bloc Jinja2.

On voulait pouvoir écrire le code suivant et obtenir la génération d’un exercice en sortie.

<!--Comment (Luca): Je suppose que vous allez compléter ici. -->

De nombreuses recherches ont dû être effectuées, l’écriture d’extensions n’étant pas la partie la mieux documentée de Jinja2. Heureusement, plusieurs exemples existent sur StackOverflow, ou GitHub, nous donnant des exemples parlant de la procédure de création de l’extension.

Au cours de nos recherches, nous avons trouvé un extrait de code ayant pour but de créer une fonction Python à partir d’une chaîne de caractères, ce qui était proche de ce qu’on devait réaliser.
Il ne restait plus qu’à créer une extension Jinja2 avec cet extrait et de l’adapter à notre application.
        
Maintenant qu’on était capable d’exécuter du code python, la partie intéressante était d’implémenter un générateur aléatoire pour diversifier les exercices. Cela passe par des fonctions comme `random.randint(n, m)` ou `randrange(n, m)` utilisées pour générer des valeurs numériques aléatoires.

<!--Comment (Luca): Exemple ? -->

<!-- Saut de ligne -->
<br/><br/>
<!-- Saut de ligne -->


<span id="bugs">
# Les difficultés rencontrées
</span>

Durant le développement de l'application, nous nous sommes heurtés à plusieurs soucis qui, parfois, nous ont pris beaucoup de notre temps.

Voici quelques recommandations pour vos développements personnels.



<!-- Saut de ligne -->
<br/><br/>
<!-- Saut de ligne -->

## Les modules Python

La création d'un module dans le langage Python capable de convertir des fichiers Markdown fut le premier obstacle majeur, même si avec du recul cela semble maintenant très simple à réaliser. A l'époque, nous ne connaissions que très peu de Python, et nous avons dû nous adapter au fur et à mesure que nous avancions dans la production. Grâce à un travail commun, nous avons pu saisir le fonctionnement général des modules et nous avons fait le rapprochement avec les bibliothèques que l'on peut retrouver dans des langages comme le JavaScript et le C++.
Après quelques tests réussis, nous étions enfin lancés dans le développement du projet, et nous savions que ce n'était que le début d'une longue expérience.



<!-- Saut de ligne -->
<br/><br/>
<!-- Saut de ligne -->


## L'extension Jinja2

Bien que le module soit dans l'ensemble bien documenté, quand il s'agit d'étendre Jinja2 les exemples sont moins nombreux, et nous avons dû effectuer quelques recherches approfondies pour expérimenter suffisamment cette tâche.


<!-- Saut de ligne -->
<br/><br/>
<!-- Saut de ligne -->



## L'encodage UTF-8

L'encodage de caractères est l'un des problèmes majeurs pour les programmeurs à cause des nombreux soucis qu'y peuvent survenir à cause de l'utilisation de caractères spéciaux dans le code Python ou dans un fichier Markdown. Étant francophone, l'utilisation de caractères accentués était indispensable. De plus, l'utilisation de plusieurs modules et formats, en passant par différents parseurs, rendent le débuggage plus long et fastidieux.

Le parseur de Markdown n'accepte que les caractères Unicode, c'est-à-dire que les caractères tels que 'à,é,è,î' produisaient une erreur lors de la conversion des fichiers `.md` en format HTML.

<!--Comment (Luca): Je ne pense pas que ce soit la faute au parseur de
Markdown. Je pense que c'est un "problème" de Python. -->

Afin de régler ce problème, il faut importer le module **codecs** de Python, et
ouvrir le fichier en précisant l'encodage adéquat


    import codecs
    
    # open file with codecs for the markdown converter
    input_file = codecs.open(path, mode="r", encoding="utf-8")
    text = input_file.read()		# read
    input_file.close()				# clode



<!-- Saut de ligne -->
<br/>
<!-- Saut de ligne -->


puis, convertir la chaîne de caractères avant de la passer dans le parseur Markdown


    import codecs
    from packages.markdown import Markdown
    markdowner = Markdown()
    
    # open file
    with open(file_path, 'r') as file:
        text = file.read()		# read
        text = text.decode('utf-8')
        html = markdowner.convert(html)


    html = markdowner.convert(text)	# conversion

Aussi, Python n'accepte pas non plus les caractères spécaux et accentués par défaut. C'est pour cette raison qu'il faut ajouter cette ligne au début de chaque document `.py` afin d'établir l'encodage UTF-8 automatiquement.

    # -*- coding: utf8 -*-

<!--Comment (Luca): Attention, ce n'est vrai que sur des machines
configurées en UTF8. -->

Nous avons du encoder le texte en sortie dans l'extension Jinja2 pour pallier à tout problème. Et nous sommes enfin parvenu à afficher correctement les caractères spéciaux en Markdown.


    html = markdowner.convert(text)	# conversion


<!-- Saut de ligne -->
<br/>
<!-- Saut de ligne -->



<span id="application">
# L'application
</span>

Au terme du projet, nous avons obtenu une application fonctionnelle comportant les fonctions principales qui étaient requises au préalable.


<!-- Saut de ligne -->
<br/><br/>
<!-- Saut de ligne -->


## Installation

Voici un simple guide d'installation de l'application.

* Assurez-vous d'avoir [Python 3.x](https://www.python.org/download/releases/3.4.0/) ou [2.7+](https://www.python.org/download/releases/2.7.6/) installé, et [easy_install](http://pythonhosted.org/setuptools/easy_install.html).

* Installer les dépendances :

        easy_install pip
        pip install flask
        pip install jinja2

* Télécharger l'application à partir du [répertoire Github](https://github.com/rootasjey/webbapp ).

* Lancer le serveur avec

		python application.py

* Visiter <http://localhost:5000/>.



<!-- Saut de ligne -->
<br/><br/>
<!-- Saut de ligne -->


## Fonctionnement

<!-- SCREENSHOT INDEX -->
<div class="iframe_control">
	<iframe src="/" class="frame"></iframe>
	<!-- <img src="/static/img/refresh_icon.png" class="iframe_button" 
		 onclick="reload_iframe(event)"> -->
</div>


La page d’accueil affiche une brève description du projet, explique ce que l’application est capable de faire. Un menu se trouve en dessous du nom de l’application, permettant de se rendre sur la page d’exercices, la partie cours, ou de rédiger un exercice.
En haut à droite un message est affiché, accueillant l’utilisateur. La barre bleue du haut peut se dérouler et affiche l’heure, un bouton de connexion ainsi que des informations sur l’utilisateur.

Le template de la page d’accueil est réutilisé pour toutes les autres pages ce qui permet un minimum de répétition de code d’une page à l’autre.


<!-- Saut de ligne -->
<br/><br/>
<!-- Saut de ligne -->

<!-- SCREENSHOT EXERCICES LIST -->
<div class="iframe_control">
	<iframe src="/exercices#body" class="frame"></iframe>
	<!-- <img src="/static/img/refresh_icon.png" class="iframe_button" onclick="reload_iframe(event)"> -->
</div>

<!--Comment (Luca): Comme je l'ai fait ici, vous pouvez sauter au bon
endroit dans la page avec un # dans l'URL. -->


Les différentes matières accessibles sur la plateforme sont présentées avec des couleurs, et d’autres domaines peuvent être aisément ajoutés.



<!-- Saut de ligne -->
<br/><br/>
<!-- Saut de ligne -->

<!-- SCREENSHOT EXERCICES CONTENT -->
<div class="iframe_control">
	<iframe src="/exercices/informatique/chapter/0/Petits-Calculs.md/" class="frame"></iframe>
	<!-- <img src="/static/img/refresh_icon.png" class="iframe_button" onclick="reload_iframe(event)"> -->
</div>


Cette capture représente l’interface client de l’application avec la présentation de l’exercice, qui, ici, présente du code en langage C. La solution de l’exercice est masquée par défaut, et le bouton rouge permet de l’afficher.

Une des fonctionnalités intéressante du projet était de pouvoir générer des valeurs aléatoires pour un exercice donné. Nous avons pu réaliser cette fonctionnalité qui est un vrai atout pour notre application web. Ainsi, plusieurs utilisateurs travaillant sur un même exercice ont des solutions différentes. 
Nous avons surtout essayé la génération aléatoire avec des valeurs numériques, mais elle peut aussi s’appliquer à un ensemble de questions.


Concernant la rédaction d’un exercice, celle-ci peut être faite directement sur une page de l’application prévue à cet effet, ou manuellement à l’aide du système de fichiers.

Pour créer un exercice sur la page, l’utilisateur doit choisir un domaine d’exercices, puis un chapitre dans lequel son exercice apparaîtra. Il peut également créer un nouveau chapitre ou ajouter une matière si cette dernière n’existe pas.
En effet, nous n’avons pas voulu nous limiter qu’aux domaines des mathématiques et de l’informatique, malgré l’appréciation que nous portons pour ces matières. Ceci pour étendre la portée de la plateforme.


Lors de la rédaction d’un exercice, il y a deux parties principales :

* L’exercice en lui-même
* La solution

L’exercice est composé de plusieurs sous-parties :

* Des énoncés
* Des questions
* Des extraits de code de programmation (facultatif)
* Des figures géométriques (facultatives)
* Des illustrations (facultatives)

Les parties peuvent être ajoutées dans l’ordre qui convient le mieux.


On peut mélanger différents styles d’écriture en rédigeant un énoncé, c’est-à-dire qu’on peut utiliser la syntaxe du HTML, du Markdown, ou même celle du langage de programmation Python pour les valeurs aléatoires. Cependant les résultats peuvent être différents de ceux souhaités à cause de l’utilisation coordonnée des parseurs de Jinja2 et de Markdown.


<!-- Saut de ligne -->
<br/><br/>
<!-- Saut de ligne -->

<!-- SCREENSHOT EXERCICES CONTENT -->
<div class="iframe_control">
	<iframe src="/lessons/conception-bdd/chapter/0/Femeture-Transitive.md/" class="frame"></iframe>
	<!-- <img src="/static/img/refresh_icon.png" class="iframe_button" onclick="reload_iframe(event)"> -->
</div>


Une partie ‘Cours’ permettant aux étudiants d’obtenir des informations sur des méthodes de travail ou de résolutions de problèmes a été ajoutée à la fin du projet. Cette partie, bien que facultative, apporte un plus à la plateforme.

Étant donné que nous avions déjà un mécanisme fonctionnel pour les exercices, nous avons adapté le gestionnaire d'URL (flask) afin que les routes prennent un paramètre de plus.

* [`/<practice>/maths/`](/lessons/maths/)

Ainsi, si l'utilisateur souhaite accéder aux cours, la variable `<practice>` prendra `lessons` comme valeur, sinon `exercices` pour s'entraîner sur des problèmes.

* [/lessons/conception-bdd/](/lessons/conception-bdd/)
* [/exercices/crypto/](/exercices/crypto/)

Là encore, nous avons facilité l'ajout de contenu en automatisant la fonction qui s'occupe de récupérer les matières, les chapitres et les exercices.
Comme pour les fichiers exercices, les cours sont écrits au format Markdown et ils sont rendus directement dans le navigateur.



<!-- Saut de ligne -->
<br/><br/><br/>
<!-- Saut de ligne -->


<span id="futur">
# Perspectives futures
</span>

Bien que nous étions très motivés par le projet sur lequel nous avons travaillé, certaines fonctionnalités, n’ont pas pu être réalisées. Voici par conséquent des pistes d’idées sur lesquelles il serait intéressant de développer pour une prochaine version.

#### Le partage des variables locales des balises `{% python %}`

Un des derniers problèmes rencontrés a été le partage de variables locales des balises `{% python %}`. Cela permettrait d’avoir plusieurs bouts de code capables d’utiliser des variables communes. La flexibilité dans l’écriture des exercices serait meilleure. Cependant, la version actuelle de l’application empêche la communication des variables appartenant à des  blocs `{% python %}` différents, pouvant rendre la syntaxe de rédaction compliquée. Cette fonctionnalité est par conséquent la première de la liste des améliorations à ajouter.

#### Une base de données

Une base de données est nécessaire et indispensable pour ce genre d’application. En gardant des statistiques des utilisateurs, ceux-ci peuvent suivre leur évolution au cours du temps. Connaître le nombre de connaissances apprises, le nombre d’exercices faits, le temps passé sur l’application.
Une interface administrateur où les professeurs pourraient mettre leurs cours et leurs exercices pour les étudiants est fortement envisageable. N’aurait le droit d’ajouter du contenu, qu’une personne agrée par le personnel de l’université.


#### La correction automatique

La vérification automatique d'une réponse à un problème permettrait à l'étudiant de réfléchir d'avantage avant de consulter la solution. Pour le moment, il est obligé de consulter toute la solution pour vérifier l'exactitude de ses réponses.
La réponse serait vérifiée du côté serveur et éventuellement corrigée. Une note pour chaque exercice motiverait aussi l’utilisateur, ce qui lui permettrait de suivre son niveau. 


<!-- Saut de ligne -->
<br/><br/><br/>
<!-- Saut de ligne -->


<span id="conclusion">
# Conclusion
</span>

Ce Projet a  représenté pour nous une réelle opportunité de mettre en pratique toutes nos connaissances acquises en cours. Il nous a été aussi d’une grande utilité puisqu’il nous a permis d’acquérir de nouvelles connaissances techniques. 

L'aboutissement de notre projet symbolise une énorme fierté pour nous, et nous avons le grand plaisir de laisser une trace dans l’université de Versailles Saint-Quentin-en-Yvelines qui, elle aussi, laissera sa trace dans notre mémoire.

Nous souhaiterions améliorer ce projet afin d'obtenir un produit de qualité pour le département informatique de l'Université de Versailles Saint-Quentin-en-Yvelines

Nous espérons que ce projet saura répondre aux attentes pour lesquelles il a été créé.


<!-- Saut de ligne -->
<br/><br/><br/>
<!-- Saut de ligne -->


<span id="contribution"></span>
# Remerciements

On tient à exprimer notre gratitude envers tous ceux qui nous ont aidés de près ou de loin dans la conception et la réalisation de notre projet, ce projet qui nous a poussé à exploiter tout notre savoir théorique et technique dans le domaine de programmation informatique, voir même consulter d’autres sources d’informations afin de compléter l’ensemble des éléments nécessaires pour boucler notre travail et donner un résultat fructueux. <!--Comment (Luca): Bravo, Proust ! -->

Nos remerciements à tout le corps professoral de l’université de Versailles Saint-Quentin-En-Yvelines et aux professeurs du département informatique. Sans eux, notre processus d’études n’aurait ni débuté ni progressé.
Nous n’oublions pas notre encadrant Mr. Luca DE FEO qui nous a fait confiance en nous offrant l’opportunité de travailler sur un tel projet, un professeur exemplaire pendant cette année d’étude à l’université. Il nous a transmis un maximum de son expérience et de ses connaissances personnelles afin  de créer un savoir-faire chez chaque étudiant de notre promotion, et pour lequel nous souhaitons tout le bonheur et la prospérité.

En fin nous remercions toute personne qui nous a présenté le moindre de soutien durant notre parcours d’étude.


<!-- Saut de ligne -->
<br/><br/><br/>
<!-- Saut de ligne -->


<span id="references">
# Références
</span>

* [Jinja2](http://jinja.pocoo.org/)
* [Jinja2 - Extensions Documentation](http://jinja.pocoo.org/docs/extensions/)
* [Flask](http://flask.pocoo.org/)
* [Markdown](http://daringfireball.net/projects/markdown/)
* [Markdown Syntax - Wikipédia](https://en.wikipedia.org/wiki/Markdown)
* [R Markdown](http://www.rstudio.com/ide/docs/r_markdown)
* [Python](https://docs.python.org/3/)
* [PyTenjin](http://www.kuwata-lab.com/tenjin/pytenjin-users-guide.html)
* [ePy](http://wids.net/lab/epy.en.html)
* [Openclassrooms - Python](http://fr.openclassrooms.com/informatique/cours/apprenez-a-programmer-en-python-1)
* [Openclassrooms - Flask](http://fr.openclassrooms.com/informatique/cours/creez-vos-applications-web-avec-flask)
* [StackOverflow](http://stackoverflow.com/)
* [GitHub](https://github.com/)
* [GitHub - Help](https://help.github.com/)
* [Kernel.org - GitHub User Manual](https://www.kernel.org/pub/software/scm/git/docs/user-manual.html)
* [CreateAFunction](http://code.activestate.com/recipes/550804-create-a-restricted-python-function-from-a-string/)
* [Hihlight.js](http://highlightjs.org/download/)
* [MathJax.org](http://www.mathjax.org/)
* [MathJax - Doc Tex](http://docs.mathjax.org/en/latest/tex.html)
* [Wikipedia - List of Mathematical Symbols](http://en.wikipedia.org/wiki/Math_markup)
* [UVSQ - Présentation des projets](http://www.prism.uvsq.fr/~Master_Info/projets.php#projet2)
