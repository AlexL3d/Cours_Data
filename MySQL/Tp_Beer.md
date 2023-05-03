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
