This first line is to break stuff if I run without selecting

/*
When typing the column as NUMERIC, the 10 indicates the maximum number of digits, while the 2
represents the number of decimals. So something like 1234.56 would work, but 1111123456.21
would not.

Floating point columns allow the decimal point to 'float' depending on the size of the number, so unlike numeric
column types where the the precision and scale are fixed, both are flexible in a float

Two types of float:
	1) Real	  - allows precision out to 6 decimal places
	2) Double - allows precision out to 15 decimal places
*/

CREATE TABLE movies_revenues (
	revenue_id SERIAL PRIMARY KEY,
	movie_id INT REFERENCES movies (movie_id),
	revenues_domestic NUMERIC (10, 2),
	revenues_international NUMERIC(10, 2)
);

SELECT * FROM movies_revenues




-------------------------------------------------------------------------------------------------------
DROP TABLE numeric_playground

CREATE TABLE numeric_playground (
	unique_id SERIAL PRIMARY KEY,
	integer_field BIGINT,
	one_decimal_a NUMERIC(6, 1), -- space for 5 whole numbers and 1 decimal
	three_decimals_a NUMERIC(6, 3), -- space for 3 whole numbers and 3 decimals
	one_decimal_b NUMERIC(10, 1),  -- space for 9 whole numbers and 1 decimal
	three_decimals_b NUMERIC(10, 3), -- space for 7 whole numbers and 3 decimals
	col_real REAL -- 6 decimal places
);


INSERT INTO numeric_playground (integer_field) VALUES (5672.594)
INSERT INTO numeric_playground (one_decimal_a) VALUES (55672.594) -- Will work since postgre will round for us
INSERT INTO numeric_playground (one_decimal_a) VALUES (555672.5) -- Will fail since we exceed the number of allowed whole numbers (6)
INSERT INTO numeric_playground (one_decimal_a) VALUES (5672.594)
INSERT INTO numeric_playground (three_decimals_a) VALUES (5672.594) -- This one will fail since 5672 >= 999
INSERT INTO numeric_playground (three_decimals_a) VALUES (5672.59) -- This one will also fail since it still has 4 whole numbers but the column only has space to hold 3
INSERT INTO numeric_playground (three_decimals_a) VALUES (672.594) -- This one will work since the scale is <= 999
INSERT INTO numeric_playground (one_decimal_b) VALUES (5672.594)
INSERT INTO numeric_playground (three_decimals_b) VALUES (5672.594)
INSERT INTO numeric_playground (col_real) VALUES (8179127345631)
INSERT INTO numeric_playground (col_real) VALUES (8179127345.631)
INSERT INTO numeric_playground (col_real) VALUES (8179127.345631)
INSERT INTO numeric_playground (col_real) VALUES (8179.127345631)
INSERT INTO numeric_playground (col_real) VALUES (8.179127345631)
INSERT INTO numeric_playground (col_real) VALUES (0.8179127345631)


SELECT * FROM numeric_playground
