drop extension if exists multicorn cascade;

create extension multicorn;

create server csv_srv foreign data wrapper multicorn
	options (
		wrapper 'multicorn.csvfdw.CsvFdw'
	);

create server xml_srv foreign data wrapper multicorn
	options (
		wrapper 'multicorn.xmlfdw.XMLFdw'
	);

create foreign table formation.ext_pers ( surname character varying, name character varying) 
	server csv_srv 
	options (
		filename '/tmp/users.csv',
		skip_header '1',
		delimiter ',',
		quotechar '"'
	); 

create foreign table formation.ext_pers_xml ( surname character varying, name character varying) 
	server xml_srv 
	options (
		filename '/tmp/users.xml',
		elem_tag 'person'
	); 
