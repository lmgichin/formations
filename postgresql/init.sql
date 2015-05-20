-- nettoyage

drop schema if exists formation cascade;

-- creation du schema

create schema formation;

-- creation des sequences

create sequence formation.sq_user;
create sequence formation.sq_author;
create sequence formation.sq_books;
create sequence formation.sq_emprunts;

-- creation des tables

create table formation.users (
		id integer default nextval('formation.sq_user') constraint pk_users primary key using index tablespace tb_indexes,
	    surname varchar(20) not null check (surname <> ''),
	    name varchar(50) not null check (name <> ''),
		description text
		)
		tablespace tb_data;

create table formation.author (
		id integer default nextval('formation.sq_author') constraint pk_author primary key using index tablespace tb_indexes,
		surname varchar(15) not null check (surname <> ''),
	    name varchar(50) not null check (name <> ''),
	    description text
		)
		tablespace tb_data;

create table formation.books ( 
		id integer default nextval('formation.sq_books') constraint pk_books primary key using index tablespace tb_indexes,
	    title varchar(75) not null check (title <> ''),
        author integer constraint fk_author references formation.author(id),
	    description text,
        available bool default true,
        CONSTRAINT uq_title UNIQUE(title,author) using index tablespace tb_indexes
		)
		tablespace tb_data;


create table formation.emprunts (
		id integer default nextval('formation.sq_emprunts') constraint pk_emprunts primary key using index tablespace tb_indexes,
		date timestamp,
		emprunteur integer constraint fk_user references formation.users(id),
		remarques text
		)
		tablespace tb_data;

-- population

copy formation.author(surname,name) from '/tmp/author.data' with CSV delimiter ',' quote '"';
copy formation.books(title,author) from '/tmp/books.data' with CSV delimiter ',' quote '"';
copy formation.users(surname,name) from '/tmp/users.data' with CSV delimiter ',' quote '"';
