-- Concatenate functions

/*

	Concatenation can be accomplished 3 ways:
	
	1) Baked - use the || operator
	2) Fried - Use CONCAT()
	3) Steamed - Use CONCAT_WS()
	
	CONCAT_WS is advantageous if concatenating data from multiple columns since you specify the separator/delimiter 
	up front, once.

	Column type does not matter with concatenation.  String, integer and date types can be thrown together without any
	type conversion.
*/

 

SELECT * FROM actors


-- Pipe operator
SELECT 
	actor_id,
	actor_id || ' ' || first_name || ' ' || last_name AS full_name
FROM 
	actors
	
	
--CONCAT()
SELECT 
	actor_id,
	CONCAT(actor_id, ' ', first_name, ' ', last_name) AS full_name
FROM
	actors
	

--CONCAT_WS()
SELECT
	actor_id,
	CONCAT_WS(', ', actor_id, first_name, last_name, gender, date_of_birth) AS with_seperator
FROM
	actors