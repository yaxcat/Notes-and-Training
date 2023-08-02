--ORDER BY using column alias names
----------------------------------------------------------------------------------------------------------------------
SELECT 
	first_name AS "First Name",
	last_name AS surname
FROM actors
ORDER BY
	"First Name", --Default ordering is ascending (ASC) if nothing is specified
	surname DESC
; -- Note that we cannot use those same aliases in the WHERE clause.  It will break, just like in Presto.

--ORDER BY using an expression/function
----------------------------------------------------------------------------------------------------------------------
SELECT 
	first_name,
	last_name,
	LENGTH(first_name) AS len --We can call the legnth function here to get the number of characters of the first name, then use the result
FROM actors
ORDER BY len ASC

--ORDER BY using column index numbers instead of names.  Indecises start at 1 rather than 0.
----------------------------------------------------------------------------------------------------------------------
SELECT
	first_name,		--1
	last_name, 		--2
	date_of_birth	--3
FROM actors
ORDER BY
	1 ASC NULLS FIRST, -- Bumps the nulls to the front of the list, default is to put them at the end.
	3 DESC
