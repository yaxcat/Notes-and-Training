-- Aliasing 

/* 

If we want to create case-aware column name, use double quotes

*/

SELECT
	first_name AS "First Name",
	last_name AS "Last Name",
	age AS "Age"
FROM upsert_functionality