-- script de creation initial de la base

-- on nettoie tout d'abord...

drop tablespace if exists tb_data;
drop tablespace if exists tb_indexes;
drop database if exists db_formation;

-- creation des tablespaces de donnees et d'indexes

create tablespace tb_data location '/data/tables';
create tablespace tb_indexes location '/data/indexes';

-- creation de la base de donnees 

create database db_formation WITH ENCODING = 'UTF-8' TEMPLATE = template0;

