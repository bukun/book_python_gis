/* spatialite new_db.sqlite */

.nullvalue NULL
.headers on
.mode list
.loadshp xx_counties  new_county utf-8
PRAGMA table_info(new_county);
SELECT count(*), GeometryType(Geometry) FROM new_county    GROUP BY GeometryType(Geometry);
