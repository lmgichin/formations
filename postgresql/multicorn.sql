create extension multicorn;

create server csv_srv foreign data wrapper multicorn
	options (
		wrapper 'multicorn.csvfdw.CsvFdw'
	);

create foreign table formation.ext_pers ( surname character varying, name character varying) 
	server csv_srv 
	options (
		filename '/tmp/users.csv',
		skip_header '1',
		delimiter ',',
		quotechar '"'
	); 
