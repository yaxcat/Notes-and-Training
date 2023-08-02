/* DATE and TIME

Date/time fields can be of several types:
	1) Date	- stores date only
	2) Time - stores time only
	3) Timestamp - stores both date and time
	4) Timestamptz - stores date, time zone and time
	5) Interval - stores the difference between two dates/times

Useful keywords:
	CURRENT_TIME - returns a time and time zone object reflecting the time of day at the server's location
	LOCAL TIME - returns a timestamp object reflecting local time (no time zone)
*/

CREATE TABLE date_time_playground(
	unique_id SERIAL PRIMARY KEY,
	emp_name VARCHAR(100) NOT NULL,
	hire_date DATE NOT NULL,
	system_add_date DATE DEFAULT CURRENT_DATE
);

-- Postgres will automatically add the current date to the system add field
INSERT INTO date_time_playground(emp_name, hire_date) 
VALUES ('Joe Sample', '2020-03-16')
-- We can add our own date to the system add field if we want, overriding postgres
INSERT INTO date_time_playground(emp_name, hire_date, system_add_date) 
VALUES ('Sampson Jike', '2020-04-11', '1900-01-01')
-- This won't work, it violates the not null constraint, so if we ant it work, we must specify a hire date
INSERT INTO date_time_playground (emp_name) 
VALUES ('Lydia Squol')


SELECT * FROM date_time_playground

SELECT CURRENT_TIME, LOCALTIME

/*
ARITHMETIC
	Use an INTERVAL when performing date/time math operations.
	An INTERVAL has two properties:
		1) n - number representing a quantity
		2) type - unit of time (second, minute, hour, day, month, year, etc.)
	* and / operators throw since they don't really make sense in this context
*/

SELECT 
	CURRENT_TIME AS current_time,
	CURRENT_TIME - INTERVAL '2 hours' AS time_subtraction,
	CURRENT_TIME + INTERVAL '2 hours' AS time_addition,
	CURRENT_TIME - INTERVAL '2 years' AS years_subtraction_time, -- Does nothing since this is just time
	CURRENT_TIME + INTERVAL '2 years' AS years_addition_time, -- Does nothing since this is just time
	CURRENT_DATE - INTERVAL '2 years' AS years_subtraction_date,
	CURRENT_DATE + INTERVAL '2 years' AS years_addition_date
	
	
	
	