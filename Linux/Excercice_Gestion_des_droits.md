# Exercice : Gestion des droits

## Partie 1

### 1.
La commande permettant de lister les fichiers ainsi que les droits affectés est :

```
ls -l
```

### 2.
```
user@debian10:~/Documents <Commande de la question 1.>
total 8
drwxr-xr-- 2 user user 4096 juil. 10 17:56 bidule
-rwxrw---x 1 user profs  0 juil. 10 17:56 machin.sh
-rwxr-x--- 1 bob profs  3 juil. 10 17:57 truc
```

- L'utilisateur est user.
- la machine utilisée est debian10.
- Le répertoire actuel est le Documents de l'utilisateur user.
- Il y a un dossier bidule et deux fichiers machin.sh et truc.
- Le premier tiret indique c'est un fichier, "rwx" indique que le propriétaire peut le lire, le modifier et l'éxecuter, "rw-" indique que le groupe peut lire et modifier le fichier mais pas l'éxecuter et "--x" permet aux autres utilisateurs d'uniquement l'éxecuter.
- pour les droits drwxr-xr--: 754 , pour -rwxrw---x : 761, pour -rwxr-x--- : 750.
  
### 3. 

Création du fichier test_droit dans Documents

```
leduca@Debian:~$ cd Documents
leduca@Debian:~/Documents$ touch test_droit
```

### 4.
Vérification des droits sur le fichier : 
```
leduca@Debian:~/Documents$ ls -l
-rw-r--r-- 1 leduca leduca         0 21 avril 10:29 test_droit
```

## Partie 2



### Forme symbolique :

#### 1.

```
leduca@Debian:~/Documents/droits$ touch s_proprio
leduca@Debian:~/Documents/droits$ chmod u=rwx,g=---,o=--- s_proprio

```

#### 2.

```
leduca@Debian:~/Documents/droits$ touch s_commun
leduca@Debian:~/Documents/droits$ chmod u=rwx,g=rws,o=--- s_commun
```

#### 3.

```
leduca@Debian:~/Documents/droits$ touch s_partiel
leduca@Debian:~/Documents/droits$ chmod u=rwx,g=r--,o=--- s_partiel
```

#### 4.

```
leduca@Debian:~/Documents/droits$ touch s_restreint
leduca@Debian:~/Documents/droits$ chmod u=rwx,g=r--,o=r-- s_restreint
```

### Forme numérique :

#### 1.

```
leduca@Debian:~/Documents/droits$ touch n_proprio
leduca@Debian:~/Documents/droits$ chmod 700 n_proprio 
```

#### 2.

```
leduca@Debian:~/Documents/droits$ touch n_commun
leduca@Debian:~/Documents/droits$ chmod 770 n_commun  
```

#### 3.

```
leduca@Debian:~/Documents/droits$ touch n_partiel
leduca@Debian:~/Documents/droits$ chmod 740 n_partiel 
```

#### 4.

```
leduca@Debian:~/Documents/droits$ touch n_restreint
leduca@Debian:~/Documents/droits$ chmod 744 n_restreint 
```

## Partie 3

### 1.

Une inode Linux est une structure de données contenant les informations du fichier (numéro inode, propriétaire, groupe, autorisations, taille du fichier, date et heure pour chaque action sur le fichier, etc...).

### 2.

Commande pour vérifier l'inode d'un fichier : 
```
ls -i nom_du_fichier
```

### 3. 
Un lien physique pointe directement sur l'espace mémoire du fichier.

### 4.

Un lien symbolique est un pointeur sur le chemin du fichier.

### 5.

```
leduca@Debian:~/Documents/droits$ touch original
leduca@Debian:~/Documents/droits$ ln original physique
```

### 6.

```
leduca@Debian:~/Documents/droits$ ls -lhi original physique
917062 -rw-r--r-- 2 leduca leduca 0 21 avril 11:46 original
917062 -rw-r--r-- 2 leduca leduca 0 21 avril 11:46 physique
```

On a les mêmes inodes et tailles de fichier.

### 7.

```
leduca@Debian:~/Documents/droits$ cat original
Je suis l'original
leduca@Debian:~/Documents/droits$ cat physique
Je suis l'original
```

La modification de l'original entraîne celle du lien physique.

### 8.

```
leduca@Debian:~/Documents/droits$ rm original
leduca@Debian:~/Documents/droits$ cat physique
Je suis l'original
```

Après suppression de l'original, le lien physique a gardé la valeur de l'original avant suppression.

### 9.

```
leduca@Debian:~/Documents/droits$ rm physique
```
### 10.

```
leduca@Debian:~/Documents/droits$ touch original
leduca@Debian:~/Documents/droits$ ln -s original symbolique
```

### 11.

```
leduca@Debian:~/Documents/droits$ ls -lhi original symbolique
916280 -rw-r--r-- 1 leduca leduca 0 21 avril 11:54 original
917046 lrwxrwxrwx 1 leduca leduca 8 21 avril 11:55 symbolique -> original
```

On n'a pas les mêmes numéro d'inodes ni la même taille de fichier.

### 12.

```
leduca@Debian:~/Documents/droits$ cat original
Je suis l'original
leduca@Debian:~/Documents/droits$ cat symbolique 
Je suis l'original
```

La modification de l'original entraîne celle du lien symbolique.

### 13.

````
leduca@Debian:~/Documents/droits$ rm original 
leduca@Debian:~/Documents/droits$ cat symbolique 
cat: symbolique: Aucun fichier ou dossier de ce type
```

La suppression de l'original entraîne celle du lien symbolique.