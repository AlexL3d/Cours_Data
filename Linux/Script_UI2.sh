#! /bin/bash

echo "Entrez votre login :"
read -n 5 login
while true; 
    do
        echo "Entrez un mot de passe : "
        read -s -t 10 MDP
        if [[ -z "$MDP" ]]; then
            echo "Vous devez entrer un mot de passe :"
        else
            break
        fi
done
echo "Votre login est : $login.
Votre MDP est : $MDP."