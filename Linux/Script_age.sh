#! /bin/bash

read -p "Entrez le nom du premier fichier : " fichier1
read -p "Entrez le nom du second fichier : " fichier2

date1=$(stat -c %Y $fichier1)
date2=$(stat -c %Y $fichier2)

if [ $date1 -gt $date2 ];
then echo "Le premier fichier est plus récent que le second."

elif [ $date1 -lt $date2 ];
then echo "Le second fichier est plus récent que le premier."

else echo "Les 2 fichiers sont aussi récents l'un que l'autre."

fi

cheminf1=$(find / -name $fichier1 2>/dev/null)
cheminf2=$(find / -name $fichier2 2>/dev/null)

echo "Le chemin du premier fichier est : $cheminf1."
echo "Le chemin du second fichier est : $cheminf2."
