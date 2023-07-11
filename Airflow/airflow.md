# Apache Airflow

Permet de gérer et d'organiser des programmes complexes. A la fois dans l'ordre d'execution mais aussi dans le temps.

L'essentiel de la fonction d'airflow est de gérer la dépendance des un par rapport aux autres, le scheduler.

## Origine 

AirBnb à trop de données à gerer et veut creer un programme qui veut avoir différentes execution de tâches qui dépendent de conditions.

Avant airFlow il avait un script qui appelait les programmes les un à la suite des autres. Et recommencer chaque jour, c'est long et fastidieux.

Ils veulent planifier des tâches de façon robuste.

# Composant et architecture.

Principal intervenant est : le scheduler.

![architecture](https://airflow.apache.org/docs/apache-airflow/stable/_images/arch-diag-basic.png)


* **Le scheduler** : soumet des tâches à des workers.

* **Worker** : réalise les tâches

* **Executeurs** : Gérer les tâches en cours. Le scheduler prévoir l'éxecution. L'executeur sait à l'instant T ce qu'il se passe en cours d'execution.

    Si il n'y a pas de worker, par défaut, l'executeur execute toutes les tâches. (c'est l'équivalent d'un ressource manager)

* **Webserver** : Ensemble de machines, simple ou multiple qui porte mes interfaces pour gérer Airflow. Partie dans laquelle l'utilisateur vient interagir.

* **DAG** : Ensemble de fichiers fondamentaux qui servent au fonctionnement d'airflow. Décrivent ce qui doit être executer dans mon flux de travail et a quel moment (conditions).

* **Database** : Pour stocker nos fichiers de travail, nos données et nos résultats. 

Ca gère des flux de travail et pas des flux de données. C'est pas Airflow qui gère les données, on doit dans nos tâches gerer les transfert de données.


# Fonctionnement

Schéma qui représente des flux de travail. Rectagle représentant des tâches. Embranchement qui représente des conditions, donc en fonction des conditions, toutes les tâches ne sont pas executées.

Chaque tâche est représenté par un noeud (=tâche), qui sont reliés par des arrêtes. L'ensemble est enregistré dans un script qu'on appelle le DAG.

## Pipeline interdite: 

Une pipeline ne peut pas contenir de boucle, elle a toujours un début et une fin.
Elle peut avoir plusieurs début

## Le DAG

Directed acyclic Graph, "script" écrit en python qui définit un flux de travail.

Il contient les différentes tâches à executer (je peux importer mes fonctions depuis un module).

Je vais devoir coder les dépendances entre mes tâches.

il va permettre de planifier quand executer mon flux de travail. Donc paramètre de temps. Et surveiller sa complétion.

Il permet de partager des variables et données entre les différentes tâches d'un même flux de données.

### Parametres du DAG

liste non exaustive:

* dag_id : mon scheduler peut planifier plusiers flux de travail (qui peuvent etre interconnecté). Je peux planifier dans mon scheduler plusieurs DAG.

* start_date : Quand démarrer le flux de travail. (on peut aussi démarrer le flux de travail manuellement au moment ou je le souhaite)

* schedule_interval : A quelle fréquence executer le travail. Une seule fois = (@once) ou tous les jours = (@daily). Si pas de schedule interval par défaut la tâche s'execute une fois.

* catchup : relance l'execution si echec (par exemple pas de worker disponible), si echec dois-je rattraper ou passer à l'itération suivante.

## Les noeuds.

Peut être n'importe quel programme à accomplir.
* Traitement de données.
* Requete sur une base de données.
* Transfert de fichiers.
* Toute autre opérations

Attention : On planifie les tâches en python mais les tâches elles même ne sont pas en python. (creer un fichier)

## Les arretes.

Représente l'ordre dans lequel s'execute les tâches.

Si une tâche plante, elle n'arrête pas forcement le flux.

creer un fichier (succes) -> connection bdd (error) -> requete api pour récup data (succes) -> envoie data vers bdd (error).

# Script DAG


Contient:
* les taches du flux
* ordre et relations
* planification des différentes tâches
* conditions

Plus qu'un script, c'est un fichier de configuration et de paramétrage. Pour planifier l'agencement de différentes travaux.

C'est un fichier qui peut être évalué rapidement, car planificateur l'execute périodiquement.

Il ne doit pas décrire les tâches elle même, on importe les fichiers de code.

Le DAG n'est pas fait pour communiquer entre les tâches.

## Definir un DAG:

**Par le contexte :**

````
from airflow import DAG

with DAG(params):
    #Toutes mes tâches
````

**Par le constructeur standard:**

````
from airflow import DAG

#objet DAG
my_dad=DAG(params)
````
Avec cette méthodes toutes mes taches vont devoir avoir mon DAG en paramêtre.

**Par annotation:**

utilise @dag(params) pour déclarer un DAG en fonction

````
from airflow.decorators import dag

@dag(param)
def mon_dag():
    # Mes taches
````

## Exemple:

````
import datetime
# import des librairies airflow
from airflow import DAG
from airflow.operators.empty import EmptyOperator
with DAG(
  dag_id="my_dag_name",
  start_date = datetime.datetime(2021, 1, 1),
  schedule="@daily",
  default_args={"key":"value"}
):
  # contexte d'execution de mes taches
  EmptyOperator(task_id="task")
````

## Les arguments DAG

Sous forme K=valeur

**dag_id:** nom du dag, permet d'être identifié

**default_args:** objet JSON qui va contenir tous les arguments communs à toutes les tâche du DAG.
````
'owner':propriétaire
'start_date'
````

**description**

**tag:** petits mots qui sont en dessous du nom DAG

**catchup** : signale si je dois rattraper mon retard ou pas.

**max_active_run** : limitte le nombre d'instance d'un même DAG en même temps, permet de limitter les capacités du DAG. AirFlow à un nombre limitter de tâche par architecture. Si j'ai un DAG avec 120 tâches, je peux limitter le nombre de tâche pour en laisser pour les autres.

**orientation** : rendu graphique

**concurrency** : nombre maximum de worker que je peux kidnapper en même temps pour un DAG. AirFlow à un nombre limitter de tâche par architecture. Si j'ai un DAG avec 120 tâches, je peux limitter le nombre de tâche pour en laisser pour les autres.

**dagrun_timeout:** : temps maximal autorisé d'éxecution pour une instance du DAG. Permet de purger les DAG qui sont placé en attente. 

### Argument temporel.

**start_date** : Date à parir de laquelle sont lancé des tâches. Retroactif si catchup = True

**end_date** :

### Les interval de temps :

Peuvent se renseigner sous deux formes, par annotation ou format cron.

* None
* @once : Une execution
* @hourly : toutes les heures au début de celles-
* @daily : Execute tous les jours à minuit
* @weekly : Toute les semaines le dimanche à minuit
* @monthly : premier de chaque mois à minuit
* @yearly : premier janvier chaque année

Format CRON : 5 chiffres
- minute
- heure
- jour du mois
- mois
- jour semaine
````
30.17.*.7.2 = tous les mardi de juillet à 17h30
````

## Les tâches:

* **Opérator :** tache pre-difinis que l'on peut associé à la chaine simplement pour construire un DAG.
Il y a des opérator pour tout : (python,postgree,bash, kubernetess...).

  Ils dérivent tous d'un element appelé "base opérator" qui est l'executeur par défaut.

* **Sensor :** Opérateurs sensible à un environnement externe à AirFlow. C'est un opérateur sensible à la variation de temps. Ils sont relancé à une intervale régulière tant qu'une condition n'est pas vérifiée. File_Sensor : détecte la présence d'un fichier.

* **@task :** Permet de définir une tâche dans une fonction en python.

Ils ont tous besoin d'un contexte déclaré par DAG pour pouvoir travaille.

Les tâches incluent tous les arguments requis pour éxecuter du travail dans Airflow:
* Des information sur la temporalité (start_time)
* des informations sur le contexte de la tache (task_id, executor_config)
* des informations sur les retours (on_execute_callback)

### Exemple d'opérator

- BashOperator :
- Python(virtualenv)Operator : 
- SQLAlchemyOperator : Envoyer des requetes SQL via SQLAlchemy déjà présent à l'interieur
- DockerOperator : Permet d'excuter des conteneur
- EmailOperator : Envoyer un mail

### Opérateurs de gestion

- DummyOperator : Creer une tâche fictive sans aucun réel effet. Il est souvent utilisé pour creer des dépendances entre les tâches sans effectuer d'action concrète. (tache finale, si celle l'a s'est executé, j'ai terminé)

- BranchPythonOperator : Effectur une branche conditionnelle basée sur une fonction python.

- SensorOperator : Attend qu'une condition ou evenement se produise avant de poursuivre l'execution du DAG.

### instancier un opérateur:

Instancier via un constructeur

ma_tache= MonOperateur(arguments)

ou le faire via une fonction python

````
@task(task_id="ma_tache")
def ma_tache_fonction(arfuments):
  pass
````

Si je déclare mon DAG par contexte, je ne doit pas mettre mon DAG en argument

Si je déclare mon DAG par constructeur, je doit préciser mon DAG en argument.

````
t1 = BashOperator(
  #attibut spécifique à l'opérateur
  task_id="print_date",
  bash_command="date",
)

t2 = BashOperator(
  #Attibut spécifique à l'opérateur
  task_id = "sleep",
  depends_on_past=False,
  bash_command="sleep 5",
  #Attribut communs à tous les opérateurs remplacé
  retries=3, #Si elle marche pas, tu la relance 3fois
)

````

## Template de tâche.

Je peux réaliser des template pour les réutiliser dans un même DAG. 

* inserer de la logique avec {% code %}
* utiliser des appel de fonction comme {{ macro.ds_add(...) }} (fonction DAG qui permet d'ajouter du temps à une date)
* utiliser des paramètres Airflow comme {{ ds }} (DAG)

````

{% for i in range(5) %}
  echo "{{ds}}"
  echo "{{ macros.ds_add(ds, 7) }}
{% endfor %}
````
    t3 = BashOperator(
        task_id="templated",
        depends_on_past=False,
        bash_command=templated_command,
    )


## Définir les dépendances entre les tâches.

Deux fonctions principales:

La bonne execution de t1 entraine t2

`` t1.set_downstream(t2) ``

t2 est induite par la bonne execution de t1

`` t2.set_upstream(t1)``

On peut utiliser l'opérateur bit shift:

Downstream dependancie

t1 >> t2

Upstream dependancie

t2 << t1

t1 >> [t2,t3]

Toutes taches qui n'ont pas de dépendance entres-elles, je n'ai aucun moyen de m'assurer l'ordre dans lequel elles vont être executé.

## Assemblage de l'ensemble dans un script.

* Definir mon DAG
* Definir toutes les tâches
* Definir les dependances entre les tâches



