/* spatialite new_db.sqlite */

.nullvalue NULL
.headers on
.mode list


.loadshp xx_counties new_county2 utf-8 3857 geom

SELECT * FROM spatial_ref_sys WHERE Srid = 3857;

SELECT * FROM geometry_columns;
SELECT * FROM geom_cols_ref_sys;

SELECT * FROM sqlite_master WHERE name = 'geom_cols_ref_sys';

SELECT * FROM sqlite_master WHERE type = 'trigger' AND tbl_name = 'new_county2';

select DiscardGeometryColumn('new_county2', 'geom');

SELECT * FROM geometry_columns;

SELECT * FROM sqlite_master WHERE type = 'trigger' AND tbl_name = 'new_county2';


update new_county2 set geom = SetSrid(geom, 3857);
SELECT RecoverGeometryColumn('new_county2', 'geom',3857, 'MULTIPOLYGON', 2);

SELECT * FROM geometry_columns;
SELECT * FROM sqlite_master WHERE type = 'trigger' AND tbl_name = 'new_county2';
