-- JSON

/*
JSON support is native to PostgreSQL.  Supports both serial and binary.

*/

-- Create the table:
CREATE TABLE table_json(
	unique_id SERIAL PRIMARY KEY,
	docs JSON
)

-- Insert some values:
INSERT INTO table_json(docs) VALUES
('[1,2,3,4,5]'), -- Will accept array lik structure
('["a", "b", "c"]'), -- Need quotes around non-numeric characters in an array like object.
('{"key":"value"}')

-- Select values:
SELECT 
	unique_id,
	docs->0 AS first_element, -- For array like objects, this works, will return null for key/value structure
	docs->'key' AS key_value, -- For key/value structure, this works if they key exists, will return null for arrays
	docs->'non_existent_key' AS non_existent_key -- Fails gracefully
FROM table_json 