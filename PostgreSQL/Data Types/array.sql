/* ARRAYS

	For every data type, there is an array.  For example:
		INTEGER -> INTEGER[]
		CHAR -> CHAR[]

*/

--Create a table with an array in it:
CREATE TABLE table_array(
	uniqe_id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
	person_name VARCHAR(100),
	array_field VARCHAR[]
);

--Insert some values
INSERT INTO table_array(person_name, array_field) VALUES
('Joe', ARRAY['A']),
('Jane', ARRAY['B', 'C', 'D']),
('Jim', ARRAY['E', 'F'])

--Query the array objects:
SELECT person_name, array_field FROM table_array -- Select everything
SELECT person_name, array_field[0] FROM table_array -- This returns null since indexing starts at 1 in postgres. Abnoxious.
SELECT person_name, array_field[1] FROM table_array -- Get the first object in the array for every record
SELECT person_name, array_field[2] FROM table_array -- Fails gracefull for the first record
