# Big Data

## Concept

    - Problème de places physiques pour le stockage de volumes extrêmement importants
    - Vitesse d'import des données en augmentation exponentielle (traitement des données)
    - Explosion du nombre de données connectées, générées et stockées
    - Développement des technologies du Cloud et de la virtualisation (augmentation des capacités de traitement)

## Loi de Moore

Evolution linéaire de la puissance des processeurs dans le temps (Ca a duré pendant 20 ans, après limite physique et technique)
Problème : Pratique mais changement de matos régulier donc onéreux

## Hadoop

Environnement de technos pour faire un programme classique et le transformer en instructions en MapReduce
Hadoop est en JAVA
En découle SPARK, spécifiquement créé pour le traitement de données mais codé en SCALA
Mais il existe la librairie PySpark pour piloter Spark

Au minimum, 4 composants :
    - HDFS (Hadoop Distributed File System)
    - Hadoop Common (pilotage, admin system, scheduler)
    - Hadoop MapReduce (gestion fichiers, shuffle & sort)
    - Hadoop YARN (ressource manager,en général: c'est le node master sinon il y a une machine ressource manager)

Création d'un réseau
```
docker network create --driver=bridge hadoopnet
```

Lancement de docker pour créer le master sur le réseau créé avec 4 ports pour communiquer avec les workers et avec l'utilisateur
```
docker run -itd --net=hadoopnet -p 50070:50070 -p 8088:8088 -p 7077:7077 -p 16010:16010 --name hadoop-master --hostname hadoop-master liliasfaxi/spark-hadoop:hv-2.7.2
```

lancement de docker pour créer un worker sur le réseau créé
```
docker run -itd --net=hadoopnet -p 8040:8042 --name hadoop-slave1 --hostname hadoop-slave1 liliasfaxi/spark-hadoop:hv-2.7.2 
```

Début de commande pour piloter Hadoop (ici, on crée un dossier)
```
hadoop fs -mkdir -p input
```

Liste des fichiers et dossiers créés avec Hadoop
```
hadoop fs -ls
```

actions sur un fichier dans un fichier
```
hadoop fs -put chemin_de_ma_cible
hadoop fs -get chemin_de_ma_cible
```

Affichage du fichier
```
hadoop fs -cat input/purchases.txt | head
hadoop fs -tail input/purchases.txt
```

Renommer un fichier
```
hadoop fs -mv ancien_nom nouveau_nom
```

Supprimer un fichier
```
hadoop fs -rm nom_fichier
```

lancer le programme WordCount avec les fichiers du dossier input en entrée
```
hadoop jar WordCount.jar input 
```
