-- BETWEEN

/*
	BETWEEN is an operator which checks a value against a range of values.  If the value being checking is >= the high
	value or <= the high value, the operator returns TRUE, otherwise FALSE 
*/


--Select all actors born between 1991 & 1995
SELECT * FROM actors
WHERE date_of_birth BETWEEN '1991-01-01' AND '1995-12-31'
ORDER BY date_of birth

--Extract all the records that are not between the range
SELECT * FROM directors
WHERE director_id NOT BETWEEN 11 AND 29