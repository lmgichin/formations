drop function if exists formation.db_oid(db_name varchar);

create or replace function formation.db_oid ( db_name varchar) returns integer as $$

declare

	r_oid integer;
begin

	select oid into r_oid from pg_database where datname = db_name;

	return r_oid;
	
end;

$$ language PLPGSQL;


-- *****************************************************************************************


drop function if exists formation.table_oid(table_name varchar);

create or replace function formation.table_oid ( table_name varchar) returns integer as $$

declare

	r_oid integer;
begin

	SELECT relfilenode into r_oid FROM pg_class WHERE relname = table_name;

	return r_oid;
	
end;

$$ language PLPGSQL;


