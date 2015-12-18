drop table if exists mytable;
create table mytable(id integer);
insert into mytable(id) select x from generate_series(1,10000000) as x;

set log_temp_files to 0;

set work_mem to '1MB';
select * from mytable order by id;
