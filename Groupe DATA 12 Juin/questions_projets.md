# Projet DataElec

## notes

Analyse conso élec (paramètres d'influence)
Sources : Open Data réseau Energies, L'INSEE, l'éducation nationale(???)
excel voca et versioning des données
DataLake avec Docker Volume

## Outils

Docker
GitHub
GCP
Qlik Sense / PowerBI
Talend

# Why Not 2026 - Résultats élections municipales

## notes

besoin d'un potentiel candidat : cibler Nord, cibler population, histo des votes de 2001 à 2020
Cadrage du projet au HDF puis recadrage au département Nord
Données : INSEE, Ministère de l'intérieur (CSV,XLS: fichiers plats) environ 8Go
déduction des cibles après analyses
Focus sur Lille et sa périphérie

## Outils

GitHub
Qlik Sense / PowerBI
Talend

# Evolution de la conso des médocs psychotropes post Covid

## notes

def de ce qu'est un psychotrope et types
projet initial sur la dépression puis dérivé car pas de Data
Données : fichiers CSV sur Data.gouv => 3 bases
Augmentation depuis Covid mais reste bas comparé à 2014

## Outils

Comm
GitHub
Talend
Bdd MySQL
PowerBI

# Find Your Future

## Notes

Trouver un métier dans le domaine de la DATA via l'API pole Emploi
migration de Drive à GCP (pyspark sur Databricks)
Automatisation de la récup des données
Dashboard avec plusieurs onglets en dynamique avec cases/filtres

## Outils

Pipeline
Talend
Pyspark
GCP
Databricks
API
Kubernetes

# Contexte socio-économiques des quartiers lillois

## Notes

Données + ETL + Analyse
Pour DataViz, Map en superposition de couches, génération de fichiers KML pour intégration QlikSense
Analyses des dynamiques de l'emploi, l'impact de spolitiques publiques et dynamiques démographiques
=> tendances et comparative

## Outils

Extract : API + Scrapping + fichier CSV => DataLake
Scrapping => Selenium puis BS4 puis Json transformé avec pandas => CSV => DataLake
Api récup en XML puis pandas en transfo CSV => DataLake
Modèle analyse données spaciales (géoloc)

# Trucs à garder, pas pensé

présentation des outils (teams, Docker, Github?, Jira, etc...)
dico voca
Qlik pour viz en carte est meilleur, Power Bi meilleur sur la def des clés
retour XP du projet
Visuels souhaités en amont pour def les Bdd en fonction (Bdd dénormalisées ???)
Travailler en Container Docker pour la collab distante ?
Intro + But + prez projet + prez équipe
Figma, logiciel de prévisualisation (maquette DataViz)
Prez de la DataViz en vidéo??
