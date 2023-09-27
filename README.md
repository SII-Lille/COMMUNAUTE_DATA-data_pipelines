# Projet de communauté Data
***
Le but de ce projet est de procéder au traitement de données d'un dataset de retail, depuis l'ingestion dans une base de données, jusqu'à l'affichage d'un indicateur sur une page web. Le tout sous le langage python.<br>
Les principaux outils utilisés sont :
- <b>duckdb</b> pour la partie base de données
- <b>pydantic</b> pour la validation de la structure de données
- <b>dbt (data build tool)</b> pour la transformation de nos données dans une table d'agrégat
- <b>flask</b> pour l'affichage d'un graphique sur une page web

Etape 1 : <br>
Dans un premier temps, nous inserons dans une base de données duckdb les données présentes dans les différents datasets de type `sales_XX_2019.csv`, les XX représentants les différents mois de l'année. Nous limitons le nombre de lignes insérées à 10 000 pour chaque dataset pour éviter que l'insertion en base de données ne prenne trop de temps. Nous utilisons pydantic en amont afin de valider le format de nos données. 

Etape 2 : <br>
Nous lançons ensuite dbt qui permet de faire une agrégation de nos données afin de récupérer le total des revenus par mois

Etape 3 : <br>
Enfin, nous lançons notre page web avec flask afin d'afficher notre graphique. Nous utilisons une librairie Javascript `chart.js` pour créer notre graphique 


### Configuration recommandée 
- Créer un nouvel environnement sous Anaconda où vous installez les différentes librairies

### Installation
Activation de l'environnement :<br>

`conda activate nom_environnement`

Installation des différentes librairies :

`pip install -r requirements.txt`
<br/>

Mettre le fichier profiles.yml dans le dossier `C:\Utilisateurs\prenom.nom\.dbt` <br>
Si le dossier `.dbt` n'existe pas, le créer.<br>
A l'intérieur du fichier `profiles.yml`, modifier le <b>path</b> afin de modifier le chemin local du fichier `sales_bdd.duckdb`. Le fichier `sales_bdd.duckdb` n'existe pas encore mais sera créé automatiquement dans le dossier `duckdb` lors de l'ingestion des données.
<br/>

### Lancement du projet 

Depuis le dossier du projet : `cd work`<br/>

`python ingestion_dataset.py`

 > **Attention**, le traitement des insertions peut prendre plusieurs minutes (environ 10 minutes)

`cd ../duckdbt`<br/>

La commande `dbt debug` (à lancer lorsque nous sommes dans le dossier duckdbt et avant la commande `dbt run`) permet de vérifier si la connexion à la base de données est bien établie<br/>

`dbt run`<br/>

`cd ../flask`<br/>

`flask --app graph run`

Une fois que flask s'est lancé, se rendre sur la page http://127.0.0.1:5000/ dans votre navigateur pour afficher le graphique


