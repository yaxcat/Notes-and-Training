-- Junction table to link the movies table to the actors table

CREATE TABLE movies_actors (
	movie_id INT REFERENCES movies (movie_id),
	actor_id INT REFERENCES actors (actor_id), 
	PRIMARY KEY (movie_id, actor_id)
);

/*
In this case, the primary key is made up of two columns, which together uniquely identify a
record in this database.
*/