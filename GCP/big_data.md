# C'est quoi le Big Data

C'est pas exactement le fait de gerer bcp de données. C'est aussi le fait de pouvoir s'adapter à une augmentation de la taille des données.

Les 3V:
- Volume : Supporte une augmentation du volume de données.
- Velocité : Peut gerer des données rapidement (quasi temps réel si nécessaire)
- Variété : Plein de données différentes.

## Spark

Est un outil big data, qui permet de faire du calcul distribué sur plusieurs machine. Systeme capable de gérer un grand volume de données.


Spark core.
Spark SQL.
Spark stream.
Spark mon cul.

## K8s

Orchestrateur de conteneur.
Permet de creer un cloud, et c'est k8s qui reparti les conteneur sur les machines. C'est lui aussi qui multiplie les conteneurs si ils ont trop de charge.

## HDFS

Permet de gerer le problème de la taille des Disques Dur. Si je veux stocker plein de donnée alors j'aurais besoin de plein de disque dur. Mais ou est enregistré quel fichier ?

HDFS, permet de savoir en permanence ou est enregistré quelle donnée. C'est une sorte de DD distribué sur plein de machines. Ca fait un cluster de systeme de stockage. HDFS réplique aussi les données en cas de perte. Et permet d'y acceder rapidement.

## Docker

S'oppose à la virtualisation. Permet de ne pas à avoir à chaque fois, besoin de reinstaller le systeme d'exploitation, tous les fichiers et tout le bordel.
Permet de deployer des conteneurs rapidement.

## Airflow


## Python

Est un langage interprété qui permet de faire des scripts.

Pandas: est une librairie qui n'est pas distribué. Pandas fonctionne que sur une seule machine.

On utilise pandas, à la fin quand on a terminé notre traitement.

## Spark

Permet de récupérer des informations sur une source, il les filtre, les transforme, et les stocke (bdd ou fichier dans un HDFS).

Spark permet d'automatiser et faire du calcul lourd avec popentiellement énormément de données. 

## Airflow

Est un ordonanceur de tâche. Permet de planifier des tâches.

Airflow est un bon outil mais que pour certains cas. (batch et stream)

## SQL

C'est une spécification, une norme.

MySQL ne fait pas de booleen, Postgres oui. Le langage n'est pas le même (certains paramètres ne sont pas dans le même sens)

## Postgres

Permet de mettre du JSON ou des liste dans des colonnes. Mais n'est pas scalable.

## MariaDB

## Les BDD nonRelationnelle

Sont des BDD qui sauvegarde colonne par colonne.

Permet d'avoir les lignes avec des colonne qui n'ont pas de valeur.

il y a enormement de BDD à l'interieur.

### MongoDB.

BDD orienté document. Permet de sauvegarder des Json avec de la profondeur. Je peux renseigner des objets complexe (adresse : Numero+Rue+CP+Ville+Pays)

### Redis.

BDD en mémoire ram, clé-valeur. Tu ne peux rechercher que sur les clefs et pas les valeurs.


# Le Batch et le stream

Batch : Traitement discontinu par paquet, qu'on peut programmer tous les jours, heures, ...

Stream : Traitement en continu

Pour les base de données en streaming. Sont orienté colonne.
- Cassandra
- Hbase
- BigTable (version payante de Hbase) Scalable, sous forme de table, peut pas faire de jointure, peut ingerer bcp de données. 

Cassandra et Hbase sont capable de gerer leur nombre de noeud dans le monde. (à 12h j'ai 2 noeud en europe 1 en amérique, à 02h j'ai 1 en europe et 2 en amérique)


- Je sais la taille de mes données : plutot du MySQL ou Postgres

- Nombre de données croissant, mais toujours structuré : BigQuerry

- Données croissantes mais qui sont au format JSON : MongoDB qui est aussi scalable.

