SELECT
 c.relname, count(*) AS buffers,usagecount
FROM pg_class c, pg_buffercache b, pg_database d
where b.relfilenode = c.relfilenode
 and (b.reldatabase = d.oid AND d.datname = current_database())
GROUP BY c.relname,usagecount
ORDER BY c.relname,usagecount;















SELECT
 c.relname,
 pg_size_pretty(count(*) * 8192) as buffered,
 round(100.0 * count(*) /
 (SELECT setting FROM pg_settings WHERE name='shared_buffers')::integer,1)
 AS buffers_percent,
 round(100.0 * count(*) * 8192 / pg_table_size(c.oid),1)
 AS percent_of_relation
FROM pg_class c
 INNER JOIN pg_buffercache b
 ON b.relfilenode = c.relfilenode
 INNER JOIN pg_database d
 ON (b.reldatabase = d.oid AND d.datname = current_database())
GROUP BY c.oid,c.relname
ORDER BY 3 DESC
LIMIT 20;
