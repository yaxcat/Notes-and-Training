/*
Investigating ST_Intersect(), which identifies whether or not two elements intersect. 
Can handle heterogenous geometry types
*/
-- Finding points that intersect polygons
-- Define the point layer columns we care about
WITH subway_stations AS (
	SELECT 
		id AS station_id,
		name AS station_name,
		ST_X(geom) AS x,
		ST_Y(geom) AS y,
		geom AS station_geom
	FROM nyc_subway_stations
),
-- Define the polygon layer columns we care about
neighborhoods AS (
	SELECT 
		name AS neigh_name,
		boroname,
		geom AS neigh_geom
	FROM nyc_neighborhoods
),
-- Get just the stations which intersect a neighborhood polygon
station_intsct AS (
	SELECT
		station_id,
		station_name,
		x,
		y,
		ST_Intersects(station_geom, neigh_geom) AS st_intersect_result
	FROM subway_stations INNER JOIN neighborhoods ON ST_Intersects(station_geom, neigh_geom)
	ORDER BY station_id ASC
),
-- Get just the neighborhood polygons which intersect a station point
-- Result table will have dupes because there are multiple subway stations per neighborhood in many cases
neigh_intsct AS (
	SELECT
		neigh_name,
		boroname,
		ST_Intersects(neigh_geom, station_geom) AS st_intersect_result
	FROM neighborhoods INNER JOIN subway_stations ON ST_Intersects(neigh_geom, station_geom)
),

-- Get just the station points which don't intersect a neighborhood polygon
stations_no_intsct AS (
	SELECT
		subway_stations.station_id,
		subway_stations.station_name,
		subway_stations.x,
		subway_stations.y
	FROM subway_stations
	LEFT JOIN station_intsct ON subway_stations.station_id = station_intsct.station_id
	WHERE station_intsct.station_id IS NULL
	ORDER BY subway_stations.station_id
)

SELECT * FROM stations_no_intsct
