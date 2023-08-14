# Avant dans l'informatique

## MainFrame 

Exemple AX400 (IBM)
On achete un gros server bien bourrin, il faut le refroidir entre 19 et 20°, sans poussière et sans humidité (évaporation en cas de chauffe), système anti incendie.

On a des interfaces sur le coté pour pour envoyer des programmes à la machine.

## Acheter un server.

On peut acheter des blades ou des racks (grosse armoire avec 42 slots).

Les composants electroniques des ordinateurs, on une durée de vie limitée en utilisation. C'est pour ça qu'on ne peut pas utiliser un ordinateur en guise de serveur.

Il existe des composants fait pour durer dans le temps. Exemple processeur Xeon qui sont fait pour durer jusqu'a 3 ans en utilisation.

Il faut installer tout le Hardware, plus tout le software (il faut un admin systeme + un admin réseau)

Ca coute très cher + faut du temps a installer + consomme énormément d'electricité.

## Louer un emplacement dans un datacenter.

Loue au mois, un espace dans un datacenter. Loue une machine virtuelle cad on rempli un datacenter de machine et ces machines sont découpées en VM sur une systeme (Vesper), on loue au mois ou à l'année. Pour une machine moyenne on est sur un prix en moyenne de 100€ à l'année.

## Le cloud.

L'idée du cloud c'est la mutualisation de ressource.

C'est plein de serveurs, connecté entre eux. On met des services (possibilité de VM ou Kubernetes).

Cloud privé Vs Cloud publique:

- Publique : Fournisseur de cloud qu'on connait (GCP,AWS,AZURE).
- Privé : Cloud qui n'est pas accessible au publique. Une entreprise achete des datacenter et les connecte entre eux.

Le problème du cloud Publique est la gouvernance des données. Les données qui sont héberger sur des plateformes américaines peuvent être consulté par les USA si l'état américain estime que pour des raisons de défense elle doit les consulter. (Patriot act).

Le défaut du cloud privé. A pour défaut sa plasticité, il s'adapte moins. Il faut aussi une équipe pour l'entretenir ça coute cher. Il faut aussi assuré la sécurité des données (incendie OVH).

### AWS et les autres

Amazon avait plein de serveur pour ses propres besoins. A décider de louer sa puissance en trop pour la proposer à d'autres entreprise.

Ils ont décidé de passer la facturation non pas au mois comme avant, mais à l'heure. Permettant aux entreprises qui on besoin de faire un traitement de quelsques heures d'aller chez eux. 

GCP et Azure se sont aligné sur eux.

Ils proposent plus que juste monter des VM. Ils ont intégrer des services (Ce sont des VM déja config avec une petite interface qu'on a pas besoin de configurer nous même)

Ils cherchent a respecter la regle des 180s, pour deployer une machine.

GCP : Google possède sont moteur de recherche. Ils n'allaient pas le vendre, mais vende la technologie de BDD qui se cache derrière BigQuerry et BigTable. (il existe d'autres technologie spécifique à Google). Azure à ses propres technologies (open AI). 

# GCP 

Cloud publique fait par Google qui permet d'acceder à des ressources sur notre machine en les payant à l'heure.

## On-Premise Vs SAAS

Les technologie On-Premise: Qu'on peut telecharger en local. Exemple Spark

Les technologie Non On-Premise : qu'on ne peut pas utiliser sur nos propres serveur SAAS. Databricks est purement saas, on ne peut pas le telecharger en local.