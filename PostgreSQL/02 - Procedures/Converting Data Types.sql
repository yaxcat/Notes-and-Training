-- DATA CONVERSION

/*

	There are two types of data conversion:
		1)  Implicit - Data conversion is done automatically
		2) 	Explicit - Data conversion is achieved via function call (i.e. CAST or ::)

	You can use CAST(<your_target_expression> AS <your_target_data_type>) to convert data as well.
		1)	<your_target_expression> - Can be a constant value, table column or expression (3+6, for example)
		2)	<your_target_data_type>	 - Boolean, character, numeric, array, JSON, UUID, hstore, time/date, special type

	You can also use <your_target_expresssion>::<your_target_data_type> to convert data types.
	
	The CAST function and :: operator are functionally equivalent.  While CAST has the advantage of following standard
	SQL syntax, and therefore being more portable, :: is specific to PostgreSQL and will break in other database systems.
	There are no significant performance differences between the two and choice of which to use comes down to personal
	preference.

*/


-- Implict conversion
SELECT
	*
FROM movies
WHERE movie_id = '1' -- Even though the movie_id column is integer, this works, because Postgres performs implicit conversion


--Explicit conversion
SELECT
	*
FROM movies
WHERE movie_id = INTEGER '1' -- This works since we're explictly converting from string to int


--CAST function
SELECT 
	CAST('10' AS INTEGER) AS cast_int, -- Will work since the data is clean
	'10'::INTEGER AS colon_int
	
SELECT
	CAST('10N' AS INTEGER) AS cast_int, --Won't work since we've got non-numeric characters
		'10n'::INTEGER AS colon_int


--TO_CHAR(<your_data>, <your_format>)
/*
	TO_CHAR can be used to explicitly convert data to TEXT format.  Its advantage over the CAST function and :: is that it
	provides a ton of ways to format your data.
*/
SELECT TO_CHAR(
	100879, -- Integer value we're converting
	'9,99999' -- Format we want it in
	)

SELECT
	release_date,
	TO_CHAR(release_date, 'DD-MM-YYYY') AS date_1,
	TO_CHAR(release_date, 'mm-Dy-YYYY') AS date_2
FROM movies

SELECT 
	movie_id,
	revenues_domestic,
	TO_CHAR(revenues_domestic, '$99999D99') -- Slap a dollar sign on the beginning and leave space for two decimals
FROM movies_revenues


--TO_NUMBER(<your_data>, <your_format>)
/*
	TO_NUMBER is much like TO_CHAR, but for numbers.  Provides many formatting options.
*/

SELECT TO_NUMBER(
	'1420.89',
	'9999.9' -- Result is not rounded, last digit is just dropped.
	)
	
SELECT TO_NUMBER(
	'$1,420.64',
	'L9G999' -- Strips the dollar sign, thousands separator, and decimals
	)

/*
	TO_DATE() and TO_TIMESTAMP() function similarly to above.  Not providing examples, but they do provide a ton of
	conversion parameters.
*/