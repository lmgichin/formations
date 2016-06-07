select query, (state_change - query_start) as duration 
from pg_catalog.pg_stat_activity;


-- index summary
SELECT
    pg_class.relname,
    pg_class.reltuples::int4 AS num_rows,
    COUNT(indexname) AS number_of_indexes,
    CASE WHEN x.is_unique = 1 THEN 'Y' ELSE 'N' END AS UNIQUE,
    SUM(CASE WHEN number_of_columns = 1 THEN 1 ELSE 0 END) AS single_column,
    SUM(CASE WHEN number_of_columns IS NULL THEN 0
             WHEN number_of_columns = 1 THEN 0 
	ELSE 1 END) AS multi_column
FROM pg_namespace 
LEFT OUTER JOIN pg_class ON pg_namespace.oid = pg_class.relnamespace
LEFT OUTER JOIN
	(SELECT indrelid,
		MAX(CAST(indisunique AS INTEGER)) AS is_unique
	 FROM pg_index
	 GROUP BY indrelid) x ON pg_class.oid = x.indrelid
LEFT OUTER JOIN
	( SELECT c.relname AS ctablename, ipg.relname AS indexname, x.indnatts AS number_of_columns 
	  FROM pg_index x
	  JOIN pg_class c ON c.oid = x.indrelid
	  JOIN pg_class ipg ON ipg.oid = x.indexrelid  ) AS foo
     ON pg_class.relname = foo.ctablename
WHERE pg_namespace.nspname='public'
 AND  pg_class.relkind = 'r'
GROUP BY pg_class.relname, pg_class.reltuples, x.is_unique
ORDER BY 2;

-- liste des indexes inutilisés
SELECT 
    relid::regclass AS table, 
    indexrelid::regclass AS index, 
    pg_size_pretty(pg_relation_size(indexrelid::regclass)) AS index_size, 
    idx_tup_read, 
    idx_tup_fetch, 
    idx_scan
FROM 
    pg_stat_user_indexes 
    JOIN pg_index USING (indexrelid) 
WHERE 
    idx_scan = 0 
    AND indisunique IS FALSE

-- liste des indexes dupliqués
SELECT pg_size_pretty(SUM(pg_relation_size(idx))::BIGINT) AS SIZE,
       (array_agg(idx))[1] AS idx1, (array_agg(idx))[2] AS idx2,
       (array_agg(idx))[3] AS idx3, (array_agg(idx))[4] AS idx4
FROM (
	    SELECT indexrelid::regclass AS idx, (indrelid::text ||E'\n'|| indclass::text ||E'\n'|| indkey::text ||E'\n'||
		                                         COALESCE(indexprs::text,'')||E'\n' || COALESCE(indpred::text,'')) AS KEY
	    FROM pg_index) sub
GROUP BY KEY HAVING COUNT(*)>1
ORDER BY SUM(pg_relation_size(idx)) DESC;

-- liste de la place disque des indexes
SELECT
    t.tablename,
    indexname,
    c.reltuples AS num_rows,
    pg_size_pretty(pg_relation_size(quote_ident(t.tablename)::text)) AS table_size,
    pg_size_pretty(pg_relation_size(quote_ident(indexrelname)::text)) AS index_size,
    CASE WHEN indisunique THEN 'Y' ELSE 'N' END AS UNIQUE,
    idx_scan AS number_of_scans,
    idx_tup_read AS tuples_read,
    idx_tup_fetch AS tuples_fetched
FROM pg_tables t
LEFT OUTER JOIN pg_class c ON t.tablename=c.relname
LEFT OUTER JOIN
	( SELECT c.relname AS ctablename, ipg.relname AS indexname, x.indnatts AS number_of_columns, idx_scan, idx_tup_read, idx_tup_fetch, indexrelname, indisunique 
	  FROM pg_index x
          JOIN pg_class c ON c.oid = x.indrelid
	  JOIN pg_class ipg ON ipg.oid = x.indexrelid
	  JOIN pg_stat_all_indexes psai ON x.indexrelid = psai.indexrelid ) AS foo
	ON t.tablename = foo.ctablename
WHERE t.schemaname='public'
ORDER BY 1,2;

-- liste des sessions

SELECT datname as database,
       pid as pid,
       usename as username,
       application_name as application,
       client_addr as client_address,
       query
  FROM pg_stat_activity;

