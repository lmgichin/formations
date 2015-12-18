drop table if exists employes;

create table employes(
		nom character varying,
	    dep character varying,
        salaire integer);

insert into employes values ('John', 'compta', 32000);
insert into employes values ('Jack', 'compta', 32000);
insert into employes values ('Bob', 'compta', 43000);
insert into employes values ('Alicia', 'accueil', 27000);
insert into employes values ('Béatrice', 'accueil', 27000);
insert into employes values ('Lydia', 'accueil', 29500);
insert into employes values ('Oscar', 'commercial', 59900);

-- requêtes fenêtrées
    select nom, dep, salaire, avg(salaire) OVER (PARTITION by dep ) from employes;
--    
    select nom, dep, salaire, rank() OVER (PARTITION by dep order by salaire desc ) from employes;
