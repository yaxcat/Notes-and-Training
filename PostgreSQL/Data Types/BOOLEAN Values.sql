CREATE TABLE my_bools (
	unique_id SERIAL PRIMARY KEY,
	key_value VARCHAR(25) NOT NULL,
	boolean_equivalent BOOLEAN NOT NULL
);

-- PostgreSQL can take quite a few aliases for boolean values, as shown below:

INSERT INTO my_bools (key_value, boolean_equivalent) 
VALUES 
--True values:
(TRUE, 'TRUE'),
('true', 'true'),
('t', 't'),
('y', 'y'),
('yes', 'yes'),
('1', '1'),
--False values:
(FALSE, 'FALSE'),
('false', 'false'),
('f', 'f'),
('n', 'n'),
('no', 'no'),
('0', '0')
RETURNING *


-- Can use the aliases for querying:
SELECT * FROM my_bools WHERE boolean_equivalent = 'f'

SELECT * FROM my_bools WHERE boolean_equivalent IS NOT FALSE