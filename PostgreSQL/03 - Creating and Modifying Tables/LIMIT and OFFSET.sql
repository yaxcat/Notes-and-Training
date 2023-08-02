
WITH 

-- Select the top 5 highest grossing movies using LIMIT
set_a AS (
	SELECT
		movie_id,
		revenues_domestic,
		'1-5' AS ranking
	FROM movies_revenues
	ORDER BY revenues_domestic DESC NULLS LAST
	LIMIT 5
),
-- Select the next 5 using LIMIT and by OFFSETTING by 5
set_b AS (
	SELECT
		movie_id,
		revenues_domestic,
		'6-10' AS ranking
	FROM movies_revenues
	ORDER BY revenues_domestic DESC NULLS LAST
	LIMIT 5 OFFSET 5
),
-- Select the last 5 by using LIMIT and OFFSETTING by another 5
set_c AS (
	SELECT
		movie_id,
		revenues_domestic,
		'11-15' AS ranking
	FROM movies_revenues
	ORDER BY revenues_domestic DESC NULLS LAST
	LIMIT 5 OFFSET 10
),

all_ranked AS (
	SELECT * FROM set_a
	UNION ALL
	SELECT * FROM set_b
	UNION ALL
	SELECT * FROM set_c

)

SELECT * FROM all_ranked;