-- kill des sessions d'un user
select pg_terminate_backend(pid) from pg_stat_activity where usename = 'username';

-- liste des sessions d'un user
select usename, pid from pg_stat_activity where usename = 'username';

select datname, xact_commit, xact_rollback 
from pg_stat_database 
order by datname;

select schemaname, relname, seq_scan, idx_scan, n_tup_ins, n_tup_upd, n_tup_del, last_vacuum, last_autovacuum, vacuum_count 
from pg_stat_all_tables 
where schemaname = 'formation' 
order by relname;

-- liste des locks

SELECT   bl.pid                 AS blocked_pid,
         a.usename              AS blocked_user,
         ka.query               AS current_or_recent_statement_in_blocking_process,
         ka.state               AS state_of_blocking_process,
         now() - ka.query_start AS blocking_duration,
         kl.pid                 AS blocking_pid,
         ka.usename             AS blocking_user,
         a.query                AS blocked_statement,
         now() - a.query_start  AS blocked_duration
  FROM  pg_catalog.pg_locks         bl
   JOIN pg_catalog.pg_stat_activity a  ON a.pid = bl.pid
   JOIN pg_catalog.pg_locks         kl ON kl.transactionid = bl.transactionid AND kl.pid != bl.pid
   JOIN pg_catalog.pg_stat_activity ka ON ka.pid = kl.pid
  WHERE NOT bl.GRANTED;

-- liste des tables n'ayant pas de PK
SELECT
    n.nspname AS "Schema",
    c.relname AS "Table Name",
    c.relhaspkey AS "Has PK"
FROM
    pg_catalog.pg_class c
JOIN
    pg_namespace n
ON (
        c.relnamespace = n.oid
    AND n.nspname IN ('public')
    AND c.relkind='r' AND c.relhaspkey = 'f'
)
ORDER BY c.relhaspkey, c.relname
;


--top 10 des tables les plus lues
SELECT relname, idx_tup_fetch + seq_tup_read AS Total
  FROM pg_stat_all_tables
  WHERE idx_tup_fetch + seq_tup_read != 0
  ORDER BY Total desc
  LIMIT 10;


-- nombre de pages et de tuples d'une table
-- valeurs réelles après un VACUUM
SELECT reltuples, relpages FROM pg_class
WHERE relname = 'villes';

-- statistiques sur les tables
-- mises à jour uniquement après un ANALYZE
SELECT starelid, staattnum, stawidth, stanullfrac FROM pg_statistic
WHERE starelid = (SELECT oid FROM pg_class WHERE relname = 'villes');

-- more stats
-- si correlation incohérent, lancer un CLUSTER sur la table (cf MAINTENANCE_WORK_MEM)
SELECT attname, null_frac, avg_width, n_distinct, most_common_vals, most_common_freqs, correlation 
FROM pg_stats where tablename = 'ti';


-- liste des 10 plus grosses tables (place sur disque)
SELECT nspname || '.' || relname AS "relation", pg_size_pretty(pg_relation_size(C.oid)) AS "size"
FROM pg_class C
LEFT JOIN pg_namespace N ON (N.oid = C.relnamespace)
WHERE nspname NOT IN ('pg_catalog', 'information_schema')
ORDER BY pg_relation_size(C.oid) DESC

-- ratio utilisation cache
SELECT 
  sum(heap_blks_read) as heap_read,
  sum(heap_blks_hit)  as heap_hit,
  sum(heap_blks_hit) / (sum(heap_blks_hit) + sum(heap_blks_read)) as ratio
FROM pg_statio_user_tables;

-- % utilisation indexes
SELECT 
  relname, 
  100 * idx_scan / (seq_scan + idx_scan) percent_of_times_index_used, 
  n_live_tup rows_in_table
FROM pg_stat_user_tables
WHERE seq_scan + idx_scan > 0 
ORDER BY n_live_tup DESC; 

-- ratio utilisation indexes
SELECT 
  sum(idx_blks_read) as idx_read,
  sum(idx_blks_hit)  as idx_hit,
  (sum(idx_blks_hit) - sum(idx_blks_read)) / sum(idx_blks_hit) as ratio
FROM pg_statio_user_indexes;


-- activité par processeur
select datname, A.pid, processor, A.state, fullcomm
from pg_stat_activity A, pg_proctab() B
where A.pid = B.pid;
