/*
Investigating ST_Disjoint(), which identifies features that do not intersect. 
Can handle heterogenous geometry types.

CAUTION - ST_Disjoint(n, m), compares every feature (record) to every other feature
so the table returned will have n*m records and won't be what you want if you're just
trying to find features which do not intersect one another.  If this is your use case
use ST_Intersect()
*/

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
-- The result may be a bit counter-intuitive. ST_Disjoint will return
-- 1 record which evaluates to false and whatever the number of polygons is minus 1
-- to true for every point since each point is compared to every polygon record in the
-- table
station_disjoint AS (
	SELECT
		station_id,
		station_name,
		x,
		y,
		ST_Disjoint(station_geom, neigh_geom) AS st_disjoint_result
	FROM subway_stations, neighborhoods
	ORDER BY station_id, st_disjoint_result ASC
)

SELECT * FROM station_disjoint