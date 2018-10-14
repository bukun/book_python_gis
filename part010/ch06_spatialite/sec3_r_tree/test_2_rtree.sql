/* spatialite new_db.sqlite */

CREATE INDEX idx_county ON new_county2(name);

DROP INDEX idx_county;

SELECT * FROM geometry_columns;

SELECT CreateSpatialIndex('new_county2', 'geom');
SELECT * FROM geometry_columns;
PRAGMA table_info(idx_new_county2_geom);
SELECT * FROM idx_new_county2_geom LIMIT 5;

SELECT name, tbl_name, sql FROM sqlite_master WHERE name LIKE 'gi%';

SELECT count(name) FROM new_county2 WHERE X(centroid(geom)) > 1000000 AND
X(centroid(geom)) < 1500000 AND
Y(centroid(geom)) > 1000000 AND
Y(centroid(geom)) < 5400000;

SELECT count(name) FROM new_county2 WHERE ROWID
IN (SELECT pkid FROM idx_new_county2_geom WHERE
xmin > 1000000 AND xmax < 1500000 AND
ymin > 1000000 AND ymax < 5400000);

EXPLAIN QUERY PLAN
SELECT count(name) FROM new_county2 WHERE ROWID
IN (SELECT pkid FROM idx_new_county2_geom WHERE
xmin > 1000000 AND xmax < 1500000 AND
ymin > 1000000 AND ymax < 5400000);


SELECT DisableSpatialIndex('new_county2', 'geom');
DROP TABLE idx_new_county2_geom;


VACUUM;


