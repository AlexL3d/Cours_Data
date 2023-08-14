# Les bases de données noSQL

* Les orienté clé : Redis
* Document : MongoDB
* Orienté colonne : Sauvegardé par colonne et pas par ligne
    - Elasticsearch : moteur de recherche, qui renvoie les résultats orienté par pertinence. (Necessite 4Go pour fonctionner en test, en production on considère que chaque node necessite 32Go)



## Redis

Lancer le docker-compose.

Dans le terminal de mon conteneur docker je tape 

    redis-cli

Je peux essuite taper mes commandes.


3 commandes principales:

- `` set <cle> <valeur> ``
- `` get <cle> ``
- `` del <cle> ``

## Cassandra 

Base de données de taille titanesque

La pluspart des SGBD on un systeme master/slave

Dans cassandra il n'y a pas de master, tous les noeuds sont équivalents. On peut se connecter depuis n'importe quel noeud du réseau.

Un systeme qui n'est jamais indisponible s'appelle la **Haute Disponibilité**

L'interet de cassandra c'est qu'on peut étendre facilement la taille du cluster, il suffit de rajouter un noeuds. 

Le défaut c'est qu'on ne peut rechercher que sur certaines colonnes, celles qui sont indexées.

Cassandra est orienté colonne (Wide column)

Les commandes de cassandra ressemble à du SQL

Dans cassandra il y a des Keyspace qui peuvent se répliquer sur des machines. C'est l'équivalent des database. 

`` CREATE KEYSPACE demo WITH REPLICATION = { 'class': 'SimpleStrategy', 'replication_factor':2};``

Je peux ensuite creer mes tables. 

    USE demo;

    CREAT TABLE users (
    id int
    nom text,
    age int,
    PRIMARY KEY (id)
    );


    INSER INTO users (id,nom,age) VALUES (1,"toto",15)

    SELECT * FROM users WHERE id=1;

    SELECT * FROM  users WHERE age<15;

La première requete va fonctionner, mais la deuxième nom car la requete se fait sur une colonne qui n'est pas indexée. Cassandra nous propose d'executer la requete quand même avec des filtres.

## Neo4j

Répond à très peu de cas, mais y répond très bien.

Dans une base de donnée relationnel c'est les jointures qui coutent cher.

Neo4J est une base faite pour représenté les relations entre les données et non les données.

BDD orienté graphe 

Les requetes ne ressemble plus au SQL langage Cypher. 

Neo4J est utile pour faire une requete qui utilise bcp de lien. (Dans quel film a jouer Tom Hanks, Quel est le chemin le plus court entre deux acteurs.)

Neo4J permet de trouver les liens entre les personnes rapidement. Si on veut les information sur les personne on peut le coupler avec une BDD Mysql.

Neo4J est une base de données secondaire (comme elastic search) qui se couple souvent avec une BDD plus traditionnelles.

## Elasticsearch 

Outil très lourd (dans les 2 sens) qui est une BDD qui permet de faire des recherches rapidement. Elasticsearch appartient à la suite elactic.

[exemple elasicsearch flight](https://demo.elastic.co/app/dashboards#/view/7adfa750-4c81-11e8-b3d7-01146121b73d?_g=()&_a=())

![La suite elastic](https://blog.linexos.fr/static/media/uploads/Logs/.thumbnails/stackelastic.jpg/stackelastic-1254x885.jpg)


## Conclusion

Les BDD noSQL ont plein de caractéritiques et d'usages différents. Dire on utilise une BDD noSQL ne signifie rien tant il y en a des différentes.

## Kubernetes

Il faut retenir l'essentiel 

* Cluster : C'est un groupe de machine, j'envoie un manifest qui va répartir mes demandes sur différentes machines. 

On utilise en data bcp d'outil statefull, c'est très chiant à déployer et c'est pas notre métier.

On a juste besoin de savoir la mentalité K8s, ce à quoi ça sert. La plus part du temps quand on fera du k8s ce sera invisible.
