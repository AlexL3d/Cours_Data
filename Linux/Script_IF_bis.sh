#! /bin/bash

read -p "Entrez un nombre : " NBR

if ! [[ $NBR =~ ^[0-9]+$ ]]; 
then echo "Ceci n'est pas un nombre."

elif [ $NBR -eq 0 ];
then echo "Vous avez entré zéro."

elif [ $NBR -gt 0 ];
then echo "Vous avez entré un nombre positif."

else echo "Vous avez entré un nombre négatif."

fi