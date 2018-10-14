-- spatialite aha.sdb
.tables

-- sqlite3 aha.db
.load 'libspatialite.so.7'
 SELECT load_extension('libspatialite.so.7');

 .nullvalue NULL
 .headers on
 .mode list
 .help
