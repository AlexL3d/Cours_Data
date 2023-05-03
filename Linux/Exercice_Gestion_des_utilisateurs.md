  # Exercice : Gestion des utilisateurs
  
  ## Partie 1

  ### 1.
  178  groupadd formateur
  180  getent group
  183  groupadd etudiant 
  184  groupadd administration
  185  getent group

  ### 2.
  186  adduser u1
  187  adduser u2
  188  adduser u3
  189  adduser u4
  190  adduser u5

  ### 3.

  201  usermod -a -G formateur u1
  202  usermod -a -G formateur u2
  203  getent formateur
  204  getent group formateur

  ### 4.

  205  usermod -a -G etudiant u3
  
  ### 5.
  207  usermod -a -G administration u4 
  208  usermod -a -G administration u5

  ### 6.
  getent group formateur
  getent group etudiant
  getent group admninistration


  ### 8.
  210  usermod --shell /bin/bash u1
  211  usermod --shell /bin/bash u2
  212  usermod --shell /bin/bash u3
  213  usermod --shell /bin/bash u4
  214  usermod --shell /bin/bash u5

  ### 9.
       cd /home/u2
       whoami
  215  touch test 

  ### 10.
  216  chgrp root test
  217  ls -l test

  ### 11.
  218  chown root:root test
  219  ls -l test  

  ### 12.
  220  cat /etc/passwd
  221  usermod -aG sudo u1

  ### 13.
  227  userdel -r u1
  228  userdel -r u2
  229  userdel -r u3
  230  userdel -r u4
  231  userdel -r u5

  ### 14.
  222  groupdel formateur
  223  groupdel etudiant
  224  groupdel administration

  ## Partie 2

  ### 1.

  305  head -2 /etc/group > /home/leduca/Documents/group_dep
  306  echo "$(wc -l < /etc/group) lignes dans /etc/group" >> /home/leduca/Documents/group_dep

  ### 2.

   308  head -2 /etc/passwd > /home/leduca/Documents/passwd_dep
  311  echo "$(wc -l < /etc/passwd) lignes dans /etc/passwd" >> /home/leduca/Documents/passwd_dep

  ### 3.

  312  head -2 /etc/shadow > /home/leduca/Documents/shadow_dep
  313  echo "$(wc -l < /etc/shadow) lignes dans /etc/shadow" >> /home/leduca/Documents/shadow_dep