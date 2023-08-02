--UPSERTS:

/* 
	PRIMARY KEY: empid, first_name, last_name

The primary key is important for an upsert to work.  If we used a primary key that was a single field
like 'unique_id', the below code would fail since in theory it would possible to have valid duplicate
values for empid, first_name and last_name in the table

*/

INSERT INTO upsert_functionality (empid, first_name, last_name, email, age)
VALUES
(3, 'Mark', 'Dreyfus', 'MARRRRK@markbro.com', 22), --If this is a new entry, it will be inserted, if not it will be ignored safely
(2, 'Cedric', 'Allan', 'NEW_FAKE_EMAIL', 54) --This is an existing record, so the email field will be updated
ON CONFLICT (empid, first_name, last_name) --Defines the constraint.  All three of these constraints must be violated in order to trip this trigger (i.e. we must have a record which duplicates the value in all three fields) 
DO UPDATE SET --Defines what to do in the event the constraint is violated
	email = EXCLUDED.email  -- References the value that would have been inserted if not for the constraint violoation
RETURNING *;

SELECT * FROM upsert_functionality