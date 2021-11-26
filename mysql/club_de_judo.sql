create database clubjudo;
use clubjudo;
create table couleur_ceinture (
id_couleur_ceinture int primary key auto_increment,
couleur varchar(20) not null
);

create table adherent (
id_adherent int primary key auto_increment,
nom varchar(50) not null,
prenom varchar(50) not null,
date_naissance date,
sexe varchar(5),
id_couleur_ceinture int not null,
foreign key (id_couleur_ceinture) references couleur_ceinture (id_couleur_ceinture)
);

create table competition (
id_competition int primary key auto_increment,
nom_competition varchar(50) not null,
date_debut date,
date_fin date
);

create table participer (
id_competition int,
id_adherent int,
primary key (id_competition, id_adherent),
foreign key (id_competition) references competition (id_competition),
foreign key (id_adherent) references adherent (id_adherent)
);