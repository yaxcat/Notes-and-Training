UPDATE customers SET
	last_name = 'Zebra',
	email = 'XXX',
	age = 1,
	test = 0
WHERE customer_id = 6 RETURNING *;


-- if we want to use SET to calculate a uniform value for all records in a particular column, no need
-- to use a dummy WHERE clause like in MySQL.