-- FETCH

/*

FETCH statement was introduced in '08 and works much like LIMIT.  Anatomy of the statement is something like the following:

FETCH <start> { ROW | ROWS }

start - an integer value that must be >= 0.  Default is 0 and if a bigger number than the number of rows in the table is
		passed, then FETCH won't return any records.

*/

-- Simple FETCH
SELECT 
	*
FROM movies
FETCH FIRST 5 ROWS ONLY; -- Get the first 5 records in the table


-- FETCH with ORDER BY
SELECT 
	* 
FROM directors
ORDER BY date_of_birth ASC
FETCH FIRST 5 ROWS ONLY; --Limit the result to the 5 oldest directors


-- FETCH using an OFFSET
SELECT
	*
FROM movies
ORDER BY movie_length DESC
FETCH FIRST 5 ROWS ONLY --Fetches rows 6-10 due to the OFFSET statement (below)
OFFSET 5

