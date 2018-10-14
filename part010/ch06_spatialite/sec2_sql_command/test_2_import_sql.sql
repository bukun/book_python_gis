-- spatialite spalite.db

.headers on
select * from county_popu limit 5;
SELECT name AS County, popu as Population FROM county_popu ORDER BY name LIMIT 5;
select name, popu from county_popu WHERE   popu > 500 order by popu DESC;
SELECT COUNT(*) AS '# 城镇',  MIN(popu) AS '最少', MAX(popu) AS '最多', SUM(popu) AS '人口总数', SUM(popu) / COUNT(*) AS '城镇平均人口' FROM county_popu;

 SELECT (10 - 11) * 2 AS number, ABS((10 - 11) * 2) AS absolution ;
 SELECT name, popu, HEX(GEOMETRY) FROM county_popu WHERE popu > 500 ORDER BY popu DESC;
.quit
