--Sets the serial/auto incrementing column number to start with whatever you specify.
--Naming convention: <table_name>_<column_name>_seq, all one line, as below.

ALTER SEQUENCE directors_director_id_seq RESTART WITH 1;