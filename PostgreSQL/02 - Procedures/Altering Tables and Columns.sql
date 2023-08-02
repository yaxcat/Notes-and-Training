-- ALTERING TABLES

-- Create the table:
CREATE TABLE persons(
	unique_id SERIAL PRIMARY KEY,
	first_name VARCHAR(20) NOT NULL,
	last_name VARCHAR(20) NOT NULL
);
SELECT * FROM persons


-- Add a new columns:
ALTER TABLE persons
ADD COLUMN age INT NOT NULL,
ADD COLUMN nationality VARCHAR(20) NOT NULL,
ADD COLUMN email VARCHAR(100) UNIQUE, -- UNIQUE keyword means that every email address in this column must be unique.  Dupes are not allowed.
ADD COLUMN droppable_column BOOL

SELECT * FROM persons


--Rename a table:
ALTER TABLE persons
RENAME TO users

SELECT * FROM persons -- No longer exists
SELECT * FROM users


--Change a column name:
ALTER TABLE users
RENAME COLUMN age TO person_age

SELECT * FROM users


--Remove a column:
ALTER TABLE users
DROP COLUMN droppable_column

SELECT * FROM users


--Change a column type:
ALTER TABLE users
ALTER COLUMN person_age TYPE VARCHAR(10) -- Changing from INT to VARCHAR is easy

ALTER TABLE users
ALTER COLUMN person_age TYPE INT -- Going from VARCHAR to INT, not so much.  This won't work
USING person_age::INTEGER -- We need to explicitly specify the target data type using :: syntax.  Here, we're saying convert all existing values from VARCHAR to type INT

SELECT * FROM users


--Set a default value for a column:
ALTER TABLE users
ADD COLUMN is_enabled VARCHAR(1)

ALTER TABLE users -- We must make another alter table statement, cannot set the default at the same time we add the column
ALTER COLUMN is_enabled SET DEFAULT 'Y'

INSERT INTO users
	(
		first_name,
		last_name,
		nationality,
		person_age
	)
VALUES ('Joe', 'Sample', 'American', 30)

SELECT * FROM users





DROP TABLE users;