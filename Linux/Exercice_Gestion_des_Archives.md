# Exercice : Gestion des archives

## 1.

root@Debian:~# apt update

## 2. 

root@Debian:~# apt upgrade

## 3.

root@Debian:~# /etc/apt/sources.list

## Partie 2.

### 1.

leduca@Debian:~/Documents$ Exercice_Archives
leduca@Debian:~/Documents$ cd Exercice_Archives

### 2.

leduca@Debian:~/Documents/Exercice_Archives$ mkdir DossierA
leduca@Debian:~/Documents/Exercice_Archives$ mkdir DossierB
leduca@Debian:~/Documents/Exercice_Archives$ mkdir DossierC
leduca@Debian:~/Documents/Exercice_Archives$ cd DossierA
leduca@Debian:~/Documents/Exercice_Archives/DossierA$ touch f1_dossierA
leduca@Debian:~/Documents/Exercice_Archives/DossierA$ touch f2_dossierA
leduca@Debian:~/Documents/Exercice_Archives/DossierA$ touch f3_dossierA
leduca@Debian:~/Documents/Exercice_Archives/DossierA$ cd ..
leduca@Debian:~/Documents/Exercice_Archives$ cd DossierB
leduca@Debian:~/Documents/Exercice_Archives/DossierB$ touch f1_dossierB
leduca@Debian:~/Documents/Exercice_Archives/DossierB$ touch f2_dossierB
leduca@Debian:~/Documents/Exercice_Archives/DossierB$ touch f3_dossierB
leduca@Debian:~/Documents/Exercice_Archives/DossierB$ touch f4_dossierB
leduca@Debian:~/Documents/Exercice_Archives/DossierB$ cd ..
leduca@Debian:~/Documents/Exercice_Archives$ cd DossierC
leduca@Debian:~/Documents/Exercice_Archives/DossierC$ touch f1_dossierC
leduca@Debian:~/Documents/Exercice_Archives/DossierC$ touch f2_dossierC

### 3.

leduca@Debian:~/Documents tar -cf tar_archive.tar Exercice_Archives

### 4.

leduca@Debian:~/Documents tar -tf tar_archive.tar

### 5.

leduca@Debian:~/Documents mv Exercice_Archives old_archive

### 6.

leduca@Debian:~/Documents tar -xf tar_archive.tar

### 7. 

ls -l Exercice_Archives

## Partie 3.

### 1.

On affiche la liste les paquets où est contenu le paquet recherché.

### 2.

On affiche les informations du paquet.

### 3.

Tree est une commande pour afficher différemment la liste des dossiers et fichiers d'un répertoire. Comme ls mais avec un affichage plus simple à lire

### 4. 

root@Debian:~# apt install tree

### 5.

root@Debian:~# apt purge tree

### 6.

root@Debian:~# apt clean

## DPKG. 

### 2.

root@Debian:~# cd /home/user/Documents
root@Debian:~# mv deb atom.deb

### 3.

le .deb permet de savoir que c'est un paquet à exécuter.

### 4.

root@Debian:~# dpkg --info atom.deb

### 5.

root@Debian:~# dpkg -i atom.deb
root@Debian:~# apt -f install

### 6.
root@Debian:~# atom







