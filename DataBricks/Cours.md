# DataBricks

## Concept

FrameWork de traitement et analyse de données en Cloud en centralisant tout en une interface
Basé sur Apache Spark, utilisation en NoteBooks (comme avec Jupiter dans le container)

## Utilités

Mise en place au centre de l'écosystème et permet de traiter les données structurées ou non et de sources diverses
DataBricks peut dont gérer les processus d'extraction, de transformation et d'analyse des données ainsi que leurs stockages dans le Cloud, tout ceci : dans des pipelines aussi gérés par DataBricks
Il peut aussi configurer les BDD, les clusters et ainsi que les problématiques réseaux par rapport aux différents NoteBooks
Plusieurs utilisateurs connectés au même DataBricks avec des droits différents

### Centralisation

DataBricks centralise 3 domaines :
    - Data Engeering
    - Data Science
    - Business Intelligence

Stockage de toutes mes sources ainsi que les transformations via NoteBooks et donc réutilisation des sources et NoteBooks pour des nouveaux projets en y incluant de nouvelles sources et de nouveaux NoteBooks

### Vision DeltaLake

Databricks = Spark + DeltaLake

### Attention

Il y a des choses uniquement viables sur DataBricks et tout ne peut pas être fait sur DataBricks

## Déploiement sur Azure

DataBricks = Compte d'essai gratuit : 14 jours gratuits => Après, paies !
Azure = 200 Dollars de crédits et 90 jours

### Ressources

Tout est géré sous forme de ressources : IP, réseaux, machines physiques, machines virtuelles, etc...
Toute ressource est rangée dans un groupe de ressources (tri et management, accès)
Chaque groupe dépend d'une souscription (abonnement : qui a la responsabilité de ces ressources => paiement)
Chaque abonnement dépend d'un groupe de gestion qui a les droits administratifs du service Cloud (attribution des droits à des ressources)

### Utilisation 

Barre de recherche : DataBricks => Ouverture d