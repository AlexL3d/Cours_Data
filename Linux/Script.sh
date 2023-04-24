#! /bin/bash

# Exo sur la VM Debian

# Création du dossier Download
mkdir /home/leduca/Documents/Download
cd /home/leduca/Documents/Download

# Création des sous-dossiers 
mkdir Autre Image Music Video

# Création du fichier Readme.txt
text="Ceci est le fichier de Téléchargement. \nMerci de respecter l'origanisation du répertoire. \nAttention aux virus. \nLe dossier téléchargement est prêt."
echo -e $text > Readme.txt

#Création du fichier music.mp3
cd Music
touch music.mp3

# Récupération des lignes avec le mot Téléchargement
cd ../..
grep "Téléchargement\|téléchargement" /home/leduca/Documents/Download/Readme.txt