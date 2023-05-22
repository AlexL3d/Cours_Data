insert into auto.client set nom='Dupont', prenom='Jean', adresse='18 rue de la mer', dateNaissance='1980-02-03';
insert into auto.client set nom='Durant', prenom='Henry', adresse='25 rue de la mer', dateNaissance='1975-01-09';
insert into auto.client set nom='Jhons', prenom='Indiana', adresse='1 boulevard Oxford', dateNaissance='1965-12-03';
insert into auto.client set nom='Skywalker', prenom='Luke', adresse='1 route l\'étoile', dateNaissance='2023-07-07';

insert into auto.cd_rom set editeur='Legrand';
insert into auto.cd_rom set editeur='Lafarge';
insert into auto.cd_rom set editeur='Le vent du large';

insert into auto.question set intitule='Doubler velo dans un virage', reponse='non', niveauDifficulte='1', theme='Doubler';
insert into auto.question set intitule='Se rabatre après doubler', reponse='oui', niveauDifficulte='1', theme='Doubler';
insert into auto.question set intitule='Metter sa ceinture', reponse='oui', niveauDifficulte='0', theme='Base';
insert into auto.question set intitule='Doubler velo dans un virage 2', reponse='non', niveauDifficulte='1', theme='Doubler';
insert into auto.question set intitule='Se rabatre après doubler 2', reponse='oui', niveauDifficulte='1', theme='Doubler';
insert into auto.question set intitule='Metter sa ceinture 2', reponse='oui', niveauDifficulte='0', theme='Base';
insert into auto.question set intitule='Doubler velo dans un virage 3', reponse='non', niveauDifficulte='1', theme='Doubler';
insert into auto.question set intitule='Se rabatre après doubler 4', reponse='oui', niveauDifficulte='1', theme='Doubler';
insert into auto.question set intitule='Metter sa ceinture 5', reponse='oui', niveauDifficulte='0', theme='Base';

insert into auto.serie set cd_rom_cdromid=1;
insert into auto.serie set cd_rom_cdromid=2;
insert into auto.serie set cd_rom_cdromid=1;

insert into auto.serie_has_question set serie_serieId=1, question_questionId=1;
insert into auto.serie_has_question set serie_serieId=1, question_questionId=2;
insert into auto.serie_has_question set serie_serieId=1, question_questionId=3;
insert into auto.serie_has_question set serie_serieId=2, question_questionId=1;
insert into auto.serie_has_question set serie_serieId=2, question_questionId=2;
insert into auto.serie_has_question set serie_serieId=2, question_questionId=3;

insert into auto.seance_code set date='2001-01-01', heure='10:00:00', nombreFautes=3, lieu='Somewhere', estExamen=false, serie_serieId=1, client_clientid=1;
insert into auto.seance_code set date='2001-01-02', heure='10:00:00', nombreFautes=4, lieu='Somewhere', estExamen=false, serie_serieId=1, client_clientid=1;
insert into auto.seance_code set date='2001-01-03', heure='10:00:00', nombreFautes=1, lieu='Somewhere', estExamen=false, serie_serieId=1, client_clientid=1;
insert into auto.seance_code set date='2001-01-04', heure='10:00:00', nombreFautes=3, lieu='Somewhere', estExamen=true, serie_serieId=2, client_clientid=1;
insert into auto.seance_code set date='2001-01-01', heure='10:00:00', nombreFautes=3, lieu='Somewhere', estExamen=false, serie_serieId=1, client_clientid=2;
insert into auto.seance_code set date='2001-01-02', heure='10:00:00', nombreFautes=5, lieu='Somewhere', estExamen=false, serie_serieId=1, client_clientid=2;
insert into auto.seance_code set date='2001-01-03', heure='10:00:00', nombreFautes=2, lieu='Somewhere', estExamen=false, serie_serieId=1, client_clientid=2;

