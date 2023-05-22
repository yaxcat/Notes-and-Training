Break stuff
/*
HSTORE 

The hstore data type stores information in key-value pairs.  It only supports strings and requres an extension to run.

*/

CREATE EXTENSION IF NOT EXISTS hstore;


CREATE TABLE hstore_playground(
	unique_id UUID DEFAULT uuid_generate_v1() PRIMARY KEY,
	title VARCHAR(100) NOT NULL,
	book_info HSTORE
);

INSERT INTO hstore_playground (title, book_info) VALUES
	-- First record.  Note how the numbers have to wrapped in quotes since only strings are supported
	(
		'FIRST BOOK',
		'
			"publisher" => "First Publisher", 
			"hard_copy_cost" => "10.00",
			"digital_cost" => "5.00"
		'
		),
	-- Second record
	(
	 'SECOND BOOK',
		'
			"publisher" => "Second Publisher",
			"hard_copy_cost" => "99.99",
			"digital_cost" => "9.99"
		'
		)

-- Select all records
SELECT * FROM hstore_playground

-- Select all records and only the publisher object from book info
SELECT 
	title,
	book_info->'publisher' AS publisher,
	book_info->'hard_copy_cost' AS hard_copy_cost,
	book_info->'digital_cost' AS digital_cost
FROM hstore_playground

