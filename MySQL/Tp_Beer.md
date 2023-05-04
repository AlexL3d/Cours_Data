# TP BEER

## Exercice 1 :

```
select 
    numero_ticket 
from 
    ventes
where 
    ventes.ID_ARTICLE =500;
```

## Exercice 2 : 

```
select 
    numero_ticket
from 
    ticket
where 
    date_vente='2014-01-15';
```

## Exercice 3 :

```
select 
    numero_ticket
from ticket
where 
    date_vente between '2014-01-15' and '2014-01-17';
```

## Exercice 4 :

```
select distinct
	NOM_ARTICLE    
FROM 
	article 
join ventes
on article.ID_ARTICLE = ventes.ID_ARTICLE
where 
    ventes.QUANTITE >= 50;
```

## Exercice 5 :

```
SELECT 
	NUMERO_TICKET
FROM
	TICKET
WHERE 
	MONTH(DATE_VENTE)=3
	AND YEAR(DATE_VENTE)=2014;
```

## Exercice 6 :

```
SELECT 
	NUMERO_TICKET
FROM
	TICKET
WHERE 
	MONTH(DATE_VENTE) BETWEEN 3 and 4
	AND YEAR(DATE_VENTE)=2014;
```

## Exercice 7 :

```
SELECT 
	NUMERO_TICKET
FROM
	TICKET
WHERE 
	MONTH(DATE_VENTE) IN (3,6)
	AND YEAR(DATE_VENTE)=2014;
```

## Exercice 8 :

```
SELECT distinct
	ID_ARTICLE,
    NOM_ARTICLE,
    ID_Couleur
FROM 
	article
WHERE ID_Couleur is not NULL
ORDER BY ID_Couleur;
```

## Exercice 9 :

```
SELECT distinct
	ID_ARTICLE,
    NOM_ARTICLE
FROM 
	article
WHERE ID_Couleur IS NULL ;
```


## Exercice 10 :

```
SELECT
	NUMERO_TICKET,
    SUM(QUANTITE) as QUANTITE_TOTALE
FROM 
	VENTES
GROUP BY NUMERO_TICKET
ORDER BY QUANTITE_TOTALE DESC;
```

## Exercice 11 :

```
SELECT
	NUMERO_TICKET,
    SUM(QUANTITE) as QUANTITE_TOTALE
FROM 
	VENTES
GROUP BY NUMERO_TICKET
HAVING QUANTITE_TOTALE > 500 
ORDER BY QUANTITE_TOTALE DESC;
```

## Exercice 12 : 

```
SELECT
	NUMERO_TICKET,
    SUM(QUANTITE) as QUANTITE_TOTALE
FROM 
	VENTES
WHERE QUANTITE < 50
GROUP BY NUMERO_TICKET
HAVING QUANTITE_TOTALE > 500 
ORDER BY QUANTITE_TOTALE DESC;
```

## Exercice 13 : 

```
SELECT
	ID_ARTICLE,
    NOM_ARTICLE,
    VOLUME,
    TITRAGE
FROM 
	article
JOIN TYPE
on article.ID_TYPE = type.ID_TYPE
WHERE type.NOM_TYPE='TRAPPISTE';
```

## Exercice 14 :

```
SELECT
	NOM_MARQUE
FROM 
	MARQUE
JOIN PAYS
on MARQUE.ID_PAYS = PAYS.ID_PAYS
JOIN CONTINENT
on PAYS.ID_CONTINENT = CONTINENT.ID_CONTINENT
WHERE CONTINENT.NOM_CONTINENT='Afrique';
```

## Exercice 15 :

```
SELECT 
	ID_ARTICLE,
	NOM_ARTICLE
FROM 
	ARTICLE
JOIN MARQUE 
ON ARTICLE.ID_MARQUE = MARQUE.ID_MARQUE
JOIN PAYS
ON MARQUE.ID_PAYS = PAYS.ID_PAYS
JOIN CONTINENT
ON PAYS.ID_CONTINENT = CONTINENT.ID_CONTINENT
WHERE CONTINENT.NOM_CONTINENT='Afrique';
```

## Exercice 16 :

```
SELECT
	ANNEE,
	NUMERO_TICKET,
    SUM(article.PRIX_ACHAT)*1.15 as Prix_Vente
FROM 
	VENTES
JOIN 
	ARTICLE
ON ventes.ID_ARTICLE = article.ID_ARTICLE
GROUP BY ANNEE, NUMERO_TICKET
ORDER BY ANNEE ;
```

## Exercice 17 :

```
SELECT
	ANNEE,
    SUM(article.PRIX_ACHAT)*1.15 as Prix_Vente
FROM 
	VENTES
JOIN 
	ARTICLE
ON ventes.ID_ARTICLE = article.ID_ARTICLE
GROUP BY ANNEE
ORDER BY ANNEE ;
```

## Exercice 18 :

```
SELECT
	ventes.ANNEE,
    article.NOM_ARTICLE,
    SUM(QUANTITE)
FROM 
	VENTES
JOIN 
	ARTICLE
ON ventes.ID_ARTICLE = article.ID_ARTICLE
WHERE ventes.ANNEE = 2016
GROUP BY ventes.ANNEE, article.NOM_ARTICLE;
```

Si l'on trie sur l'ID de l'article plutôt que sur son nom, cela donne :

```
SELECT
	ventes.ANNEE,
    article.ID_ARTICLE,
    article.NOM_ARTICLE,
    SUM(ventes.QUANTITE)
FROM 
	VENTES
JOIN 
	ARTICLE
ON ventes.ID_ARTICLE = article.ID_ARTICLE
WHERE ventes.ANNEE = 2016
GROUP BY ANNEE,ventes.ID_ARTICLE;
```

## Exercice 19 :


```
SELECT
    ventes.ANNEE,
    article.ID_ARTICLE,
    article.NOM_ARTICLE,
    SUM(QUANTITE)
FROM 
	VENTES
JOIN 
	ARTICLE
ON ventes.ID_ARTICLE = article.ID_ARTICLE
WHERE ventes.ANNEE BETWEEN 2014 AND 2016
GROUP BY ventes.ANNEE, article.NOM_ARTICLE;
```

## Exercice 20 :

Même principe que pour le 18

```
SELECT
    article.NOM_ARTICLE
FROM 
	VENTES
JOIN 
	ARTICLE
ON ventes.ID_ARTICLE = article.ID_ARTICLE
WHERE ventes.ANNEE = 2014 
GROUP BY article.NOM_ARTICLE
HAVING SUM(QUANTITE) = 0;
```

## Exercice 21 :

```
SELECT distinct
    pays.NOM_PAYS
FROM 
	pays
JOIN 
	marque
ON pays.ID_PAYS = marque.ID_PAYS
join 
	article
on marque.ID_MARQUE = article.ID_MARQUE
join 
	type
on article.ID_TYPE = type.ID_TYPE
WHERE type.NOM_TYPE = 'Trappiste';
```

