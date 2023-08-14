initiation au cloud

GCP est quasiment tout traduit en Français

Et a des tutos.

IAM interface administration
Facturation
Comment monter une VM, comment découper ça VM.
DataProc
BDD

# Bienvenue sur GCP

2 manières de gérer. Interface graphique ou Gcloud (invité de commande)

Les cloud sont fait pour travailler en entreprise et en général les entreprises on plusieurs projet.

On travail en projet, les projet sont un peu délié les un des autres.

Il y aussi des API

API : ensemble d'outils qu'on peut activer sur notre compte GCP. Certaines API sont payantes

IAM : C'est l'administration, la ou l'on gère les utilisateurs, les rôles.

Facturation : La doulourante, facturation du projet.

## Faire une machine virtuel

Cliquer sur Creer une machine virtuel, ou sur Compute Engine API.

Il faut activer l'API.

On accede au site Compute Engine, qui donne accès à toutes les machines sur ce projet.

On a tous les outils pour gerer les machines virtuelles (Observabilité).

On peut faire de la planification d'instance. (Je la lance à 8h et s'arrete à 20h)

Je creer une VM.

Region = Dans quel region je veux que mes données se trouvent.

Mémoire optimisé : Entre 200 et 400 CPU. Entre 5To et 11To de ram.

Le choix des machines c'est un métier Architect Cloud.

On peut rajouter des services en plus.

Service Confidential VM : Systeme qui sécurise les données de la VM

Disque de démarrage : Choix de l'iso. On peut mettre nos propres ISO.

On peut changer le type de disque et la taille.

Par feu : Il faut l'activer si notre VM doit communiquer en HTTP ou HTTPS.

On a acces en SSH à la VM. Pour se connecter par SSH en dehors de Google Cloud (sur ma machine), il faudra passer par un outil semblable à un VPN.

Quand on arrete une VM on ne paye plus la VM, mais on paye toujours le disque.

Supprimer : Delete la VM + le disque en même temps.

## Les images docker

Pour utiliser une image docker il faut soit l'avoir sur dockerHub, soit directement dans GCP. Et c'est moins cher de les mettre directement dans GCP (Car ils payent moins de bande passante)

Quand je lance une VM/Conteneur/Deployer un conteneur

J'ajoute une image.

Je dois aller dans les parametres avancés, pour mettre en réseau ma machine virtuel.

## Le service Mysql

Plutot que de lancer une VM avec un conteneur mysql, il y a un service SQL qui le fait directement.

On tape SQL dans la base de recherche.

* MySQL
* Postgres
* SQLserver

Le service SQL coute un peu cher, on peut réduire son cout avec des réduction. On peut changer aussi les performance du serveur.

Dans la version bac à sable, on peut ajouter des disques de stockage, changer le type (SSD à HDD)

On peut passer à coeur partagé : Le CPU est partagé avec d'autres personnes (C'est lent on évite en général).

### Les VPC

Cloud privé virtuel, permettent de creer une sorte de réseau entre plein d'instance et de VM.

Pour se connecter de manière simple. On va dans connexion et la on ajoute un réseau.
    nom : m2i
    Reseau : adresse du batiment 185.31.149.99

Ainsi j'autorise les connexion depuis ce network. Ce n'est pas une bonne pratique, normalement on n'autorise pas les connections à notre BDD depuis l'extérieur.

## Stockage de fichier ou Bucket

Le bucket est une espace de stockage qui est l'element de base de plusieurs outils. Spark à besoin de bucket.

Pour creer un bucket, on clique sur create a bucket dans la page acceuil ou on tape cloud storage dans la barre de recherche.

Les tags permettent de regrouper les buckets, pour les administrer.

region où stocker les données : Multi-region il se démerde pour choisir ou

**Classe de stockage** : Performance en fonction de la fréquence à laquelle je consulte mon bucket.

**Controle d'acces** : J'ai une API google en python pour me connecter directement dans le bucket.

On peut ajouter des règles par exemple la gestion de la version d'objet. Ca peut être obligatoire dans certains projets.

# Spark + Jupyter

Afficher tous les produits / Analyse

