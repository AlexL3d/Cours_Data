#! /bin/bash

echo "Choisissez entre les options "r","s" "d" ou "h" : " 
select option in "r" "s" "d" "h" ;
do
    case $option in 
        "r" )
            echo "Le programe démarre." 
            break
            ;;
        "s" )
            echo "Le programe s'arrête." 
            break
            ;;
        "d" )
            echo "Le programe se supprime." 
            break
            ;;
        "h" )
            echo "Le programe affiche l'aide disponible." 
            break
            ;;
        * )
            echo "Option invalide." 
            ;;
    esac
done