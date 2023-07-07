# Utilisez une image de base Python
FROM python

# Définition du répertoire de travail dans le conteneur
WORKDIR /app

# Copie des fichiers requis dans le conteneur
# Le point sert à copier le fichier dans le dossier du WORKDIR
COPY requirements.txt .
COPY appFlask.py .

# Installation des dépendances
RUN pip install -r requirements.txt

# Exposer le port utilisé par l'application Flask
EXPOSE ${PORT_FLASK}

# Définir les variables d'environnement pour MongoDB
ENV MONGO_HOST=localhost
ENV MONGO_PORT=${PORT_MONGODB}
ENV MONGO_DB=Bdd_user
ENV MONGO_COLLECTION=user

# Commande pour exécuter l'application Flask
CMD ["python", "appFlask.py"]
