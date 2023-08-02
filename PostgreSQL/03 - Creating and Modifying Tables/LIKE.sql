-- LIKE

/*

	1) LIKE and ILIKE are logical pattern matching operators.
	2) Returns TRUE or FALSE
	3) LIKE is case sensitive
	4) ILIKE is not case sensitive
	5) Search strings using two special characters:
		
		%	matches any sequence of zero or more characters
		_	matches a single character
	
	6) Costly to run on large databases
*/

-- %
SELECT 'hello' LIKE 'hello'; --Returns true

SELECT 'hello' LIKE 'h%'; --Returns true

SELECT 'hello' LIKE '%e%'; --Returns true

SELECT 'hello' LIKE '%Z%'; --Returns false

SELECT 'hello' LIKE '%ll'; --Returns false

-- _
SELECT 'hello' LIKE '_ello'; --Returns true

SELECT 'hello' LIKE '__ll_'; --Returns true

SELECT 'hello' LIKE '____z'; --Returns false

-- % and _
SELECT 'hello' LIKE '%ll_'; --Returns true
