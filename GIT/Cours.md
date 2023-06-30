# GIT

### Commandes et explications

##### Configuration GiT

git config --global uer.name "Votre Nom" => Déf votre nom d'utilisateur pour Git
git config --global user.email "votre Email" => déf du mail pour Git
git config --list pour voir les infos de Git

##### Convention nommage Commit

exemple : git commit -m "feat:CréationDeLaFeature"

"fix" pour la réparation
"feat" pour l'ajout de feature
"docs" pour la documentation
"refactor" pour optimisation du contenu ou compréhension du code
"style" pour changement qui modif pas la compréhension du code

"git status" pour voir si des commits sont en attente
"git add ." pour ajouter tout ce qu'il y a dans le folder
"git log" ou "gitk" permet de voir les commits réalisés

Doc Git Officiel sur le site Git
"git help nomdelacommande" pour afficher les infos
"git remote add origin https://github.com/AlexL3d/TestGit.git" 
"git branch -M main" => renommer (modify)
"git push -u origin main"

si erreur avec le READme auto-généré : 
"git branch --set-upstream-to=origin/main main"
"git pull origin main --allow-unrelated-histories"

##### Bonnes pratiques

Ne jamais bosser sur la branche main(nouvelle convention pour master), il faut développer sur une autre branche pour ensuite merge le tout sur main.

Quand tu as fini de développer la feature, tu merges sur la branche develop et tu supprimes sur la branche de la feature sur le repo mais pas en local.

##### Récupérer un repo distant en local

"git pull" : récupérer le distant pour le mettre en local
"git clone" + lien de repo : création du repo distant en local et connexion au repo

##### Naviguer entre les branches

"git checkout -b feat" : créer ou aller sur une branche existante
"git switch feat" : créer ou aller sur une branche existante
"git fetch" : récupérer l'historique mais pas de fusion en local
"git pull" : récupérer l'historique en fusionnant en local

git push --set-upstream origin NomDeLaBranche : créer branche en distant lorsque la branche n'existait pas en distant mais présente en local

git branch -d NomDeLaBranche : suppression de la branche en local
git push origin --delete NomDeLaBranche : suppression de la branche en distant

##### Travailler simultanément

"merge" : Fusion des branches pour intégrer les modifs apportées par les branches de développement avec une branche principale.

"git merge develop NomBrancheàMerger" : commande pour merge en local

##### Git rebase

"git rebase" : mettre à jour la branche actuelle avec les modifications d'une autre branche. Tout en préservant l'historique de modif.

On s'en sert pour intégrer les modifs d'une branche principale dans une branche secondaire. Garde une liste historique de commits claires et propres.

##### Git merge et Git rebase

git merge : fusion des branches en créant un nouveau commit qui incorpore les changements des branches
nouvel historique de commit distinct pour les 2 branches fusionnées.

git rebase : réapplique les modifs sur une branche à partir de son point de départ.

On réécrit tous les commits de la branche que l'on veut intégrer dans l'historique de la branche qu'on intègre.

##### Pull requests

Demande pour faire les modifs qui ont été push à une branche principale.

La PR doit être validé par un autre contributeur.
La PR se fait sur GitHub.


Exercices sur le site LearnGitBranching