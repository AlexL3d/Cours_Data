#! /bin/bash

echo "Choisissez le format de dates :"
options=("J/M/A" "M/A/J" "A/J/M")
select option in "${options[@]}"
echo "Vous avez choisi la date en $option"