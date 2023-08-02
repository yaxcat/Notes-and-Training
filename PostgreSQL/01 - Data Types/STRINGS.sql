-- STRING FIELD TYPES

/*

There are three main types of character data:
	1)  CHARACTER(n) or CHAR(n)
		- String type field with a fixed length.  Data for all records in this field will have the same length
		  regardless of the strings input since the system will pad input values with spaces if < the specified length
		- Field length = n
		- Field contents length = n
	2)  CHARACTER VARYING(n) or VARCHAR(n) 
		- String type field with a variable length.  Since there is no constraint on the character size, input strings
		  will have whatever their input length is up to the maximum field length
		- Field length  = n
		- Field contents length <= n
	3)  TEXT or VARCHAR
		- String type field that is as long as you want.  There is no limit or maximum field length
		- Field length = None
		- Field contents length = YOLO
		- Probably about 1 GB max size
		- Similar but not identical to TEXT type in MySQL.  Not part of standard SQL.
*/

CREATE TABLE string_fields (
	unique_id SERIAL PRIMARY KEY,
	my_char CHAR(10) NOT NULL, --Fixed length
	my_varchar_lim VARCHAR(25) NOT NULL, --Fixed max length
	my_varchar_no_lim VARCHAR NOT NULL, --Unlimited length
	my_text TEXT NOT NULL --Unlimited length
);

INSERT INTO string_fields (
	my_char, 
	my_varchar_lim, 
	my_varchar_no_lim, 
	my_text
	)
VALUES
	('A', 'A', 'A', 'A'),
	('This is a ', -- System won't auto truncate a value, will throw
	 'This is a long, long stri', -- System won't auto truncate a value, will throw
	 'This is a long, long string.  Lets see what happens',
	 'This is a long, long string.  Lets see what happens'
	)
	
SELECT 
	my_char,
	LENGTH(my_char) AS my_char_length, --Length function will not include the padding spaces
	my_varchar_lim,
	LENGTH(my_varchar_lim) AS my_varchar_lim_length,
	my_varchar_no_lim,
	LENGTH(my_varchar_no_lim) AS my_varchar_no_lim_length,
	my_text,
	LENGTH(my_text) AS my_text_length
FROM string_fields
