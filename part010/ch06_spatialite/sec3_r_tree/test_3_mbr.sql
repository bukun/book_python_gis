/* spatialite new_db.sqlite */


SELECT CreateMbrCache('new_county', 'Geometry');

SELECT * FROM geometry_columns;


PRAGMA table_info(cache_new_county_Geometry);

SELECT * FROM cache_new_county_Geometry LIMIT 5;

SELECT name, tbl_name, sql FROM sqlite_master  WHERE name LIKE 'gc%';

SELECT name FROM new_county
     WHERE MbrWithin(Geometry, BuildMbr(0, 0, 734000,
    4850000));

SELECT name FROM new_county WHERE ROWID IN
     (SELECT rowid FROM cache_new_county_Geometry WHERE
     mbr = FilterMbrWithin(0, 0, 734000, 4850000));
