# Kubernetes ou k8s

C'est un orchestrateur de conteneurs, gérer le déploiement, mise à l'échelle et maintenabilité de conteneurs.
Utilisé en micro-services qui a les mêmes propriétés que Hadoop et le travail distribué.

- Node : Equivalent d'un worker(machine de travail), peut contenir plusieurs Pods.
- Pod : Inclus dans le Node, une unité fonctionnelle de Kubernetes(+/- un conteneur Docker donc une appli).
- Service : Associé à un Pod (et ses copies), possède une IP fixe même si le Pod est détruit et recréé (et fais le lien entre le Pod et le réseau). Tous les services ont la fonction de LoadBalancing (équilibre la quantité de travail sur les Pods sous son contrôle). Les services peuvent être duppliqués si l'un crash.
    -> Service Externe : Utile pour l'accès à des utilisateurs (UI).
    -> Service Interne : Utile pour isoler des Pods qui n'ont pas lieu d'être approchés par l'utilisateur (ex : Base de données)
- Ingress : DNS qui fait correspondre un nom de domaine à une IP d'un service externe. duppliquable pour éviter des pbs si l'un crash
- CongifMap : Charger les infos persistantes (nom de services, etc...) Comme un .env. Fichier commun
- Secret : Permet de garder les infos sensibles, encodé en base 64 (user, password). Fichier commun
- Volumes : dans les Nodes, permet la persistance des données si destruction ou suppression du Pod. (Local ou distant)
- Deployment : Fichier mode d'emploi pour déployer l'architecture (un peu comme un docker-compose), ça ne stocke pas l'état de mon système.
- StatefulSet : Deployment spécifique pour conserver l'état de ce qui a été déployé pour les bases de données

K8s: 
    - Node :
      - Master :
        - API server (peut permettre de gérer la sécurité des connexions)
        - Scheduler (quand est déployé un pod avec ses caractéristiques)
      - Slave

Chaque node contient :
    - un containerRunetime pour faire tourner les conteneurs (Majorité des cas : Docker).
    - Kubelet : intermédiaire entre ce que veut l'utilisateur et le node va fabriquer dans son environnement. (il utilise le runtime et surveille l'état du node(état CPU,RAM,Stockage,puissance)).
    - K-Proxy : process d'architecture réseau interne , passerelle de communication entre services et pods.
    - ControlManager : surveiller l'état de tous les pods et le sauvegarder (cartographie tout ce qui a été exécuté). Equivalent au RessourceManager (état actuel réel)
    - ETCD : Dictionnaire qui enregistre les métadonnées du cluster. (qui est déployé où pourquoi sur quel machine etc) (état actuel souhaité)

# Minikube

déploiement dans un conteneur docker la totalité d'un micro cluster-Kubernetes (permet de bosser en formation sans avoir besoin de beaucoup de machines physiques ou virtuelles )

# KubECTL

Interface en ligne de commande pour contrôle Minikube

# Maccro

kubetcl apply -f "NomDuFichierADéployer"
kubetcl get pod/node/service/deployment/secret/etc...

# Namespace

Permet d'organiser les pods etc (que pour la gestion, C'est TOUT)

kubectl get namespace
Par défaut, on utilise le default.
Ne pas toucher à celui du système !!!!!
Le Node-lease ne sert qu'au monitoring

kubectl create namespace mon-namespace pour créer son propre namespace
kubectl get pod -n mon-namespace pour check les pods de ce namespace

kubens permet de ne pas toujours renseigner le namespace et garde le dernier en mémoire
kubetcx permet de switch entre environnement de prod et dev

# Ingress

Ajout de l'IP de l'INGRESS dans le fichier C:\Windows\System32\drivers\etc\hosts
avec l'IP et le nom du host renseigné dans l'Ingress

# Helm Charts

Manager de paquets pour K8s
Quand on a besoin d'un cluster avec bcp d'images, fichiers de config etc, on utilise un équivalent docker pour K8s => Helm charts
site : artifacthub.io

# Volume

PersistantVolume pour la persistance des données
On passe par un PersistantVolumeClaim pour lier le Pod au PV