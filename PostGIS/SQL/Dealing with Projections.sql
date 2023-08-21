


-- Get the SRID for the subway stations dataset
SELECT 
	ST_SRID(geom),
	srtext
FROM nyc_subway_stations
LEFT JOIN spatial_ref_sys ON (SELECT ST_SRID(geom) FROM nyc_subway_stations LIMIT 1) = spatial_ref_sys.srid
LIMIT 1

-- Get the SRID for the homicides dataset
SELECT 
	ST_SRID(geom),
	srtext
FROM nyc_homicides
LEFT JOIN spatial_ref_sys ON (SELECT ST_SRID(geom) FROM nyc_homicides LIMIT 1) = spatial_ref_sys.srid
LIMIT 1


-- Transform the subway points from UTM to WGS 84 so that we can view them as clickable points on the
-- geometry viewer courtesy of leaflet (may have to click to enable the first time)
SELECT ST_Transform(geom, 4326), name FROM nyc_subway_stations


-- Get the SRID for all tables in the public schema
SELECT * FROM  geometry_columns