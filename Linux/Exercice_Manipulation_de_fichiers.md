# Exercice Manipulation de fichiers

## 1 & 2.

leduca@Debian:~$ cd /home/leduca/Documents

## 3.

leduca@Debian:~/Documents$ mkdir IT Communication RH Marketing
leduca@Debian:~/Documents$ ls
Communication  IT  known_hosts  Marketing  RH

## 4.

leduca@Debian:~/Documents$ cd RH
leduca@Debian:~/Documents/RH$ mkdir Projet
leduca@Debian:~/Documents/RH$ ls
Projet

## 5.

leduca@Debian:~/Documents/RH$ cd Projet
leduca@Debian:~/Documents/RH/Projet$ touch Projet_IT Projet_Marketing Projet_Communication
leduca@Debian:~/Documents/RH/Projet$ ls
Projet_Communication  Projet_IT  Projet_Marketing
leduca@Debian:~/Documents/RH/Projet$ nano Projet_IT
leduca@Debian:~/Documents/RH/Projet$ nano Projet_Marketing
leduca@Debian:~/Documents/RH/Projet$ nano Projet_Communication
leduca@Debian:~/Documents/RH/Projet$ cat Projet_IT
Ce fichier est composé du projet IT
leduca@Debian:~/Documents/RH/Projet$ cat Projet_Marketing
Ce fichier est composé du projet Marketing
leduca@Debian:~/Documents/RH/Projet$ cat Projet_Communication
Ce fichier est composé du fichier Communication

## 6.

leduca@Debian:~/Documents/RH/Projet$ cd ../..
leduca@Debian:~/Documents$ cp -r RH copy_RH
leduca@Debian:~/Documents$ ls
Communication  copy_RH  IT  known_hosts  Marketing  RH

## 7.

leduca@Debian:~/Documents/RH$ cp -r Projet /home/leduca/Documents/Marketing

## 8. 

leduca@Debian:~/Documents/RH$ cd ../Marketing
leduca@Debian:~/Documents/Marketing$ cd Projet
leduca@Debian:~/Documents/Marketing/Projet$ mv Projet_IT m_Projet_IT
leduca@Debian:~/Documents/Marketing/Projet$ mv Projet_Communication m_Projet_Communication
leduca@Debian:~/Documents/Marketing/Projet$ mv Projet_Marketing m_Projet_Marketing
leduca@Debian:~/Documents/Marketing/Projet$ ls
m_Projet_Communication  m_Projet_IT  m_Projet_Marketing

## 9.

leduca@Debian:~/Documents/Marketing/Projet$ cd ..
leduca@Debian:~/Documents/Marketing$ mkdir Backup
leduca@Debian:~/Documents/Marketing$ ls
Backup  Projet

## 10.

leduca@Debian:~/Documents$ mv /home/leduca/Documents/Marketing/Projet /home/leduca/Documents/Marketing/Backup
leduca@Debian:~/Documents$ cd Marketing/Backup
leduca@Debian:~/Documents/Marketing/Backup$ ls
Projet
leduca@Debian:~/Documents/Marketing/Backup$ cd Projet
leduca@Debian:~/Documents/Marketing/Backup/Projet$ ls
m_Projet_Communication  m_Projet_IT  m_Projet_Marketing

## 11.

leduca@Debian:~/Documents/Marketing/Backup$ cd ../Projet

## 12.

leduca@Debian:~/Documents/Marketing/Backup/Projet$ cd ../../../
leduca@Debian:~/Documents$ rm -r Marketing 
leduca@Debian:~/Documents$ ls
Communication  copy_RH  IT  known_hosts  RH

## 13.

leduca@Debian:~/Documents$ cd /
leduca@Debian:/$ pwd
/