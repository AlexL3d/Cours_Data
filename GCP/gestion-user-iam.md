# La gestion des utilisateurs.


github : je creer un compte de service qui permet à github de se connecter pour faire du CD.

Pour les humain on utilise IAM.

IAM fonctionne par projet. 

Il faut creer un projet GCP pour notre projet fil rouge.

On peut ajouter un compte principal.

## Ajouter un compte.

Aller dans IAM et administration, accorder l'acces.

On donne l'adresse mail du compte GCP de l'utilisateur. 

Il faut choisir un role. Qui donne accès à des service en lecture ou écriture.

Pour le projet on peut se comtempter de l'instance de base. 

* Editeur : Peut acceder et modifier toutes les ressources
* lecteur : ne peut rien creer rien faire
* explorateur : Peut voir toutes les ressources mais ne pas les modifier
* propriétaire : in god we trust

## Les brokers

On a des applications génératrices de données (site web, scripts ....) - Publisher

On a des applications consommatrices de données. - Subscriber

Pour envoyer des données de l'un à l'autre on peut faire des requetes. Mais à chaque fois que je change de consommateur (ip) je dois changer le code du produceur. Si un cosommateur tombe il fait bugger le produceur. Il faut prendre en charge le scaling. Bref c'est la merde.

On met entre les deux un pub/sub (ou broker). Un publisher modifie un Topic et envoie l'information au subscriber. Il garde aussi les info en cas de crash ou surcharge.

Le pub/sub est au centre de pas mal de choses en GCP. Le plus connu de tous c'est Kafka.

Je peux faire un script python qui s'execute dès qu'il y a un changement dans un topic. Je peux aussi demander au publisher, de publier sur des topic à interval de temps regulier.

On doit activer l'API pub/sub.

Utiliser un schema : Forcer les messages à prendre une certaine forme

Activer la conservation des messages : Stocke les messages.

### Coder un Publisher

    from google.cloud import pubsub_v1

    TOPIC_NAME = "demo-on-my-first-project"

    PROJECT_ID = "rugged-truck-393808"

    TOPIC_STR = f"projects/{PROJECT_ID}/topics/{TOPIC_NAME}"



    publisher = pubsub_v1.PublisherClient()

    publisher.publish(TOPIC_STR, b"Hello world")

### Coder un subscriber 

    # Un subscriber ça s'ouvre et se ferme
with pubsub_v1.SubscriberClient() as sub:
    #Create a subscription if not exist
    sub.create_subscription(
        name=SUB_STR,
        topic=TOPIC_STR
    )
    
    
    # We subscribe to a subscription
    # We add a callback, when the sub receive a message it will execute the function print
    future = sub.subscribe(SUB_STR, print)
    try:
        future.result()
    except KeyboardInterrupt:
        future.cancel()

Le pub/sub permet de faire du streaming.

(Mais ça marche pas il vas regarder)

## Executer un scipt tous les matins

Plein de méthode (exemple acheter une VM qui lance tout les matins)

Ou passer par un outil Cloud Functions

### Creer un trigger

Trigger : Peut être plusieurs chose, une requette Http ou un pub/sub

Add Triger/ pub/sub et nom du pubsub

Appuyer sur suivant. 

Choisir l'environnement d'execution

Il faut mettre nos dépendances particulières dans le requirements.txt

On paye à la requete, si on fait quelques requetes par jour on ne va pas payer bcp gratuit jusqu'a 2 millions de requetes par jour.

On peut mettre le code a executer dans l'editeur

    import base64
        import functions_framework

    # Triggered from a message on a Cloud Pub/Sub topic.
    @functions_framework.cloud_event
    def hello_pubsub(cloud_event):
        # Print out the data from Pub/Sub, to prove that it worked
        print(base64.b64decode(cloud_event.data["message"]["data"]))

Là par exemple, il imprime le message et la data du message.

Je peux remplace la fonction hello_pubsub par ma fonction à moi.

### Creer un pub/sub qui publie tout les jours.

## Cloud skeduler 

Permet de planifier une tâche tous les certain temps.

Creer une tâche, nom de la tâche, fréquence au format CRON.

Aller dans configurer l'execution, cibler le PUB/SUB, je selectionne le sujet dans lequel publier et j'ajoute le message. 


    Je peux par exemple faire une tâche qui quand elle reçoie un message, en fonction du message, revoit un message dans un autre topic. Une fois ce nouveau topic mis à jour, alors ça relance une nouvelle fonction.


