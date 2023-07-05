# Prendre une image de base
# Je fais une app node alors je prend une image alpine node de base.
FROM node:alpine

#Creer un repertoire de travail
WORKDIR /app/node

#Copier la liste de mes dépendances
COPY package*.json .

#install les dépendances, installe les dépendance de package.json
RUN npm install

#copie de mon application node js
COPY index.js .

#ouvrir le port de mon application
EXPOSE 3333

#Demarre mon application
CMD ["npm","start"]

# il me reste ensuite à faire la commande "docker build -t manodeapp ."