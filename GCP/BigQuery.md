# Exemple

````
SELECT  
  name,  
  gender,  
  SUM(number) AS total  
FROM  
  bigquery-public-data.usa_names.usa_1910_2013  
WHERE  
  gender = "F"  
GROUP BY  
  name,  
  gender  
ORDER BY  
  total DESC  
LIMIT  
  25;  
````

# Afficher les nombre de fois ou le prénom "Marie" a été donnée en 1914 par état

````
SELECT  
  name,  
  year AS annee,  
  state,  
  SUM(number) AS number  
FROM  
  `bigquery-public-data.usa_names.usa_1910_2013`  
WHERE  
  name = 'Annie'  
  AND year = 1914  
GROUP BY  
  name,  
  annee,  
  state  
ORDER BY  
  number DESC;
````


# Donner les 3 années ou ce prénom a été le plus données

````
SELECT  
  year AS annee,  
  SUM(number) AS number  
FROM  
  `bigquery-public-data.usa_names.usa_1910_2013`  
WHERE  
  name = 'Annie'  
GROUP BY  
  name,  
  annee  
ORDER BY  
  number DESC  
LIMIT 3;
````

 # Faite la somme entre homme et femme,toutes années confondues

````
SELECT  
  gender,  
  SUM(number) AS number  
FROM  
  `bigquery-public-data.usa_names.usa_1910_2013`  
WHERE  
  name = 'Marie'  
GROUP BY  
  gender  
ORDER BY  
  number DESC;
````

#CONDITION dans la requete

````
SELECT  

#Se comporte comme un opérateur ternaire  
#if condition ? si vrai : si faux  

if(gender = 'F','Femme','Homme'),  
sum(number) as total  

FROM  
  `bigquery-public-data.usa_names.usa_1910_2013`  
WHERE  
  name = 'Marie'  
GROUP BY  
  gender;
````

# Condition dans la requete

#Condition dans la requete   
#Aller dans la table "crime" placé dans le dataset "austin_crime"  
````
SELECT 
ifnull(clearance_status, 'Non renseigné') as clearance_status
FROM 
  `bigquery-public-data.austin_crime.crime` 
ORDER BY
  clearance_status desc
LIMIT
  1000;
````

````
SELECT
#Nous pouvons faire la même chose avec "if"
if(clearance_status is null, 'Non renseigné', clearance_status) as clearance_status
FROM
  `bigquery-public-data.austin_crime.crime`
ORDER BY
  clearance_status desc
LIMIT
  1000;
````

# CASE WHEN

````
SELECT

#reprend un switch case
CASE
  # si clearance_status égal à 'Not cleared', alors on affiche "Pas d'arrestation"
  WHEN clearance_status = 'Not cleared' THEN 'Pas d\'arrestation'
  WHEN clearance_status = 'Cleared by arrest' THEN 'Arrestation'
  # dans tous les autres cas, on affiche autre
  ELSE 'Autre'
# nom de la colonne
# Le END est obligatoire pour indiquer la fin du "CASE"
END AS etat_enquete

FROM `bigquery-public-data.austin_crime.crime`
LIMIT 1000;
````

# WITH

WITH permet de faire des sous-requete

````
#Creation de la requete

WITH nbr_stations AS(
  SELECT
    region_id,
    COUNT(distinct station_id) as nbr_de_stations

  FROM `bigquery-public-data.san_francisco_bikeshare.bikeshare_station_info`

  GROUP BY region_id
)

#Appel de la requete

SELECT 
region_id,
nbr_de_stations
FROM 
  nbr_stations`
````