* BigQuery : entrepot de données pour faire des analyse
* Pub/sub : systemes sur lequels on peut travailler, on peut publier dans des topics. Et d'autres application vont souscrire un abonnement au topic. Une fois que quelque chose est publié dans le topic, les applications sont notifiées.
* Dataflow : Utilise Apache Beam qui est un concurent de spark. Melange entre airflow et spark.
* Composer : Equivalent de airflow
* Dataproc : Qu'on va voir maintenant
* Dataprep : Outil visuel
* IoT Core : gere les outils connectés (osef)
* DataFusion : permet de faire des pipeline
* Looker :
* Healthcare : Pour des données médicaux, avec des algo spécifiques
* Datastream :
* Databricks
* Elasticloud : equivalent elasticsearch

DataProc est un HDFS avec un spark déja installé.

On ne parle plus de creer une instance, mais de creer un cluster.

Il faut pour la première utilisation activer l'API.

Cluster sur Compute Engine :
Cluster sur GKE : Kubernetess c'est très bien mais très cher.

Avec GKE le spark est plus élastic, plus facilement scalable, on peut aussi ajouter d'autres outils pour aller plus loin.
On choisit donc Compute Engine qui est très suffisant.

**Emplacement**

**Type de cluster**

- Standard : un noeud maitre et n noeuds de calcul réparti sur plusieurs noeuds (si on choisi ça il faut mettre des règle pour l'auto scaling)
- Haute disponibilité : Plusieurs noeuds maitres, ça coute vite très cher.

**Metastore** : Endroit ou sont gerer nos metadonnées

**Activer la passerelle des composant** : OUI, car je peux mettre en composant facultatif jupyter notebook. (met jupyter)


**Aller dans l'onglet de configuration des noeuds :**
Dataprocs il faut l'arreter dès que j'en ai pas besoin.
Il faut pas forcement prendre les trucs les plus nuls. (E2 standard 2, taille du disque principal : 50Go devrait suffire)
nombre de noeuds : 2 c'est déja bien (attention il y a trois serveur qui tourne, penser à bien l'éteindre). En mémoire on met 50Go.

**Les noeuds de calcul secondaire** : OSEF frere

Une fois que mon cluster est créer je peux cliquer dessus, aller dans interface web et je peux cliquer sur JupyterLab pour lancer jupyter.

Si je vais dans compute Engine, je vois bien mes machines virtuelles

Si je vais dans Cloud Storage, je vois qu'il m'a créer deux buckets temp et staging.

Dans staging c'est là qu'il y a mes notebook. Je peux importer mes notebook locaux ici avec le bouton spark.

## Lancer un notebook

Je creer un notebook pyspark (pas python)

Je n'ai pas besoin de creer un spark context ou une session, c'est déja configuré.

## Arreter un cluster.

Je vais dans dataproc, j'arrete mon cluster il arrete automatiquement les VM du cluster. On ne paye plus les machines, mais on continu de payer les disques.

# Exercice : Creer un word count

Le Bucket de préproduction: Avoir un bucket réutilisable pour mettre nos données à l'intérieur. On peut supprimer le bucket quand on en a plus besoin.

    gcloud dataproc clusters create cluster-2de7 --enable-component-gateway --region europe-west1 --zone europe-west1-b --master-machine-type e2-standard-2 --master-boot-disk-size 50 --num-workers 2 --worker-machine-type e2-standard-2 --worker-boot-disk-size 50 --image-version 2.1-debian11 --optional-components JUPYTER --max-idle 7200s --project arcane-mission-393809

On peut le lancer depuis le local, pour cela il faut telecharger le cli gcloud.

Je creer un Bucket pour ranger mes fichiers source.

Je creer deux dossiers: input et output.

On peut rendre un bucket visible en dehors de GCP, mais dans ce cas il faut s'identifier dans le script. On ne s'identifie pas avec nos credentials à nous, mais il faut creer un compte de service(on voit ça plus tard.)

Dans les configuration de mon bucket, il y a une ligne URI gsutil (unified identifiant), qui est l'identifiant du bucket DANS GCP (pas depuis l'exterieur donc)