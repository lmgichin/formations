drop table if exists formation.capitales;
drop table if exists formation.villes;

drop domain if exists cpostal;

create domain cpostal as text
	check ( VALUE ~ '^\d{5}$' ) ;

CREATE TABLE formation.villes (
    nom             text,
    population      float,
    code			cpostal,
    altitude        int     -- (en pied)
) WITH OIDS;

CREATE TABLE formation.capitales (
    etat           char(2)
) INHERITS (formation.villes) WITH OIDS;


create unique index ix_ville on formation.villes(nom);
create unique index ix_villecap on formation.capitales(nom);

insert into formation.villes (nom,population,code, altitude) values ('Evry', 16750, '91000', 700 ) ;
insert into formation.villes (nom,population,code, altitude) values ('Poissy', 36420, '95634', 1200 ) ;
insert into formation.villes (nom,population,code, altitude) values ('Paris', 32938376420, '75000', 200 ) ;
insert into formation.capitales (nom,population,code, altitude,etat)values ('Paris', 12749, '75000', 200, 'FR' ) ;

-- query : select nom, population, altitude, relname from formation.villes v, pg_catalog.pg_class p where v.tableoid = p.oid;
--         select nom, population, altitude from only formation.villes;
