CREATE TABLE movies (
	movie_id SERIAL PRIMARY KEY,
	movie_name VARCHAR(100) NOT NULL,
	movie_length INT,
	movie_lang VARCHAR(20),
	age_certificate VARCHAR(10),
	release_date DATE,
	director_id INT REFERENCES directors (director_id) -- Foreign key
);

/*
'REFERENCES' key word establishes that this column acts as a foreign key for a related
table.  That table's name follows the 'REFERENCES' key word and the table name in 
turn is followed by the column name.  The structure goes something like this:
[This table col name, This table col type, 'REFERENCES', foreign table name, foreign table's primary key column name]


*/